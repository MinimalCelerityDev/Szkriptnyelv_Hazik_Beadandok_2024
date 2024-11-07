def palindromeNumber(n):
    myStr = str(n)
    revStr = myStr[::-1]
    if revStr==myStr: return True


def binaryPalindrome(n):
    myStr = str(bin(n))[2:]
    revStr = myStr[::-1]
    if revStr==myStr: return True