from fastapi import APIRouter
from pydantic import BaseModel
from controllers.auth_controller import signup, login

router = APIRouter(prefix="/auth", tags=["Auth"])


class SignupReq(BaseModel):
    email: str
    password: str
    password_confirm: str
    nickname: str


class LoginReq(BaseModel):
    email: str
    password: str


@router.post("/signup")
def signup_route(body: SignupReq):
    return signup(body.email, body.password, body.password_confirm, body.nickname)


@router.post("/login")
def login_route(body: LoginReq):
    return login(body.email, body.password)
