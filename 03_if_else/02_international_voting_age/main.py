def decide_vote(age) -> None:
    age_limit_pak = 18
    age_limit_ind = 20
    age_limit_afg = 23

    if age >= age_limit_afg:
        print("You are eligible for voting in all three countries (Pakistan, India, Afghanistan).")
    elif age >= age_limit_ind:
        print("You are eligible for voting in Pakistan and India.")
    elif age >= age_limit_pak:
        print("You are eligible for voting only in Pakistan.")
    else:
        print("You are not eligible to vote in any of the countries!")

def get_user_age():
    try:
        user_age = int(input("Enter your age: "))
        return user_age
    except ValueError:
        print("Please enter a valid value!")
        
    

def main():
    age = get_user_age()
    decide_vote(age)

if __name__ == "__main__":
    main()
