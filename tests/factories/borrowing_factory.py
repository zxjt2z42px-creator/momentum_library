from datetime import datetime

import factory

from app.models.borrowing import Borrowing
from tests.factories.book_factory import (
    BookFactory,
)
from tests.factories.user_factory import (
    UserFactory,
)


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
