from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from database import Base

class ChatMessage(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    session_id = Column(String(100), index=True)
    role = Column(String(20))
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    session_id = Column(String(100), index=True)
    filename = Column(String(255))
    media_type = Column(String(100))
    path = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)

class Diagnosis(Base):
    __tablename__ = "diagnoses"
    id = Column(Integer, primary_key=True)
    session_id = Column(String(100), index=True)
    diagnosis = Column(Text)
    recommendation = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    phone = Column(String(30))
    car_model = Column(String(120))
    issue = Column(Text)
    preferred_date = Column(String(30))
    preferred_time = Column(String(30))
    status = Column(String(30), default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
