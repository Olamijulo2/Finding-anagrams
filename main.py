# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
   
    if len(word) == len(anagram):

    # Sorting and checking values equality
        if sorted(word) == sorted(anagram):
            return True
        return False

    return "The strings are not anagrams, they have different lengths"

print(find_anagram("pots", "stop"))