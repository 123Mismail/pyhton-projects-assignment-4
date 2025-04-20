def main():
    for i in range(13):
        res=is_odd(i)
        if res :
            print(i,"is odd." ,end=" ")
    

def is_odd(num):
    remainder=num%2
    return remainder == 1

if __name__ == "__main__":
    main()
