#!/usr/bin/env python3
# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.

# További sztring műveletek


# E. verbing
# Ha az adott sztring hossza legalább 3, akkor
# a végéhez adjuk hozzá az 'ing' ragot.
# Ha 'ing'-re végződik, akkor ehelyett az 'ly'
# ragot tegyük hozzá.
# Ha a sztring hossza rövidebb 3 karakternél, akkor
# hagyjuk változatlanul.
# Adjuk vissza az eredménysztringet.
def verbing(s):
    if len(s)<3:
        return s
    else:
        if s[-3:] == "ing":
            s += "ly"
        else:
            s += "ing"
    return s

# F. not_bad
# Egy adott sztringben keressük meg a 'not' és
# 'bad' szavak előfordulási helyét. Ha a 'bad'
# a 'not' szót követi, akkor cseréljük ki az
# egész 'not'...'bad' részsztringet a 'good' szóra.
# Adjuk vissza az eredmény sztringet.
# Példa: 'This dinner is not that bad!' ->
#        This dinner is good!
def not_bad(s):
    the_string_number_locations_for_not = 0
    the_string_number_location_for_good = 0
    if "not" and "bad" in s:
        for i in range(len(s)-1):
            if s[i-1] + s[i] + s[i+1] == "not":
                the_string_number_locations_for_not = i - 1
        for j in range(len(s)-1):
            if s[j-1] + s[j] + s[j+1] == "bad":
                the_string_number_location_for_good = j + 1
        if the_string_number_locations_for_not < the_string_number_location_for_good:
            the_new_string = s.replace(s[the_string_number_locations_for_not:the_string_number_location_for_good+1],"good")
            return the_new_string
        else:
            return s
    else:
        return s


# G. front_back
# Egy sztringet osszunk két részre, s a két részt nevezzük
# a sztring elejének és végének. Ha a sztring hossza páros, akkor
# a két rész hossza azonos. Ha a hossz páratlan, akkor az eleje
# legyen egy karakterrel hosszabb mint a vége.
# Például 'abcde' esetén a két rész: 'abc' és 'de'.
# Két adott sztring (a és b) esetén adjunk vissza egy sztringet, mely
# a következőképpen épül fel:
# a-eleje + b-eleje + a-vége + b-vége
# Például ha a = 'abcd' és b = 'xy', akkor az eredmény 'abxcdy' legyen.
def front_back(a, b):
    a_first_half = ""
    b_first_half = ""
    a_second_half = ""
    b_second_half = ""
    final_string = ""
    if len(a)%2==0:
        for i in range(len(a)//2):
            a_first_half += a[i]
        for i in range(len(a)//2,len(a)):
            a_second_half += a[i]
    if len(b)%2==0:
        for i in range(len(b)//2):
            b_first_half += b[i]
        for i in range(len(b)//2,len(b)):
            b_second_half += b[i]
    if len(a)%2==1:
        for i in range(len(a)//2+1):
            a_first_half += a[i]
        for i in range(len(a)//2+1,len(a)):
            a_second_half += a[i]
    if len(b)%2==1:
        for i in range(len(b)//2+1):
            b_first_half += b[i]
        for i in range(len(b)//2+1,len(b)):
            b_second_half += b[i]
    final_string = a_first_half + b_first_half + a_second_half + b_second_half
    return final_string



# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

#############################################################################

if __name__ == '__main__':
    main()