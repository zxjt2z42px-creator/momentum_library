from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db import Base


class Borrowing(Base):
    __tablename__ = "borrowings"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    book_id = Column(
        Integer,
        ForeignKey("books.id"),
        nullable=False,
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    borrowed_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
    )
    returned_at = Column(
        DateTime,
        nullable=True,
    )
    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
    )

    book = relationship(
        "Book",
        back_populates="borrowings",
    )

    user = relationship(
        "User",
        back_populates="borrowings",
    )
