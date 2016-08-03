from app.managers.db_manager import Base, db_session
from sqlalchemy import Column, String, Integer, asc


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{"id":%d, "name":"%s"}' %\
               (self.id, self.name)


def insert_category(category_name):
    category = db_session.query(Category).filter(Category.name == category_name).first()
    if category:
        print('category "{}" is already used.'.format(category.name))
        return False
    category = Category(category_name)
    try:
        db_session.add(category)
        db_session.commit()
        return db_session.query(Category).filter(Category.name == category_name).first()
    except Exception as error:
        print('insert category Error = {}'.format(error))
        db_session.rollback()
    return False


def get_categories():
    categories = db_session.query(Category).order_by(asc(Category.id)).all()
    return categories


def delete_category(category_ids):
    try:
        for category_id in category_ids:
            db_session.query(Category).filter(Category.id == category_id).delete()
        db_session.commit()
        return True
    except Exception as error:
        db_session.rollback()
        print(error)
        return False


def update_category(category_id, category_name):
    try:
        if db_session.query(Category).filter(Category.name == category_name).first():
            return 301
        db_session.query(Category).filter(Category.id == category_id).update({
            Category.name: category_name
        })
        db_session.commit()
        return 200
    except Exception as error:
        print(error)
        db_session.rollback()
    return 302
