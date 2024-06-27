from datetime import datetime

from database.db import db
from sqlalchemy import Column, String, Uuid
from uuid import uuid4
from sqlalchemy import event
from werkzeug.security import generate_password_hash
from sqlalchemy import Integer, String, DateTime,Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(type_=Uuid, primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(type_=String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(type_=String(250), nullable=False)
    fullname: Mapped[str] = mapped_column(type_=String(250), nullable=False)
    initial: Mapped[str] = mapped_column(type_=String(250), nullable=False)
    isVerified: Mapped[bool] = mapped_column(type_=Boolean, nullable=False,default=False)
    verifyId: Mapped[str] = mapped_column(type_=String(40), nullable=True)
    otp: Mapped[int] = mapped_column(type_=Integer, nullable=True)
    createdAt = mapped_column(type_=DateTime, default=datetime.utcnow)
    updatedAt = mapped_column(type_=DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    signature = relationship("Signature", back_populates="user", uselist=False)
    documents = relationship("Document", back_populates="user", foreign_keys="Document.user_id")
    documents_sent_to = relationship("Document", back_populates="to_user", foreign_keys="Document.to_id")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "fullname": self.fullname,
            "initial": self.initial,
            "isVerified":self.isVerified,
            "verifyId":self.verifyId,
            "otp":self.otp
        }


@event.listens_for(User, "before_insert")
def hash_password(mapper, connect, target):
    if target.password:
        target.password = generate_password_hash(target.password, method="pbkdf2:sha256", salt_length=18)


