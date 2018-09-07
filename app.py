from flask import Flask, render_template, json, request,redirect,url_for
from flaskext.mysql import MySQL

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
# mysql = MySQL()

# Data base Url here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/hazem/Desktop/FlaskApp/Sample.db'


db = SQLAlchemy(app)


# Database Name = Flask
# Database User =root
# Database Password =''
# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'Flask'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#
# mysql.init_app(app)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column('id', db.Integer, primary_key=True)
    Author = db.Column(db.String(60))
    title = db.Column(db.String(60))
    body = db.Column(db.String(200))
    def __init__(self, Author=None, title=None,body=None):
        self.Author = Author
        self.title = title
        self.body = body

# conn = mysql.connect()
# cursor = conn.cursor()

db.create_all()


@app.route("/")
def main():
    return "Home Page"

@app.route("/posts",methods=['GET'])
def posts():
    posts=Post.query.all()
    print posts
    return render_template('viewposts.html',posts=posts)
    conn.close()
    cursor.close()


@app.route('/create',methods=['GET'])
def create():
    return render_template('createposts.html')

@app.route('/store',methods=['POST'])

def store():
    post = Post(request.form['Author'], request.form['title'],request.form['body'])
    db.session.add(post)
    db.session.commit()
    #flash('Post was successfully added')
    #return redirect(url_for('show_all'))
    return redirect(url_for('posts'))










if __name__ == "__main__":
    app.run()
