def main():
    fisrt_name,last_name,email=return_multiple_values()
    print(f"Hello here is your detail : \n First Name: {fisrt_name} \n Last Name :{last_name} \n Email : {email}")
def return_multiple_values():
    """
    Get details of user and return them.
    """
    try:
        fisrt_name:str= input("Enter your fisrt name : ").strip()
        last_name:str=input ("Enter your last name : ").strip()
        email:str=input("Enter your email id : ").strip()
    except ValueError :
        print("Invalid value error !")
    return (fisrt_name,last_name,email)

if __name__ == "__main__":
    main()
