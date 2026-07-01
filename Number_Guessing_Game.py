'''
Number Guessing Game 
Play And FUN

'''
import random

rand = random.randint(1,100)
while True:
    user = input("Enter a number between 1 to 100: ")
    user_input = int(user)

    if(user_input < 1 or user_input > 100) :
        print("Invalid Number ! Enter a number between 1 and 100.")
    
    elif(user_input > rand):
        print("Guess Small Number")

    elif(user_input < rand):
        print("Guess Large Number")
    
    else:
        print("\033[96m🏆VICTORY🏆 YOU WIN GAME.\033")
        print("YOUR NICE PERFORMATION.")
        print(f"Computer Number : {rand}")
        break