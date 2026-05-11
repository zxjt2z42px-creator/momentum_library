import factory

from app.models.book import Book


class BookFactory(factory.Factory):
    class Meta:
        model = Book

    serial_number = factory.Sequence(lambda n: f"{100000 + n}")
    title = factory.Faker("sentence", nb_words=2)
    author = factory.Faker("name")
    is_borrowed = False
