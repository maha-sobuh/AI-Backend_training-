from fastapi import APIRouter , HTTPException , Path , Query
from schemas.product import productResponse , productCreat , filterParams
from services.product_service import create_product,found_product , list_products
from typing import Annotated 

router = APIRouter() 

@router.post("/products" , status_code=201)
def add_product(product:productCreat): 
    result= create_product(product) 
    if result is None : 
        raise HTTPException(status_code=409 , detail= "product name already exists") 
    return result 

@router.get("/products/{id}")
def get_product(id : Annotated[ int , Path(gt=0)]) : 
    result = found_product(id) 
    if result is None: 
        raise HTTPException(status_code=404 , detail={"detail": "Product not found", "error_code": "NOT_FOUND"}) 
    return result 


@router.get("/products") 
def get_products(filters: Annotated [filterParams , Query()]): 
    if filters.max_price!=0 and filters.min_price > filters.max_price : 
        raise HTTPException(status_code=400 , detail="min price can not be greater than max price ") 
    return list_products(filters) 



