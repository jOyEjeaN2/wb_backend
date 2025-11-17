from fastapi import APIRouter
from pydantic import BaseModel
from controllers.comment_controller import (
    add_comment,
    update_comment,
    delete_comment,
    get_comments
)

router = APIRouter(prefix="/comments", tags=["Comments"])

class CommentReq(BaseModel):
    content: str


# 댓글 목록 조회
@router.get("/{post_id}")
def get_comments_route(post_id: int):
    return {"comments": get_comments(post_id)}


# 댓글 작성
@router.post("/{post_id}")
def add_comment_route(post_id: int, body: CommentReq):
    return add_comment(post_id, body.content)


# 댓글 수정
@router.put("/{comment_id}")
def update_comment_route(comment_id: int, body: CommentReq):
    return update_comment(comment_id, body.content)


# 댓글 삭제
@router.delete("/{comment_id}")
def delete_comment_route(comment_id: int):
    return delete_comment(comment_id)
