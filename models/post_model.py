from datetime import datetime

posts = []
post_id = 1


def create_post_data(title, content, image):
    global post_id

    new_post = {
        "id": post_id,
        "title": title,
        "content": content,
        "image": image,
        "created_at": datetime.now().isoformat(),
        "views": 0,
        "likes": 0
    }

    posts.append(new_post)
    post_id += 1
    return new_post


def get_post_by_id(pid: int):
    return next((p for p in posts if p["id"] == pid), None)


def update_post_data(pid: int, title, content):
    post = get_post_by_id(pid)
    if post:
        post["title"] = title
        post["content"] = content
        return post
    return None


def delete_post_data(pid: int):
    post = get_post_by_id(pid)
    if post:
        posts.remove(post)
        return True
    return False
