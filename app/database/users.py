from typing import Iterable, Type, Optional

from fastapi import HTTPException
from sqlmodel import Session, select
from app.database.engine import engine
from app.models.models import User


def get_user(user_id: int) -> Optional[User]:
    with Session(engine) as session:
        return session.get(User, user_id)


def get_users() -> Iterable[User]:
    with Session(engine) as session:
        statement = select(User)
        return session.exec(statement).all()


def create_user(user: User) -> User:
    with Session(engine) as db:
        db_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            avatar=str(user.avatar)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


def update_user(user_id: int, user: User) -> Type[User]:
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = user.model_dump(exclude_unset=True)
        db_user.sqlmodel_update(user_data)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


def delete_user(user_id: int):
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(db_user)
        session.commit()
