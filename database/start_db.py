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
    try:
        engine = create_engine(f"mysql+pymysql://{DB_SETTINGS['DB_USERNAME']}:{DB_SETTINGS['PASSWORD']}@"
                               f"{DB_SETTINGS['SERVER_ADDRESS']}:{DB_SETTINGS['PORT_NUMBER']}/{DB_SETTINGS['DB_NAME']}")

        Session = sessionmaker(engine)
        Base.metadata.create_all(bind=engine)
        return Session

    except sqlalchemy.exc.DatabaseError:
        dotenv_server = find_dotenv('.env.2')

        load_dotenv(dotenv_server)

        DB_SETTINGS_2 = {'SERVER_ADDRESS': os.getenv('SERVER_ADDRESS'),
                         'DB_NAME': os.getenv('DB_NAME'),
                         'DB_USERNAME': os.getenv('DB_USERNAME'),
                         'PASSWORD': os.getenv('PASSWORD'),
                         'PORT_NUMBER': os.getenv('PORT_NUMBER')
                         }

        engine = create_engine(f"mysql+pymysql://{DB_SETTINGS_2['DB_USERNAME']}:{DB_SETTINGS_2['PASSWORD']}@"
                               f"{DB_SETTINGS_2['SERVER_ADDRESS']}:{DB_SETTINGS_2['PORT_NUMBER']}/{DB_SETTINGS_2['DB_NAME']}")

        Session = sessionmaker(engine)
        Base.metadata.create_all(bind=engine)
        return Session
