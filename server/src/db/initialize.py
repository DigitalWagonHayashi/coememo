import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db.models import Base
from src.db.common import db_path


def initialize():
    engine = create_engine(f'sqlite:///{db_path}')
    Base.metadata.create_all(engine)
