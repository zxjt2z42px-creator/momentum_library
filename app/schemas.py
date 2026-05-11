from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    card_number: str = Field(
        ...,
        pattern=r"^[0-9]{6}$",
    )
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    id: int
    card_number: str
    first_name: str
    last_name: str

    model_config = {
        "from_attributes": True,
    }


class BookCreate(BaseModel):
    serial_number: str = Field(
        ...,
        pattern=r"^[0-9]{6}$",
    )

    title: str
    author: str


class BookResponse(BaseModel):
    id: int

    serial_number: str
    title: str
    author: str

    is_borrowed: bool

    model_config = {
        "from_attributes": True,
    }


class BorrowBookRequest(BaseModel):
    card_number: str = Field(
        ...,
        pattern=r"^[0-9]{6}$",
    )


class BorrowingResponse(BaseModel):
    id: int
    borrowed_at: datetime
    returned_at: Optional[datetime]
    is_active: bool
    user: UserResponse
    book: BookResponse

    model_config = {
        "from_attributes": True,
    }
