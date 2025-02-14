# engine works with PyMySQL package
import os

import sqlalchemy
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

dotenv_server = find_dotenv('.env')

load_dotenv(dotenv_server)

DB_SETTINGS = {'SERVER_ADDRESS': os.getenv('SERVER_ADDRESS'),
               'DB_NAME': os.getenv('DB_NAME'),
               'DB_USERNAME': os.getenv('DB_USERNAME'),
               'PASSWORD': os.getenv('PASSWORD'),
               'PORT_NUMBER': os.getenv('PORT_NUMBER')
               }


class Base(DeclarativeBase):
    pass


def start_db():
    engine = create_engine(f"mysql+pymysql://{DB_SETTINGS['DB_USERNAME']}:{DB_SETTINGS['PASSWORD']}@"
                           f"{DB_SETTINGS['SERVER_ADDRESS']}:{DB_SETTINGS['PORT_NUMBER']}/{DB_SETTINGS['DB_NAME']}")

    session = sessionmaker(engine)
    Base.metadata.create_all(bind=engine)
    return session
