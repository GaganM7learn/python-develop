from fastapi import FastAPI , HTTPException

app = FastAPI()

valid_users = {1 : "Gagan" , 2:"Vidya"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in valid_users:
        raise HTTPException(
            status_code = 404 , 
            detail= f"User ID {user_id} does not exit in our system.")
    return {"user_id" : user_id , "name" : valid_users[user_id]}