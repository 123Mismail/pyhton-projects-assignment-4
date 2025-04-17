from typing import Union

def print_first_elmt(my_list: list[Union[int, float, str]]) -> None:
    """
    Prints the first element of a list.
    """
    print(my_list[0], ": is the first element of the list")

def get_elemt() -> list[Union[int, float, str]]:
    my_list = []
    while True:
        user_input = input("Please enter an element (or press enter to stop): ")
        if user_input == "":
            break
        my_list.append(user_input)
    return my_list

def main():
    lst = get_elemt()
    print(lst, "list elements")
    if lst:
        print_first_elmt(lst)
    else:
        print("The list is empty, no first element.")

if __name__ == "__main__":
    main()

 
    
 
