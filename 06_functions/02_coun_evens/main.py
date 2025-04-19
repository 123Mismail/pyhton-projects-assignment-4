
def list_numb_user():
    """
    Takes input from user as integer and store it into a list.
    """
    my_list:list[int]=[]
    while True:
            user_int=input("Enter numbers like ,(1,2,3,4,5,...) and press empty for stop : ")
            if user_int =="":
                break
        
            try:
                print(user_int)
                my_list.append(int(user_int))
            except ValueError:
                print("Invalid data type !")
    return my_list
                
def find_evens(data:list[int]):
    """
    takes list o numbers and seperate even numbers from it.
    """
    even_nums:list[int]=[]
    for i in data:
        if i%2 ==0:
            even_nums.append(i)
    return even_nums
def main():
    data:list[int]=list_numb_user()
    result:list[int] =find_evens(data)
    print(f"Before filtering : {data}")
    print(f"After filtering even numbers : {result}")
    
    for i in result :
        print(i ,end=' ')
    


if __name__ == "__main__":
    main()
