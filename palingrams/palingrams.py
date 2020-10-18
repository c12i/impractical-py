"""
Find all word-pair palingrams in a dictionary file.
"""

import load_data

word_list = load_data.load("./words.txt")

def find_palingrams():
    """
    Finds word-pair palingrams

    Returns:
        - A list of strings
    """
    pali_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        
        if end > 1:
            for idx in range(end):
                if word[idx:] == rev_word[:end-idx] and rev_word[end-idx:] in word_list:
                    pali_list.append((word, rev_word[end-idx:]))
                if word[:idx] == rev_word[end-idx:] and rev_word[:end-idx] in word_list:
                    pali_list.append((word, rev_word[:end-idx]))

    return pali_list

if __name__ == "__main__":
    palingrams = find_palingrams()
    print(palingrams)
