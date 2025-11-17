from fastapi import HTTPException
import re


def update_profile(nickname: str):
    if not nickname:
        raise HTTPException(400, "닉네임을 입력해주세요")

    if " " in nickname:
        raise HTTPException(400, "띄어쓰기를 없애주세요")

    if len(nickname) > 10:
        raise HTTPException(400, "닉네임은 최대 10자까지 작성 가능합니다")

    # TODO: 닉네임 중복 확인(DB)
    return {"message": "수정완료"}


def update_password(password: str, confirm_password: str):
    if not password:
        raise HTTPException(400, "비밀번호를 입력해주세요")

    if not confirm_password:
        raise HTTPException(400, "비밀번호를 한 번 더 입력해주세요")

    if password != confirm_password:
        raise HTTPException(400, "비밀번호가 다릅니다.")

    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,20}$"
    if not re.match(pattern, password):
        raise HTTPException(
            400,
            "비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다.",
        )

    # TODO: DB에 비밀번호 반영
    return {"message": "수정완료"}


def logout():
    return {"message": "로그아웃 완료"}


def delete_user():
    # TODO: DB에서 계정 삭제
    return {"message": "회원탈퇴 완료"}
