 
 
def get_number()->int:
    """
    takes input number from user 
    """
    user_input:str=input("enter your number to double.: ")
    try:
        num:int=int(user_input)
    except Exception as e:
        print(f"There is error of {e}")
    return num 

def doubel_num(num:int)->int:
    """
    double the given number.
    """
    doubel:int=num*2
    return doubel
    
def main():
    """
    this function is responsible for running all other functions inside it.
    """
    number_frodouble:int=get_number()
    num_doubled=doubel_num(number_frodouble)
    print(f"{number_frodouble} double is : {num_doubled}")
    


if __name__ == "__main__":
    main()
