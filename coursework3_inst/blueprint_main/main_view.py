from flask import Blueprint, render_template, request
from dao.posts_dao import PostsDAO


blueprint_main = Blueprint("blueprint_main", __name__)


@blueprint_main.route("/")
def index_page():
    posts_dao = PostsDAO("./data/posts.json")
    posts = posts_dao.get_posts_all()
    return render_template("index.html", posts=posts)



@blueprint_main.route("/search")
def page_tag():
    posts_dao = PostsDAO("./data/posts.json")
    substring = request.values.get("s")
    posts = posts_dao.search_for_posts(substring)
    posts_number = len(posts)
    return render_template("search.html", posts=posts, posts_number=posts_number)
