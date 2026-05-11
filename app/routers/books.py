from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.crud.books import BookCRUD
from app.dependencies import get_db
from app.schemas import (BookCreate, BookResponse, BorrowBookRequest,
                         BorrowingResponse)

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.post(
    "",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    payload: BookCreate,
    db: Session = Depends(get_db),
):
    return BookCRUD(db).create_book(payload)


@router.get(
    "",
    response_model=list[BookResponse],
)
def get_books(
    db: Session = Depends(get_db),
):
    return BookCRUD(db).get_books()


@router.delete(
    "/{serial_number}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_book(
    serial_number: str,
    db: Session = Depends(get_db),
):
    BookCRUD(db).delete_book(serial_number)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.patch(
    "/{serial_number}/borrow",
    response_model=BorrowingResponse,
)
def borrow_book(
    serial_number: str,
    payload: BorrowBookRequest,
    db: Session = Depends(get_db),
):
    return BookCRUD(db).borrow_book(
        serial_number,
        payload.card_number,
    )


@router.patch(
    "/{serial_number}/return",
    response_model=BorrowingResponse,
)
def return_book(
    serial_number: str,
    db: Session = Depends(get_db),
):
    return BookCRUD(db).return_book(
        serial_number,
    )
