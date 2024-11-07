#!/usr/bin/env python3

def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))

            szam2 = float(input("2. szam: "))

            result = szam1 / szam2

            print('Az osztas eredmenye: {0:.2f}'.format(result))

            print('-' * 10)

        except ValueError:
            print("nem szám lett megadva!")
        except ZeroDivisionError:
            print("nullával történt!")
        except (KeyboardInterrupt, EOFError):
            print("\nKilepes...")
            break

if __name__ == "__main__":
    main()
