/*
 * 
 */

#include <iostream>

using namespace std;


bool czy_lpierwsza(int n)
{
    if(n < 2)
        return false;
    for(int i=2; i*i <= n; i++)
        if(n%i == 0)
            return false;
    return true;
    
    }



int main(int argc, char **argv)
{
	int n;
    
    cout << "Podaj liczbę naturalną : ";
    
    cin >> n;
    
    if(czy_lpierwsza(n))
        cout << "Liczba "<< n << " to jest liczba pierwsza" << endl;
    else{
        cout << "Liczba " << n << " to nie jest liczba pierwsza" << endl;
    }
	return 0;
    
    
}

