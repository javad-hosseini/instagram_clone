from starlette import status

from routers.schemas import CommentBase, UserAuth
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_comments
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/comment",
    tags=["comment"],
)

@router.get("/all/{post_id}")
def comments(post_id: int, db: Session = Depends(get_db)):
    return db_comments.get_all(db, post_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_comments.create(db, request)