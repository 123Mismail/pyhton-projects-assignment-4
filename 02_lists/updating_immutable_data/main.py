def copy_message(my_tuple: tuple[str], data: str) -> None:
    # Attempt to "add" data 3 times (will create new tuples, but not stored)
    for i in range(3):
        my_tuple += (data,)  # Creates a new tuple, doesn't affect the original
        print(f"Inside function: {my_tuple}")
    return my_tuple

def main():
    my_tuple: tuple[str] = ()
    message: str = input("Enter your message: ")
    print(f"Tuple before copy_message: {my_tuple}")
    return_tuple:tuple[str]=copy_message(my_tuple, message)
    print(f"Tuple after copy_message: {return_tuple}")  # Still empty

if __name__ == "__main__":
    main()