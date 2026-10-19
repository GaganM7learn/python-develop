products = [("Phone", 30000), ("Mouse", 800), ("Laptop", 55000)]

products.sort( key=lambda pro : pro[1])

print(products)