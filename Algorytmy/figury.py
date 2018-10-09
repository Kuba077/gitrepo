#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
# Program drukuje wypełniony prostokąt o bokach długości podanej przez użytkownika za pomocą podanego znaku  


def prostokat1(a, b, znak):
    for i in range(a):
        for j in range(b):
			print(znak, end='')
		print()

    
def prostokat2(a, b, znak):
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b - 1 or i == 0 or i == a - 1:
                print(znak, end='')
            else:
                print(" ", end='')
        print()


def choinka1(h, znak):
    for i in range(h):
        for j in range(i + 1):
            print(znak, end='')
        print()

def choinka2(h, znak):
    for i in range(h):
        for j in range(h - i):
            print(znak, end='')
        print()

def trojkat(h, znak)
    n = (h-1)*2
    for i in range(h-1, -1, -1):
        for j in range(n + 1):
            if j < i or j > n - i:
                print(" ", end='')
            else:
                print(znak, end='')
	print()
        
def main(args):
    a = int(input('Wysokość prostokąta: '))
    b = int(input('Długość prostokąta: '))
    znak = input('Wypełnienie: ')
    h = int(input('Wysokość choinki: ')) 
    
    prostokat1(a, b, znak)
    print()
    prostokat2(a, b, znak)
    print()
    choinka1(h, znak)
    print()
    choinka2(h, znak)
    print()
    trokat(h, znak)
    print()
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
