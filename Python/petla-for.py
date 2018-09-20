#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-for.py
#  



def main(args):
    start = int(input('Podaj początek zakresu: '))
    stop = int(input('Podaj koniec zakresu: '))

    while start>= stop:
        stop = int(input("Błędny zakres! Podaj poprawny!"))
    
    
    if start >= stop:
        print("Błędny zakres!")
        exit()
    
    for liczba in range(start, stop + 1):
        if liczba % 2 == 0:
            print(liczba)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
