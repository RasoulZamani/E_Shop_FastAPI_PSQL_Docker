""" #cruds/products.py: crud funcs related to products"""

from typing import Optional
from sqlalchemy.orm import Session

from schema_models import  ProductCreate
from db_models import  Product

def get_product(name: str, db: Session = None) -> Optional[Product]:
    """ Return the product with the corresponding name """
    return db.query(Product).filter(Product.name == name).first()

def get_all_products(db: Session = None, skip: int = 0, limit: int = 100):
    """ Return all products """
    return db.query(Product).offset(skip).limit(limit).all()
    
def create_product(product: ProductCreate, db: Session) -> Product:
    """ Create a new entry in the database product table """
    product_data = product.dict()
    db_product = Product(**product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(name: str, db: Session = None):
    """ Return the product with the corresponding name """
    product = get_product(name, db)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return {"message":f"produce {name} was deleted seccessfully."}

def update_product(name: str, new_product:ProductCreate , db: Session) -> Product:
    """ update product with declared name in the database """
    product = get_product(name, db)
    if not product:
        return None
    # updating by new materials
    product.name= new_product.name
    product.description= new_product.description
    product.price = new_product.price
    product.quantity = new_product.quantity
    
    db_product = product
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



