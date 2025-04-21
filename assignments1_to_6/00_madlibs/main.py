def main():
    adjective ,verb1, verb2, famous_person =get_data()
    madlib = f"Spending time in nature is so {adjective}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
    print(madlib)

def get_data():
    try:
        adjective:str=input("Please enter an adjective like ('refreshing',) :")
        verb1:str=input("Please eter a verb like ('explore',) :")
        verb2:str=input("Please eter a verb like ('breathe',) :")
        famous_person:str=input("Please enter famous prson name like ('Bear Grylls') : ")
    except ValueError:
        print("Error of invalid value!")
    return (adjective,verb1,verb2,famous_person)
if __name__ == "__main__":
    main()
