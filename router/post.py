from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from db.database import get_db
from router.schemas import PostBase, PostDisplay
from db import db_post

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

image_url_types = ['absolute', 'relative']

@router.post('/', response_model=PostDisplay, status_code=status.HTTP_201_CREATED)
def create(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Image url type is invalid, it can only take values 'absolute' or 'relative'"
        )
    return db_post.create(db, request)
