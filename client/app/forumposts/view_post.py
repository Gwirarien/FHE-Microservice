from app.forumposts import posts
from flask import render_template, abort
from flask_login import current_user
from app.models import Post

@posts.route("/post/<int:post_id>")
def post(post_id):
    if current_user.is_authenticated:
        current_post = Post.query.get_or_404(post_id)
        return render_template('post.html', title=current_post.title, post=current_post)
    else:
        abort(403)