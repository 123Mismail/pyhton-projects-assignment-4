
def copy_message(my_list:list[str],data:str)->None:
    for i in range(3):
        my_list.append(data)
        print(my_list)
    
def main():
    my_list:list[str]=[]
    message:str=input("Enter your message : ")
    print(f"List value before copy_message  {my_list}")
    copy_message(my_list,message)
    print(f"List value after copy_message  {my_list}")
    
if __name__ == "__main__":
    main()

