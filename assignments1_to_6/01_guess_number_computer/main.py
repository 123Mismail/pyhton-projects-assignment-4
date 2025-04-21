import random




def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
          if not low > high:
            guess = random.randint(low, high)
            print(guess,"initial guess")
          else:
            print("Invalid range error !")
        else:
            guess = low  
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
            print(high,"high is printing")
        elif feedback == 'l':
            low = guess + 1
            print(low ,"low is printing")

    print(f'Yay! The computer guessed your number, {guess}, correctly!')
def main():
    computer_guess(6)
  
if __name__ == "__main__":
    main()


