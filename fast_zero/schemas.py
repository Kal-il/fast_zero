from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UsserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UsserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserDB(UsserSchema):
    id: int

class UserList(BaseModel):
    users: list[UserPublic]