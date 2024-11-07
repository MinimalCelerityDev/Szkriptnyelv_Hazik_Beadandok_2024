#!/usr/bin/env python3
# coding: utf-8

def lista_elemeinek_szorzata(s: list):
    sum = 1
    for i in range(len(s)):
        sum *= s[i]
    return sum


print(lista_elemeinek_szorzata([1,2,3,4,5,6]))
print(lista_elemeinek_szorzata([2,3]))
print(lista_elemeinek_szorzata([0,1,1,1,1,1]))
print(lista_elemeinek_szorzata([3,4]))