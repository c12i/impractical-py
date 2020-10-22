"""
A much more optimized version of find_palingrams that searches words from a hash set rather than a list.
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
    words = set(word_list)

    for word in words:
        end = len(word)
        rev_word = word[::-1]
        
        if end > 1:
            for idx in range(end):
                if word[idx:] == rev_word[:end-idx] and rev_word[end-idx:] in word_list:
                    pali_list.append((word, rev_word[end-idx:]))
                if word[:idx] == rev_word[end-idx:] and rev_word[:end-idx] in word_list:
                    pali_list.append((word, rev_word[:end-idx]))

    return pali_list
    
palingrams = find_palingrams()
print(palingrams)
