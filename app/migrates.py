from app import db
from . import models
from app.utils import open_json, convert_string_to_date


def migrate_user_roles(filepath):
    """Миграция данных о ролях пользователя из json-файла в таблицу user_roles"""
    user_roles = open_json(filepath)
    result = []
    for role in user_roles:
        result.append(
            models.UserRole(**role)
        )
    db.session.add_all(result)
    db.session.commit()


def migrate_users(filepath):
    """Миграция данных о пользователях из json-файла в таблицу users"""
    users = open_json(filepath)
    result = []
    for user in users:
        result.append(
            models.User(**user)
        )

    db.session.add_all(result)
    db.session.commit()


def migrate_orders(filepath):
    """Миграция данных о заказах из json-файла в таблицу orders"""
    orders = open_json(filepath)
    result = []
    for order in orders:
        order["start_date"] = convert_string_to_date(order["start_date"])
        order["end_date"] = convert_string_to_date(order["end_date"])

        result.append(
            models.Order(**order)
        )

    db.session.add_all(result)
    db.session.commit()


def migrate_offers(filepath):
    """Миграция данных о сделках из json-файла в таблицу offers"""
    offers = open_json(filepath)
    result = []
    for offer in offers:
        result.append(
            models.Offer(**offer)
        )

    db.session.add_all(result)
    db.session.commit()
