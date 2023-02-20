import pytest
from dao.posts_dao import PostsDAO

# Ожидаемая структура данных, множество ключей
keys_should_be = {"poster_name",
                  "poster_avatar",
                  "pic",
                  "content",
                  "views_count",
                  "likes_count",
                  "pk"}


# Создаю фикстуру, которая даст мне экземпляр DAO
@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO("data/posts.json")
    return posts_dao_instance


# Тестирую функции
class TestPostsDAO:
    def test_get_posts_all(self, posts_dao):
        """Проверяем получение всех постов"""

        posts = posts_dao.get_posts_all()
        assert type(posts) == list
        assert len(posts) > 0
        assert set(posts[0].keys()) == keys_should_be

    def test_get_posts_by_user(self, posts_dao):
        """Проверяем получение постов определенного пользователя"""

        user_posts = posts_dao.get_posts_by_user("leo")
        assert type(user_posts) == list, "Тип данных не совпадает"
        assert len(user_posts) > 0, "Постов пользователя не найдено"
        assert set(user_posts[0].keys()) == keys_should_be, "Нарушена структура данных"

    def test_search_for_posts(self, posts_dao):
        """Проверяем получение списка постов по ключевому слову"""

        found_posts = posts_dao.search_for_posts("еда")
        assert type(found_posts) == list, "Тип данных не совпадает"
        assert len(found_posts) > 0, "Постов пользователя не найдено"
        assert set(found_posts[0].keys()) == keys_should_be, "Нарушена структура данных"

    def test_get_post_by_pk(self, posts_dao):
        """Проверяем получение поста по его идентификатору"""
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict
        assert post["pk"] == 1
        assert set(post.keys()) == keys_should_be, "Нарушена структура данных"
