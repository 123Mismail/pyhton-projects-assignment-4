def main():
    name=get_name()
    greeting(name)
def get_name()-> str:
    try:
        name:str= input("Enter your name: ")
    except ValueError:
        print("Invalid value error !")
    return name
def greeting(name:str)-> str:
    print(f"Assalamu Alaikum dear '{name}' how are you ?")
if __name__ == "__main__":
    main()
