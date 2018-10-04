#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
# Program drukuje wypełniony prostokąt o bokach podanych przez użytkownika
# 
#  

def prostokat1(a, b, znak):
    a = int(input('Podaj liczbę 1: '))
    b = int(input('Podaj liczbę 2: '))
    znak = input('Wypełnienie: ')
    for i in range(a):
        for j in range(b):
            print ( znak, end='')
        print()
    
    return 0

def prostokat2(a, b, znak):
    a = int(input('Podaj liczbę 1: '))
    b = int(input('Podaj liczbę 2: '))
    znak = input('Wypełnienie: ')

    for i in range(a):
        for j in range(b):
            if j== 0 or j == b -1:
                print ( znak, end='')
            else:
                print(" ", end= '')
        print()

    return 0



def main(args):
    a = int(input('Podaj liczbę 1: '))
    b = int(input('Podaj liczbę 2: '))
    znak = input('Wypełnienie: ')
    
    for i in range(a):
        for j in range(b):
            print ( "#", end='')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
