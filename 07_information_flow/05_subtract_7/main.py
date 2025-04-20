def main():
    res :int =get_num()
    print(res)

def get_num():
    """
    Takes input an integer from user and subtract 7 from the number .
    """
    try:
        num:int= int(input("Enter your number : "))
    except ValueError :
        print("Error occur of invalid value !")
    res:int = num - 7
    return res
if __name__ == "__main__":
    main()
