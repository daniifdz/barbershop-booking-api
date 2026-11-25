from decimal import Decimal
from datetime import datetime

from sqlalchemy import CheckConstraint, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint("role IN ('barber', 'client', 'admin')", name="ck_users_role_valid"),
    )
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column (String(255))
    full_name: Mapped[str] = mapped_column (String(100))
    phone: Mapped[str] = mapped_column( String(20))
    role: Mapped[str] = mapped_column(
        String(20), default="client", server_default = "client"
    )
    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )