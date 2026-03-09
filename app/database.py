import os
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

def create_db_and_tables(): #SQLModel way to create all tables on startup.
    SQLModel.metadata.create_all(engine) 

def get_db():
    with Session(engine) as session:   # with block automatically handles closing the session,
        yield session