from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from app.schemas import UserUpdate
from sqlalchemy import or_
from sqlalchemy import asc
from sqlalchemy import desc

def create_user(db: Session, user: UserCreate):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        return None

    db_user = User(
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_id(db: Session, user_id: int):

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

def update_user(
    db: Session,
    user_id: int,
    user_update: UserUpdate
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return None

    update_data = user_update.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()

    db.refresh(user)

    return user

def get_users(
    db: Session,
    page: int = 1,
    size: int = 10,
    search: str = None,
    age: int = None,
    sort_by: str = "id",
    order: str = "asc"
):
    query = db.query(User)

    if search:
        query = query.filter(
            or_(
                User.name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%")
            )
        )


    if age is not None:
        query = query.filter(
            User.age == age
        )


    sort_column = getattr(
        User,
        sort_by,
        User.id
    )

    if order.lower() == "desc":
        query = query.order_by(
            desc(sort_column)
        )
    else:
        query = query.order_by(
            asc(sort_column)
        )

    offset = (page - 1) * size

    users = (
        query
        .offset(offset)
        .limit(size)
        .all()
    )

    return users

def bulk_create_users(
    db: Session,
    users: list[UserCreate]
):
    db_users = []

    for user in users:

        db_user = User(
            name=user.name,
            email=user.email,
            age=user.age
        )

        db_users.append(db_user)

    db.add_all(db_users)

    db.commit()

    return db_users