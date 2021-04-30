from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)


db.create_all()


@app.route('/posts', methods=["GET", "POST", "DELETE"])
def hello_world():
    if request.method == "GET":
        posts = {}
        for post in Post.query.all():
            posts[post.id] = post.text
        return posts
    elif request.method == "POST":
        new_post = Post(text=request.form.get("text"))
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('static', filename='index.html'))
    elif request.method == "DELETE":
        post_id = request.json['id']
        Post.query.filter_by(id=post_id).delete()
        db.session.commit()
        return '', 200
