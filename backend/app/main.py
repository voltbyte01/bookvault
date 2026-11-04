from fastapi import FastAPI

from app.api.books import router as books_router

app = FastAPI(
    title="BookVault",
    version="0.2.0"
)

app.include_router(books_router)


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