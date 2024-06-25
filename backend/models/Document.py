from database.db import db
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Uuid, String, DateTime, ForeignKey, Text, null
from uuid import uuid4
from datetime import datetime
from models.DocumentStatus import DocumentStatus


class Document(db.Model):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(type_=Uuid, default=uuid4, primary_key=True)
    document: Mapped[str] = mapped_column(type_=String(250), nullable=False)
    status: Mapped[str] = mapped_column(String(250), ForeignKey("documents_status.status"),
                                        default="INITIALIZED", nullable=False)
    user_id: Mapped[str] = mapped_column(Uuid, ForeignKey("users.id"), nullable=False)
    sign_coordinates: Mapped[str] = mapped_column(type_=Text, nullable=False)
    initial_coordinates: Mapped[str] = mapped_column(type_=Text, nullable=False)
    to: Mapped[str] = mapped_column(String(250), nullable=False)
    to_id: Mapped[str] = mapped_column(Uuid, ForeignKey("users.id"), nullable=True, default=null())
    createdAt = mapped_column(type_=DateTime, default=datetime.utcnow)
    updatedAt = mapped_column(type_=DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    documents_status: Mapped["DocumentStatus"] = relationship("DocumentStatus", back_populates="documents")
    user = relationship("User", back_populates="documents", foreign_keys=user_id)
    to_user = relationship("User", back_populates="documents_sent_to", foreign_keys=to_id)
