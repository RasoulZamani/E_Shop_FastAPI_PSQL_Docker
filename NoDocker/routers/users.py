from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException


from schema_models import UserCreate, UserResponse,Token, OrderCreate, OrderResponse
from db import get_db
from security import manager, verify_password
import cruds.users as crud_func

user_router = APIRouter()
@user_router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db=Depends(get_db)):
    """registering user by unique email, username and password"""
    if crud_func.get_user(user.email) is not None:
        raise HTTPException(status_code=400, detail="A user with this email already exists")
    else:
        db_user = crud_func.create_user(db, user)
        if user.username == "admin":
            db_user.is_admin=True
        return db_user #UserResponse(id=db_user.id, email=db_user.email, username=db_user.username, is_admin=db_user.is_admin)


@user_router.post("/auth/token", response_model=Token)
def login(data: OAuth2PasswordRequestForm = Depends()):
    """login by email and password and getting Bearer token"""
    email = data.username # because auth get username, in frontend we can show it email later
    password = data.password

    user = crud_func.get_user(email)  # we are using the same function to retrieve the user
    if user is None:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif not verify_password(password, user.hashed_password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data=dict(sub=user.email))
    return {'access_token': access_token, 'token_type': 'Bearer'}


@user_router.get("/me")
def private_route(user=Depends(manager)):
    """returns email of loged in user in this session"""
    return {"detail": f"Welcome {user.email}"}


@user_router.post("/orders/create", response_model=OrderResponse)
def add_new_order(order: OrderCreate, db =Depends(get_db), user=Depends(manager)):
    """adding new product to db"""
    db_order = crud_func.user_create_order(order=order, db=db, user_id=user.id) 
    if db_order is None:
        raise HTTPException(status_code=404, detail="Product not found or finished!")
    return db_order    

# Not mentained in this task but in is better to have delete, read and update for 
# orders too. In that case for better organization, order codes should be seperated.