def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):

    result = ""

    for c in text:

        if c in chars:

            result += c

    return result


print(valid("Barking!"))            # -> "B"
print(valid("KL754", "0123456789"))  # -> "754"
print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))  # -> ""
