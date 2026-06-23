from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("DBPost", back_populates="user")

class DBPost(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DBUser", back_populates="items")
    comments = relationship("DBComment", back_populates="post")


class DBComment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text = Column(String)
    username = Column(String)
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("DBPost", back_populates="comments")