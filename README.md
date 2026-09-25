# 🚗 AI Car Mechanic

An AI-powered full-stack web application that helps users describe vehicle problems, analyze symptoms, receive AI-based diagnosis and recommendations, upload vehicle images for visual diagnosis, and book a mechanic.

The project is built using **Angular 22, Python, FastAPI, Gemini API, and SQLite**.

---

## 🌐 Live Project

- **Live Frontend:** https://ai-car-mechanic-frontend.onrender.com
- **Live Backend API:** https://ai-car-mechanic-2y4j.onrender.com
- **API Documentation:** https://ai-car-mechanic-2y4j.onrender.com/docs

---

# ✨ Features

## 🤖 AI Car Mechanic Chatbot

- Users can describe their vehicle problems in natural language.
- The chatbot focuses on car and mechanical-related queries.
- Python-based logic handles basic validation and follow-up questions.
- Gemini AI provides detailed diagnosis and recommendations when required.
- The chatbot can ask additional questions to understand the vehicle issue.

## 🔍 Vehicle Diagnosis

The application provides possible causes and recommendations based on information such as:

- Vehicle model and year
- Vehicle symptoms
- Unusual sounds
- Warning lights
- Driving conditions
- User-provided problem description

The system provides:

- Possible causes
- Recommended checks
- Suggested next steps
- Safety guidance where required

> AI-generated diagnosis is informational and should not replace professional mechanical inspection.

## 🖼️ AI Image Diagnosis

Users can upload a vehicle or engine image for AI-based analysis.

Workflow:

```text
Vehicle Image
     ↓
Angular Frontend
     ↓
FastAPI Backend
     ↓
Gemini AI
     ↓
Image Analysis
     ↓
Diagnosis & Recommendations
```

## 🔧 Mechanic Booking

After receiving a diagnosis, users can book a mechanic.

The system:

- Creates a booking
- Generates a booking ID
- Stores booking information in SQLite
- Allows booking details to be retrieved through the API

## 💬 Conversation History

- Each chat uses a session ID.
- Conversation history can be stored and retrieved.
- Previous conversations can be accessed through the history API.

## 💾 SQLite Database

SQLite is used for application data persistence.

The database is automatically created when the backend starts.

## 📱 Responsive Angular UI

- Modern Angular 22 frontend
- Responsive user interface
- Chat-based interaction
- Image upload
- Diagnosis display
- Mechanic booking flow

---

# 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Angular 22 |
| Language | TypeScript |
| Backend | Python |
| API Framework | FastAPI |
| AI | Google Gemini API |
| Database | SQLite |
| API Documentation | Swagger / OpenAPI |
| Version Control | Git & GitHub |
| Deployment | Render |

---

# 🏗️ Application Architecture

```text
                    ┌──────────────────────┐
                    │      Angular 22      │
                    │       Frontend       │
                    └──────────┬───────────┘
                               │
                               │ HTTP REST API
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │       Backend        │
                    │       Python         │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             ┌──────────────┐     ┌──────────────┐
             │  Gemini API  │     │    SQLite    │
             │   AI Engine  │     │   Database   │
             └──────────────┘     └──────────────┘
```

---

# 📂 Project Structure

```text
AI-Car-Mechanic/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── mechanic_logic.py
│   ├── ai_service.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   └── app/
│   ├── package.json
│   └── angular.json
│
└── README.md
```

---

# 🚀 Backend Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Rishipathak02/ai-car-mechanic.git
```

Move into the project:

```bash
cd ai-car-mechanic
```

---

## 2. Open Backend Folder

```bash
cd backend
```

---

## 3. Create Python Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Gemini API Key

Create a `.env` file inside the `backend` folder.

```env
GEMINI_API_KEY=your_gemini_api_key
```

> **Important:** Never upload your real Gemini API key to GitHub.

---

## 6. Start FastAPI Backend

```bash
uvicorn main:app --reload
```

The backend will run locally on:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

# 💻 Frontend Setup

Open a new terminal.

Go to the project:

```bash
cd ai-car-mechanic
```

Move into the frontend:

```bash
cd frontend
```

Install Angular dependencies:

```bash
npm install
```

Start the Angular application:

```bash
npm start
```

The frontend will run locally on:

```text
http://localhost:4200
```

---

# 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Backend health/basic response |
| POST | `/api/chat/` | AI mechanic chatbot |
| POST | `/api/upload/` | File upload |
| POST | `/api/image-diagnosis/` | AI image diagnosis |
| POST | `/api/diagnosis/` | Vehicle diagnosis |
| POST | `/api/booking/` | Create mechanic booking |
| GET | `/api/booking/{booking_id}/` | Get booking details |
| GET | `/api/history/{session_id}/` | Get conversation history |

---

# 🧠 AI Chat Workflow

```text
User describes vehicle problem
             ↓
Angular sends request
             ↓
FastAPI receives request
             ↓
Python validates the request
             ↓
Basic follow-up logic
             ↓
Gemini AI analysis
             ↓
Diagnosis + Recommendations
             ↓
Angular displays result
             ↓
User can book a mechanic
```

---

# 🖼️ Image Diagnosis Workflow

```text
User uploads vehicle image
             ↓
Angular Frontend
             ↓
FastAPI Backend
             ↓
Gemini Image Analysis
             ↓
AI Diagnosis
             ↓
Recommendations
             ↓
Result displayed in Angular
```

---

# 🔧 Mechanic Booking Workflow

```text
Vehicle Problem
      ↓
AI Diagnosis
      ↓
User selects Book a Mechanic
      ↓
Booking API
      ↓
SQLite Database
      ↓
Booking ID Generated
      ↓
Booking Confirmation
```

---

# 🗄️ Database

The application uses **SQLite** for data persistence.

The database is created automatically when the backend starts.

The application stores information related to:

- Conversation history
- Sessions
- Vehicle diagnosis
- Mechanic bookings
- Booking IDs

---

# ☁️ Deployment

The application is deployed on **Render**.

## Backend Deployment

Technology:

```text
Python + FastAPI
```

Render configuration:

```text
Root Directory:
backend
```

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

The Gemini API key is configured as a secure environment variable in Render.

---

## Frontend Deployment

Technology:

```text
Angular 22
```

Render configuration:

```text
Root Directory:
frontend
```

Build command:

```bash
npm install && npm run build
```

Publish directory:

```text
dist/ai-car-mechanic/browser
```

---

# 🧪 Testing & Verification

The deployed application has been tested for the following functionality:

- ✅ Car-related chatbot queries
- ✅ Non-car query validation
- ✅ Follow-up questions
- ✅ Detailed AI vehicle diagnosis
- ✅ Gemini AI integration
- ✅ Vehicle image upload
- ✅ AI image diagnosis
- ✅ Diagnosis generation
- ✅ Mechanic booking
- ✅ Booking ID generation
- ✅ Booking retrieval
- ✅ Conversation history API
- ✅ FastAPI Swagger documentation
- ✅ Angular-to-FastAPI communication
- ✅ Production CORS configuration
- ✅ Live frontend deployment
- ✅ Live backend deployment

---

# 📋 Assignment Coverage

The project covers the major requirements of an AI-based vehicle assistance system:

- AI-powered vehicle assistance
- Car problem analysis
- Follow-up questions
- AI diagnosis
- Recommendations
- Image-based vehicle analysis
- REST API development
- Database persistence
- Mechanic booking
- Conversation history
- Responsive frontend
- API documentation
- Cloud deployment

The implementation uses **Angular 22 + Python/FastAPI**, which is the technology stack selected for this implementation.

---

# 🎯 Project Objective

The objective of this project is to develop a practical AI-powered automobile assistance platform that allows users to:

1. Describe a vehicle problem.
2. Provide additional information through follow-up questions.
3. Receive AI-generated possible diagnosis.
4. Get recommendations and safety guidance.
5. Upload vehicle images for visual analysis.
6. Book a mechanic when required.
7. Maintain conversation and booking information.

---

# 🔐 Security

The project follows basic security practices:

- Gemini API keys are stored using environment variables.
- API keys are not hard-coded in the application.
- Sensitive configuration is kept outside the source code.
- Production environment variables are configured through Render.

---

# 📌 Important Note

AI-generated vehicle diagnosis is intended for informational purposes only.

For serious mechanical problems, users should consult a qualified mechanic or automotive professional.

---

# 👨‍💻 Technologies Used

```text
Angular 22
TypeScript
Python
FastAPI
Google Gemini API
SQLite
REST API
Swagger / OpenAPI
Git
GitHub
Render
```

---

# 🚀 Future Improvements

Possible future enhancements include:

- User authentication
- Vehicle profile management
- Mechanic/admin dashboard
- Appointment scheduling
- Email/SMS notifications
- More detailed service history
- Advanced vehicle image analysis
- Voice-based interaction
- Production-grade database such as PostgreSQL
- Monitoring and logging
- Automated testing and CI/CD

---

# 📞 Project -

**AI Car Mechanic**

Built with:

**Angular 22 + Python + FastAPI + Gemini AI + SQLite**