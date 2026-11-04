from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.models.book import Book

from app.services.isbn_service import lookup_isbn

from app.core.dependencies import get_db

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("/import/{isbn}")
def import_book(
    isbn: str,
    db: Session = Depends(get_db)
):

    existing = (
        db.query(Book)
        .filter(Book.isbn == isbn)
        .first()
    )

    if existing:
        return existing

    metadata = lookup_isbn(isbn)

    if not metadata:
        return {
            "error": "Book not found"
        }

    book = Book(
        isbn=metadata["isbn"],
        title=metadata["title"],
        authors=metadata["authors"],
        publisher=metadata["publisher"],
        publish_date=metadata["publish_date"],
        cover_url=metadata["cover_url"]
    )

    db.add(book)

    db.commit()

    db.refresh(book)

    return book

@router.get("/")
def get_books(
    db: Session = Depends(get_db)
):
    return db.query(Book).all()