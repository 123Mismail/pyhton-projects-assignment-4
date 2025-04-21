import random 

def main():
    print("Welcome to umber guessing game .")
    gues_number()
   
def gues_number():
    start:int = 1
    end_range:int = int(input("Enter the range iin which you want to guess from 1 to _ :"))
    random_number:int=random.randint(start , end_range)
    print(random_number ,"random number ")
    while True:
        guess:str= input(f"Guess a number between ({start } to {end_range}) : ")
        if guess =="":
                break
        try:
            guess=int(guess)
            
            if  random_number == guess:
                print(f"You have selected the correct  value 🎈  {random_number}={guess}")
                break
            elif guess < random_number:
                print(f"Your guess is less then random number !")
            elif guess > random_number:
                print("Your guess is high then random number !")
        except ValueError :
            print("Invalid value error !")

if __name__ == "__main__":
    main()
