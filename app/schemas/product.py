from pydantic import BaseModel , Field 
from enum import Enum

class CategoryEnum(str , Enum ): 
    electronics = "electronics" 
    books = "books" 
    clothing = "clothing"


class productCreat(BaseModel):
    name:str= Field(...,min_length=3)
    price: float=Field(gt=0)
    quantity: int = Field(ge=0)
    category: CategoryEnum 

class productResponse(BaseModel) : 
    id: int
    name: str
    price: float
    quantity: int
    category: CategoryEnum