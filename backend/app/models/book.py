from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)

    isbn = Column(
        String,
        unique=True,
        nullable=False
    )

    title = Column(String)

    authors = Column(String)

    publisher = Column(String)

    publish_date = Column(String)

    cover_url = Column(String)