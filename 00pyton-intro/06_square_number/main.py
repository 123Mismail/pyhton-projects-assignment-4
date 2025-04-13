def main():
    print("Enter the number you want to square (or type 'q' to quit).")
    while True:
        user_input:str = input("Enter your number (e.g., 1, 2, 3...) or 'q' to quit: ")

        if user_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            num:float = float(user_input)
            num_squared:float = num ** 2
            print(f"{num} squared is {num_squared}")
        except ValueError:
            print("Please enter a valid numeric value!")

if __name__ == "__main__":
    main()
