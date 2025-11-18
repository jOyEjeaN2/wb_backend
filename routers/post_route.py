from fastapi import APIRouter
from pydantic import BaseModel
from controllers.post_controller import (
    get_posts,
    create_post,
    get_post_detail,
    update_post,
    delete_post,
    toggle_like
)

router = APIRouter(prefix="/posts", tags=["Posts"])



class PostCreate(BaseModel):
    title: str
    content: str

class PostUpdate(BaseModel):
    title: str
    content: str


# 게시글 목록 조회
@router.get("")
def get_posts_route():
    return get_posts()


# 게시글 생성
@router.post("")
def create_post_route(body: PostCreate):
    return create_post(body)


# 게시글 상세 조회
@router.get("/{post_id}")
def get_post_detail_route(post_id: int):
    return get_post_detail(post_id)


# 게시글 수정
@router.put("/{post_id}")
def update_post_route(post_id: int, body: PostUpdate):
    return update_post(post_id, body)


# 게시글 삭제
@router.delete("/{post_id}")
def delete_post_route(post_id: int):
    return delete_post(post_id)


# 좋아요 토글
@router.post("/{post_id}/like")
def toggle_like_route(post_id: int):
    return toggle_like(post_id)
