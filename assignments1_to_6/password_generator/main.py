import random
import hashlib
import os

HASH_FILE = "password_hashes.txt"

def main():
    print("Hello from password-generator!")
    length_pass, no_passwords = get_length_num()
    generate_unique_passwords(length_pass, no_passwords)

def get_length_num():
    while True:
        try:
            length_pass = int(input("Enter the desired length of password: "))
            number_pass = int(input("Enter the number of passwords you want to generate: "))
            return length_pass, number_pass
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def load_hashes():
    if not os.path.exists(HASH_FILE):
        return set()
    with open(HASH_FILE, 'r') as file:
        print(file.read())
        return set(line.strip() for line in file )

def save_hash(hash_str):
    with open(HASH_FILE, 'a') as file:
        file.write(hash_str + '\n')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_unique_passwords(length, no_passwords):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    used_hashes = load_hashes()
    generated_passwords = []

    while len(generated_passwords) < no_passwords:
        password = ''.join(random.choice(characters) for _ in range(length))
        password_hash = hash_password(password)

        if password_hash not in used_hashes:
            used_hashes.add(password_hash)
            save_hash(password_hash)
            generated_passwords.append(password)

    print("\nGenerated Unique Passwords:")
    for i, p in enumerate(generated_passwords, start=1):
        print(f"{i}: {p}")

if __name__ == "__main__":
    main()
