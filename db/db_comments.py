from datetime import datetime

from sqlalchemy.orm import Session

from db.models import DBComment
from routers.schemas import CommentBase


def create(db: Session, request: CommentBase):
    new_comment = DBComment(
        text=request.text,
        username=request.username,
        timestamp=datetime.now(),
        post_id=request.post_id,

    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DBComment).offset(skip).limit(limit).all()
