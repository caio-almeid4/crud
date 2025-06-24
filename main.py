from crud import User
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    age: int
    email: str
    
@app.post("/add_user")
def create_user(user: UserCreate):
    user_obj = User(user.name, user.age, user.email)
    user_obj.create()
    
    return {"message: user created successfully"}

    
    
    
        
        
    