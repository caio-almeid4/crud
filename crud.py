from db import connect_db
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str
           
def create(user: User):
        
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute(
        "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
        (user.name, user.age, user.email)
    )
    
    conn.commit()
    cur.close()
    conn.close()
        
def delete(email: str):
        
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute(
        "DELETE FROM users WHERE email = (%s)",
        (email,)
    )
    
    conn.commit()
    cur.close()
    conn.close()
    
    
def  get(email: str):
    
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute(
        "SELECT name, age, email FROM users WHERE email = (%s)",
        (email,)
    )
    
    info = dict(zip(("name", "age", "email"), cur.fetchall()[0]))
    
    conn.commit()
    cur.close()
    conn.close()
    
    return info

def update(email: str):
    
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute(
        "UPDATE name, age, email FROM users WHERE email = (%s)",
        (email,)
    )
    
    conn.commit()
    cur.close()
    conn.close()