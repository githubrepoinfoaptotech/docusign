from database.db import db
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Uuid, String, DateTime
from uuid import uuid4
from datetime import datetime


class DocumentStatus(db.Model):
    __tablename__ = "documents_status"

    id: Mapped[str] = mapped_column(type_=Uuid, primary_key=True, default=uuid4)
    status: Mapped[str] = mapped_column(type_=String(250), nullable=False, unique=True)
    createdAt = mapped_column(type_=DateTime, default=datetime.utcnow)
    updatedAt = mapped_column(type_=DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    documents = relationship("Document", back_populates="documents_status", uselist=True)

    def to_dict(self):
        return {
            "status": self.status
        }
