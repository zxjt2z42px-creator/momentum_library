from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud.users import UserCRUD
from app.dependencies import get_db
from app.schemas import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    return UserCRUD(db).create_user(payload)
