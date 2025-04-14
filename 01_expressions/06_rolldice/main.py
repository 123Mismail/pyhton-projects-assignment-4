import random

# Simulate rolling two dice, and prints results of each roll as well as the total.
NUM_SIDES:int =6
def roll_dice():
   roll_1:int=random.randint(1,NUM_SIDES)
   print(f"Value of first roll of dice : {roll_1} ")
   roll_2:int=random.randint(1,NUM_SIDES) 
   print(f"Valuse of second roll of dice : {roll_2}")
   sum_roll:int= roll_1+roll_2
   print(f"Sum of dices roll is = {sum_roll}")
def main():
    print("Hello welcome lets roll two dice !")
    roll_dice()

if __name__ == "__main__":
    main()
