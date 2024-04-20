from pydantic import BaseModel


class User(BaseModel):
    password: str
    username: str

    def __str__(self):
        # return self.username
        return f"object : <username:{self.username} password:{self.password}>"