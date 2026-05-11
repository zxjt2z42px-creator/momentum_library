def test_create_book(client):
    response = client.post(
        "/books",
        json={
            "serial_number": "222222",
            "title": "Title",
            "author": "TestAuthor",
        },
    )

    assert response.status_code == 201
    data = response.json()

    assert data["serial_number"] == "222222"


def test_create_book_serial_number_must_be_unique(client):
    book_data = {
        "serial_number": "222222",
        "title": "Title",
        "author": "TestAuthor",
    }

    response = client.post(
        "/books",
        json=book_data,
    )
    assert response.status_code == 201

    response = client.post(
        "/books",
        json=book_data,
    )
    assert response.status_code == 400


def test_create_book_serial_number_must_match_pattern(client):
    response = client.post(
        "/books",
        json={
            "serial_number": "test",
            "title": "Title",
            "author": "TestAuthor",
        },
    )

    assert response.status_code == 422


def test_delete_book(client, user_factory, book_factory):
    book = book_factory()

    response = client.delete(
        f"/books/{book.serial_number}",
    )

    assert response.status_code == 204


def test_get_books(client, book_factory):
    book_factory()
    book_factory()

    response = client.get(
        f"/books",
    )

    assert response.status_code == 200

    data = response.json()

    assert type(data) == list


def test_borrow_book(client, user_factory, book_factory):
    user = user_factory()
    book = book_factory()

    response = client.patch(
        f"/books/{book.serial_number}/borrow",
        json={
            "card_number": user.card_number,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["is_active"] is True
    assert data["user"]["card_number"] == user.card_number
    assert data["book"]["serial_number"] == book.serial_number


def test_borrow_book_not_found(client, user_factory):
    user = user_factory()

    response = client.patch(
        f"/books/111111/borrow",
        json={
            "card_number": user.card_number,
        },
    )

    assert response.status_code == 404


def test_borrow_book_already_borrowed(client, user_factory, book_factory):
    user = user_factory()
    book = book_factory()

    response = client.patch(
        f"/books/{book.serial_number}/borrow",
        json={
            "card_number": user.card_number,
        },
    )

    assert response.status_code == 200

    response = client.patch(
        f"/books/{book.serial_number}/borrow",
        json={
            "card_number": user.card_number,
        },
    )

    assert response.status_code == 400


def test_return_book(client, user_factory, book_factory):
    user = user_factory()
    book = book_factory()

    response = client.patch(
        f"/books/{book.serial_number}/borrow",
        json={
            "card_number": user.card_number,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["user"]["card_number"] == user.card_number
    assert data["book"]["serial_number"] == book.serial_number
    assert data["is_active"] is True

    response = client.patch(
        f"/books/{book.serial_number}/return",
    )

    assert response.status_code == 200

    data = response.json()

    assert data["user"]["card_number"] == user.card_number
    assert data["book"]["serial_number"] == book.serial_number
    assert data["is_active"] is False


def test_return_book_not_found(client, user_factory, book_factory):
    user = user_factory()
    book = book_factory()

    client.patch(
        f"/books/{book.serial_number}/borrow",
        json={
            "card_number": user.card_number,
        },
    )

    response = client.patch(
        f"/books/111111/return",
    )

    assert response.status_code == 404
