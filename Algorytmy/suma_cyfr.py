#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfr.py
#  
#  Copyright 2018  <>
#  

def sumuj_cyfry1(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba / 10)
    return suma

def sumuj_cyfry2(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba / 10)
    return suma



def main(args):
    
    liczba = input("Podaj liczbę 2-cyfrową: ")
    liczba = int(liczba)
    
    while liczba < 10:
        liczba = input("Podaj liczbę 2-cyfrową: ")
        liczba = int(liczba)
    
    
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba / 10)
    
    print("Suma:", suma)
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
