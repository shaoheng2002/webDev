#encoding: utf-8
from flask import Flask, session, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import config
from exts import db
from models import User
from decorators import login_required
from datetime import datetime


app = Flask(__name__)
app.config.from_object(config)


from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy(app)
db.init_app(app)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    phone = db.Column(db.Text(11), nullable = False)
    username = db.Column(db.Text(50), nullable= False)
    password = db.Column(db.Text(100), nullable= False)

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref = db.backref('questions'))

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    comment = db.Column(db.Text(), nullable = False)

    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    comment_author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)

    question = db.relationship('Question', backref = db.backref('question'))#, backref=db('question'))
    comment_author = db.relationship('User', backref=db.backref('question'))



db.create_all()

@app.route('/1')
def add():
    user1 = User(phone='123', username='ss', password='123')
    db.session.add(user1)
    db.session.commit()
    return 'added'


@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by('-create_time').all()
    }
    # print (context['question'].title)
    return render_template('index.html', **context)

@app.route('/profile/')
@login_required
def profile():
    user_id = session.get('user_id')
    context={
        'profile':User.query.filter(User.id==user_id).first()
    }
    return render_template('profile.html', **context)

@app.route('/detail/<question_id>')
def detail(question_id):
    question_model = Question.query.filter(Question.id ==question_id).first()
    return render_template('detail.html', question=question_model)


@app.route("/add_comment", methods=['GET', 'POST'])
@login_required
def add_comment():
    comment_content = request.form.get('comment_content')
    question_id = request.form.get('question_id')
    comment = Comment(comment=comment_content, question_id=question_id)
    user_id= session.get('user_id')
    user = User.query.filter(User.id==user_id).first()
    comment.comment_author_id = user.id
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))

@app.route("/logout/", methods=['GET', 'POST'])
def logout():
    session.pop('user_id')
    flash(f"You have logged out", "success")
    return render_template('login.html')



@app.route("/question/", methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        user_id= session.get('user_id')
        user = User.query.filter(User.id== user_id).first()
        question= Question(title = title, content= content)

        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))



@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone = request.form.get('phone')
        password = request.form.get('password')

        user = User.query.filter(User.phone == phone, User.password==password).first()

        if user:
            session['user_id'] = user.id
            flash("Login success", "success")
            print (user.username, user.password)
            return redirect(url_for('index'))
        else:
            flash(f"phone number or Password are not correct, please register first!", 'warning')
            return render_template('Reg.html')


@app.route('/Reg/', methods=['GET', 'POST'])
def Reg():
    if request.method == 'GET':
        return render_template('Reg.html')
    else:
        phone = request.form.get('phone')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter(User.phone == phone).first()
        if user:
            flash(f"Phone number already exist!", "warning")
            return render_template(url_for('Reg'))
        else:
                userAdded = User(phone=phone, username=username, password=password)
                db.session.add(userAdded)
                db.session.commit()
                flash(f"Registration success!", "success")
                return render_template('login.html')


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}

if __name__=="__main__":
    app.run(port=5000)