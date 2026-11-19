from fastapi import FastAPI 

app = FastAPI()

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):

    record_url = f"Database lookup for ID :{emp_id}"
    return {"employee_id": emp_id , "action": record_url}