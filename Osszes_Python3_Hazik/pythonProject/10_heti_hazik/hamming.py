# hamming.py

def hamming_distance(s1: str, s2: str) -> int:

    if len(s1) != len(s2):

        raise ValueError("A két sztring hossza nem egyezik meg.")

    return sum(1 for a, b in zip(s1, s2) if a != b)
