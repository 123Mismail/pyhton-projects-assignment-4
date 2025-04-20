
def get_divisor(num):
    for i in range(1,int(num)+1):
        if num%i ==0:
            print(i , end=" ")

def get_num()->int:
    try:
        number:float=float(input("Enter your number her : "))
    except Exception as e :
        print(f"error of {e}")
    return number
    

def main():
    num_val:int=get_num()
    get_divisor(num_val)
    


if __name__ == "__main__":
    main()
