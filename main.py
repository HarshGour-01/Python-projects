'''
Number Guessing Game 
Play And FUN

'''
import random

com = random.randint(1,100)
while True:
    user = input("Enter a number between 1 to 100: ")
    user_input = int(user)

    if(user_input < 1 or user_input > 100) :
        print("Invalid Number ! Enter a number between 1 and 100.")
    
    elif(user_input > com):
        print("Guess Small Number")

    elif(user_input < com):
        print("Guess Large Number")
    
    else:
        print("\033[96m🏆VICTORY🏆 YOU WIN GAME.\033")
        print("YOUR NICE PERFORMATION.")
        print(f"Computer Number : {com}")
        break

'''
SDBCT Cafeteria Bill Calculator☕🍔

'''
user = input("What would you like to have? (Burger / Chai): ")
Quantity = int(input("How much to Quantity : "))
Burgeroffer = Quantity*50
Chaioffer = Quantity*10

if (user in "Burger"):
    if (Burgeroffer > 200):
        print("\033[93m-------------------------------------------------------\033[0m")
        print("\033[92mSDBCT Cafeteria Bill🍔☕\033[0m")
        print("\033[93m-------------------------------------------------------\033[0m") 
        print("\033[95mYOUR BILL IS GREATER 200 RUPEES THAN 10 PERSENT OFF☑️\033[0m")
        print(f"Dish : {user}\nQuantity : {Quantity}\nTotal Rupees : {Burgeroffer * 90/100}")
        print("\033[93m-------------------------------------------------------\033[0m")
        
    else:
        print("\033[93m-------------------------------------------------------\033[0m")
        print("\033[92mSDBCT Cafeteria Bill🍔☕\033[0m")
        print("\033[93m-------------------------------------------------------\033[0m") 
        print(f"Dish : {user}\nQuantity : {Quantity}\nTotal Rupees : {Burgeroffer}")
        print("\033[93m-------------------------------------------------------\033[0m") 

elif (Chaioffer > 200):
    print("\033[93m-----------------------------------------------------------\033[0m")
    print("\033[92mSDBCT Cafeteria Bill🍔☕\033[0m")
    print("\033[93m-----------------------------------------------------------\033[0m") 
    print("\033[95mYOUR BILL IS GREATER 200 RUPEES THAN 10 PERSENT OFF☑️\033[0m")
    print(f"Dish : {user}\nQuantity : {Quantity}\nTotal Rupees : {Chaioffer * 90/100}")        
    print("\033[93m-----------------------------------------------------------\033[0m")

else:
    print("\033[93m-----------------------------------------------------------\033[0m")
    print("\033[92mSDBCT Cafeteria Bill🍔☕\033[0m")
    print("\033[93m-----------------------------------------------------------\033[0m") 
    print(f"Dish : {user}\nQuantity : {Quantity}\nTotal Rupees : {Chaioffer}")
    print("\033[93m-----------------------------------------------------------\033[0m") 

'''
SDBCT Caferteria Bill Calculator☕🍔
'''

user = input("What would you like to have? (Burger / Chai): ")
Quantity = int(input("How much to Quantity : "))

# 1. Pehle base bill calculate karo item ke hisab se
if "Burger" in user:
    bill = Quantity * 50
elif "Chai" in user:
    bill = Quantity * 10
else:
    bill = 0
    print("Unknown Item")

# 2. Ab check karo ki kya discount milna chahiye ya nahi
if bill > 200:
    final_bill = bill * 0.90
    print("\033[92mSDBCT Cafeteria Bill🍔☕\033[0m")
    print(f"\033[95m10% OFF APPLIED! Total Rupees : {final_bill}\033[0m")
else:
    print("\033[92mSDBCT Cafeteria Bill🍔☕\033[0m")
    print(f"Total Rupees : {bill}")

def name(n):
    '''
    Hello, Harsh 
    '''
    print(name.__doc__)
name(1)

'''
The SDBCT Grace Marks System
'''
def give_grace_marks(marks):
    
    if (marks >= 30) and (marks < 35):
        return marks + 5
    else:
        return marks

'''
Indore Temperature Alert
'''
def weather_alert(temp):
    if (temp >= 40):
        return "Too Hot"
    elif (temp <= 15):
        return "Too Cold"
    else:
        return "Pleasant"
    
'''
The Username Formatter
'''
def format_username(name):
    names = name.lower()
    return names + "_sdbct"

import time
tim = time.strftime("%H,%M,%S")
print(tim)

list = [i*i for i in range(10)]
print(list)
list = [i*i for i in range(10) if i%2==0]
print(list)



