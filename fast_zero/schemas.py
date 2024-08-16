from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr

from fast_zero.models import TodoState


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState


class TodoPublic(TodoSchema):
    id: int


class TodoList(BaseModel):
    todos: list[TodoPublic]


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: TodoState | None = None


class BookSchema(BaseModel):
    id: int
    year: int
    title: str
    author: str


class BookPublic(BookSchema):
    id: int


class BookList(BaseModel):
    books: list[BookPublic]


class AuthorSchema(BaseModel):
    id: int
    name: str


class AuthorList(BaseModel):
    authors: list[AuthorSchema]


class BookUpdate(BaseModel):
    year: Optional[int] = None
    title: Optional[str] = None
