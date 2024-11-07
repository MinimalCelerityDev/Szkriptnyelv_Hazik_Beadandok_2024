def ervenyesseg(reszleg):

    szavak = reszleg.split()


    return len(szavak) == len(set(szavak))

def szamo(s):

    valid_count = sum(1 for phrase in s if ervenyesseg(phrase))

    return valid_count


reszek = [

    "aa bb cc dd ee",
    "aa bb cc dd aa",
    "aa bb cc dd aaa"

]

print(szamo(reszek))
