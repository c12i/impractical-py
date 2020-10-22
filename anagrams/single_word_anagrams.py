"""
Find anagrams (a word formed by rearranging the letters of another word) of a user provided word from a dictionary file
"""

import load_data

word_list = load_data.load("words.txt")

# input a SINGLE word or a SINGLE name below to find its anagrams
while True:
    anagram_list = []

    name = input(f"Input name or type q to quit: ").lower()
    while len(name.split(" ")) > 1:
        name = input("Single words only! Try again: ").lower()

    if name.lower() == "q":
        break

    print(f"Using the name {name}")
    name_sorted = sorted(name)

    for word in word_list:
        if word != name:
            if sorted(word) == name_sorted:
                anagram_list.append(word)

    # printing out anagram list
    if len(anagram_list) == 0:
        print("You need a larger dictionary or a new name")
    else:
        print(f"{len(anagram_list)} anagrams found: ", *anagram_list, sep="\n")
