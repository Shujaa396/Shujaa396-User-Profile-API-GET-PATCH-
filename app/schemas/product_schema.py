from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    image: str
    price: float
    category: str
    stock: int
    module: str

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True

