from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class UserSignup(BaseModel):
    username : str
    email : str
    age : int

@app.post("/register")

def user_profile(user : UserSignup ):
    db_log = f"Saved {user.username} email {user.email} to the database"

    return {"status": "Account created", "user_email": user.email}