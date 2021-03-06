from numpy.random import uniform
from math import pi, sqrt
import numpy as np
import time

def czy_wewnatrz_figury(x, y, z):
    if x*x + y*y < 0.25 and x*x + y*y + z*z < 1.:
        return 1.
    return 0.

def objetosc(liczba_krokow):
    wynik = 0.
    for i in range(liczba_krokow):
        x = uniform(-1., 1.)
        y = uniform(-1., 1.)
        z = uniform(-1., 1.)
        wynik = wynik + czy_wewnatrz_figury(x, y, z)
    return wynik * (8 / liczba_krokow)

def teoretyczna_objetosc(H, h, r, R):
    return (pi*r**2*H + 2*(pi*h**2*(3*R-h)/3))

def zapisz_wynik(wywolania, H, h, r, R):
    moj_wynik = np.zeros((len(wywolania), 4))
    j=0
    t_objetosc = teoretyczna_objetosc(H,h,r, R)
    for i in wywolania:
        czas_start = time.time()
        obliczona_objetosc = objetosc(i)
        roznica = abs(t_objetosc - obliczona_objetosc)
        czas_koniec = time.time()
        czas = (czas_koniec - czas_start)
        moj_wynik[j,0] = i
        moj_wynik[j,1] = obliczona_objetosc
        moj_wynik[j,2] = roznica
        moj_wynik[j,3] = czas
        j = j+1
    np.savetxt("results\ result.txt", moj_wynik, delimiter=' & ', fmt='%2.8e', newline=' \\\\\n')
    #zapis do pliku: 1 wiersz-l. powtórzeń 2-obliczona V, 3-obliczona roznica 4- czas trwania petli
    return moj_wynik

H = sqrt(3)
h = (2-sqrt(3))/2
r = 0.5
R=1

print(teoretyczna_objetosc(H,h,r,R))

#print(teoretyczna_objetosc(H,h,r,R))
tablica_wywolan = np.array([10**3,10**4,10**5, 10**6,10**7,10**8,10**9])
print(zapisz_wynik(tablica_wywolan, H, h, r, R))

