 
 
def decide_leap_year(year):
    """
    Validates if it is a leap year or not!
    """
    leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False

    return leap_year

            
     
 
def get_year():
    """
    takes year as an input from user .
    """
    try:
        input_year:int= int(input("Please enter year : "))
    except ValueError:
        print("Please enter a valid value")
    return input_year #remember the variable initialized inside try block is accessibel outside of block
    
    

def main():
    year=get_year()
    result=decide_leap_year(year)
    print(f"your entere year {year} is Leap year : {result}")
    
   

if __name__ == "__main__":
    main()
