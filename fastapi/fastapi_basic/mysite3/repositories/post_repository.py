from mysite3.schemas.post import Post


class PostRepository:
    def __init__(self):
        # 데이터베이스 연결
        self.posts = []
        self.post_id = 0

    def save(self, new_post: Post):
        # <-- db를 사용하면 없어질 로직
        self.post_id += 1
        new_post.id = self.post_id
        # -->

        self.posts.append(new_post)
        return new_post

    def find_all(self):
        return self.posts

    def find_by_id(self, id: int):
        for post in self.posts:
            # 해당하는 id가 있는 경우에는 post를 return.
            if post.id == id:
                return post
        return None


post_repository = PostRepository()
