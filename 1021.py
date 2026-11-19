from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def get_home_page():
    return {"message": "Welcome to my new web application!"}


@app.get("/about")

def get_about_page():
    return {"message", "Gagan Tech"}