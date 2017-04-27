
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="kjfamulegun",
    password="finalproject",
    hostname="kjfamulegun.mysql.pythonanywhere-services.com",
    databasename="kjfamulegun$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

@app.route("/", methods=["GET", "POST"])
def home():
    # return redirect(url_for('home'))
    return render_template("home.html")

    # if request.method == "GET":
     #   return render_template("main_page.html", comments=Comment.query.all())
    # return redirect(url_for('index'))

@app.route("/addpost", methods=["GET", "POST"])
def addpost():
    content=request.form["contents"]
    return redirect(url_for('index'))


@app.route("/timeline")
def index():
   # if request.method == "POST":
        # comment = Comment()
      #  db.session.add(comment)
       # db.session.commit()
    return render_template("main_page.html", comments=Comment.query.all())
    # return redirect(url_for('index'))