from decimal import Decimal

from sqlalchemy import CheckConstraint, Numeric, String, true
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Service(Base):
    __tablename__= "services"
    __table_args__= (
        CheckConstraint("duration_minutes > 0", name="ck_services_duration_positive"),
        CheckConstraint("price >= 0", name="ck_services_price_non_negative"),
    )
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    duration_minutes: Mapped[int]
    price: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    active: Mapped[bool] = mapped_column(default=True, server_default=true())