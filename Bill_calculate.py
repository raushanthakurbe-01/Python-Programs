medicine_code = input("Enter medicine name/code: ")
quantity   = int(input("Enter medicine Quantity: "))
unit_price = float(input("Enter unit price of Medicine: "))
tax_rate   = float(input("Enter the tax rate %: "))

subtotal = quantity * unit_price
tax_amount = subtotal * tax_rate /100
final_bill = subtotal + tax_amount
print("\n================ PHARMACY BILL==============")
print(f"Medicine Code: {medicine_code} \n Quantity :{quantity}\n unit Price Rs : {unit_price:.2f}\n Subtotal: Rs.{subtotal:.2f}\n Tax Rate : {tax_rate:.2f}\n Tax Amount : Rs.{tax_amount:.2f}\n Final Bill: Rs. {final_bill:.2f}" )
print("=====================================================================================")
    
