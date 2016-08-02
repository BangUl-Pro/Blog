from app.managers.db_manager import Base, db_session
from sqlalchemy import Column, String
from flask import session


class User(Base):
    __tablename__ = 'users'
    id = Column(String(30), primary_key=True)
    password = Column(String(30))
    name = Column(String(30))
    email = Column(String(50), unique=True)

    def __init__(self, user_id, password, name=None, email=None):
        self.id = user_id
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return '{"id": "%s", "password":"%s", "name":"%s", "email":"%s"' %\
               (self.id, self.password, self.name, self.email)


def get_user(user):
    return db_session.query(User)\
        .filter(User.id == user.id, User.password == user.password).first()


def insert_user(user):
    try:
        query_user = db_session.query(User).filter(User.id == user.id).first()
        if query_user:
            return 301

        query_user = db_session.query(User).filter(User.email == user.email).first()
        if query_user:
            return 302

        db_session.add(user)
        db_session.commit()
        return 200
    except Exception as error:
        print(error)
        db_session.rollback()
        return 303


def update_user(user, cur_user):
    try:
        if user.id != cur_user.id:
            print('1')
            if db_session.query(User).filter(User.id == cur_user.id).first():
                return 301

        if user.email != cur_user.email:
            print('2')
            if db_session.query(User).filter(User.email == cur_user.email).first():
                return 301

        print('email = {}'.format(cur_user.email))

        db_session.query(User).filter(User.id == user.id).update({
            User.id: cur_user.id,
            User.password: cur_user.password,
            User.name: cur_user.name,
            User.email: cur_user.email
        })
        db_session.commit()
        session.pop('user')
        session['user'] = cur_user
        return 200
    except Exception as error:
        print('update_user Error = {}'.format(error))
        db_session.rollback()
        return 302
