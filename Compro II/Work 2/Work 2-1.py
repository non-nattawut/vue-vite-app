product = {}
for i in range(1,5): # Add Product
    product_name = input("Product %d : "%i)
    price = int(input("    Price : "))
    product.update({product_name : price})

max_values = max(product.values()) # Find max price product
for i in product:
    print(i)
    if(product[i] == max_values):
        max_keys = i
        break

print("Product in dictionary:",product) # Output
print("Product with highest price is \"%s\" "%max_keys)
print("Its price is \"%d\" baht."%max_values)