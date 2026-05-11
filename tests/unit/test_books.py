from app.crud.books import BookCRUD
from app.schemas import BookCreate


def test_create_book(
    db_session,
):
    book_data = {
        "serial_number": "123456",
        "title": "Test Book",
        "author": "Test Author",
    }
    crud = BookCRUD(db_session)

    book = crud.create_book(BookCreate(**book_data))

    assert book.serial_number == book_data["serial_number"]
    assert book.title == book_data["title"]
    assert book.author == book_data["author"]


def test_get_books(
    db_session,
    book_factory,
):
    book_factory()
    book_factory()

    crud = BookCRUD(db_session)
    books = crud.get_books()

    assert type(books) == list
    assert len(books) == 2


def test_borrow_book(
    db_session,
    user_factory,
    book_factory,
):
    user = user_factory()
    book = book_factory()

    crud = BookCRUD(db_session)

    borrowing = crud.borrow_book(
        book.serial_number,
        user.card_number,
    )

    assert borrowing.is_active is True
    assert borrowing.user.card_number == user.card_number
    assert borrowing.book.serial_number == book.serial_number
    assert borrowing.book.is_borrowed is True
    assert borrowing.returned_at is None


def test_return_book(
    db_session,
    user_factory,
    book_factory,
):
    user = user_factory()
    book = book_factory()

    crud = BookCRUD(db_session)

    crud.borrow_book(
        book.serial_number,
        user.card_number,
    )

    response = crud.return_book(book.serial_number)

    assert response.is_active is False
    assert response.user.card_number == user.card_number
    assert response.book.serial_number == book.serial_number
    assert response.book.is_borrowed is False
    assert response.borrowed_at is not None
    assert response.returned_at is not None
    assert response.returned_at > response.borrowed_at
