from app import database
from app.forumposts import posts
from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_required
from app.models import Post
from app.forumposts.forum_forms import ForumPostForm

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def create_post():
    post_form = ForumPostForm()
    if post_form.validate_on_submit():
        new_post = Post(title=post_form.title.data, content=post_form.content.data, author=current_user)
        database.session.add(new_post)
        database.session.commit()
        flash('The post has been created!', 'success')
        return redirect(url_for('main.forum'))
    return render_template('create_post.html', title='New post', form=post_form, legend='New post')