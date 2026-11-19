from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    in_stock = bool = True

@app.post("/create-product")

def create_new_product(new_item: Product):
    db_log = f"Saved {new_item.name} costing ${new_item.price} to the database."
    return {"message": "Success" , "product_added" : new_item.name , "log": db_log}