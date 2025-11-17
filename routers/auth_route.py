from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re

router = APIRouter(prefix="/auth", tags=["Auth"])

# 임시 DB
users = []
user_auto_id = 1

EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
PASSWORD_REGEX = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,20}$"
)

class RegisterRequest(BaseModel):
    email: str
    password: str
    password_confirm: str
    nickname: str

class LoginRequest(BaseModel):
    email: str
    password: str


def validate_email(email: str):
    if not email or len(email) < 6 or not EMAIL_REGEX.match(email):
        raise HTTPException(status_code=400, detail="올바른 이메일 주소 형식을 입력해주세요. (예: example@example.com)")


def validate_password(password: str):
    if not password:
        raise HTTPException(status_code=400, detail="비밀번호를 입력해주세요")
    if not PASSWORD_REGEX.match(password):
        raise HTTPException(
            status_code=400,
            detail="비밀번호는 9자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다."
        )


@router.post("/register")
def register(data: RegisterRequest):
    global user_auto_id

    email = data.email
    password = data.password
    password_confirm = data.password_confirm
    nickname = data.nickname

    validate_email(email)
    validate_password(password)

    if password != password_confirm:
        raise HTTPException(status_code=400, detail="비밀번호가 다릅니다.")

    # TODO: DB에서 이메일 중복 조회
    if any(u["email"] == email for u in users):
        raise HTTPException(status_code=400, detail="중복된 이메일입니다.")

    if not nickname:
        raise HTTPException(status_code=400, detail="닉네임을 입력해주세요")

    if len(nickname) > 10:
        raise HTTPException(status_code=400, detail="닉네임은 최대 10자까지 작성 가능합니다")

    # TODO: DB에서 닉네임 중복 체크
    if any(u["nickname"] == nickname for u in users):
        raise HTTPException(status_code=400, detail="중복된 닉네임입니다")

    # TODO: DB 저장 로직
    new_user = {
        "id": user_auto_id,
        "email": email,
        "password": password,
        "nickname": nickname,
        "profile_image": None,
        "is_active": True
    }

    users.append(new_user)
    user_auto_id += 1

    return {"message": "회원가입 성공", "user": new_user}


@router.post("/login")
def login(data: LoginRequest):
    email = data.email
    password = data.password

    validate_email(email)
    validate_password(password)

    # TODO: DB에서 사용자 조회
    user = next((u for u in users if u["email"] == email and u["is_active"]), None)

    if not user or user["password"] != password:
        raise HTTPException(status_code=400, detail="아이디 또는 비밀번호를 확인해주세요")

    return {"message": "로그인 성공", "user_id": user["id"]}