import random
from words import list_words
from typing import List, Set

def get_words(list_words: List[str]) -> str:
    word = random.choice(list_words)
    while '-' in word and ' ' in word:
        word = random.choice(list_words)
    return word.upper()

def guess_letter_in_word(word: str) -> None:
    your_guessed: Set[str] = set() 
    while len(your_guessed) < len(word):
        guess_letter: str = input("Guess a letter which is in currect word : ").upper()
        your_guessed.add(guess_letter)
        print(your_guessed)
        if len(guess_letter) != 1:
            print("Please enter a single letter.")
            return
        if guess_letter in word:
            print(f"Correct! The letter  {guess_letter} is in the word  '{word}' 🎈🎉")
            return
        else:
            print("Incorrect! The letter is not in the word.")
            print(f"Your guessed letters : {your_guessed}")
    print("You have over the length of letters in the word.")
    return

def main() -> None:
    word: str = get_words(list_words)
    guess_letter_in_word(word)
    print(word)

if __name__ == "__main__":
    main()
