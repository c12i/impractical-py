import sys
from collections import Counter
import load_data

dict_file = load_data.load("words.txt")

# ensure "a" ad "I" (both lowercase are included)
dict_file.append("a")
dict_file.append("i")

dict_file = sorted(dict_file)

initial_name = input("Enter a name: ")


def find_anagrams(name, word_list):
    """
    Read the name and dictionary file and display all anagrams in name
    :param name: string
    :param word_list: list of strings
    """
    name_letter_map = Counter(name)
    anagrams = []

    for word in set(word_list):
        test = ""
        word_letter_map = Counter(word.lower())
        for letter in word:
            # If the count for each letter in a word is <= the count for the same letter in a name,
            # then the word can be derived from the name
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep="\n")
    print("*" * 100)
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining real world anagrams = {len(anagrams)}")


def main():
    find_anagrams(initial_name, dict_file)


if __name__ == '__main__':
    main()