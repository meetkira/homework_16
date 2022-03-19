from app import models, db
from flask import current_app as app, jsonify, request

from app.utils import return_user_json, return_order_json, return_offer_json


@app.route('/users')
def get_users():
    """Получение списка пользователей"""
    users = models.User.query.all()
    result = []
    for user in users:
        result.append(return_user_json(user))

    return jsonify(result)


@app.route('/users/<int:id>')
def get_user_by_id(id):
    """Получение данных пользователя по его id"""
    user = models.User.query.get(id)
    if user is None:
        return "No user"
    result = return_user_json(user)

    return jsonify(result)


@app.route('/users', methods=["POST"])
def add_user():
    """Добавление нового пользователя"""
    data = request.json
    if data.get('id') is None or data.get('role_id') is None:
        return "Empty data"

    if models.UserRole.query.get(data.get('role_id')) is None:
        return "No roles"

    user = models.User(
        id=data.get('id'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        age=data.get('age'),
        email=data.get('email'),
        role_id=data.get('role_id'),
        phone=data.get('phone')
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(return_user_json(user))


@app.route('/users/<int:id>', methods=["PUT"])
def update_user(id):
    """Обновление данных пользователя"""
    data = request.json

    user = models.User.query.get(id)
    if user is None:
        return f"No user with id {id}"
    if data.get('role_id') and models.UserRole.query.get(data.get('role_id')) is None:
        return "No roles"

    db.session.query(models.User).filter(models.User.id == user.id).update(data)
    db.session.commit()

    return jsonify(return_user_json(user))


@app.route('/users/<int:id>', methods=["DELETE"])
def delete_user(id):
    """Удаление пользователя"""
    user = models.User.query.get(id)
    if user is None:
        return f"No user with id {id}"

    db.session.query(models.User).filter(models.User.id == user.id).delete()
    db.session.commit()

    return f"User with id {id} removed"


@app.route('/orders')
def get_orders():
    """Получение списка заказов"""
    orders = models.Order.query.all()
    result = []
    for order in orders:
        result.append(return_order_json(order))

    return jsonify(result)


@app.route('/orders/<int:id>')
def get_order_by_id(id):
    """Получение данных заказа по его id"""
    order = models.Order.query.get(id)
    if order is None:
        return "No order"

    result = return_order_json(order)

    return jsonify(result)


@app.route('/orders', methods=["POST"])
def add_order():
    """Добавление нового заказа"""
    data = request.json
    if data.get('id') is None or data.get('customer_id') is None or data.get('executor_id') is None:
        return "Empty data"

    if models.User.query.get(data.get('customer_id')) is None or models.User.query.get(data.get('executor_id')) is None:
        return "No users"

    order = models.Order(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        start_date=data.get('start_date'),
        end_date=data.get('end_date'),
        address=data.get('address'),
        price=data.get('price'),
        customer_id=data.get('customer_id'),
        executor_id=data.get('executor_id')
    )
    db.session.add(order)
    db.session.commit()

    return jsonify(return_order_json(order))


@app.route('/orders/<int:id>', methods=["PUT"])
def update_order(id):
    """Обновление данных заказа"""
    data = request.json

    order = models.Order.query.get(id)
    if order is None:
        return f"No order with id {id}"

    if data.get('customer_id') and models.User.query.get(data.get('customer_id')) is None or data.get(
            'executor_id') and models.User.query.get(data.get('executor_id')) is None:
        return "No users"

    if data.get('customer_id') == order.executor_id or data.get('executor_id') == order.customer_id:
        return "Customer and executor can't be the same person"

    db.session.query(models.Order).filter(models.Order.id == order.id).update(data)
    db.session.commit()

    return jsonify(return_order_json(order))


@app.route('/orders/<int:id>', methods=["DELETE"])
def delete_order(id):
    """Удаление заказа"""
    order = models.Order.query.get(id)
    if order is None:
        return f"No order with id {id}"

    db.session.query(models.Order).filter(models.Order.id == order.id).delete()
    db.session.commit()

    return f"Order with id {id} removed"


@app.route('/offers')
def get_offers():
    """Получение списка сделок"""
    offers = models.Offer.query.all()
    result = []
    for offer in offers:
        result.append(return_offer_json(offer))

    return jsonify(result)


@app.route('/offers/<int:id>')
def get_offer_by_id(id):
    """Получение данных сделки по её id"""
    offer = models.Offer.query.get(id)
    if offer is None:
        return "No offer"

    result = return_offer_json(offer)

    return jsonify(result)


@app.route('/offers', methods=["POST"])
def add_offer():
    """Добавление новой сделки"""
    data = request.json

    if data.get('id') is None or data.get('order_id') is None or data.get('executor_id') is None:
        return "Empty data"

    if models.Order.query.get(data.get('order_id')) is None or models.User.query.get(data.get('executor_id')) is None:
        return "No orders/users"

    offer = models.Offer(
        id=data.get('id'),
        order_id=data.get('order_id'),
        executor_id=data.get('executor_id')
    )
    db.session.add(offer)
    db.session.commit()

    return jsonify(return_offer_json(offer))


@app.route('/offers/<int:id>', methods=["PUT"])
def update_offer(id):
    """Обновление данных сделки"""
    data = request.json

    offer = models.Offer.query.get(id)
    if offer is None:
        return f"No offer with id {id}"

    if data.get('order_id') and models.Order.query.get(data.get('order_id')) is None or data.get(
            'executor_id') and models.User.query.get(data.get('executor_id')) is None:
        return "No users"

    db.session.query(models.Offer).filter(models.Offer.id == offer.id).update(data)
    db.session.commit()

    return jsonify(return_offer_json(offer))


@app.route('/offers/<int:id>', methods=["DELETE"])
def delete_offer(id):
    """Удаление сделки"""
    offer = models.Offer.query.get(id)
    if offer is None:
        return f"No offer with id {id}"

    db.session.query(models.Offer).filter(models.Offer.id == offer.id).delete()
    db.session.commit()

    return f"Order with id {id} removed"
