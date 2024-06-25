from database.db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from sqlalchemy import Uuid, String, DateTime, Column, ForeignKey
from datetime import datetime
from models.User import User


class Signature(db.Model):
    __tablename__ = "signatures"

    id: Mapped[str] = mapped_column(primary_key=True, type_=Uuid, default=uuid4)
    font_name: Mapped[str] = mapped_column(String(250), nullable=False)
    signature_name: Mapped[str] = mapped_column(String(250), nullable=False)
    initial_name: Mapped[str] = mapped_column(String(250), nullable=False)
    user_id: Mapped[str] = Column(Uuid, ForeignKey('users.id'), nullable=False)
    createdAt = mapped_column(type_=DateTime, default=datetime.utcnow)
    updatedAt = mapped_column(type_=DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped["User"] = relationship("User", back_populates="signature", uselist=False)

    def to_dict(self):
        return {
            "font_name": self.font_name,
            "signature_name": self.signature_name,
            "initial_name": self.initial_name,
            "user_id": self.user_id,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
         }
