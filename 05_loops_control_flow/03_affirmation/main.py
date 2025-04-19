
def get_affirmation(affirmation):
    user_sent=input(f"Enter the affirmation as it is '{affirmation}' :")
    while user_sent != affirmation:
        if user_sent =="":
            break
        print("Please enter the correct affirmation .")
        user_sent=input(f"Enter the affirmation as it is '{affirmation}' :")
        # print(input(f"Enter the correct affirmation '{affirmation}' :"))
    print("You have written the correct affirmation .")

def main():
    AFFIRMATION: str = "I am growing and improving every single day."
    get_affirmation(AFFIRMATION)
    
if __name__ == "__main__":
    main()
