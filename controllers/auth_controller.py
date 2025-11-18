from fastapi import HTTPException
import re


users = []
user_id = 1

def signup(email: str, password: str, password_confirm: str, nickname: str, profile_image: str = None):
    global user_id

    # 이메일 검사
    if not email:
        raise HTTPException(400, "이메일을 입력해주세요")

    email_allowed = r"^[A-Za-z0-9@.]+$"
    if not re.match(email_allowed, email):
        raise HTTPException(400, "올바른 이메일 주소 형식을 입력해주세요. (예: example@example.com)")

    email_format = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(email_format, email):
        raise HTTPException(400, "올바른 이메일 주소 형식을 입력해주세요. (예: example@example.com)")

    # 이메일 중복 확인 (DB)
    for u in users:
        if u["email"] == email:
            raise HTTPException(400, "중복된 이메일입니다.")

    # 비밀번호 검사
    if not password:
        raise HTTPException(400, "비밀번호를 입력해주세요")

    pw_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,20}$"
    if not re.match(pw_pattern, password):
        raise HTTPException(
            400,
            "비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다.",
        )

    if not password_confirm:
        raise HTTPException(400, "비밀번호를 한 번 더 입력해주세요")

    if password != password_confirm:
        raise HTTPException(400, "비밀번호가 다릅니다.")

    # 닉네임 검사
    if not nickname:
        raise HTTPException(400, "닉네임을 입력해주세요")

    if " " in nickname:
        raise HTTPException(400, "띄어쓰기를 없애주세요")

    if len(nickname) > 10:
        raise HTTPException(400, "닉네임은 최대 10자까지 작성 가능합니다")

    # 닉네임 중복 확인 (DB)
    for u in users:
        if u["nickname"] == nickname:
            raise HTTPException(400, "중복된 닉네임입니다")

    new_user = {
        "user_id" : user_id,
        "email": email,
        "password": password,
        "nickname": nickname,
        "profile_image": profile_image
    }
    users.append(new_user)
    user_id += 1

    return {"message": "회원가입 완료", "user": new_user}


def login(email: str, password: str):
    if not email:
        raise HTTPException(400, "올바른 이메일 주소 형식을 입력해주세요. (예: example@example.com)")

    email_format = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(email_format, email):
        raise HTTPException(400, "올바른 이메일 주소 형식을 입력해주세요. (예: example@example.com)")

    if not password:
        raise HTTPException(400, "비밀번호를 입력해주세요")

    pw_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{9,20}$"
    if not re.match(pw_pattern, password):
        raise HTTPException(
            400,
            "비밀번호는 9자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다.",
        )
    for u in users:
        if u["email"] == email and u["password"] == password:
            return {"message": "로그인 성공"}

    # 이메일 또는 비밀번호 불일치 시
    raise HTTPException(400, "아이디 또는 비밀번호를 확인해주세요")
