from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database_manager import get_session
from database.models import User
from schemas.users_schemas import UserSchema

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=UserSchema, status_code=201)
async def create_user(user: UserSchema, session: Session = Depends(get_session)):
    try:
        new_user = User(
            username=user.username,
            email=user.email,
            password=user.password
        )
        session.add(new_user)
        session.commit()
        return new_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Помилка при створенні нового користувача: {str(e)}")
