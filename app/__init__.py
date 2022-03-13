from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Создание flask-приложения, БД и миграций"""
    app = Flask(__name__)

    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from app import routes
        db.drop_all()
        db.create_all()

        from app import migrates
        migrates.migrate_user_roles(app.config['USER_ROLES_PATH'])
        migrates.migrate_users(app.config['USERS_PATH'])
        migrates.migrate_orders(app.config['ORDERS_PATH'])
        migrates.migrate_offers(app.config['OFFERS_PATH'])

        return app
