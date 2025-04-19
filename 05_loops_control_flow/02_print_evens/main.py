def generate_evens(n):
    for i in range(n):
        if i%2 ==0:
            print(i , end=' ')
    

def main():
    range_num=30
    generate_evens(range_num)


if __name__ == "__main__":
    main()
