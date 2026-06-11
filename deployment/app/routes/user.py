from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.crud import get_users
from typing import List
from sqlalchemy.orm import Session
from app.crud import update_user
from app.schemas import UserUpdate
from app.crud import create_user
from app.dependencies import get_db
from app.schemas import UserCreate
from app.crud import get_user_by_id
from typing import List
from app.crud import bulk_create_users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user_api(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    created_user = create_user(db, user)

    if not created_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return created_user

@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.put(
    "/{user_id}"
)
def update_user_api(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
):

    updated_user = update_user(
        db,
        user_id,
        user_update
    )

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user

@router.get("/")
def list_users(
    page: int = 1,
    size: int = 10,
    search: str = None,
    age: int = None,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    return get_users(
        db=db,
        page=page,
        size=size,
        search=search,
        age=age,
        sort_by=sort_by,
        order=order
    )
@router.post("/bulk")
def bulk_create_user_api(
    users: List[UserCreate],
    db: Session = Depends(get_db)
):
    return bulk_create_users(
        db,
        users
    )