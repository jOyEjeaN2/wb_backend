from fastapi import HTTPException
import re
from models.user_model import (
    get_user_by_id,
    update_user_nickname,
    update_user_password,
    delete_user_data,
)


def update_profile(user_id: int, nickname: str):
    if not nickname:
        raise HTTPException(400, "닉네임을 입력해주세요")

    if " " in nickname:
        raise HTTPException(400, "띄어쓰기를 없애주세요")

    if len(nickname) > 10:
        raise HTTPException(400, "닉네임은 최대 10자까지")

    updated = update_user_nickname(user_id, nickname)
    if updated:
        return {"message": "수정완료", "updated_nickname": updated["nickname"]}

    raise HTTPException(404, "유저를 찾을 수 없습니다.")


def update_password(user_id: int, password: str, password_confirm: str):
    if not password or not password_confirm:
        raise HTTPException(400, "비밀번호를 입력해주세요")

    if password != password_confirm:
        raise HTTPException(400, "비밀번호가 다릅니다.")

    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,20}$"
    if not re.match(pattern, password):
        raise HTTPException(400, "비밀번호 형식을 확인해주세요")

    updated = update_user_password(user_id, password)
    if updated:
        return {"message": "수정완료", "updated_password": updated["password"]}

    raise HTTPException(404, "유저를 찾을 수 없습니다.")


def logout():
    return {"message": "로그아웃 완료"}


def delete_user(user_id: int):
    if delete_user_data(user_id):
        return {"message": "회원탈퇴 완료"}

    raise HTTPException(404, "유저를 찾을 수 없습니다.")
