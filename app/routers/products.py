from fastapi import APIRouter , HTTPException
from schemas.product import productResponse , productCreat 
from services.product_service import create_product 

router = APIRouter() 

@router.post("/product" , status_code=201)
def add_product(product:productCreat): 
    result= create_product(product) 
    if result is None : 
        raise HTTPException(status_code=409 , detail= "product name already exists") 
    return result 
