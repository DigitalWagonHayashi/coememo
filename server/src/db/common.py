import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_path = os.path.abspath(__file__).replace('common.py', 'db.sqlite3')


class DAO:
    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite://{db_path}')

    def get_session(self):
        return sessionmaker(bind=self.engine)

