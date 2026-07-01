'''
SDBCT Caferteria Bill Calculator☕🍔

'''

user = input("What would you like to have? (Burger / Chai): ")
Quantity = int(input("How much to Quantity : "))

if "Burger" in user:
    bill = Quantity * 50
elif "Chai" in user:
    bill = Quantity * 10
else:
    bill = 0
    print("Unknown Item")

if bill > 200:
    final_bill = bill * 90/100
    print("SDBCT Cafeteria Bill🍔☕")
    print(f"10% OFF APPLIED! Total Rupees : {final_bill}")
else:
    print("SDBCT Cafeteria Bill🍔☕")
    print(f"Total Rupees : {bill}")

