from fastapi import APIRouter
from controllers.user_controller import (
    update_profile,
    update_password,
    logout,
    delete_user,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.put("/profile")
def update_profile_route(nickname: str):
    return update_profile(nickname)


@router.put("/password")
def update_password_route(password: str, confirm_password: str):
    return update_password(password, confirm_password)


@router.post("/logout")
def logout_route():
    return logout()


@router.delete("/delete")
def delete_user_route():
    return delete_user()
