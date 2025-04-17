

def get_elet()-> None:
    my_list=[]
    while True:
        user_input=input("enter your elemnts of array : ")
        if user_input =="":
            break
        my_list.append(user_input)
    return my_list


def main():
    lst=get_elet()
    print(f"List elements : {lst}")


if __name__ == "__main__":
    main()
