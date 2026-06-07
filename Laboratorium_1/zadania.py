# -------------------- ZADANIE 1 ----------------------

print("Zadanie 1")

import numpy as np

def suma_pojedyncza_precyzja(a, b):
    a32 = np.float32(a)
    b32 = np.float32(b)
    return np.float32(a32 + b32)

poj = suma_pojedyncza_precyzja(0.1, 0.2)

print(poj)

def suma_podwojna_precyzja(a: float, b: float) -> float:
    return a + b

pod = suma_podwojna_precyzja(0.1, 0.2)

print(pod)

print("Czy równe?: ", poj == pod)

# -------------------- ZADANIE 2 ----------------------

print("Zadanie 2")

a = 10000000000000000
b = 0.000000000000001

wynik = (a + b) - a

print(wynik)

# -------------------- ZADANIE 3 ----------------------

print("Zadanie 3")

import numpy as np

liczba = 0.1

# float - pojedyncza precyzja
liczba_f = np.float32(liczba)

# double - podwójna precyzja
liczba_d = float(liczba)

print("float: ", format(liczba_f, ".20f"))
print("double: ", format(liczba_d, ".20f"))

# -------------------- ZADANIE 4 ----------------------

print("Zadanie 4")

import math

wynik = 0.3 * 3 + 0.1

print("Wynik zwykły: ", wynik)
print("Wynik zaokrąglony w dół: ", math.floor(wynik))
print("Wynik zaokrąglony w górę: ", math.ceil(wynik))

# -------------------- ZADANIE 5 ----------------------

print("Zadanie 5")

wynik1 = 1.0000001 - 1.0000000
wynik2 = 1.0000002 - 1.0000001

print("wynik1: ", wynik1)
print("wynik2: ", wynik2)

# -------------------- ZADANIE 6 ----------------------

print("Zadanie 6")

# wynik1 = 1.0 / 0.0
wynik1 = np.divide(1.0, 0.0)
# wynik2 = 0.0 / 0.0
wynik2 = np.divide(0.0, 0.0)

print("wynik dzielenia pierwszego: ", wynik1)
print("wynik dzielenia drugiego: ", wynik2)

# -------------------- ZADANIE 7 ----------------------

print("Zadanie 7")

import numpy as np

def epsilon_float32():
    eps = np.float32(1.0)
    while np.float32(1.0) + eps / np.float32(2.0) > np.float32(1.0):
        eps = eps / np.float32(2.0)
    return eps

def epsilon_float64():
    eps = 1.0
    while 1.0 + eps / 2.0 > 1.0:
        eps = eps / 2.0
    return eps

eps32 = epsilon_float32()
eps64 = epsilon_float64()

print("Epsilon float32:", eps32)
print("Epsilon float64:", eps64)

# -------------------- ZADANIE 8 ----------------------

print("Zadanie 8")

# liczba iteracji
n = 1_000_000
wartosc = 0.0001

# Sumowanie w pętli
suma_petla = 0.0
for _ in range(n):
    suma_petla += wartosc

# Mnożenie
suma_mnozenie = n * wartosc

# Różnica
roznica = suma_petla - suma_mnozenie

print("Wynik sumowania w pętli:", suma_petla)
print("Wynik mnożenia:", suma_mnozenie)
print("Różnica:", roznica)

# -------------------- ZADANIE 9 ----------------------

print("Zadanie 9")

n = 1_000_000

# 1️⃣ Sumowanie w kolejności rosnącej (od 1 do 1_000_000)
suma_rosnaco = 0.0
for i in range(1, n + 1):
    suma_rosnaco += 1.0 / i

# 2️⃣ Sumowanie w kolejności malejącej (od 1_000_000 do 1)
suma_malejaco = 0.0
for i in range(n, 0, -1):
    suma_malejaco += 1.0 / i

# Różnica
roznica = suma_rosnaco - suma_malejaco

print("Suma rosnąco:", suma_rosnaco)
print("Suma malejąco:", suma_malejaco)
print("Różnica:", roznica)

# -------------------- ZADANIE 10 ----------------------

print("Zadanie 10")

import math

def f(x):
    return math.sqrt(x**2 + 1) - 1

def g(x):
    return x**2 / (math.sqrt(x**2 + 1) + 1)

print(f"{'x':>12} {'f(x)':>20} {'g(x)':>20} {'różnica':>20}")

for k in range(1, 11):
    x = 8**(-k)
    fx = f(x)
    gx = g(x)
    print(f"{x:12.5e} {fx:20.15e} {gx:20.15e} {(fx-gx):20.15e}")