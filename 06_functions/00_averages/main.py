# Write a function that takes  numbers and finds the average between the two.
def takes_numbers()->list[float]:
    """
    Takes numbers from user and store it into a list.
    """
    nums:list[float] =[]
    while True:
        user_input:str=input("Enter your numbers : (1,2,3,4,5,6,...) : ")
        if user_input == "":
            break
        try:
            num:float =float(user_input)
            nums.append(num)
            print(nums)
        except ValueError :
            print("Error invalid data type ! ")
    return nums

def find_avg(nums)->float:
    """
    Takes list of integers and return the average of elements in it.
    """
    average_val:float=0
    sum=0
    num_list:list[float]=nums
    n:int =len(nums)
    for  i in num_list:
        sum +=  i
    average_val = sum/n
    return average_val
     
def main():
    nums=takes_numbers()
    average=find_avg(nums)
    print(f"Average of list numbers is : {average}")
    
if __name__ == "__main__":
    main()
