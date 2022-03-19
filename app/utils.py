import json
import os.path
from datetime import datetime


def open_json(filename):
    """Получеине данных из json-файла"""
    json_data = []
    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as f:
            json_data = json.load(f)

    return json_data


def convert_string_to_date(str_date):
    """Перевод даты из строкового формата в datetime"""
    dateString = str_date
    dateFormatter = "%m/%d/%Y"

    return datetime.strptime(dateString, dateFormatter)


def return_user_json(user):
    """Сериализация данных пользователя"""
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age,
        'email': user.email,
        'role': user.role.name,
        'phone': user.phone,
    }


def return_order_json(order):
    """Сериализация данных заказа"""
    return {
        'id': order.id,
        'name': order.name,
        'description': order.description,
        'start_date': order.start_date,
        'end_date': order.end_date,
        'address': order.address,
        'price': order.price,
        'customer': f"{order.customer.first_name} {order.customer.last_name}",
        'executor': f"{order.executor.first_name} {order.executor.last_name}"
    }


def return_offer_json(offer):
    """Сериализация данных сделки"""
    return {
        'id': offer.id,
        'order': offer.order.name,
        'executor': f"{offer.executor.first_name} {offer.executor.last_name}"
    }
