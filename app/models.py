from . import db


class UserRole(db.Model):
    """UserRole database model"""
    __tablename__ = "user_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    user = db.relationship("User", back_populates='role')


class User(db.Model):
    """User database model"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age >= 14"))
    email = db.Column(db.String(50))

    role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    role = db.relationship("UserRole", back_populates='user')

    phone = db.Column(db.String(25))


class Order(db.Model):
    """Order database model"""
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer, db.CheckConstraint("price >= 0"))

    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    customer = db.relationship("User", foreign_keys='Order.customer_id')

    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor = db.relationship("User", foreign_keys='Order.executor_id')


class Offer(db.Model):
    """Offer database model"""
    __tablename__ = "offers"
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship("Order")

    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor = db.relationship("User")
