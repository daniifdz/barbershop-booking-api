
from sqlalchemy import ForeignKey, Time, UniqueConstraint, CheckConstraint, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from app.models.base import Base

from datetime import time

class BarberSchedule(Base):
    __tablename__= "barber_schedules"
    __table_args__= (
        CheckConstraint(
            "weekday BETWEEN 0 AND 6", name="ck_barber_schedules_weekday_valid"
            ),
        CheckConstraint(
            "end_time > start_time", name="ck_barber_schedules_ends_after_start"
            ),
        UniqueConstraint(
            "barber_id", "weekday", name = "uq_barber_schedules_barber_weekday"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key= True)
    barber_id:Mapped [int] = mapped_column(
        ForeignKey("barbers.id", ondelete="RESTRICT"),
        )
    weekday:Mapped [int] = mapped_column(SmallInteger)
    start_time:Mapped[time] = mapped_column(Time)
    end_time:Mapped[time] = mapped_column(Time)
