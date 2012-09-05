from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from models import *
import context

app = Flask(__name__)
app.config.from_envvar("BLOGEX_SETTINGS_MODULE")
Context = app.config["CONTEXT_FACTORY"](app)

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        new_user = BlogexUser(
                username = request.form['username'],
                email = request.form['email'],
                password = request.form['password']
        )
        
        Context.user_repository.create(new_user)
        return redirect(url_for('login'))
    else:
        return render_template('signup_page.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        this_user = BlogexUser(username=request.form['username'])
        Context.authentication_service.login_user(this_user)
        return redirect(url_for("write_post"))
    else:
        return render_template('login.html')

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    Context.authentication_service.logout_current_user()
    return redirect(url_for("login"))

@app.route('/write/', methods=['GET', 'POST'])
@Context.authentication_service.login_required
def write_post():
    user = Context.authentication_service.get_current_user()
    if request.method == "POST":
        new_post = Post(
            title=request.form['title'],
            text=request.form['text'],
            author=user
        )       
        Context.post_repository.create(new_post)
        return redirect(url_for('blog', username=user.username))
    else:
        return render_template('write-post.html', username=user.username)

@app.route('/blog/<username>/')
def blog(username):
    blog_owner = Context.user_repository.get_by_username(username)
    return render_template('post-list.html', 
        username=username,
        posts=blog_owner.posts
    )

if __name__ == '__main__':
    app.run()
