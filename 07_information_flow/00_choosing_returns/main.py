def main()->None:
    age:int=take_age()
    res:bool=is_adult(age)
    print(f"Person is adult : {res}")
    

def take_age()->int:
    """
    Takes age as input form user .
    """
    try:
        age:int= int(input("Enter you age : "))
    except ValueError:
        print("Error of invalid value!")
    return age

def is_adult(age:int)-> bool:
    """
    return true of false basis of age .
    """
    ADULT_AGE=20
    if age >= ADULT_AGE:
        return True
    else:
        return False
     
if __name__ == "__main__":
    main()
