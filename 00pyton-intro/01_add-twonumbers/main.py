def main():  
    # we have write the code inside the try block so if there any error then we can handel it
    try:
        # taking two numbers from user and converting them into float
        user_number1:float=float(input("Enter your first number (1,2,3 ,..): "))
        user_number2:float=float(input("Enter your second number (1,2,3,...): "))
        # adding two numbers 
        print(f"result of number {user_number1} + {user_number2 }= {user_number1+user_number2}")
        # excepting value error 
    except ValueError:
        print("your input value must be float type")
    except Exception as e:
        print(f"error occurs {e}")
        

if __name__ == "__main__":
    main()
