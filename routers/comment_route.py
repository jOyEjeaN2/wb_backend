from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from routers.post_route import posts

router = APIRouter(prefix="/comments", tags=["Comments"])

# 전역
comments = []
comment_auto_id = 1

class CreateCommentRequest(BaseModel):
    post_id: int
    author_id: int
    content: str

class UpdateCommentRequest(BaseModel):
    content: str


@router.post("/")
def write_comment(data: CreateCommentRequest):
    global comment_auto_id

    post = next((p for p in posts if p["id"] == data.post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="게시글 없음")

    if not data.content:
        raise HTTPException(status_code=400, detail="댓글 내용을 입력해주세요")

    new_comment = {
        "id": comment_auto_id,
        "post_id": data.post_id,
        "author_id": data.author_id,
        "content": data.content
    }

    # TODO: DB 저장 로직
    comments.append(new_comment)
    post["comment_count"] += 1
    comment_auto_id += 1

    return new_comment


@router.put("/{comment_id}")
def update_comment(comment_id: int, data: UpdateCommentRequest):
    comment = next((c for c in comments if c["id"] == comment_id), None)
    if not comment:
        raise HTTPException(status_code=404, detail="댓글 없음")

    if not data.content:
        raise HTTPException(status_code=400, detail="댓글 내용을 입력해주세요")

    # TODO: DB 업데이트
    comment["content"] = data.content

    return comment


@router.delete("/{comment_id}")
def delete_comment(comment_id: int):
    global comments

    comment = next((c for c in comments if c["id"] == comment_id), None)
    if not comment:
        raise HTTPException(status_code=404, detail="댓글 없음")

    # TODO: DB 삭제
    comments = [c for c in comments if c["id"] != comment_id]

    return {"message": "댓글 삭제 완료"}
