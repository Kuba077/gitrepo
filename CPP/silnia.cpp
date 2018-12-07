/*
 * silnia.cpp
 * 
 */
#include <iostream>
using namespace std;

int silnia_it(int a) {
    int wynik = 1;
    for (int  i = 1; i < a; i++) {
        wynik = a * (a - 1);
        }
    return wynik;
    }

// silnia_re(5)
// silnia_re(4) * 5
// silnia_re(3) * 4
// silnia_re(2) * 3
// silnia_re(1) * 2
// silnia_re(0) * 1
// 1
// 1 * 1
// 1 * 2
// 2 * 3
// 6 * 4





int silnia_re(int a) {
    if (a == 1)
        return 1;
    return a * silnia_re(a - 1);
    
    }
int main(int argc, char **argv)
{
	int a;
    cout << "Podaj liczbę: ";
    cin >> a;
    cout << "Silnia: " << silnia_it(a) << endl;
    cout << "Silnia: " << silnia_re(a) << endl;
	return 0;
}

