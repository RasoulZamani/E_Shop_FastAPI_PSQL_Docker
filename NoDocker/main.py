from fastapi import FastAPI
from sqlalchemy import inspect
from fastapi.openapi.utils import get_openapi

from db import  Base, engine
from routers.users import user_router
from routers.products import product_router

# instantiaye fastAPI app and adding routers
app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["User"])
app.include_router(product_router, prefix="/products", tags=["Product"])


@app.on_event("startup")
def setup():
    print("Creating db tables...")
    Base.metadata.create_all(bind=engine)
    inspection = inspect(engine)
    print(f"Created {len(inspection.get_table_names())} tables: {inspection.get_table_names()}")

@app.get("/")
def home():
    return {"message":"Wellcome to E-Commerce Shop!"}

# schema for overwritting openapi documentation _______________________
def custom_openapi():
    """customizing openapi defaults"""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="E-Shop API",
        version="1.2",
        summary="This is a simple e-shop as a test task",
        description="You can see products and if you register and login then you can place an order!\nOnly admin can create, update and delete products. ",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
# for running app: ____________________________________________________
if __name__ == "__main__":
    import uvicorn
    import os
    
    # creating secretkey in .env
    if os.path.exists(".env"):
        print(".env file already exists. Exiting...")
    else:
        with open(".env", "w") as f:
            f.write(f"SECRET={os.urandom(24).hex()}")
    
    # running app
    uvicorn.run("main:app",host='localhost', reload=True)
