from numpy.random import uniform
from math import pi

def czy_wewnatrz_figury(x):
    if sum(x ** 2) < 1.:
        return 1.
    return 0.


def czy_miazsz(x):
    if sum(x ** 2) < 0.81:
        return 1.
    return 0.


def czesc1(liczba_krokow, wymiar):
    wynik = 0.
    for i in range(liczba_krokow):
        x = uniform(-1., 1., wymiar)
        wynik = wynik + czy_wewnatrz_figury(x)
    return wynik / liczba_krokow


def czesc2(liczba_krokow, wymiar):
    miazsz = 0.
    pomarancza = 0.
    for i in range(liczba_krokow):
        x = uniform(-1., 1., wymiar)
        if czy_wewnatrz_figury(x):
            pomarancza = pomarancza + 1
            miazsz = miazsz + czy_miazsz(x)
    return miazsz / pomarancza

# Obliczenia Część I
#promień hiperkuli r, krawędź hipersześcianu a

print('Część I')
r = 1
a = 2
#objętość kuli 3D
Vk3d = 4/3*pi*r**3
#objętość sześcianu 3D
Vsz3d = a**3

print('Iloraz teoretyczny w 3D')
print(Vk3d/Vsz3d)
print('Wartość wyznaczona przez algorytm')
print(czesc1(1000, 3))

#objętość kuli 9D
Vk9d = 32*pi**4/945 * r**9
#objętość sześcianu 9D
Vsz9d = a**9

print('Iloraz teoretyczny w 9D')
print(Vk9d/Vsz9d)
print('Wartość wyznaczona przez algorytm')
print(czesc1(1000, 9))

print("czesc 1")
#objętość kuli 15D
Vk15d = 256*pi**7/2027025 * r**15
#objętość sześcianu 15D
Vsz15d = a**15

print('Iloraz teoretyczny w 15D')
print(Vk15d/Vsz15d)
print('Wartość wyznaczona przez algorytm')
print(czesc1(10**6, 15))

#objętość kuli 21D
Vk21d = 2048*pi**10/13749310575*r**21

#objętość sześcianu 21D
Vsz21d = a**21

print('Iloraz teoretyczny w 21D')
print(Vk21d/Vsz21d)
print('Wartość wyznaczona przez algorytm')
print(czesc1(10**7, 21))


#Obliczenia część II
print('część II')

# Objetosc miaszu w 3D
Vm3d = 4/3*pi*(0.9*r)**3
print('Wartość teoretyczna w 3D')
print(Vm3d/Vk3d)
print('Wartość wyznaczona:')
print(czesc2(1000, 3))

# Objetosc miaszu w 9D
Vm9d = 32*pi**4/945*(0.9*r)**9
print('Wartość teoretyczna w 9D')
print(Vm9d/Vk9d)
print('Wartość wyznaczona:')
print(czesc2(10**6, 9))

# Objetosc miaszu w 15D
Vm15d = 256*pi**7/2027025*(0.9*r)**15
Vk15d = 256*pi**7/2027025*r**15
print('Wartość teoretyczna w 15D')
print(Vm15d/Vk15d)
print('Wartość wyznaczona:')
print(czesc2(10**7, 15))


# Objetosc miaszu w 21D
Vm21d = 2048*pi**10/13749310575*(0.9*r)**21
Vk21d = 2048*pi**10/13749310575*r**21

print('Wartość teoretyczna w 21D')
print(Vm21d/Vk21d)
print('Wartość wyznaczona:')
print(czesc2(10**8, 21)) #-> Error: float division by zero
