from fastapi import FastAPI
from pydantic import BaseModel

from crud import User
from crud import create, delete, get

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


    

        
        
    