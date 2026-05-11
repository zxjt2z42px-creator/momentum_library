def test_create_user(client):
    response = client.post(
        "/users",
        json={
            "card_number": "111111",
            "first_name": "TestFirst",
            "last_name": "TestLast",
        },
    )
    assert response.status_code == 201
    data = response.json()

    assert data["card_number"] == "111111"


def test_create_user_card_number_must_be_unique(client):
    user_data = {
        "card_number": "111111",
        "first_name": "TestFirst",
        "last_name": "TestLast",
    }

    response = client.post("/users", json=user_data)
    assert response.status_code == 201

    response = client.post("/users", json=user_data)
    assert response.status_code == 400


def test_create_user_card_number_must_match_pattern(client):
    user_data = {
        "card_number": "test",
        "first_name": "TestFirst",
        "last_name": "TestLast",
    }

    response = client.post("/users", json=user_data)
    assert response.status_code == 422
