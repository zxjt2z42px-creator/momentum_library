import logging

from fastapi import FastAPI

from app.db import Base, engine
from app.routers.books import router as books_router
from app.routers.users import router as users_router

Base.metadata.create_all(bind=engine)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


app = FastAPI(
    title="Momentum Library API",
)

app.include_router(books_router)
app.include_router(users_router)


@app.get("/health")
def health():
    return {
        "status": "ok",
    }
