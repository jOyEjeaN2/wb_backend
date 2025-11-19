from fastapi import HTTPException
from models.post_model import (
    create_post_data,
    posts,
    get_post_by_id,
    update_post_data,
    delete_post_data
)
from models.comment_model import comments


def create_post(data):
    if not data.title or not data.content:
        raise HTTPException(400, "제목, 내용을 모두 작성해주세요")

    if len(data.title) > 26:
        raise HTTPException(400, "제목 최대 26자")

    new_post = create_post_data(data.title, data.content, data.image)
    return {"message": "게시글 등록 완료", "post": new_post}


def get_posts(page: int = 1, size: int = 10):
    start = (page - 1) * size
    end = start + size

    sliced = posts[start:end]

    result = []
    for post in sliced:
        comment_count = sum(1 for c in comments if c["post_id"] == post["id"])
        p = post.copy()
        p["comments_count"] = comment_count
        result.append(p)

    return {"page": page, "size": size, "posts": result}


def get_post_detail(post_id: int):
    post = get_post_by_id(post_id)

    if not post:
        raise HTTPException(404, "게시글을 찾을 수 없습니다")

    post["views"] += 1
    return post


def update_post(post_id: int, data):
    if len(data.title) > 26:
        raise HTTPException(400, "제목 최대 26자")

    updated = update_post_data(post_id, data.title, data.content)
    if updated:
        return {"message": "게시글 수정 완료", "post": updated}

    raise HTTPException(404, "게시글을 찾을 수 없습니다")


def delete_post(post_id: int):
    if delete_post_data(post_id):
        return {"message": "게시글 삭제 완료"}

    raise HTTPException(404, "게시글을 찾을 수 없습니다")


def toggle_like(post_id: int):
    post = get_post_by_id(post_id)
    if not post:
        raise HTTPException(404, "게시글을 찾을 수 없습니다")

    if post["likes"] == 0:
        post["likes"] = 1
        return {"message": "좋아요 추가", "likes": 1}

    post["likes"] = 0
    return {"message": "좋아요 취소", "likes": 0}
