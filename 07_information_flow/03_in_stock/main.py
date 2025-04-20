def main():
  try:
    fruit:str =input("Write fruit name (Apple ,Banana , Orange , Grapes , Mango) : ").strip()
    check_stock(fruit)
  except ValueError:
    print("Error of invalid value !")

def check_stock(fruit:str):

    stock_fruits = [
    {"fruit": "Apple", "stock": 50},
    {"fruit": "Banana", "stock": 0},
    {"fruit": "Orange", "stock": 45},
    {"fruit": "Grapes", "stock": 0},
    {"fruit": "Mango", "stock": 25}
    ]
    for fruits in stock_fruits:
      if (fruit).lower() == (fruits["fruit"]).lower():
        print(f"fruit {fruit} is availbel in stock of : {fruits['stock']}")
      
      
        
    
if __name__ == "__main__":
    main()
