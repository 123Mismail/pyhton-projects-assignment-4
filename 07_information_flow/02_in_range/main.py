def main():
    # here also try with n less then range and higher the range and also in range
    res:bool=in_range(21,5,20)
    print(res)


def in_range(n, low , high):
    if n< high and n>low:
        return True
    return False

if __name__ == "__main__":
    main()
