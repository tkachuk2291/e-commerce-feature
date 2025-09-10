import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
    with engine.connect() as conn:
        print("Database connected successfully")
except OperationalError as e:
    print(f"Database connection failed: {e}")
    sys.exit(1)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise

    finally:
        session.close()


Base = declarative_base()
