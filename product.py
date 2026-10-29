product_code = input("Enter prodcut code:")
quantity = int(input("Enter quantity:"))
price = float(input("Enter th price :"))
total = quantity * price 
print(
    f"Product: {product_code}\n"
    f"Quantity:{quantity}\n"
    f"Price Rs: {price:.2f}\n"
    f"Total Rs: {total:.2f}\n")