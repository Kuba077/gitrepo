#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kompresja.py
#  


def main(args):
    
    
    # ~Vk = input('Podaj rozmiar danych skompresowanych (Bajty): ')
    # ~Vnk = input ('Rozmiar danych nieskompresowanych (Bajty): ')
    
    Vk = 74171
    Vnk = 117760
    Rc = int(Vk) / int (Vnk) * 100
    R2c = (1 - int(Vk) / int (Vnk)) * 100
    
    Vk2 = 70074
    Vnk2 = 117760
    Rc2 = int(Vk2) / int (Vnk2) * 100
    R2c2 = (1 - int(Vk2) / int (Vnk2)) * 100
    
    
    print ('O ile zmniejszyły się dane:  ', Rc)
    print ('Ile miejsca zaoszczędzon ', R2c)
    
    print ('O ile zmniejszyły się dane:  ', Rc2)
    print ('Ile miejsca zaoszczędzon ', R2c2)
    
    return 0
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
