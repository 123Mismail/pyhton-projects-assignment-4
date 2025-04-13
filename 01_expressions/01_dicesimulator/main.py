# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
import random 
NUM_SIDES:int=6
def rol_dice():
    """
    roles the dice two times and calculate the sum and print it.
    """
    roll_dice1:int=random.randint(1,NUM_SIDES)
    print(f"Value of roll dice 1 : {roll_dice1}")
    roll_dice2:int=random.randint(1,NUM_SIDES)
    print(f"Value of roll dice 2 : {roll_dice2}")
    total:int =roll_dice1 + roll_dice2
    print(f"sum of rolle of (dice-1): {roll_dice1} and (dice-2): {roll_dice2} and total : {total}")
    


def main():
    roll_dice1=10
    print(f"die 1 in main starts with value :{roll_dice1}")
    rol_dice() #here should be the value of dice 1 form roll dice function
    rol_dice() #here should be the value of dice 1 form roll dice function
    rol_dice() #here should be the value of dice 1 form roll dice function
    print(f"die1 in main() is {roll_dice1}") #but here should be the number value as initialize in this functions scope
    

if __name__ == "__main__":
    main()
