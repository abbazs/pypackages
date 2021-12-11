from pydantic import BaseModel

class User(BaseModel):
    name:str
    telegram:str
    email:str