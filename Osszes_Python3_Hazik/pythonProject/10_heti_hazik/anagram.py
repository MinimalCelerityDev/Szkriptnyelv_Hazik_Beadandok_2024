# anagram.py

def is_anagram(word1: str, word2: str) -> bool:

    return sorted(word1.replace(" ", "").lower()) == sorted(word2.replace(" ", "").lower())
