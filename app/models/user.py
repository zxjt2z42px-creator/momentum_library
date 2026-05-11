from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    card_number = Column(
        String(6),
        unique=True,
        nullable=False,
        index=True,
    )
    first_name = Column(
        String,
        nullable=False,
    )
    last_name = Column(
        String,
        nullable=False,
    )
    borrowings = relationship(
        "Borrowing",
        back_populates="user",
    )
