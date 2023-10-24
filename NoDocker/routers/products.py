from fastapi import Depends, APIRouter, HTTPException
from typing import List

from schema_models import  ProductCreate, ProductResponse
from db import get_db
from security import manager
import cruds.products as crud_func

product_router = APIRouter()

@product_router.post("/create", response_model=ProductResponse)
def add_new_product(product: ProductCreate, db =Depends(get_db), user=Depends(manager)):
    """adding new product to db"""
    if user.username == "admin":
        new_product = crud_func.create_product(product, db)
        return new_product 
    else:
        raise HTTPException(status_code=403, detail="only admin can add new products")

@product_router.get("/all", response_model=List[ProductResponse])
def read_all_products(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    """ return all products"""
    return crud_func.get_all_products(db, skip=skip, limit=limit)

    
@product_router.get("/{name}", response_model=ProductResponse)
def read_product_by_name(name: str, db=Depends(get_db)):
    """ return product with declared name"""
    product = crud_func.get_product(name, db)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@product_router.put("/{name}", response_model=ProductResponse)
def update_product(name: str, new_product:ProductCreate, db=Depends(get_db), user=Depends(manager)):
    """update product drclared by name"""
    if user.username == "admin":
        new_product = crud_func.update_product(name, new_product, db)
        if not new_product:
            raise HTTPException(status_code=404, detail="Product not found")
        return new_product
    else:
        raise HTTPException(status_code=403, detail="only admin can add new products")

@product_router.delete("/{name}")
def delete_product(name:str, db=Depends(get_db), user=Depends(manager)):
    """deleting product declared by name"""
    if user.username == "admin":
        product = crud_func.delete_product(name, db)  
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"message":f"produce {name} was deleted seccessfully."}
    else:
        raise HTTPException(status_code=403, detail="only admin can add new products")
    
    

