import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shift_cipher import decrypt


def load_dictionary():
    dictionary_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "dictionary",
        "english_words.txt"
    )

    with open(dictionary_path, "r") as file:
        return set(word.strip().lower() for word in file if word.strip())


def dictionary_score(text, dictionary):
    words = text.lower().split()
    score = 0

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if word in dictionary:
            score += 1

    return score


def brute_force_dictionary(ciphertext):
    dictionary = load_dictionary()

    results = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = dictionary_score(plaintext, dictionary)

        results.append((score, key, plaintext))

    results.sort(reverse=True)

    return results


if __name__ == "__main__":
    ciphertext = "KHOOR ZRUOG"

    results = brute_force_dictionary(ciphertext)

    print("Brute Force + Dictionary Attack")
    print("--------------------------------")

    for score, key, plaintext in results:
        print(f"Key: {key:2} | Score: {score:2} | {plaintext}")

    best_score, best_key, best_plaintext = results[0]

    print("\nBest Result")
    print("-----------")
    print("Predicted Key:", best_key)
    print("Plaintext    :", best_plaintext)
    print("Score        :", best_score)
