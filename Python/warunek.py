#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunek.py
#  



def main(args):
    a = int(input('Podaj 1. liczbę: '))
    print (a)
    b = int(input('Podaj 2. liczbę: '))
    print (b)
    c = int(input('Podaj 3. liczbę: '))
    print (c)
    
    if b <= a >= c:
        print(a,"jest największe")
    elif a <= b >= c:
        print(b,"jest najwieksze")
    else:
        print(c,"jest najwieksze")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
