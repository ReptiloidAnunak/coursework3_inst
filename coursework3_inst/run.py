from flask import Flask, render_template, Blueprint
from blueprint_main.main_view import blueprint_main
from blueprint_post.post_view import blueprint_post
from blueprint_user.user_view import blueprint_user
from blueprint_api.api_view import api_bluebrint

app = Flask(__name__)

app.register_blueprint(blueprint_main)
app.register_blueprint(blueprint_post)
app.register_blueprint(blueprint_user)
app.register_blueprint(api_bluebrint)



@app.errorhandler(404)
def not_found_error(error):
    return render_template('Error_404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("Error_500.html"), 500

if __name__ == "__main__":
        app.run()
