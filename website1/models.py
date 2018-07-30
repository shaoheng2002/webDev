#encoding: utf-8
from datetime import datetime
from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    phone = db.Column(db.Text(11), nullable = False)
    username = db.Column(db.Text(50), nullable= False)
    password = db.Column(db.Text(100), nullable= False)


# class Question(db.Model):
#     __tablename__ = 'question'
#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     title = db.Column(db.String(100), nullable = False)
#     content = db.Column(db.Text(), nullable = False)
#     create_time = db.Column(db.DateTime, default=datetime.now)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     author = db.relationship('User', backref = db.backref('questions'))
#
# class Comment(db.Model):
#     __tablename__ = 'comment'
#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     comment = db.Column(db.Text(), nullable = False)
#
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
#     comment_author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     question_id = db.relationship('Question', backref=db('comment'))
#     comment_author_id = db.relationship('User', backref=db('comment'))