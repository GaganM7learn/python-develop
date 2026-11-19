from fastapi import FastAPI , HTTPException

app = FastAPI()

inventory = {100: "Laptop" , 101: "Mouse"}

@app.delete("/inventory/{item_id}")

def get_product_detail(item_id : int):
    if item_id not in inventory :
        raise HTTPException (
            status = 404 ,
            detail = f"item not found"
        )
    else :
        inventory.pop(item_id)
        return {"status" : "deleted" , "item_id" : item_id}
    