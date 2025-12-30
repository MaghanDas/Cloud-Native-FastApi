from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers=["*"],
)


def get_db():
    db = session()
    try: 
        yield db 
    finally: 
        db.close()

def init_db():
    try:
        database_models.Base.metadata.create_all(bind=engine)
    except Exception as e:
        print("DB init error:", e)

init_db()

# def init_db():
#     db = session()
#     count = db.query(database_models.Product).count

#     if(count==0):
#       for product in products: 
#             db.add(database_models.Product(**product.model_dump()))
#         # model_dump gives dictionary and then with ** we convert it to key value pair .
#       db.commit()


@app.get("/")
def greet():
    return "Hello world"

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product 
    return "product not found"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product,db: Session = Depends(get_db)): 
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name = product.name 
        db_product.description = product.description 
        db_product.price = product.price 
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated"
    else:
        return "No product Found!"

@app.delete("/products")
def delete_product(id: int,db: Session = Depends(get_db)): 
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "No product Found!"