def is_prime(n):
    """
    Decide whether a number is prime or not.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True

def palindromeNumber(n):
    myStr = str(n)
    revStr = myStr[::-1]
    if revStr==myStr: return True

if __name__ == "__main__":
    l = [i for i in range(20) if is_prime(i)]
    print(l)