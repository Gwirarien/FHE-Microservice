from app import database
from app.forumposts import posts
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from app.models import Post
from app.forumposts.forum_forms import ForumPostForm

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    current_post = Post.query.get_or_404(post_id)
    if current_post.author != current_user:
        abort(403)
    post_form = ForumPostForm()
    if request.method == 'GET':
        post_form.title.data = current_post.title
        post_form.content.data = current_post.content
    elif post_form.validate_on_submit():
        current_post.title = post_form.title.data
        current_post.content = post_form.content.data
        database.session.commit()
        flash('The post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=current_post.id))
    return render_template('create_post.html', title='Update Post', form=post_form, legend='Update Post')