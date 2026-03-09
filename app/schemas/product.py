from pydantic import BaseModel , Field 
from enum import Enum
from typing import Optional 
from datetime import datetime
from sqlmodel import SQLModel

class CategoryEnum(str , Enum ): 
    electronics = "electronics" 
    books = "books" 
    clothing = "clothing"


class productCreat(SQLModel):
    name:str= Field(...,min_length=3)
    price: float=Field(gt=0)
    quantity: int = Field(ge=0)
    category: CategoryEnum 

class productResponse(SQLModel) : 
    id: int
    name: str
    price: float
    quantity: int
    category: CategoryEnum
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class filterParams(SQLModel) : 
    min_price : float = Field(0.0, ge=0.0)
    max_price :float=Field(0.0, ge=0.0) 
    in_stock : bool = None
    limit : int = Field(10 ,le=100)
    offset:int = Field(0 , ge=0) 

class productUpdate(SQLModel): 
    name:Optional[str]=None 
    price:Optional[float]=Field(None , ge=0)
    quantity: Optional[int] = Field(None, ge=0)
    category: Optional[str] = None

