comments = []
comment_id = 1


def create_comment(post_id, content):
    global comment_id

    new_comment = {
        "id": comment_id,
        "post_id": post_id,
        "content": content
    }

    comments.append(new_comment)
    comment_id += 1
    return new_comment


def get_comments_by_post(post_id: int):
    return [c for c in comments if c["post_id"] == post_id]


def get_comment_by_id(cid: int):
    return next((c for c in comments if c["id"] == cid), None)


def update_comment_data(cid: int, content: str):
    comment = get_comment_by_id(cid)
    if comment:
        comment["content"] = content
        return comment
    return None


def delete_comment_data(cid: int):
    comment = get_comment_by_id(cid)
    if comment:
        comments.remove(comment)
        return True
    return False
