from fastapi import HTTPException
from datetime import datetime

from controllers.comment_controller import comments

# ------------ 임시 DB ------------
posts = []
post_id_counter = 1
# --------------------------------


def create_post(data):
    global post_id_counter

    # 제목/내용 빈값 검사
    if not data.title or not data.content:
        raise HTTPException(400, "제목, 내용을 모두 작성해주세요")

    if len(data.title) > 26:
        raise HTTPException(400, "제목 최대 26자까지 입력 가능합니다")

    new_post = {
        "id": post_id_counter,
        "title": data.title,
        "content": data.content,
        "image" : data.image,
        "created_at" : datetime.now().isoformat(),
        "views": 0,
        "likes": 0
    }

    posts.append(new_post)
    post_id_counter += 1

    return {"message": "게시글 등록 완료", "post": new_post}


def get_posts(page: int =1, size: int = 10):
    # return {"posts": posts}

    start = (page -1) * size
    end = start + size

    sliced = posts[start:end]

    result = []
    for post in posts:
        comment_count = sum(1 for c in comments if c["post_id"] == post["id"])
        post_data = post.copy()
        post_data["comments_count"] = comment_count
        result.append(post_data)
    return {
        "page" : page,
        "size" : size,
        "posts": result
    }

def get_post_detail(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            post["views"] += 1
            return post
    raise HTTPException(404, "게시글을 찾을 수 없습니다")


def update_post(post_id: int, data):
    for post in posts:
        if post["id"] == post_id:

            if len(data.title) > 26:
                raise HTTPException(400, "제목 최대 26자까지 작성 가능합니다")

            post["title"] = data.title
            post["content"] = data.content

            return {"message": "게시글 수정 완료", "post": post}

    raise HTTPException(404, "게시글을 찾을 수 없습니다")


def delete_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            return {"message": "게시글 삭제 완료"}

    raise HTTPException(404, "게시글을 찾을 수 없습니다")

def toggle_like(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            # 좋아요 +1 / -1 토글
            if post["likes"] == 0:
                post["likes"] += 1
                return {"message": "좋아요 추가", "likes": post["likes"]}
            else:
                post["likes"] -= 1
                return {"message": "좋아요 취소", "likes": post["likes"]}

    raise HTTPException(404, "게시글을 찾을 수 없습니다")
