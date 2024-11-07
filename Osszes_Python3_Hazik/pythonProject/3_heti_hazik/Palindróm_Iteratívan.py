#!/usr/bin/env python3
# coding: utf-8

#Megoldás Iteratívan
def Palindrom_e_vagy_sem_itaratívan(a):
    for i in range(0, int(len(a)/2)):
        if a[i] != a[len(a)-i-1]:
            return "Hamis"
    return "True"
def Vizsgálás_Ha_Palindróm(s):
    if Palindrom_e_vagy_sem_itaratívan(s)=="Hamis":
        print("Nem Palindróm")
    else:
        print("Palindróm")

def main():
    print(Palindrom_e_vagy_sem_itaratívan("görög"))
    print(Palindrom_e_vagy_sem_itaratívan("Nem vagyok Palindróm"))

if __name__ == "__main__":
    main()

