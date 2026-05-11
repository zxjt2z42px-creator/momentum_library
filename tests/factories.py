from datetime import datetime

import factory

from app.models.book import Book
from app.models.borrowing import Borrowing
from app.models.user import User


class BookFactory(factory.Factory):
    class Meta:
        model = Book

    serial_number = factory.Sequence(lambda n: f"{100000 + n}")
    title = factory.Faker("sentence", nb_words=2)
    author = factory.Faker("name")
    is_borrowed = False


class UserFactory(factory.Factory):
    class Meta:
        model = User

    card_number = factory.Sequence(lambda n: f"{100000 + n}")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class BorrowingFactory(factory.Factory):
    class Meta:
        model = Borrowing

    user = factory.SubFactory(
        UserFactory,
    )
    book = factory.SubFactory(
        BookFactory,
    )
    borrowed_at = factory.LazyFunction(
        datetime.now(),
    )
    returned_at = None
    is_active = True
