# mysite/post_api.py

from fastapi import APIRouter
from .post import Post

router = APIRouter()

# 데이터를 저장할 리스트와 번호표
posts = []
post_id = 0


# ---------------------------------------------------------
# 1. 생성 (Create) -> POST /posts
# ---------------------------------------------------------
# 주소는 /posts 로 같지만, 방식이 POST라서 겹치지 않습니다!
@router.post("/posts")
def create_post():
    global post_id
    post_id += 1
    post = Post(post_id, "제목", "내용")
    posts.append(post)
    return post


# ---------------------------------------------------------
# 2. 목록 조회 (Read List) -> GET /posts
# ---------------------------------------------------------
# 주소는 /posts 로 같지만, 방식이 GET이라서 위와 구분됩니다!
@router.get("/posts")
def read_posts():
    return posts


# ---------------------------------------------------------
# 3. 단일 조회 (Read Detail) -> GET /posts/{id}
# ---------------------------------------------------------
@router.get("/posts/{id}")
def read_post_by_id(id: int):
    for post in posts:
        if post.id == id:
            return post
    return None


# ---------------------------------------------------------
# 4. 수정 (Update) -> PUT /posts/{id}
# ---------------------------------------------------------
@router.put("/posts/{id}")
def update_post(id: int):
    for post in posts:
        if post.id == id:
            post.title = "수정된 제목"
            post.content = "수정된 내용"
            return post
    return {"message": "게시글을 찾을 수 없습니다."}


# ---------------------------------------------------------
# 5. 삭제 (Delete) -> DELETE /posts/{id}
# ---------------------------------------------------------
@router.delete("/posts/{id}")
def delete_post(id: int):
    for post in posts:
        if post.id == id:
            posts.remove(post)
            return {"message": "삭제되었습니다."}
    return {"message": "게시글을 찾을 수 없습니다."}
