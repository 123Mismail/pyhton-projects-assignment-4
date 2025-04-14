def second_year():
    """
    Convert seconds into years, e.g., 360000 seconds ≈ 0.0114 years
    """
    while True:
        user_input = input("Enter your value in seconds or 'q' to quit: ")
        if user_input.lower() == "q":
            break 
        try:
            seconds:float = float(user_input)
            years:float = float(seconds / (60 * 60 * 24 * 365))
            print(f"{seconds} seconds is approximately {years:0.4f} years\n")
        except ValueError:
            print("Invalid input! Please enter a numeric value.\n")

def main():
    print("👋 Hello Welcome!")
    second_year()

if __name__ == "__main__":
    main()
