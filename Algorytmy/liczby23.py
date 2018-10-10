#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py
#  

def liczby2():
    """
    FUNKCJA DRUKUJE WSZYSTKIE LICZBY 2-CYFROWE,
    W KTÓRYCH CYFRY NIE POWTARZAJĄ SIĘ. FUN. ZWRACA ICH LICZBĘ.
    WYKLUCZONE LICZBY: 11, 22, 33 ITD.
    """
	ile = 0 # licznik
	for i in range(1,10):
		for j in range(0,10):
			if i != j:
				print("{}{} ".format(i, j), end= '')
				ile = ile +1
	return ile
            
def liczby3():
    ile = 0
    for i in range(1, 10):
        for j in range(10):
            for l in range(10):
                if i!=j and j!=l and i!=l:
                    print(i*100+j*10+l,end=" ")
                    ile += 1
    print()
return ile

def main(args):
	print("Liczb 2-cyfrowych: ", liczby2())
	print("Liczb 3 cyfrowych", liczby3())
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
