from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas import UserCreate


class UserCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_user(
        self,
        payload: UserCreate,
    ) -> User:
        existing_user = (
            self.db.query(User).filter(User.card_number == payload.card_number).first()
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="User already exists",
            )

        user = User(
            card_number=payload.card_number,
            first_name=payload.first_name,
            last_name=payload.last_name,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
