def make_decision(height,min_height):
    """
    Makes decisions on the basis of user height.
    """
    if height >= min_height:
        print(f"{height} : is able to ride.")
    else:
        print(f"{height} height : is not able to ride.")
        
    
def get_height_user()->None:
    """
    Get height from user in cm.
    """
    try:
        user_height:float=float(input("Enter your height in cm."))
    except ValueError:
        print("Please enter a valid valid")
    return user_height

def main():
    mi_height =100
    height =get_height_user()
    make_decision(height,mi_height)
    
    


if __name__ == "__main__":
    main()
