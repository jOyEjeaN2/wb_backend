from fastapi import HTTPException
import re

from models.user_model import (
    users,
    create_user,
    get_user_by_email
)


def signup(email: str, password: str, password_confirm: str, nickname: str, profile_image: str = None):

    if not email:
        raise HTTPException(400, "이메일을 입력해주세요")

    email_format = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(email_format, email):
        raise HTTPException(400, "올바른 이메일 형식입니다.")

    if get_user_by_email(email):
        raise HTTPException(400, "중복된 이메일입니다.")

    if not password:
        raise HTTPException(400, "비밀번호를 입력해주세요")

    pw_rule = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,20}$"
    if not re.match(pw_rule, password):
        raise HTTPException(400, "비밀번호 형식을 확인해주세요")

    if password != password_confirm:
        raise HTTPException(400, "비밀번호가 다릅니다.")

    if not nickname or " " in nickname or len(nickname) > 10:
        raise HTTPException(400, "닉네임 형식을 확인해주세요")

    new_user = create_user(email, password, nickname, profile_image)

    return {"message": "회원가입 완료", "user": new_user}


def login(email: str, password: str):
    if not email:
        raise HTTPException(400, "이메일을 입력해주세요")

    user = get_user_by_email(email)

    if not user or user["password"] != password:
        raise HTTPException(400, "아이디 또는 비밀번호를 확인해주세요")

    return {"message": "로그인 성공", "user_id": user["user_id"]}
