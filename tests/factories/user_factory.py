import factory

from app.models.user import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    card_number = factory.Sequence(lambda n: f"{100000 + n}")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
