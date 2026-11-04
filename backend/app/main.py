from fastapi import FastAPI
import time

from app.api.books import router as books_router
from app.core.init_db import create_tables

app = FastAPI(
    title="BookVault",
    version="0.2.1"
)

app.include_router(books_router)


@app.on_event("startup")
def startup_event():

    for attempt in range(10):

        try:

            create_tables()

            print("Database ready")

            break

        except Exception as e:

            print(f"Database not ready: {e}")

            time.sleep(3)


@app.get("/")
def root():
    return {
        "message": "Welcome to BookVault"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }