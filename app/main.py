from fastapi import FastAPI
from routers.products import router
from database import engine, create_db_and_tables
from models import Product  # ← must import so metadata knows about it

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router)