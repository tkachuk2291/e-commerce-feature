from pydantic import BaseModel


class UserSchema(BaseModel):
    email : str
    username : str
    password : str

    class Config:
        from_attributes = True