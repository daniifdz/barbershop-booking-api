from datetime import datetime

from sqlalchemy import CheckConstraint, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base



class Appointment(Base):
    __tablename__= "appointments"
    __table_args__= (
        CheckConstraint("status IN ('confirmed', 'cancelled')", name="ck_appointments_status_valid"),
        CheckConstraint("ends_at > starts_at", name="ck_appointments_ends_after_starts"),
    )
    
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    barber_id: Mapped[int] = mapped_column(
        ForeignKey("barbers.id", ondelete="RESTRICT")
    )
    service_id: Mapped[int] = mapped_column(
        ForeignKey("services.id", ondelete="RESTRICT")
    )
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ends_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(
        String(20), default="confirmed", server_default="confirmed"
    )
