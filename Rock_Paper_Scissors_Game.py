''' 
Rock, Paper, Scissors Game
Play and Fun
'''
import random

def play_game():
    print("-" * 40)
    print("✊✋✌️ ROCK, PAPER, SCISSORS GAME ✊✋✌️")
    print("-" * 40)

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter Rock, Paper, or Scissors (or type 'quit' to exit): ").lower().strip()
        
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!👋")
            break

        elif user_choice not in choices:
            print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("🤝 It's a tie!\n")

        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
                print("🎉 Victory! You win this round!🏆\n")
        else:
            print("💥 Computer wins! Better luck next time.\n")

if __name__ == "__main__":
    play_game()
    