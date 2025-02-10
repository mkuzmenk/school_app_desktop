from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.dialects import mysql
from dotenv import load_dotenv

import os

load_dotenv()

DB_SETTINGS = {'SERVER_ADDRESS': os.getenv('SERVER_ADDRESS'),
               'DB_NAME': os.getenv('DB_NAME'),
               'DB_USERNAME': os.getenv('DB_USERNAME'),
               'PASSWORD': os.getenv('PASSWORD'),
               'PORT_NUMBER': os.getenv('PORT_NUMBER')
               }


class Base(DeclarativeBase):
    pass
