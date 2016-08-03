from app import app
from app.managers.url_manager import ADD_CATEGORY, REMOVE_CATEGORY, UPDATE_CATEGORY
from app.models.category import insert_category, delete_category, update_category
from flask import request, jsonify
from random import randint


@app.route(ADD_CATEGORY, methods=['POST'])
def add_category():
    name = 'random{}{}'.format(randint(0, 60000), randint(0, 60000))
    print(name)
    category = insert_category(name)
    if category:
        print('success')
        return jsonify(result=name, id=category.id)
    else:
        print('error')
    return jsonify(result=False)


@app.route(REMOVE_CATEGORY, methods=['POST'])
def remove_category():
    form = dict(request.form)
    category_ids = form['selected[]']
    if delete_category(category_ids):
        return jsonify(result=True)
    return jsonify(result=False)


@app.route(UPDATE_CATEGORY, methods=['POST'])
def update_category_name():
    form = dict(request.form)
    category_id = form['category_id'][0]
    category_name = form['category_name'][0]
    print('category_id = {}'.format(category_id))
    print('category_name = {}'.format(category_name))
    category = update_category(category_id, category_name)
    if category == 200:
        print('success')
        return jsonify(result=200)
    elif category == 301:
        print('이름 중복')
        #TODO 이름 중복 알람
        return jsonify(result=301)
    return jsonify(result=303)
