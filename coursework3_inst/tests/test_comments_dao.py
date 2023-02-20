import pytest
from dao.comments_dao import CommentDAO

COMMENT_PATH_FOR_TEST = "data/comments.json"

#Ожидаемая структура данных, множество ключей
keys_should_be = {"post_id", "commenter_name", "comment", "pk"}

#Создаю фикстуру, которая даст мне экземпляр DAO
@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentDAO(COMMENT_PATH_FOR_TEST)
    return comments_dao_instance


# Тестирую функции
class TestCommentDAO:
    def test_get_comments_all(self, comments_dao):
        """Проверяем получение всех комментариев"""
        comments = comments_dao.get_comments_all()
        assert type(comments) == list
        assert len(comments) > 0
        assert set(comments[0].keys()) == keys_should_be


    def test_get_comments_by_post_id(self, comments_dao):
        """ Проверяем получение комментариев определенного поста"""

        comments = comments_dao.get_comments_by_post_id(2)
        assert type(comments) == list, "Тип данных не совпадает"
        assert len(comments) > 0, "Постов пользователя не найдено, а они есть"
        assert set(comments[0].keys()) == keys_should_be, "Нарушена структура данных"