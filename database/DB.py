from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.dialects import mysql


class Base(DeclarativeBase):
    pass


