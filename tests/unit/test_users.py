from app.crud.users import UserCRUD
from app.schemas import UserCreate


def test_create_book(
    db_session,
):
    user_data = {
        "card_number": "123456",
        "first_name": "Test First",
        "last_name": "Test Last",
    }
    crud = UserCRUD(db_session)

    user = crud.create_user(UserCreate(**user_data))

    assert user.card_number == user_data["card_number"]
    assert user.first_name == user_data["first_name"]
    assert user.last_name == user_data["last_name"]
