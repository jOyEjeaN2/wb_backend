from fastapi import APIRouter
from pydantic import BaseModel
from controllers.comment_controller import (
    add_comment,
    update_comment,
    delete_comment,
)

router = APIRouter(prefix="/comments", tags=["Comments"])


class CommentReq(BaseModel):
    content: str


@router.post("/{post_id}")
def add_comment_route(post_id: int, body: CommentReq):
    return add_comment(post_id, body.content)


@router.put("/{comment_id}")
def update_comment_route(comment_id: int, body: CommentReq):
    return update_comment(comment_id, body.content)


@router.delete("/{comment_id}")
def delete_comment_route(comment_id: int):
    return delete_comment(comment_id)
