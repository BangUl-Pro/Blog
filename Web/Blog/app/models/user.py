from app.managers.db_manager import Base, db_session
from sqlalchemy import Column, String


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

    def get_user(self):
        return db_session.query(User)\
            .filter(User.id == self.id, User.password == self.password).first()

    def insert_user(self):
        try:
            query_user = db_session.query(User).filter(User.id == self.id).first()
            if query_user:
                return 301

            query_user = db_session.query(User).filter(User.email == self.email).first()
            if query_user:
                return 302

            db_session.add(self)
            db_session.commit()
            return 200
        except Exception as error:
            print(error)
            db_session.rollback()
            return 303
