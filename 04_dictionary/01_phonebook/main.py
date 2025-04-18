# In this program we show an example of using dictionaries to keep track of information in a phonebook.
def take_vlaues():
    """
    Takes user name and user phone number.
    """
    phonebook={}
    while True:
        user_name=input("Enter your name '' to exit :")
        if user_name =="":
            break
        user_num=input("Enter your number :")
        phonebook[user_name] =user_num
    return phonebook

def show_all(phonebook):
    """
    Show all users with their names and numbers.
    """
    print("Here is the detail of all users .")
    for name, number in phonebook.items():
        print(f"Name: {name}, Number: {number}")

    
        
def lookup_user(phonbook):
    """
    Search for user in the phonbook.
    """
    while True :
        name_ueser=input("Enter user name for search i phonebook : ")
        if name_ueser == "":
            break
        for i in phonbook:
            print(i)
            if name_ueser not in phonbook:
                 
                print(f"User {name_ueser} is not in phonebook.")
                
            print(f"User {name_ueser} is availabel in the phonebook.")
           
                
            
    
def main():
    result =take_vlaues()
    show_all(result)
    lookup_user(result)
    print(result)


if __name__ == "__main__":
    main()
