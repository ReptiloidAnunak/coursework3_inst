import json
from dao.posts_dao import PostsDAO

COMMENT_PATH = "./data/posts.json"

class CommentDAO:
    def __init__(self, path):
        self.path = path

    def get_comments_all(self):
        """Загружает все комментарии из файла"""
        with open(self.path, "r", encoding="utf-8") as file:
            posts = json.load(file)
        return posts

    def get_comments_by_post_id(self, post_id):
        """ Возвращает комментарии определенного поста"""

        comments_base = self.get_comments_all()
        post_comments = []
        post_id = int(post_id)

        for comment in comments_base:
            if post_id == comment["post_id"]:
                post_comments.append(comment)
        return post_comments
