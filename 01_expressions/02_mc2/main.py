# When light travels through materials (like air, water, or glass), it slows down due to interactions with the particles in the medium. Here's how it compares:
#Medium	Approx. Speed of Light
# Vacuum	299,792,458 m/s (exact)
# Air	~299,702,547 m/s
# Water	~225,000,000 m/s
# Glass	~200,000,000 m/s
# Diamond	~124,000,000 m/s
# but we generally use vacuum = 299,792,458 m/s (exact)

def main():
    # print("Hello Covert mass into energy \n as we know that the mass energy formula is given by sir Einstain \n according to which E=m*c^2 \ where m is the mass of object \n and c is the speed of light ")
    while True:
        user_input:str =input("Enter mass in kg (23 ,22,34,..) for quit 'q': ").lower()
        if user_input =="q":
            break
        try :
            mass_kg:float = float(user_input)
            c:float=float(299792458) 
            print(f"mass of object is = {mass_kg}kg")
            print("as value of constant c in vacuum is = 299,792,458 m/s ")
            print(f" E=mc^2 = {mass_kg*c**2} joules")
        except ValueError:
            print("Plese enter a valid value !")
        
    
    

if __name__ == "__main__":
    main()
