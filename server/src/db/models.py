from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Records(Base):
    __tablename__ = 'records'

    id = Column(String, primary_key=True)
    machine_id = Column(String)
    recorded_at = Column(Integer)
    inference_at = Column(Integer, nullable=True)
    text = Column(String, nullable=True)
    voice_id = Column(String)
    audio_path = Column(String)
