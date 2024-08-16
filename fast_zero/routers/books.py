from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import Book, User
from fast_zero.schemas import BookList, BookPublic, BookSchema, BookUpdate, Message
from fast_zero.security import get_current_user

router = APIRouter(prefix='/books', tags=['books'])
Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=BookPublic)
def add_book(book: BookSchema, session: Session):
    db_book = session.scalar(select(Book).where(Book.title == book.title))

    if db_book:
        if db_book.title == book.title:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Book already exists in database',
            )
    db_book = Book(title=book.title, author=book.author, year=book.year)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)


@router.get('/', status_code=HTTPStatus.OK, response_model=BookList)
def get_book(session: Session, skip: int = 0, limit: int = 100):
    def list_books( #noqa
        session: Session,
        title: str = Query(None),
        year: int = Query(None),
        author: str = Query(None),
        limit: int = Query(None),
    ):
        query = select(Book).where


@router.get('/', response_model=BookList)
def list_books(
    session: Session,
    title: str = Query(None),
    year: int = Query(None),
    offset: int = Query(0),
    limit: int = Query(20),
):
    query = select(Book)

    if title:
        query = query.filter(Book.title.contains(title.strip().title()))

    if year:
        query = query.filter(Book.year == year)

    books = session.scalars(query.offset(offset).limit(limit)).all()

    return {'books': books}


@router.patch('/{todo_id}', response_model=BookPublic)
def patch_todo(book_id: int, session: Session, user: CurrentUser, book_update: BookUpdate):
    db_book = session.scalar(
        select(Book).where(Book.id == book_id)
    )

    if not db_book:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='book not found.')

    if book_update.title:
        sanitized_title = book_update.title.strip().title()
        existing_book = session.scalar(
            select(Book).where(Book.title == sanitized_title)
        )
        if existing_book and existing_book.id != book_id:
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='New title already exists.')

        db_book.title = sanitized_title

    if book_update.year is not None:
        db_book.year = book_update.year

    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book


@router.delete('/{book_id}', response_model=Message)
def delete_book(book_id: int, session: Session, user: CurrentUser):
    book = session.scalar(select(User).where(Book.id == book_id))
    if not book:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='book does not exists')
    session.delete(book)
    session.commit()

    return {'message': 'Book has been deleted successfully'}
