import random
def generte_random_number():
    """
    Generates random numbers.
    """
    
    for i in range(1,11):
        print(random.randint(1,100) ,end=" ")
    

def main():
    generte_random_number()


if __name__ == "__main__":
    main()
