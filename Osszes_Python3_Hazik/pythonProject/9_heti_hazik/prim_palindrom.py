from isprime_module import is_prime, palindromeNumber
import itertools


def primePalindrome(n):
    for i in itertools.count(start=n):
        if palindromeNumber(i) and is_prime(i):
            print(i)
            break


def main():
    N = 1977
    primePalindrome(N)


if __name__ == "__main__":
    main()