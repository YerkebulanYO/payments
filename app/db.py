import os

import databases
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as _orm
from sqlalchemy.orm import sessionmaker

from databases import Database


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:boom@db/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:boom@localhost/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://db/localhost"
# database = databases.Database(SQLALCHEMY_DATABASE_URL)
# metadata = MetaData()
# SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
# metadata.create_all(engine)

Base = declarative_base()
