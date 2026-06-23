from datetime import datetime

from fastapi import HTTPException, status

from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DBPost

def create(db: Session, request: PostBase):
    new_post = DBPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def delete(db: Session, post_id: int, user_id: int):
    post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} does not found"
        )

    if post.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Only user with id {user_id} does can delete"
        )
    db.delete(post)
    db.commit()

    return "post deleted"