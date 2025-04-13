
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
print("Hello! Let's calculate the perimeter of a triangle.\nLet's say there is a triangle with sides a, b, and c.")
def main():
     
        try:
            print("Note that a valid triangle must follow:\n a + b > c\n a + c > b\n b + c > a")

            side_a: float = float(input("Enter the first side length of the triangle (e.g., 1, 2, 3...): "))
            print(f"Length of side a of the triangle is: {side_a}")

            side_b: float = float(input("Enter the second side length of the triangle : "))
            print(f"Length of side b of the triangle is: {side_b}")

            side_c: float = float(input("Enter the third side length of the triangle : "))
            print(f"Length of side c of the triangle is: {side_c}")

            if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a :
                perimeter_triangle: float = side_a + side_b + side_c
                print(f"Perimeter of the triangle is: {perimeter_triangle}")
                 
            else:
                print("Your triangle side lengths are invalid. Please enter them again.")

        except ValueError:
            print("Please enter valid numeric values.")
             

# Call the main function
main()

if __name__ == "__main__":
    main()
