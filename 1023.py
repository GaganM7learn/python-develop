from fastapi import FastAPI

app = FastAPI()

@app.get("/store/{category}/{item_id}")
def get_item(category:str , item_id:int):
    return {{"category_searched": "laptop" , "item_number": 405 , "in_stock" : True}}

