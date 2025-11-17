from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"])

# 전역(임시)
users = []

class UpdateUserRequest(BaseModel):
    nickname: str


@router.get("/{user_id}")
def get_user(user_id: int):
    # TODO: DB 조회
    user = next((u for u in users if u["id"] == user_id and u["is_active"]), None)
    if not user:
        raise HTTPException(status_code=404, detail="회원을 찾을 수 없습니다")
    return user


@router.put("/{user_id}")
def update_user(user_id: int, data: UpdateUserRequest):
    nickname = data.nickname

    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="존재하지 않는 회원입니다.")

    if not nickname:
        raise HTTPException(status_code=400, detail="닉네임을 입력해주세요.")

    if len(nickname) > 10:
        raise HTTPException(status_code=400, detail="닉네임은 최대 10자까지 작성 가능합니다.")

    # TODO: DB 닉네임 중복 체크
    if any(u["nickname"] == nickname and u["id"] != user_id for u in users):
        raise HTTPException(status_code=400, detail="중복된 닉네임입니다.")

    # TODO: DB 저장 로직
    user["nickname"] = nickname

    return {"message": "수정완료", "user": user}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="존재하지 않는 회원입니다.")

    # TODO: DB에서 soft delete
    user["is_active"] = False
    return {"message": "회원탈퇴 완료"}
