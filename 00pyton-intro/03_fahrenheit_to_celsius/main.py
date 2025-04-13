def main():
    print("Hello! Here you can convert from Fahrenheit to Celsius and vice versa.")
    unit_validation:list[str]=["F","C"]
    # take an input from user 
    print("Select one of the blow")
    print("1-for Fahrenheite enter : F ")
    print("2-for celsius enter : C ")
    user_input:str=input("Enter you value in F | C :").upper()
    if user_input not in unit_validation:
        print("Please select between F ,C to convert")
    else :
        print("Please enter your value")
        user_value:float=float(input("Enter you value :"))
        try:
            
            if user_input =="C":
                celsius_value = (user_value - 32) * 5 / 9
           
                print(f"{user_value}°F is equal to : {celsius_value:.2f}°C")
            elif user_input =="F":
                fahrenheit_value = (user_value * 9 / 5) + 32
                print(f"{user_value}°C is equal to {fahrenheit_value:.2f}°F")
        except ValueError :
            print("Invalid Value!")
        except Exception as e:
            print(f"Error of {e}")    

    


if __name__ == "__main__":
    main()
