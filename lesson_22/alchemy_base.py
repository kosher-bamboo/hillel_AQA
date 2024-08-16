from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql://postgres:Qwerty123@localhost/postgres22"


engine = create_engine(DATABASE_URL)

Base = declarative_base()
