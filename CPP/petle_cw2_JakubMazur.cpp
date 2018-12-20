/*
 * petle_cw2_JakubMazur.cpp
 */


#include <iostream>
using namespace std;

void cw2(){
    int a, b, c;
    
    cout << "Podaj liczbę I: " << endl;
    cin >> a;
    
    cout << "Podaj liczbę II: " << endl;
    cin >> b;
    
    cout << "Podaj liczbę III: " << endl;
    cin >> c;
    while (a+b!=c){
        a = b;
        b = c;
        cin >> c;
    }
    cout << "Liczba " << c << " jest sumą liczby I i liczby II";    
}

int main(int argc, char **argv)
{
    cw2();
    return 0;
}

