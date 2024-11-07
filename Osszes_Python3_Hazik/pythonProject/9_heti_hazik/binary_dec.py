from binary_decimal_module import palindromeNumber, binaryPalindrome


def isPal():
    osszeg = 0
    n = 1000000
    for i in range(1,n):
        if palindromeNumber(i) and binaryPalindrome(i):
            osszeg += i
    print(osszeg)


def main():
    isPal()


if __name__ == "__main__":
    main()