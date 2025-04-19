
def generate_fibonacci(n):
    a,b = 0,1
    for i in range(n):
        print(a ,end=" ")
        a,b =  b , a+b
         
def main():
    generate_fibonacci(10)
if __name__ == "__main__":
    main()
