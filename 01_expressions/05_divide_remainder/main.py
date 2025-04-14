# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
    print("Hello welcome here you can divide two numbers and output will be result and remainder also!")
    while True :
        user_input:str= input("Enter you first number or 'q' for quit :")
        if user_input =='q':
            break
        try:
            num_1:int =int(user_input)
            print(f"User frist  number is {num_1}")
            num_2:int= int(input("Enter you first number or 'q' for quit : "))
            print(f"User enter second number is {num_2} ")
            divsion_value:int = num_1 / num_2
            remainder_value:int= num_1 // num_2
            print(f"The result of this division is {divsion_value:.0f} with a remainder of {remainder_value}")
        except ValueError:
            print("Enter a valid number !")
        except Exception as e:
            print (f"Error occurs of {e}")
                       


if __name__ == "__main__":
    main()
