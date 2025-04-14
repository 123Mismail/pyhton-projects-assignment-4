import math

def main():
    print("Let's consider a right triangle ABC, with the right angle at C.")
    print("According to the Pythagorean theorem: BA² = AC² + BC²")

    while True:
        user_input1 = input("Enter one side perpendicular to the right angle triangle (or 'q' to quit): ").lower()
        
        
        if user_input1 == "q" :
            break

        try:
            side_1 = float(user_input1)
            print(f"Perpendicular side of the triangle: {side_1}")
            side_2:float = float(input("Enter the other side perpendicular to the right angle triangle (or 'q' to quit): "))
            
            print(f"Base side of the triangle: {side_2}")
            
            hypotenuse = math.sqrt(side_1**2 + side_2**2)
            print(f"Hypotenuse of the triangle = {hypotenuse:.2f}\n")
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")

if __name__ == "__main__":
    main()
