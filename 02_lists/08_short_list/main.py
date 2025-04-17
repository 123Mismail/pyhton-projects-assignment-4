

def resize_list(lst,max_length):
    """
    resize the list according to the max_length
    """
    if len(lst) >= max_length:
        while True:
            if len(lst) == max_length:
                break
            remove_ele=lst.pop()
            print(f"Every removed element: {remove_ele} ")
        return lst
    return lst
    

def get_list_elt():
    """
    get elements from user and add it into list.
    """
    my_list=[]
    while True:
        user_input=input(f"Enter elements to add into list {my_list} :")
        if user_input =="":
            break
        my_list.append(user_input)
    return my_list

def main():
    max_length=3
    list_elmt=get_list_elt()
    print(f"my list elemets : {list_elmt}")
    resizesd_list=resize_list(list_elmt,max_length)
    print(f"List after resized : {resizesd_list}")
    


if __name__ == "__main__":
    main()
