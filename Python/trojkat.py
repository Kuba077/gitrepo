#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#

def trojkat (a, b, c):
    
    if a + b > c and a + c > b and b + c > a:
        return True
    
    return False
def main(args):
    
    assert(trojkat(3,4,5) == True)
    assert(trojkat(3,4,1) == False)
    
    
    # ~a = int(input('Podaj 1. bok: '))
    
    # ~b = int(input('Podaj 2. bok: '))
    
    # ~c = int(input('Podaj 3. bok: '))
    
    # ~if trojkat (a, b, c):
        # ~print("Da się")
    # ~else:
        # ~print("Ni hu hu")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
