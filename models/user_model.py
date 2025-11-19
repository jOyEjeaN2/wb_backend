users = []
user_id = 1   # 자동 증가 ID


def create_user(email, password, nickname, profile_image=None):
    global user_id

    new_user = {
        "user_id": user_id,
        "email": email,
        "password": password,
        "nickname": nickname,
        "profile_image": profile_image
    }

    users.append(new_user)
    user_id += 1
    return new_user


def get_user_by_email(email: str):
    return next((u for u in users if u["email"] == email), None)


def get_user_by_id(uid: int):
    return next((u for u in users if u["user_id"] == uid), None)


def update_user_nickname(uid: int, new_nickname: str):
    user = get_user_by_id(uid)
    if user:
        user["nickname"] = new_nickname
        return user
    return None


def update_user_password(uid: int, new_password: str):
    user = get_user_by_id(uid)
    if user:
        user["password"] = new_password
        return user
    return None


def delete_user_data(uid: int):
    user = get_user_by_id(uid)
    if user:
        users.remove(user)
        return True
    return False
