import random
import time
def done():
    """
    returns true if the val is less the 0.2 else false
    """
    val=random.random()
    return val < 0.2

def chaotic_counting():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    for i in range(15):
        time.sleep(1)
        if done():
            return
        print(i)

def main():
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()
