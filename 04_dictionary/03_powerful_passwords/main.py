from hashlib import sha256
def get_password():
    try:
        user_pass=input("Enter your password :")
    except Exception as e:
        print(f"Error occurs of {e}")
    return user_pass # as variable initialized inside the try block is available outside of the block
def generate_hash(password):
     """ 
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """
     return sha256(password.encode()).hexdigest()
def validate_password(password,hashed_passwords):
    for key , value in hashed_passwords.items():
        if value == generate_hash(password):
            return True
        return False
    
def main():
    hashed_passwords={
        "hello":"2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        "balti":"367282a965be69b645b5dc0cc71e8a7ac1351b2568875827deb0b66945feadb5"
    }
    password=get_password()
    hashed_pass=generate_hash(password)
    result =validate_password(password,hashed_passwords)
    print(f"Password is correct : {result}")
    print(f"Hashed password is : {hashed_pass}")
   
if __name__ == "__main__":
    main()
