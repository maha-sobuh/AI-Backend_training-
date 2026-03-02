from schemas.product import productCreat , productResponse , filterParams , productUpdate
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

def list_products(filters : filterParams ) : 
    filtered = [
        p for p in products_DB 
        if p["price"]>=filters.min_price and (filters.max_price==0 or p["price"]<= filters.max_price) 
    ]

    if filters.in_stock is not None : 
        filtered = [
            p for p in filtered 
            if (p["quantity"]>0) == filters.in_stock 
        ]
    start = filters.offset 
    end = start+filters.limit 
    paginated = filtered[start:end] 

    return {
        "total":len(filtered), 
        "limit":filters.limit, 
        "offset":filters.offset , 
        "items":paginated 
    }

def update_product(id , updates:productUpdate) : 
    product=None 
    for p in products_DB : 
        if id == p["id"]:
            product=p 
    if product is None :
        return product 
    if updates.name : 
        product["name"]=updates.name 
    if updates.price : 
        product["price"]=updates.price 
    if updates.category: 
        product["category"]= updates.category 
    if updates.quantity : 
        product["quantity"]=updates.quantity 
    return product 
