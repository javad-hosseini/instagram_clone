from sqlalchemy import Column, Integer, String

from .database import Base

class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
