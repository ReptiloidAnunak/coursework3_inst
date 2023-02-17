from flask import Blueprint, jsonify
from dao.posts_dao import PostsDAO
import logging
from logger_api import logger_api



posts_dao = PostsDAO("./data/posts.json")

api_bluebrint = Blueprint("api_bluebrint", __name__)

@api_bluebrint.route("/api/posts/")
def all_posts_api():
    logger_api.info('Запрос /api/posts')
    posts = posts_dao.get_posts_all()
    return jsonify(posts), 200

@api_bluebrint.route("/api/posts/<int:id>")
def post_api(id):
    post = posts_dao.get_post_by_pk(id)
    logger_api.info(f'Запрос /api/posts/{id}')
    return jsonify(post), 200
