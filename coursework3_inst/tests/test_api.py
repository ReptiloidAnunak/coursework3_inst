import logger_api
from run import app

post_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
def test_api_all_posts():
    """Проверяет структуру данных API всех постов"""

    response = app.test_client().get("/api/posts/", follow_redirects=True)
    response.status_code == 200, "Test test_api_all_posts: Posts API is not loaded"
    logger_api.logger_api.info("Test test_api_all_posts: Posts API loaded")
    answer_keys = set(response.json[0].keys())
    logger_api.logger_api.info(f'Тип полученных данных: {type(response.json)}')
    logger_api.logger_api.info("Test test_api_all_posts: Response structure is correct\n")
    response.mimetype == "application/json", "Получен не JSON"
    assert answer_keys == post_keys, "Полученные ключи не совпадают"
    assert type(response.json) == list, "Получен не список"




def test_api_post():
    """Проверяет структуру данных API одного поста"""

    params = 1
    response = app.test_client().get(f"/api/posts/{params}")
    response.status_code == 200, "Test test_api_post: Unique post is not loaded"
    logger_api.logger_api.info("Test test_api_post: Unique post loaded")
    logger_api.logger_api.info(f'Тип полученных данных: {type(response.json)}')
    logger_api.logger_api.info("Test test_api_post: Response structure is correct\n")


    answer_keys = set(response.json.keys())
    assert answer_keys == post_keys, "Полученные ключи не совпадают"
    response.mimetype == "application/json", "Получен не JSON"
    assert type(response.json) == dict, "Получен не словарь"





