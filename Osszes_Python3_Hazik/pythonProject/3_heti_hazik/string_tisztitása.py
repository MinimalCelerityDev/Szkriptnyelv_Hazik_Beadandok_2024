#!/usr/bin/env python3
# coding: utf-8

def string_clean(a):
    b = ""
    for i in range(len(a)):
        if a[i] == " ":
            b += ""
        else:
            b += a[i]
    return b

def main():
    print(string_clean("Egy     -Ketto  -Harom     -Negy   -Finish"))
    print(string_clean("192.20.246.138:\n 6666"))
    print(string_clean("206.130.99.82:\n8080"))

if __name__=="__main__":
    main()

    #Saját meglátásomból, azt kell csinálja a függvény,
    #hogy, a whitespaceket ki kell törölni.
