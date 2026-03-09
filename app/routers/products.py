from fastapi import APIRouter , HTTPException , Path , Query , Depends
from schemas.product import productResponse , productCreat , filterParams,productUpdate
from services.product_service import create_product,found_product , list_products,update_product , delete_product
from typing import Annotated 
from database import get_db 
from sqlalchemy.orm import Session 

router = APIRouter() 

@router.post("/products" , status_code=201)
def add_product(product:productCreat , db :Session=Depends(get_db)): 
    result= create_product(product,db) 
    return result 

@router.get("/products/{id}")
def get_product(id : Annotated[ int , Path(gt=0)] , db: Session = Depends(get_db)) : 
    result = found_product(id,db) 
    return result 


@router.get("/products") 
def get_products(filters: Annotated [filterParams , Query()], db:Session=Depends(get_db)): 
    return list_products(filters , db) 


@router.patch("/products/{id}")
def patch_product(id:int , updates:productUpdate , db : Session=Depends(get_db)):
    product=update_product(id , updates,db) 
    return product 

@router.delete("/products/{id}")
def delete_products(id:int , db:Session=Depends(get_db)): 
    return delete_product(id,db)

