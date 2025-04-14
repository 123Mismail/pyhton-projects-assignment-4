
# Here's a sample run (user input is in bold italics):
# Please type an adjective and press enter. tiny
# Please type a noun and press enter. plant
# Please type a verb and press enter. fly
# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

SENTENCE_START="GIAIC is fun. I learned to program and used Python to make my"
def main():
    
    print("Hello mad lib game !")
    try:
        adjective:str=input("Please type an adjective and press enter : ")
        noun:str=input("Please type an noun and press enter : ")
        verb:str=input("Please type an verb and press enter : ")
        print(SENTENCE_START  + " " + adjective + " " + noun + " " + verb + "!")
    except ValueError:
        print(f"Error invalid input")
        


if __name__ == "__main__":
    main()
