import os.path

DATABASE_FILE_PATH = os.path.join(os.getcwd(), 'test_db.db')
FIXTURE_PATH = 'fixtures'


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_ROLES_PATH = os.path.join(FIXTURE_PATH, 'user_roles.json')
    USERS_PATH = os.path.join(FIXTURE_PATH, 'users.json')
    ORDERS_PATH = os.path.join(FIXTURE_PATH, 'orders.json')
    OFFERS_PATH = os.path.join(FIXTURE_PATH, 'offers.json')
