import os
import shutil
import uuid
from pathlib import Path

from fastapi import (
    FastAPI,
    Depends,
    UploadFile,
    File,
    Form,
    HTTPException
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from database import Base, engine, get_db
from models import ChatMessage, Media, Diagnosis, Booking
from schemas import ChatRequest, DiagnosisRequest, BookingRequest
from mechanic_logic import rule_based_reply, is_car_related
from ai_service import gemini_answer, gemini_image_analysis


load_dotenv()

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


app = FastAPI(
    title="AI Car Mechanic API",
    version="1.0.0"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "https://ai-car-mechanic-frontend.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# =========================
# STATIC UPLOADS
# =========================

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads"
)


# =========================
# ROOT
# =========================

@app.get("/")
def root():
    return {
        "message": "AI Car Mechanic API is running"
    }


# =========================
# CHAT
# =========================

@app.post("/api/chat/")
def chat(
    payload: ChatRequest,
    db: Session = Depends(get_db)
):

    db.add(
        ChatMessage(
            session_id=payload.session_id,
            role="user",
            message=payload.message
        )
    )

    reply = rule_based_reply(payload.message)

    if (
        reply
        and is_car_related(payload.message)
        and len(payload.message.split()) > 12
    ):
        reply = gemini_answer(payload.message)

    db.add(
        ChatMessage(
            session_id=payload.session_id,
            role="assistant",
            message=reply
        )
    )

    db.commit()

    return {
        "session_id": payload.session_id,
        "reply": reply
    }


# =========================
# MEDIA UPLOAD
# =========================

@app.post("/api/upload/")
async def upload(
    session_id: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    allowed = {
        "image/",
        "audio/",
        "video/"
    }

    if not any(
        (file.content_type or "").startswith(x)
        for x in allowed
    ):
        raise HTTPException(
            status_code=400,
            detail="Only image, audio and video files are allowed"
        )

    safe_name = (
        f"{uuid.uuid4().hex}_"
        f"{Path(file.filename or 'media').name}"
    )

    destination = UPLOAD_DIR / safe_name

    with destination.open("wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    item = Media(
        session_id=session_id,
        filename=safe_name,
        media_type=file.content_type or "unknown",
        path=str(destination)
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return {
        "id": item.id,
        "filename": safe_name,
        "media_type": item.media_type,
        "url": f"/uploads/{safe_name}"
    }


# =========================
# AI IMAGE DIAGNOSIS
# =========================

@app.post("/api/image-diagnosis/")
async def image_diagnosis(
    session_id: str = Form(...),
    file: UploadFile = File(...)
):

    if not (file.content_type or "").startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed"
        )

    safe_name = (
        f"{uuid.uuid4().hex}_"
        f"{Path(file.filename or 'image').name}"
    )

    destination = UPLOAD_DIR / safe_name

    with destination.open("wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = gemini_image_analysis(
        str(destination)
    )

    return {
        "session_id": session_id,
        "filename": safe_name,
        "diagnosis": result,
        "image_url": f"/uploads/{safe_name}"
    }


# =========================
# AI TEXT DIAGNOSIS
# =========================

@app.post("/api/diagnosis/")
def diagnosis(
    payload: DiagnosisRequest,
    db: Session = Depends(get_db)
):

    result = gemini_answer(
        payload.symptoms
    )

    diagnosis_text = result

    recommendation = (
        "If symptoms are severe, unsafe to drive, "
        "or involve brakes/steering, stop driving "
        "and arrange a professional inspection."
    )

    item = Diagnosis(
        session_id=payload.session_id,
        diagnosis=diagnosis_text,
        recommendation=recommendation
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return {
        "id": item.id,
        "diagnosis": diagnosis_text,
        "recommendation": recommendation
    }


# =========================
# BOOKING
# =========================

@app.post("/api/booking/")
def booking(
    payload: BookingRequest,
    db: Session = Depends(get_db)
):

    item = Booking(
        **payload.model_dump()
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return {
        "booking_id": item.id,
        "status": item.status,
        "message": "Mechanic booking created successfully"
    }


# =========================
# GET BOOKING
# =========================

@app.get("/api/booking/{booking_id}/")
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    item = db.get(
        Booking,
        booking_id
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return {
        "booking_id": item.id,
        "name": item.name,
        "phone": item.phone,
        "car_model": item.car_model,
        "issue": item.issue,
        "preferred_date": item.preferred_date,
        "preferred_time": item.preferred_time,
        "status": item.status
    }


# =========================
# CHAT HISTORY
# =========================

@app.get("/api/history/{session_id}/")
def history(
    session_id: str,
    db: Session = Depends(get_db)
):

    rows = (
        db.query(ChatMessage)
        .filter(
            ChatMessage.session_id == session_id
        )
        .order_by(
            ChatMessage.created_at
        )
        .all()
    )

    return [
        {
            "role": r.role,
            "message": r.message,
            "created_at": r.created_at
        }
        for r in rows
    ]