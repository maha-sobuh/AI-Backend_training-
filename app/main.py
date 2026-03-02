from fastapi import FastAPI
from routers.products import router

app = FastAPI()
####
app.include_router(router)