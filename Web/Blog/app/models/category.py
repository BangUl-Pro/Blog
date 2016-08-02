from app.managers.db_manager import Base, db_session
from sqlalchemy import Column, String, Integer, asc


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{"id":%d, "name":%d}' %\
               (self.id, self.name)

    def insert_category(self):
        category = db_session.query(Category).filter(Category.name == self.name).first()
        if category:
            print('category "{}" is already used.'.format(self.name))
            return False
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as error:
            print('insert category Error = {}'.format(error))
            db_session.rollback()

    def get_categories(self):
        categories = db_session.query(Category).order_by(asc(Category.id)).all()
        return categories
