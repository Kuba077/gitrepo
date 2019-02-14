/*
 * znaki.cpp
 */
#include <iostream>
#include <string.h>

using namespace std;

void licz_znaki(char tb[], int roz) {
    //~for(int i=0; i < roz; i++) {
        //~cout << tb[i];
    //~}
    int i = 0;
    int biale, inter, reszta;
    biale = inter = reszta = 0;
    while (tb[i] != '\0') {
        //~if (tb[i] == ' ' || tb[i] == '\t') biale++;
        //~else if (tb[i] == ',' || tb[i] == '.') inter++;
        //~else reszta++;
        switch (tb[i]) {
            case ' ':
            case '\t':
                biale++;
            break;
            case ',':
            case '.':
                inter++;
            break;
            default:
                reszta++;
        }
        i++;  // inkrementacja indeksu
    }
    cout << "Białych: " << biale << endl;
    cout << "Interpu: " << inter << endl;
    cout << "Reszta: " << reszta << endl;
}

int zlicz(char tb[]){
    int i = 0;
    while (tb[i] != '\0') i++;
    return i;
}

void ascii(char tb[], int roz) {
    int kod = 0;
    for(int i = 0; i < roz; i++) {
        kod = (int)tb[i];
        if (kod > 96 && kod < 123)
            kod -= 32;
            //cout << (char)(kod-32) << " ";
        else if (kod > 64 && kod < 91)
            kod += 32;
            //cout << (char)(kod+32) << " ";
        //~else
            //~cout << tb[i] << " ";
        cout << (char)kod << " ";
    }
}

void odwroc(char tb[], int roz){
    for(int i = roz-1; i >= 0; i--)
        cout << tb[i] << " ";
}

int main(int argc, char **argv)
{
    const int rozmiar = 20;
    char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    // licz_znaki(znaki, cin.gcount());
    int ilosc = 0;
    //ilosc = cin.gcount();
    //ilosc = zlicz(znaki);
    ilosc = strlen(znaki);
    ascii(znaki, ilosc);
    return 0;
}
