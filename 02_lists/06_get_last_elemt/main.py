
def get_last_elemt(my_list)->None:
    last_elemt=my_list[len(my_list) -1]
    print(last_elemt ," : Last element of the list")

def get_elemt()->None:
    """
    get elements from user and append it into a list
    """
    my_list=[]
    while True:
        user_input=input(f"Enter elemetns to add into the list {my_list} :")
        if user_input =="":
            break
        my_list.append(user_input)
    return my_list
    

def main():
     lst=get_elemt()
     print(lst)
     get_last_elemt(lst)


if __name__ == "__main__":
    main()
