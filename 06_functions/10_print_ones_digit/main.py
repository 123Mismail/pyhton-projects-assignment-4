

def print_place_values(num):
    place_names = ["ones", "tens", "hundreds", "thousands", "ten-thousands",
                   "hundred-thousands", "millions", "ten-millions", "hundred-millions", "billions"]

    num_digits = len(str(num))

    for i in range(num_digits):
         
        digit = (num // (10 ** i)) % 10
        place = place_names[i] if i < len(place_names) else f"10^{i} place"
        print(f"{place.capitalize()} digit: {digit}")

 

def main():
    print("Hello from 10-print-ones-digit!")
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invald value")
    print_place_values(num)

if __name__ == "__main__":
    main()
