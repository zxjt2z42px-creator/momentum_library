from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    serial_number = Column(
        String(6),
        unique=True,
        nullable=False,
        index=True,
    )
    title = Column(
        String,
        nullable=False,
    )
    author = Column(
        String,
        nullable=False,
    )
    is_borrowed = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    borrowings = relationship(
        "Borrowing",
        back_populates="book",
    )
