from flask import Blueprint, render_template
from dao.posts_dao import PostsDAO

blueprint_user = Blueprint("blueprint_user", __name__)
@blueprint_user.route("/users/<username>")
def user_posts(username):
    username = username.strip().lower()
    posts_dao = PostsDAO("./data/posts.json")
    posts = posts_dao.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, username=username)
