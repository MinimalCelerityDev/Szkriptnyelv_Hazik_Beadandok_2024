def xor_check(a, b):

    return bool(a) != bool(b)

str1 = "python"
str2 = None

eredmenyesseg = xor_check(str1, str2)

print("Az egyik igaz, a másik hamis:", eredmenyesseg)
