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
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining real world anagrams = {len(anagrams)}")


def process_choice(name):
    """
    check user choice for validity, returns choice and left over letters
    :param name:
    :return: tuple (string, string)
    """
    while True:
        choice = input("\nMake a choice else Enter to start over or '#' to end: ")

        if choice == "":
            main()
        elif choice == "#":
            sys.exit()
        else:
            # Once the user makes a successful choice, the string is assigned to the variable candidate, stripped off
            # whitespace and converted to all lowercase; so as it can be directly compared to the name variable. After
            # that, a list is build from the name variable to hold any remaining letters
            candidate = "".join(choice.lower().split())
            left_over_list = list(name)

            # Now we begin a loop to subtract the letters used in candidate. If a chosen letter is present in the list
            # it's removed
            for letter in candidate:
                if letter in left_over_list:
                    left_over_list.remove(letter)

            if len(name) - len(left_over_list) == len(candidate):
                print("You entered a word that isn't displayed on the list, or entered multiple words", file=sys.stderr)
                break
            else:
                print("Won't work! Please make another choice!", file=sys.stderr)

    # makes display more readable
    name = "".join(left_over_list)

    return choice, name


def main():
    """
    Helps user build anagram phrase from their name
    """
    name = "".join(initial_name.lower().split())
    name = name.replace("-", "")
    limit = len(name)
    phrase = ""
    running = True

    while running:
        temp_phrase = phrase.replace(" ", "")

        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase = {len(temp_phrase)}")

            find_anagrams(name, dict_file)
            print("Current anagram phrases = ", end=" ")
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + ""
        elif len(temp_phrase) == limit:
            print("\n *****FINISHED*****\n")
            print("Anagram of name=", end=" ")
            print(phrase, file=sys.stderr)
            print()

            try_again = input("\n\nTry again? (Press Enter else 'n' to quit)\n")
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()
