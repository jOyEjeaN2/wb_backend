from fastapi import HTTPException

# 임시 DB
comments = []
comment_id_counter = 1


def add_comment(post_id: int, content: str):
    global comment_id_counter

    if not content:
        raise HTTPException(400, "댓글을 입력해주세요")

    new_comment = {
        "id": comment_id_counter,
        "post_id": post_id,
        "content": content
    }

    comments.append(new_comment)
    comment_id_counter += 1

    return {"message": "댓글 등록 완료", "comment": new_comment}


def update_comment(comment_id: int, content: str):
    for c in comments:
        if c["id"] == comment_id:
            if not content:
                raise HTTPException(400, "댓글을 입력해주세요")

            c["content"] = content
            return {"message": "댓글 수정 완료", "comment": c}

    raise HTTPException(404, "댓글을 찾을 수 없습니다")


def delete_comment(comment_id: int):
    for c in comments:
        if c["id"] == comment_id:
            comments.remove(c)
            return {"message": "댓글 삭제 완료"}

    raise HTTPException(404, "댓글을 찾을 수 없습니다")


def get_comments(post_id: int):
    return [c for c in comments if c["post_id"] == post_id]

