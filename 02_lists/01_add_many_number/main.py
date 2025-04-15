
def add_lis_evens_numb(number:list[int],mode:str="all")->int:
    """
    Add   elements of a list on the basis of even , odd, all
    """
    initial_sum:int=0
    for num in number :
        if mode=="all":
            initial_sum += num
        elif mode =="even":
            if num%2 == 0:
                initial_sum += num
        elif mode =="odd":
            if num%2 !=0:
                initial_sum += num
    return initial_sum

def main():
    my_list:list[int]=[2,3,4,5,6]
    sum=add_lis_evens_numb(my_list,"all")
    print(f"Sum of  {my_list} element  is = {sum}")


if __name__ == "__main__":
    main()
