def get_valid_count(name):
    """
    Prompts the user for a valid count of fruits and ensures the input is a positive integer.
    """
    while True:
        count = input(f"Enter how many {name} (positive number): ")
        if count.isdigit() and int(count) > 0:
            return int(count)
        else:
            print("Invalid input. Please enter a positive number.")

def buy_fruits(fruits):
    summary = []
    
    for name, price in fruits.items():
        # Using better variable naming and cleaning up the process
        count = get_valid_count(name)
        total_amount = price * count
        
        # Directly create the dictionary for each fruit purchase
        fruit_bought = {
            "name": name,
            "price": price,
            "count": count,
            "total_amonut": total_amount
        }
        
        summary.append(fruit_bought)
        print(f"count: {count}, name: {name}, price: {total_amount}")

    return summary

def display_summary(total_price):
    """
    Displays the fruit purchase details and calculates the total bill.
    """
    total = 0
    print("=================================")
    for details in total_price:
        line = ""
        for key, value in details.items():
            line += f"{key}: {value}, "
            if key == "total_amonut":
                total += value
        print(line.rstrip(", "))  # Removing trailing comma and space
    return total

def main():
    available_fruits = {
        "apple": 23,
        "banana": 10,
        "mango": 30,
        "orange": 15,
        "grapes": 40
    }
    
    total_price = buy_fruits(available_fruits)  # Calling buy_fruits to get the details
    print("Total summary of purchase:")
    total = display_summary(total_price)  # Calling display_summary to print and calculate total bill
    print(f"Total bill is: ${total}")

if __name__ == "__main__":
    main()
