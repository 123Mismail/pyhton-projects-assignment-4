
def buy_fruits(fruits):
    summary=[]
    
    try:
        for name,price in fruits.items():
            fruis_baught={}
            fruis_baught["name"]=name
            fruis_baught["price"]=price
            count=input(f"Enter how  many (1,2,3,4,0 ..) '{name}':")
            fruis_baught["count"]=count
            price=int(price)*int(count)
            fruis_baught["total_amonut"]=price
            print(f"count : {count} , name :{name} , price {price} ")
            summary.append(fruis_baught)
           
            
    except Exception as e:
        print(f"Error occurs of {e}")
    return summary

def main():
    available_fruits = {
    "apple": 23,
    "banana": 10,
    "mango": 30,
    "orange": 15,
    "grapes": 40
}
    total_price=buy_fruits(available_fruits)
    print(f"Total summary of purcahse : {total_price}")
    print("=================================")
    total=0
    for details in total_price:
        line = ""
        for key, value in details.items():
            line += f"{key}: {value}, "
            if key =="total_amonut":
                total += value
                
                
        print(line.rstrip(", ")) 
    print(f"Total bill is : ${total}")  

if __name__ == "__main__":
    main()
