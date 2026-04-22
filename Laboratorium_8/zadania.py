# zad 1

import time, math

def exp_maclaurin(x, n):
    suma = 1.0
    wyraz = 1.0

    for k in range(1, n+1):
        wyraz = wyraz * (x / k)
        suma += wyraz

    return suma

def porownaj_exp(x, n, liczba_powtorzen=100000):
    start = time.perf_counter()
    for _ in range(liczba_powtorzen):
        wynik_maclaurin = exp_maclaurin(x, n)
    czas_maclaurin = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(liczba_powtorzen):
        wynik_biblioteczny = math.exp(x)
    czas_biblioteczny = time.perf_counter() - start

    blad = abs(wynik_maclaurin - wynik_biblioteczny)

    print(f"x = {x}, n = {n}")
    print(f"Wynik Maclaurina:   {wynik_maclaurin}")
    print(f"Wynik biblioteczny: {wynik_biblioteczny}")
    print(f"Błąd bezwzględny:   {blad}")
    print(f"Czas Maclaurina:    {czas_maclaurin:.10f} s")
    print(f"Czas biblioteczny:  {czas_biblioteczny:.10f} s")
    print("-" * 50)

print("-------------------- ZADANIE 1 --------------------")

porownaj_exp(1.0, 10)
porownaj_exp(2.0, 15)
porownaj_exp(-1.0, 15)
porownaj_exp(5.0, 25)

# zad 2

import math, time

def sin_maclaurin(x, n):
    x = x % (2 * math.pi)

    suma = x
    wyraz = x
    znak = -1.0

    for k in range(2, n+1):
        wyraz = wyraz * x * x / ((2 * k - 2) * (2 * k - 1))
        suma += znak * wyraz
        znak = -znak

    return suma

def porownaj_sin(x, n, liczba_powtorzen=100000):
    start = time.perf_counter()
    for _ in range(liczba_powtorzen):
        wynik_maclaurin = sin_maclaurin(x, n)
    czas_maclaurin = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(liczba_powtorzen):
        wynik_biblioteczny = math.sin(x)
    czas_biblioteczny = time.perf_counter() - start

    blad = abs(wynik_maclaurin - wynik_biblioteczny)

    print(f"x = {x}, n = {n}")
    print(f"Wynik Maclaurina:   {wynik_maclaurin}")
    print(f"Wynik biblioteczny: {wynik_biblioteczny}")
    print(f"Błąd bezwzględny:   {blad}")
    print(f"Czas Maclaurina:    {czas_maclaurin:.10f} s")
    print(f"Czas biblioteczny:  {czas_biblioteczny:.10f} s")
    print("-" * 50)


print("-------------------- ZADANIE 2 --------------------")

porownaj_sin(0.5, 10)
porownaj_sin(1.0, 10)
porownaj_sin(math.pi / 2, 12)
porownaj_sin(10.0, 15)

# zad 3

def wspolczynniki_newtona(x, y):
    n = len(x)

    if len(y) != n:
        raise ValueError("Listy x i y muszą mieć taką samą długość.")

    a = y[:]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            if x[i] == x[i - j]:
                raise ValueError("Wartości x muszą być różne.")
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])

    return a


print("-------------------- ZADANIE 3 --------------------")

x = [0.0, 1.0, 2.0, 3.0]
y = [1.0, 2.0, 0.0, 5.0]

a = wspolczynniki_newtona(x, y)

print("Węzły x:", x)
print("Wartości y:", y)
print("Współczynniki wielomianu Newtona:")
for i in range(len(a)):
    print(f"a{i} = {a[i]}")

# zad 4

def wspolczynniki_newtona(x, y):
    n = len(x)

    if len(y) != n:
        raise ValueError("Listy x i y muszą mieć taką samą długość.")

    a = y[:]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            if x[i] == x[i - j]:
                raise ValueError("Wartości x muszą być różne.")
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])

    return a


def wartosc_wielomianu_newtona(x_wezly, a, X):
    n = len(a)

    if len(x_wezly) != n:
        raise ValueError("Liczba węzłów x i liczba współczynników musi być taka sama.")

    result = a[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (X - x_wezly[i]) + a[i]

    return result

print("-------------------- ZADANIE 4 --------------------")

x = [0.0, 1.0, 2.0, 3.0]
y = [1.0, 2.0, 0.0, 5.0]

a = wspolczynniki_newtona(x, y)

X = 1.5
wartosc = wartosc_wielomianu_newtona(x, a, X)

print("Węzły x:", x)
print("Wartości y:", y)
print("Współczynniki Newtona:", a)
print("Punkt X:", X)
print("Wartość wielomianu w punkcie X:", wartosc)