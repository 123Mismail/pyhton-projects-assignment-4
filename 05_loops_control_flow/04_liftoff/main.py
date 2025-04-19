import time
def launch_roccet(_time):
    """
    This will print seconds 0 to the determine range and print them.
    """
    for i in range(_time):
        time.sleep(1)
        print(i)
    print("rocket launched!")
        
def main():
    launch_roccet(12)
    
if __name__ == "__main__":
    main()
