from fastapi import FastAPI
from app.posts.router import router

app = FastAPI()

app.include_router(router)