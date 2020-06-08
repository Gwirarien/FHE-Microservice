from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.models import Post
from app.main import main

@login_required
@main.route("/forum")
def forum():
    if current_user.is_authenticated:
        # Always display the first page of the forum - post will be shown in a chronological order 
        display_page = request.args.get('page', 1, type=int)
        current_posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=display_page, per_page=5)
        
        return render_template('forum.html', posts=current_posts)
    return redirect(url_for('users.login'))