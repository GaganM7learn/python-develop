from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def get_users(keyword : str , page : int = 1) :
   search_log = f"Keyword : {keyword} , Page {page}"
   return {"search_term": keyword, "current_page": page, "results_found": 42}
