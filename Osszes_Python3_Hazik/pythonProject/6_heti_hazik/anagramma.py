def kis_minimalizalas(t):

    return ''.join(t.lower().split())

def are_anagrams(elso_szo, masodik_szo):

    return sorted(kis_minimalizalas(elso_szo)) == sorted(kis_minimalizalas(masodik_szo))


print(are_anagrams("listen", "silent"))

print(are_anagrams("A gentleman", "Elegant man"))

print(are_anagrams("Clint Eastwood", "Old west action"))

print(are_anagrams("dormitory", "dirty room"))

print(are_anagrams("apple", "pale"))

