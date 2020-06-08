from app import database
from app.forumposts import posts
from flask import url_for, flash, redirect, abort
from flask_login import current_user, login_required
from app.models import Post

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    current_post = Post.query.get_or_404(post_id)
    if current_user != current_post.author:
        abort(403)
    database.session.delete(current_post)
    database.session.commit()
    flash('The post has been deleted!', 'success')
    return redirect(url_for('main.home'))