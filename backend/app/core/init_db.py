from app.core.database import Base
from app.core.database import engine

from app.models.book import Book


def create_tables():
    Base.metadata.create_all(bind=engine)
