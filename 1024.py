from fastapi import FastAPI

app = FastAPI()

@app.get("/users")

def get_users(limit: int = 10, sort_by: str = "name"):
    query_log = f"Fetching {limit} users, sorting by {sort_by}"
    return {"status": "success" , "action" : query_log}