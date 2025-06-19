from db import connect_db

class User:
    
    def __init__(
        self,
        name: str,
        age: int,
        email: str
    ) -> None:
        
        
        self.name = name
        self.age = age
        self.email = email
        
        
    def create(self):
        
        conn = connect_db()
        cur = conn.cursor()
        
        cur.execute(
            "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
            (self.name, self.age, self.email)
        )
        
        conn.commit()
        cur.close()
        conn.close()

        
