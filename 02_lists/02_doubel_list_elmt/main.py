
def double_list_el(list_elm:list[int])->list[int]:
    """
    Doubles the elements of a list.
    """
    double_list:list[int]=[]
    for i  in list_elm:
        new_elm:int=i*2
        double_list.append(new_elm)
    return double_list
    


def main():
    my_list:list[int]=[1,2,3,4,5,6]
    result:list[int]=double_list_el(my_list)
    print(f"double of elements of {my_list} is {result} ")
    
    


if __name__ == "__main__":
    main()
