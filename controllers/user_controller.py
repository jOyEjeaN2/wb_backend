from fastapi import HTTPException
import re

from controllers.auth_controller import users, user_id


def update_profile(user_id: int, nickname: str):
    if not nickname:
        raise HTTPException(400, "닉네임을 입력해주세요")

    if " " in nickname:
        raise HTTPException(400, "띄어쓰기를 없애주세요")

    if len(nickname) > 10:
        raise HTTPException(400, "닉네임은 최대 10자까지 작성 가능합니다")

    for user in users:
        if user["nickname"] == nickname and user["user_id"] != user_id:
            raise HTTPException(400, "중복된 닉네임입니다")

    # DB에 닉네임 업데이트
    for user in users:
        if user["user_id"] == user_id:
            user["nickname"] = nickname
            return {
                "message": "수정완료",
                "updated_nickname": user["nickname"]
            }

    raise HTTPException(404, "유저를 찾을 수 없습니다.")


def update_password(user_id: int, password: str, password_confirm: str):
    if not password:
        raise HTTPException(400, "비밀번호를 입력해주세요")

    if not password_confirm:
        raise HTTPException(400, "비밀번호를 한 번 더 입력해주세요")

    if password != password_confirm:
        raise HTTPException(400, "비밀번호가 다릅니다.")

    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,20}$"
    if not re.match(pattern, password):
        raise HTTPException(
            400,
            "비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다.",
        )

    # DB에 비밀번호 반영
    for user in users:
        if user["user_id"] == user_id:
            user["password"] = password
            return {
                "message": "수정완료",
                "updated_password": user["password"]
            }

    raise HTTPException(404, "유저를 찾을 수 없습니다.")


def logout():
    return {"message": "로그아웃 완료"}


def delete_user(user_id : int):
    # DB에서 계정 삭제
    for idx, user in enumerate(users):
        if user["user_id"] == user_id:
            del users[idx]
            return {"message": "회원탈퇴 완료"}

    raise HTTPException(404, "유저를 찾을 수 없습니다.")
