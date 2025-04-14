def main():
    print("Hello to convert feet into nches!")
    while True:
        user_input:str =input("Enter your value in feet / (12,3,45...) for quit 'q' : ").lower()
        if user_input =="q":
            break
        try:
            feet:float =float(user_input)
            print(f"User input value in feet is {feet} /feet")
            inches:float =feet*12
            print(f"{feet}/feet = {inches}/inches")
        except ValueError:
            print("Please enter a valid value !")


if __name__ == "__main__":
    main()
