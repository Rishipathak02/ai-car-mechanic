# AI Car Mechanic Chatbot

Full-stack assignment starter built with Angular 22 + FastAPI + SQLite + Gemini.

> Note: The supplied assignment explicitly asks for React/Next.js and Django/DRF. This implementation uses Angular + FastAPI as requested by the candidate, so this is a deliberate stack deviation.

## Features
- Car/mechanical-only chatbot behavior
- Follow-up questions using simple Python rules
- Gemini used for richer diagnosis when appropriate/configured
- Image/audio/video upload API
- Diagnosis and recommendation
- Mechanic booking
- SQLite persistence
- Conversation history API
- Angular responsive UI

## 1. Backend

```bash
cd backend
python -m venv venv
# Windows PowerShell
.\\venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Put your Gemini key in `.env`:

```env
GEMINI_API_KEY=your_key_here
```

Run:

```bash
uvicorn main:app --reload
```

API docs: http://localhost:8000/docs

## 2. Frontend

```bash
cd frontend
npm install
npm start
```

Open http://localhost:4200

## APIs
- POST `/api/chat/`
- POST `/api/upload/`
- POST `/api/diagnosis/`
- POST `/api/booking/`
- GET `/api/booking/{id}/`
- GET `/api/history/{session_id}/`

## Database
SQLite file `backend/mechanic.db` is created automatically when the backend starts.

## Assignment submission checklist
- GitHub repository
- Live frontend URL
- Live backend API URL
- README
- API documentation
- Architecture explanation
- Test screenshots/video if desired

## Architecture
Angular UI -> FastAPI REST API -> Python business logic / Gemini -> SQLite

The design intentionally keeps simple routing, validation and follow-up logic in Python and calls Gemini only for richer natural-language diagnosis.
