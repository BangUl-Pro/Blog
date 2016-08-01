from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from app.managers.db_manager import Base, db_session
import datetime


class Notice(Base):
    __tablename__ = 'notices'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Text)
    content = Column(Text)
    author = Column(String(30), ForeignKey('users.id'), nullable=False)
    created = Column(DateTime)
    category = Column(Integer)

    def __init__(self, title, content, author, category):
        self.title = title
        self.content = content
        self.author = author
        self.created = datetime.datetime.now()
        self.category = category

    def __repr__(self):
        return '{"id": %s, "title":"%s", "content":"%s", "author":"%s", "created":"%s", "category":%d}' %\
            self.id, self.title, self.content, self.author, self.created, self.category

    def insert_notice(self):
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as error:
            print('error = {}'.format(error))
            db_session.rollback()
