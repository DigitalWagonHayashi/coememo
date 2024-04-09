import os
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

db_path = pathlib.Path(__file__).parent.parent / "db.sqlite3"


class DAO:
    def __init__(self, db_path=db_path):
        self.engine = create_engine(f'sqlite:///{db_path}')

    def new_session(self):
        return Session(self.engine)


