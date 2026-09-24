from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    session_id: str
    message: str = Field(min_length=1, max_length=2000)

class DiagnosisRequest(BaseModel):
    session_id: str
    symptoms: str = Field(min_length=1, max_length=5000)

class BookingRequest(BaseModel):
    name: str
    phone: str
    car_model: str
    issue: str
    preferred_date: str
    preferred_time: str
