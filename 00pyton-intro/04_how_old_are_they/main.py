def main():
    print("Hello Anton, Beth, Chen, Drew, and Ethan are all friends! \n Here is below the age of all of them .")
    anton_age:int=21
    print(f"Anton is {anton_age}.")
    beth_age:int=anton_age+6
    print(f"Beth is {beth_age}.")
    chen_age:int=beth_age + 20
    print(f"Chen is {chen_age}.")
    drew_age:int=chen_age+anton_age
    print(f"Drew is {drew_age}.")
    ethan_age:int=chen_age
    print(f"Ethan is {ethan_age}.")


if __name__ == "__main__":
    main()
 