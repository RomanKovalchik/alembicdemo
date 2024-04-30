from sqlalchemy.orm import declarative_base

from database.database import Base
from sqlalchemy import Column, Integer, String
#Необходимо включить в файл где создаются модели
#А потом импортировать в env file
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(120), unique=True, nullable=True)

    def __init__(self, username=None, email=None, phone=None):
        self.username = username
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f'<User {self.username!r}>'
