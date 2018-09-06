from flask import Flask, render_template, json, request,redirect
from flaskext.mysql import MySQL

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
mysql = MySQL()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/Flask'


# db = SQLAlchemy(app)




# Database Name = Flask
# Database User =root
# Database Password =''
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Flask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


# class Post(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column('id', db.Integer, primary_key=True)
#     Author = db.Column(db.String(60))
#     title = db.Column(db.String)
#     body = db.Column(db.String)

conn = mysql.connect()
cursor = conn.cursor()




@app.route("/")
def main():
    return "Home Page"

@app.route("/posts",methods=['GET'])
def posts():

    cursor.execute("SELECT * from posts")
    data = cursor.fetchall()
    print data

    return render_template('viewposts.html',posts=data)
    conn.close()
    cursor.close()


@app.route('/create',methods=['GET'])
def create():
    return render_template('createposts.html')

@app.route('/store',methods=['POST'])

def store():
      result = request.form
      Author = result['Author']
      title = result['title']
      body =result['body']
      cursor.execute('INSERT INTO posts (Author,title,body) VALUES (%s, %s,%s)', (Author, title,body))
      conn.commit();
      return redirect("/posts", code=200)
      cursor.close()









if __name__ == "__main__":
    app.run()
