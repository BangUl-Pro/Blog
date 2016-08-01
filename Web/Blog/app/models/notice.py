from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, desc
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
        # TODO 고쳐야 함
        if not self.category:
            self.category = 0
        return '{"id": %s, "title":"%s", "content":"%s", "author":"%s", "created":"%s", "category":%d}' %\
               (self.id, self.title, self.content, self.author, self.created, self.category)


def insert_notice(notice):
    try:
        db_session.add(notice)
        db_session.commit()
    except Exception as error:
        print('error = {}'.format(error))
        db_session.rollback()


def get_notices(category=None):
    if not category:
        return db_session.query(Notice).order_by(desc(Notice.created)).limit(10).all()
