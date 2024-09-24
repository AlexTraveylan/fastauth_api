from pydantic import BaseModel


class RegisterSchema(BaseModel):
    username: str
    password: str
    api_key: str


class LoginSchema(BaseModel):
    username: str
    password: str
