
def get_number_values():
    """
    Get numbers array from user.
    """
    values:int=[]
    while True:
        user_inpt=input("Eneter a number press enter : ")
        if user_inpt =="":
            break
        nums=int(user_inpt)
        values.append(nums)
    return values 

def count_nums(num_list):
    """
    Counts umbers in list.
    """
    counts_dict ={}
    for i in num_list:
        if i not in counts_dict:
            counts_dict[i]=1
        else:
            counts_dict[i] += 1
    return counts_dict
            
def main():
    """
    Runs the entire code inside this file .
    """
    lst=get_number_values()
    count_lst= count_nums(lst)
    print(f"Counts of number of values occur is {count_lst}")

if __name__ == "__main__":
    main()
