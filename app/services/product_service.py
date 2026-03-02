from schemas.product import productCreat , productResponse
products_DB = [] 
counter = 1 

def create_product(product: productCreat) -> productResponse : 
    global counter 
    for p in products_DB : 
        if p["name"]==product.name : ##lower? 
            return None 
    
    new_product = { 
        "id" : counter ,
        "name": product.name , 
        "price":product.price , 
        "category":product.category , 
        "quantity":product.quantity 
    }
    products_DB.append(new_product) 
    counter +=1 

    return productResponse(**new_product) 

def found_product(id : int) -> productResponse : 
    for i in products_DB : 
        if i["id"] == id : 
            return productResponse(**i) 
    return None 