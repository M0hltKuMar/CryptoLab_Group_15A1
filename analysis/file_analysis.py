from collections import Counter

def analyze_file(filename):

    with open(filename, "r") as file:
        text = file.read()

    characters = len(text)

    words = len(text.split())

    lines = len(text.splitlines())

    unique_characters = len(set(text))

    letters = []

    for ch in text:

        if ch.isalpha():

            letters.append(ch.lower())

    frequency = Counter(letters)

    print("\n========== File Analysis ==========\n")

    print("Characters :", characters)

    print("Words      :", words)

    print("Lines      :", lines)

    print("Unique Characters :", unique_characters)

    print("\nLetter Frequency\n")

    for letter in sorted(frequency):

        print(letter, ":", frequency[letter])