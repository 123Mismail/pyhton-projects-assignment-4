import time

def count_down(secnd):
    while secnd:
        print(secnd); time.sleep(1); secnd -= 1 # we have written the multiline code in just one line by seperating with semicolumns but here is the general syntax too
        
        #print(secnd)
        #time.sleep(1)
        #secnd -= 1
    

def main():
    start_from=int(input("Enter the number to count down from : "))
    print("SART COUNTDOWN")
    count_down(start_from)
    print("END")


if __name__ == "__main__":
    main()
