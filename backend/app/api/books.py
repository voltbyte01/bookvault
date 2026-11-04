from fastapi import APIRouter

from app.services.isbn_service import lookup_isbn

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get("/isbn/{isbn}")
def get_book(isbn: str):

    result = lookup_isbn(isbn)

    if not result:
        return {
            "error": "Book not found"
        }

    return result