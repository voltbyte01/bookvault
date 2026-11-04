from fastapi import FastAPI

app = FastAPI(
    title="BookVault",
    version="0.1.0"
)


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