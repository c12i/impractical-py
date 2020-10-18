"""
Find palindromes (letter palingrams) in a dictionary file
"""

import load_data

word_list = load_data.load("./words.txt")
pali_list = [w for w in word_list if len(w) > 1 and w == w[::-1]]

print(f"\nNumber of palindromes found = {len(pali_list)}")
print(*pali_list, sep="\n")