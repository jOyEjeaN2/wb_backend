from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/posts", tags=["Posts"])

# 전역
posts = []
likes = []
post_auto_id = 1

class CreatePostRequest(BaseModel):
    title: str
    content: str
    author_id: int

class UpdatePostRequest(BaseModel):
    title: str
    content: str

class ToggleLikeRequest(BaseModel):
    user_id: int


@router.get("/")
def list_posts():
    # TODO: DB 조회
    return posts


@router.post("/")
def create_post(data: CreatePostRequest):
    global post_auto_id

    if not data.title or not data.content:
        raise HTTPException(status_code=400, detail="제목, 내용을 모두 작성해주세요")

    if len(data.title) > 26:
        raise HTTPException(status_code=400, detail="제목은 최대 26자까지 작성 가능합니다")

    new_post = {
        "id": post_auto_id,
        "title": data.title,
        "content": data.content,
        "image": None,
        "author_id": data.author_id,
        "view_count": 0,
        "like_count": 0,
        "comment_count": 0,
    }

    # TODO: DB 저장 로직
    posts.append(new_post)
    post_auto_id += 1

    return new_post


@router.get("/{post_id}")
def post_detail(post_id: int):
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")

    # 조회수 증가
    post["view_count"] += 1
    return post


@router.put("/{post_id}")
def update_post(post_id: int, data: UpdatePostRequest):
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="게시글 없음")

    if len(data.title) > 26:
        raise HTTPException(status_code=400, detail="제목은 최대 26자까지 작성 가능합니다")

    # TODO: DB 업데이트 로직
    post["title"] = data.title
    post["content"] = data.content

    return post


@router.delete("/{post_id}")
def delete_post(post_id: int):
    global posts

    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="게시글 없음")

    # TODO: DB 삭제 로직
    posts = [p for p in posts if p["id"] != post_id]

    return {"message": "삭제 완료"}


@router.post("/{post_id}/like")
def toggle_like(post_id: int, data: ToggleLikeRequest):
    user_id = data.user_id

    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="게시글 없음")

    key = (post_id, user_id)

    if key in likes:
        likes.remove(key)
        post["like_count"] -= 1
        return {"liked": False, "like_count": post["like_count"]}

    likes.append(key)
    post["like_count"] += 1
    return {"liked": True, "like_count": post["like_count"]}
