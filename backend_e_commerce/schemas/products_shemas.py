from pydantic import BaseModel

class ProductSchema(BaseModel):
    id: int = None
    name: str
    description: str
    price: int
    stock: int
    category: str
    image: str
    user_id: int

    class Config:
        from_attributes = True

class ProductUpdateSchema(BaseModel):
    name: str=None
    description: str=None
    price: int=None
    stock: int=None
    category: str=None
    image: str=None
    user_id: int=None

    class Config:
        from_attributes = True
