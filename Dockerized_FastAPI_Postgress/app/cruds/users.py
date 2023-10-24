from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime

from ..schema_models import UserCreate, OrderCreate
from ..db import DBContext
from ..db_models import User, Product, Order
from ..security import hash_password, manager

@manager.user_loader
def get_user(email: str, db: Session = None) -> Optional[User]:
    """ Return the user with the corresponding email """
    if db is None:
        # No db session was provided so we have to manually create a new one
        # Closing of the connection is handled inside of DBContext.__exit__
        with DBContext() as db:
            return db.query(User).filter(User.email == email).first()
    else:
        return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    """ Create a new entry in the database user table """
    user_data = user.dict()
    plain_password = user.password
    del user_data["password"]
    user_data["hashed_password"] = hash_password(plain_password)
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def user_create_order(order: OrderCreate, db: Session, user_id):
    """ Create a new entry in the database order table """
    product = db.query(Product).filter(Product.id == order.product_id).first()
    if (product is None) or (product.quantity==0):
        return None
    db_order= Order(user_id = user_id, 
        product_id=order.product_id, quantity=order.quantity,
        order_date = datetime.now())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
