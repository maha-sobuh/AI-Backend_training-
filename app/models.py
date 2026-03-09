from sqlmodel import SQLModel , table , Field
from typing import Optional
from datetime import datetime 
from sqlalchemy import Column, DateTime, func, Enum as SAEnum
from enum import Enum 
from schemas.product import CategoryEnum 


#meta class 
class Product(SQLModel , table=True ):
    __tablename__ = "products"
    id: Optional[int]=Field(default=None , primary_key=True)
    name:str = Field(unique=True)
    price : float 
    quantity : int
    category :  str = Field( ########### not working 
        sa_column=Column(
            SAEnum(CategoryEnum, name="categoryenum")  
        )
    ) 
    created_at: Optional[datetime] = Field(default=None,sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: Optional[datetime] = Field(default=None,sa_column=Column(DateTime(timezone=True), onupdate=func.now()))