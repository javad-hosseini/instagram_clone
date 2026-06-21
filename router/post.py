import random
import shutil
import string

from fastapi import APIRouter, Depends, status, HTTPException, File
from sqlalchemy.orm.session import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from router.schemas import PostBase, PostDisplay, UserAuth
from db import db_post
from fastapi.datastructures import UploadFile

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

image_url_types = ['absolute', 'relative']

@router.post('/', response_model=PostDisplay, status_code=status.HTTP_201_CREATED)
def create(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Image url type is invalid, it can only take values 'absolute' or 'relative'"
        )
    return db_post.create(db, request)

@router.get('/image', status_code=status.HTTP_200_OK)
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    rand_str = "".join(random.choices(string.ascii_letters) for _ in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.split('.', 1))
    path = f"images/{filename}"

    with open(path, 'w + b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}

@router.delete('/delete/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(post_id: int, db:Session=Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_post.delete(db, post_id, current_user.id)
