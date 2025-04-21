import random
from typing import List

def main() -> None:
    print("Hello from Rock Paper Scissors Game!")
    start_game()

def start_game() -> None:
    values: List[str] = ['r', 'p', 's']
    my_socre:int=0
    computer_scor:int=0
    while True:
        user_select: str = input("Enter your choice — 'r' for Rock, 'p' for Paper, 's' for Scissors: ").strip().lower()
        if user_select == "":
            print("Game exited.")
            break
        
        comp_select: str = random.choice(values)
        print(f"Computer chose: {comp_select}")

        if user_select == comp_select:
            print("It's a tie!")
        elif (user_select == 'r' and comp_select == 's') or \
             (user_select == 'p' and comp_select == 'r') or \
             (user_select == 's' and comp_select == 'p'):
            print("You win! 🎉🎈🎈")
            my_socre += 1
        else:
            print("You lose!")
            computer_scor += 1
    print(f"Final Score - You: {my_socre}, Computer: {computer_scor}")

if __name__ == "__main__":
    main()
