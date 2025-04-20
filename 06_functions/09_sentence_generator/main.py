def make_sentence(word: str, part_of_speech: int) -> None:
    if part_of_speech == 0:
        print(f"I am thrilled to add this {word} to my treasured collection of unique items!")
    elif part_of_speech == 1:
        print(f"The weather is perfect today—it makes me want to {word} all afternoon!")
    elif part_of_speech == 2:
        print(f"Gazing out the window, the sky appears endlessly {word} and calm.")
    else:
        print("Invalid input! Part of speech must be 0 (noun), 1 (verb), or 2 (adjective).")

def get_word_partof_speech() -> tuple[str, int] | None:
    try:
        word = input("Please type a noun, verb, or adjective: ").strip()
        part_of_speech = int(input("Type 0 for noun, 1 for verb, or 2 for adjective: "))
        return word, part_of_speech
    except ValueError:
        print("Invalid input! Please enter a word and choose 0, 1, or 2.")
        return None

def main():
    print("Welcome to the Sentence Generator!")
    print("You'll enter a word and say whether it's a noun, verb, or adjective.\n")
    
    result = get_word_partof_speech()
    if result:
        word, part_of_speech = result
        make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
