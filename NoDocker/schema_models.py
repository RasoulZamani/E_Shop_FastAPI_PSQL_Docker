from pydantic import ConfigDict, BaseModel, EmailStr
from datetime import datetime

# schemas for User model ______________________________________________
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username:str
    email: str
    is_admin: bool
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
# schemas for Product model ___________________________________________
class ProductCreate(BaseModel):
    """Base schema for creating Product model"""
    name: str
    description: str
    price: float
    quantity: int
     
     
class ProductResponse(ProductCreate):
    """Schema for returning products"""
    id: int
    model_config = ConfigDict(from_attributes=True)
    
# schemas for Order model ___________________________________________
class OrderCreate(BaseModel):
    """Schema for creating orders"""
    product_id: int
    quantity: int
    
    
class OrderResponse(OrderCreate):
    """Schema for returning orders"""
    id: int
    user_id: int
    order_date: datetime
    model_config = ConfigDict(from_attributes=True)
