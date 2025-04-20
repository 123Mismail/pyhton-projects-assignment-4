
def get_name()->str:
    """
    takes input from user and simply return it.
    """
    try:
        my_name:str=input("Enter my your : ")
    except Exception as e:
        print(f"Here is the error of {e}")
    return my_name


def main():
    my_name:str=get_name()
    print(f"your name is '{my_name}'")
    


if __name__ == "__main__":
    main()
