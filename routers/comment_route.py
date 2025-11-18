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


@router.post("/{post_id}")
def add_comment_route(post_id: int, body: CommentReq):
    return add_comment(post_id, body.content)


@router.put("/{comment_id}")
def update_comment_route(comment_id: int, body: CommentReq):
    return update_comment(comment_id, body.content)

@router.get("/{post_id}")
def get_comments_route(post_id: int):
    return get_comments(post_id)


@router.delete("/{comment_id}")
def delete_comment_route(comment_id: int):
    return delete_comment(comment_id)
