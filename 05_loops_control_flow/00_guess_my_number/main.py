import random

def genrerate_random_num():
    rand_num=random.randint(1,11)
    
    return rand_num
def guess_number():
    """
    takes a number from user and compares with the random number.
    """
    while True:
        random_num=genrerate_random_num()
        user_inpt=input("Guess a number between (1,10) : ")
        if user_inpt =="":
            break
        if int(user_inpt) == random_num:
            print(f"Congratulations you have guess {user_inpt} = {random_num} correctly!")
        elif int(user_inpt) > random_num:
            print(f"Sorry your guess was higer then random number {user_inpt} > {random_num} .")
        elif int(user_inpt) < random_num:
            print(f"Sorry your guess was lower then random number {user_inpt} < {random_num} .")
        
def main():
    
    guess_number()
    


if __name__ == "__main__":
    main()
