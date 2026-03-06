# zad1
import numpy as np

def generuj_tablice(n, m):
    tablica = []

    for k in range(n):
        licznik = 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)

        element = licznik / mianownik

        tablica.append(np.float32(element))

    return tablica

n = 64
m = 16

tablica = generuj_tablice(n, m)

print("Elementy ciągu:")
for i, wartosc in enumerate(tablica):
    print("a_", i, "=", wartosc)

#zad2
import numpy as np

def generuj_tablice(n, m):
    tablica = []

    for k in range(n):
        licznik = 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)

        a = licznik / mianownik
        tablica.append(np.float32(a))

    return tablica

def sumuj_tablice(tablica):
    suma = np.float32(0.0)

    for element in tablica:
        suma = np.float32(suma + element)

    return suma

n = 64
m = 16

tablica = generuj_tablice(n, m)

suma = sumuj_tablice(tablica)

print("Elementy tablicy:")
for i, wartosc in enumerate(tablica):
    print("a_", i, "=", wartosc)

print("\nSuma elementów:", suma)

#zad3
import numpy as np

def generuj_tablice(n, m):
    tablica = []

    for k in range(n):
        licznik = 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)

        a = licznik / mianownik
        tablica.append(np.float32(a))

    return tablica

def sumuj_tablice(tablica):
    suma = np.float32(0.0)
    poprawka = np.float32(0.0)

    for element in tablica:
        t = np.float32(suma + element)
        poprawka = np.float32(poprawka + (element - (t-suma)))
        suma = t

    return np.float32(suma + poprawka)

n = 64
m = 16

tablica = generuj_tablice(n, m)

suma = sumuj_tablice(tablica)

print("Suma:", suma)

#zad4
import numpy as np

def generuj_tablice(n, m):
    tablica = []

    for k in range(n):
        licznik = 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)

        a = licznik / mianownik
        tablica.append(np.float32(a))

    return tablica

def sumuj_tablice(tablica):
    suma = np.float32(0.0)

    for element in tablica:
        suma = np.float32(suma + element)

    return suma

def sumuj_tablice_Møller(tablica):
    suma = np.float32(0.0)
    poprawka = np.float32(0.0)

    for element in tablica:
        t = np.float32(suma + element)
        poprawka = np.float32(poprawka + (element - (t-suma)))
        suma = t

    return np.float32(suma + poprawka)

def sumuj_tablice_Kahan(tablica):
    suma = np.float32(0.0)
    c = np.float32(0.0)

    for element in tablica:
        y = np.float32(element - c)
        t = np.float32(suma + y)
        c = np.float32((t-suma) - y)
        suma = t

    return np.float32(suma)

n = 64
m = 16

tablica = generuj_tablice(n, m)

suma = sumuj_tablice(tablica)
suma_m = sumuj_tablice_Møller(tablica)
suma_k = sumuj_tablice_Kahan(tablica)

print("Suma zwykła:", suma)
print("Suma Møller:", suma_m)
print("Suma Kahan:", suma_k)

print("Sprawdznie dokładności:", n/(m+1))

#zad5
def generuj_tablice(n, m):
    tablica = []

    for k in range(n):
        licznik = 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)

        a = licznik / mianownik
        tablica.append(float(a))

    return tablica

def sumuj_tablice(tablica):
    suma = float(0.0)

    for element in tablica:
        suma = float(suma + element)

    return suma

def sumuj_tablice_Møller(tablica):
    suma = float(0.0)
    poprawka = float(0.0)

    for element in tablica:
        t = float(suma + element)
        poprawka = float(poprawka + (element - (t-suma)))
        suma = t

    return float(suma + poprawka)

def sumuj_tablice_Kahan(tablica):
    suma = float(0.0)
    c = float(0.0)

    for element in tablica:
        y = float(element - c)
        t = float(suma + y)
        c = float((t-suma) - y)
        suma = t

    return float(suma)

n = 64
m = 16

tablica = generuj_tablice(n, m)

suma = sumuj_tablice(tablica)
suma_m = sumuj_tablice_Møller(tablica)
suma_k = sumuj_tablice_Kahan(tablica)

print("Suma zwykła:", suma)
print("Suma Møller:", suma_m)
print("Suma Kahan:", suma_k)

print("Sprawdznie dokładności:", n/(m+1))