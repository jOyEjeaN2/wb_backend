from fastapi import HTTPException
from models.comment_model import (
    create_comment,
    get_comments_by_post,
    update_comment_data,
    delete_comment_data
)


def add_comment(post_id: int, content: str):
    if not content:
        raise HTTPException(400, "댓글을 입력해주세요")

    comment = create_comment(post_id, content)
    return {"message": "댓글 등록 완료", "comment": comment}


def update_comment(comment_id: int, content: str):
    if not content:
        raise HTTPException(400, "댓글을 입력해주세요")

    updated = update_comment_data(comment_id, content)
    if updated:
        return {"message": "댓글 수정 완료", "comment": updated}

    raise HTTPException(404, "댓글을 찾을 수 없습니다")


def delete_comment(comment_id: int):
    if delete_comment_data(comment_id):
        return {"message": "댓글 삭제 완료"}

    raise HTTPException(404, "댓글을 찾을 수 없습니다")


def get_comments(post_id: int):
    return get_comments_by_post(post_id)
