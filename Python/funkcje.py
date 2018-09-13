#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py

# Zasięg zmiennych: lokalny, globalny

def dodaj(a, b):
   return a + b

def iloraz(a, b):
   return a /b

def iloczyn(a, b):
   return a * b





def main(args):
   # a = 0 # inicjacja zmiennej
    a = int(input('Podaj 1. liczbę: '))
    print(a)
    
    b = int(input('Podaj 2. liczbę: '))
    print(b)
    
    
    print("Suma: ",dodaj( a, b))
    print("Iloczyn: ", iloczyn(a, b))
    print("Iloraz: ", iloraz(a, b))
    print("Różnica: ", a - b)
    
    
    return 0
    
# duck typing

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
