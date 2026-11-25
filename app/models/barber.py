
from sqlalchemy import String, true, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from app.models.base import Base


class Barber(Base):
    __tablename__= "barbers"
   

    id: Mapped[int] = mapped_column(primary_key= True)
    user_id:Mapped [int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), unique=True
        )
    display_name:Mapped [str] = mapped_column(String(100))
    active:Mapped[bool]= mapped_column(default=True, server_default=true())
