from schemas.product import productCreat , productResponse , filterParams , productUpdate
from models import Product 
from sqlmodel import SQLModel , Session , select 
from fastapi import HTTPException

########################################## 
def create_product(product: productCreat , db:Session) -> productResponse : 

    existing = db.exec(select(Product).where(Product.name == product.name)).first()
    if existing:
        raise HTTPException(status_code=409, detail=f"Product already exists")
    
    new_product = Product(
        name=product.name,
        price=product.price,
        quantity=product.quantity,
        category=product.category
    )
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)  # fetches the generated id , created_at
    
    return new_product

def found_product(id : int ,db:Session ) -> productResponse : 
    result = db.exec(select(Product).where(Product.id==id)).first()
    if result is None: 
        raise HTTPException(status_code=404 , detail={"detail": "Product not found", "error_code": "NOT_FOUND"}) 
    return productResponse.model_validate(result)


def list_products(filters : filterParams  , db:Session) : 
    if filters.max_price!=0 and filters.min_price > filters.max_price : 
        raise HTTPException(status_code=400 , detail="min price can not be greater than max price ") 
    query = select(Product) 

    if filters.min_price>0 : 
        query=query.where(Product.price>=filters.min_price) 
    if filters.max_price>0: 
        query=query.where(Product.price<=filters.max_price) 
    
    if filters.in_stock is not None : 
        if filters.in_stock : 
            query=query.where(Product.quantity!=0) 
        else : 
            query=query.where(Product.quantity== 0) 
    
    total = len(db.exec(query).all())####check
    query = query.offset(filters.offset).limit(filters.limit)
    products = db.exec(query).all()

    return {
        "total": total,
        "limit": filters.limit,
        "offset": filters.offset,
        "items": products
    }

def update_product(id , updates:productUpdate , db:Session) : 
    product= db.exec(select(Product).where(Product.id==id)).first()
    if product is None: 
        raise HTTPException(status_code=404 , detail="product not found") 
    if not any([updates.name , updates.price , updates.quantity , updates.category]): 
        raise HTTPException(status_code=400 , detail="must provide one update at least")
    
    if updates.name is not None:
        product.name = updates.name   
    if updates.price is not None:
        product.price = updates.price
    if updates.category is not None:
        product.category = updates.category
    if updates.quantity is not None:
        product.quantity = updates.quantity

    db.add(product)
    db.commit()
    db.refresh(product)
    
    return product

def delete_product(id:int , db:Session) : 
    product = db.exec(select(Product).where(Product.id == id)).first() 
    if product is None:
        raise HTTPException(status_code=404 , detail="product not found") 
    
    db.delete(product)
    db.commit()
    return  {"detail": "Product deleted successfully"}
