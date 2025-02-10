# engine works with PyMySQL package
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

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

    Session = sessionmaker(engine)
    Base.metadata.create_all(bind=engine)
    return Session
