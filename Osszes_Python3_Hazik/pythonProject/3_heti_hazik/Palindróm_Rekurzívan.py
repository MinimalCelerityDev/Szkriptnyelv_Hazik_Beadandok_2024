def Palindrom_Rekurzívan_Megoldva(a):
    hossza = len(a)
    a = a.lower()
    if hossza < 2:
        return True
    elif a[0] == a [hossza - 1]:
        return Palindrom_Rekurzívan_Megoldva(a[1:hossza-1])
    else:
        return False

def Check_Palindrom_With_Relativ_Method(s):
    if Palindrom_Rekurzívan_Megoldva(s) == True:
        print("Palindróm")
    else:
        print("Nem palindróm")

def main():
    print(Check_Palindrom_With_Relativ_Method("görög"))
    print(Check_Palindrom_With_Relativ_Method("Nem Palindróm"))

if __name__ == "__main__":
    main()