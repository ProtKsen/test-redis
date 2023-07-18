from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from src.config import config

engine = create_engine(config.db.url)

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

Base.query = db_session.query_property()


def create_all():
    Base.metadata.create_all(bind=engine)


def drop_all(engine):
    Base.metadata.drop_all(bind=engine)
