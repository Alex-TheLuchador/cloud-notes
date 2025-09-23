import math
# Status: Completed

def return_mismatched_words(str1, str2):
    words1, words2 = str1.split(), str2.split() # splits string on spaces
    set1, set2 = set(words1), set(words2) # sets provide O(1) membership checks

    only_in_1 = [w for w in words1 if w not in set2]
    only_in_2 = [w for w in words2 if w not in set1]

    print(only_in_1 + only_in_2)
    return (only_in_1 + only_in_2)

return_mismatched_words("Firstly this is the first string", "Next is the second string")