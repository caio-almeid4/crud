from fastapi import FastAPI

from crud import User
from crud import create, delete, get, update


app = FastAPI()

    
@app.post("/add_user")
def create_user(user: User):
    
    create(user)
   
    
    return {"message": "user created successfully"}

@app.delete("/del_user")
def delete_user(email: str):
    
    delete(email)
    
    return {"message": "user deleted successfully"}
    

@app.get("/get_user")
def get_user(email: str):
    
    return get(email)


@app.put("/update_user")
def update_user(email: str, data: dict = {"name": "", "age": 0, "email": ""}):
    
    update(email, data)
    
    return {"message": "user updated successfully"} | get_user(data["email"])
    
    

    

        
        
    