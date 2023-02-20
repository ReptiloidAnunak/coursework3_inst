from flask import Blueprint, render_template
from dao.posts_dao import PostsDAO
from dao.comments_dao import CommentDAO

blueprint_post = Blueprint("post", __name__)


@blueprint_post.route("/post/<id>")
def post_page(id):
    posts_dao = PostsDAO("./data/posts.json")
    comments_dao = CommentDAO("./data/comments.json")
    post = posts_dao.get_post_by_pk(id)
    comments = comments_dao.get_comments_by_post_id(id)
    comments_number = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_number=comments_number)


