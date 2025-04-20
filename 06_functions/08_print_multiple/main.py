def print_multiple_times(message:str,times:int)-> None:
    """
    prints the message mention no of times.
    """
    for _ in range(times):
        print(message)
def get_message_times()-> None:
    """
    Get the message and no of times to pront the message.
    """
    try:
        message:str=input("Enter your message to print : ")
        times:int=int(input("Enter no of times you wants to print the message : "))
    except ValueError:
        print("Invalid values !")
    return message , times
def main():
    message,times= get_message_times()
    print_multiple_times(message ,times )
    
   


if __name__ == "__main__":
    main()
