import json

class PostsDAO:
    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        """Загружает все посты из файла"""
        with open(self.path, "r", encoding="utf-8") as file:
            posts = json.load(file)
        return posts

    def get_posts_by_user(self, username):
        """Возвращает посты определенного пользователя"""
        username = str(username).strip().lower()
        posts_base = self.get_posts_all()
        users_posts = []

        for post in posts_base:
            if username == post["poster_name"]:
                users_posts.append(post)

        if users_posts == []:
            raise ValueError

        return users_posts
    #
    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову"""

        query = str(query).strip().lower()
        posts_base = self.get_posts_all()
        found_posts = []

        for post in posts_base:
            post["content"] = post["content"].lower()
            if query in post["content"]:
                found_posts.append(post)
        return found_posts
    #
    def get_post_by_pk(self, pk):
        """Возвращает один пост по его идентификатору"""
        pk = int(pk)
        posts_base = self.get_posts_all()

        for post in posts_base:
            if pk == post["pk"]:
                return post
