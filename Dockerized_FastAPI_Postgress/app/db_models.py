from sqlalchemy import ForeignKey, Boolean, Integer, Column, String, Float, DateTime
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String, unique=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    
    orders = relationship("Order", back_populates="user")

class Product(Base):
    """ Class for modeling products in db"""
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, comment="name of product")
    description = Column(String, comment="description for product")
    price = Column(Float, comment="price of product")
    quantity = Column(Integer, comment="quantity of product")
    
    orders = relationship("Order", back_populates="products")
    
    
class Order(Base):
    """ Class for modeling orders in db"""
    
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity   = Column(Integer)
    order_date = Column(DateTime)

    user = relationship("User", back_populates="orders")
    products = relationship("Product", back_populates="orders")
