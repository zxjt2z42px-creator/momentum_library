from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.book import Book
from app.models.borrowing import Borrowing
from app.models.user import User
from app.schemas import BookCreate


class BookCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_book(self, payload: BookCreate):
        existing_book = (
            self.db.query(Book)
            .filter(Book.serial_number == payload.serial_number)
            .first()
        )

        if existing_book:
            raise HTTPException(
                status_code=400,
                detail="Book already exists",
            )

        book = Book(**payload.model_dump())

        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)

        return book

    def get_books(self):
        return self.db.query(Book).all()

    def delete_book(self, serial_number: str):
        book = self.db.query(Book).filter(Book.serial_number == serial_number).first()

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        self.db.delete(book)
        self.db.commit()

    def borrow_book(
        self,
        serial_number: str,
        card_number: str,
    ):
        book = self.db.query(Book).filter(Book.serial_number == serial_number).first()

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        if book.is_borrowed:
            raise HTTPException(
                status_code=400,
                detail="Book already borrowed",
            )

        user = self.db.query(User).filter(User.card_number == card_number).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )

        borrowing = Borrowing(
            book_id=book.id,
            user_id=user.id,
        )
        book.is_borrowed = True

        self.db.add(borrowing)
        self.db.commit()
        self.db.refresh(borrowing)

        return borrowing

    def return_book(
        self,
        serial_number: str,
    ):
        book = self.db.query(Book).filter(Book.serial_number == serial_number).first()

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        borrowing = (
            self.db.query(Borrowing)
            .filter(
                Borrowing.book_id == book.id,
                Borrowing.is_active.is_(True),
            )
            .first()
        )

        if not borrowing:
            raise HTTPException(
                status_code=400,
                detail="Book is not borrowed",
            )

        borrowing.is_active = False
        borrowing.returned_at = datetime.now()

        book.is_borrowed = False

        self.db.commit()
        self.db.refresh(borrowing)

        return borrowing
