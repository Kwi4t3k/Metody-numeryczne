# import sys
# print("URUCHAMIAM PYTHONA Z:", sys.executable)

#zad 1
print("-------------------- ZADANIE 1 --------------------")

# punkty = [(1, 1), (3, 12), (5, 25), (7, 38)] # test z wykładu
punkty = [(1.1, 2.1), (1.4, 2.3), (1.8, 2.9), (2.5, 3.2),(2.8, 3.6), (3.0, 4.2)]

n = len(punkty)

A = 0.0
B = 0.0
C = 0.0
D = 0.0

for x, y in punkty:
    B += x
    C += y
    D += x * x
    A += x * y

a = (n * A - B * C) / (n * D - B * B)
b = (C * D - A * B) / (n * D - B * B)

print("Współczynniki prostej aproksymacyjnej:")
print("a =", a)
print("b =", b)

print("\nProsta aproksymacyjna:")
print(f"y = {a} * x + {b}")

h = 0.0 # suma kwadratów błędów
for x, y in punkty:
    h += (a * x + b - y) ** 2

print("\nSuma kwadratów błędów:")
print(h)

#zad 2
print("-------------------- ZADANIE 2 --------------------")

punkty = [(0.0, 2.0), (0.5, 2.48), (1.0, 2.84), (1.5, 3.0), (2.0, 2.91)]

def rozwiaz_uklad_gaussa(macierz, wyrazy_wolne):
    n = len(wyrazy_wolne)

    for i in range(n):
        if macierz[i][i] == 0:
            raise ValueError("Na przekątnej pojawiło się zero - nie można wykonać eliminacji Gaussa.")

        for j in range(i + 1, n):
            wspolczynnik = macierz[j][i] / macierz[i][i]

            for k in range(i, n):
                macierz[j][k] = macierz[j][k] - wspolczynnik * macierz[i][k]

            wyrazy_wolne[j] = wyrazy_wolne[j] - wspolczynnik * wyrazy_wolne[i]

    rozwiazanie = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += macierz[i][j] * rozwiazanie[j]

        rozwiazanie[i] = (wyrazy_wolne[i] - suma) / macierz[i][i]

    return rozwiazanie

n = len(punkty)

suma_x = 0.0
suma_x2 = 0.0
suma_x3 = 0.0
suma_x4 = 0.0
suma_y = 0.0
suma_xy = 0.0
suma_x2y = 0.0

for x, y in punkty:
    suma_x += x
    suma_x2 += x ** 2
    suma_x3 += x ** 3
    suma_x4 += x ** 4
    suma_y += y
    suma_xy += x * y
    suma_x2y += x ** 2 * y

macierz_ukladu = [
    [suma_x4, suma_x3, suma_x2],
    [suma_x3, suma_x2, suma_x],
    [suma_x2, suma_x, n]
]

wyrazy_wolne = [suma_x2y, suma_xy, suma_y]

macierz_kopia = []
for wiersz in macierz_ukladu:
    macierz_kopia.append(wiersz.copy())

wyrazy_wolne_kopia = wyrazy_wolne.copy()

rozwiazanie = rozwiaz_uklad_gaussa(macierz_kopia, wyrazy_wolne_kopia)

a = rozwiazanie[0]
b = rozwiazanie[1]
c = rozwiazanie[2]

print("Współczynniki wielomianu aproksymacyjnego:")
print("a =", a)
print("b =", b)
print("c =", c)

print("\nWielomian aproksymacyjny:")
print(f"y = {a} * x^2 + {b} * x + {c}")

h = 0.0
for x, y in punkty:
    h += (a * x**2 + b * x + c - y) ** 2

print("\nSuma kwadratów błędów:")
print(h)

#zad 3
print("-------------------- ZADANIE 3 --------------------")

def rozwiaz_uklad_gaussa(A, b):
    n = len(b)

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("Na przekątnej pojawiło się zero - nie można wykonać eliminacji Gaussa.")

        for j in range(i + 1, n):
            wspolczynnik = A[j][i] / A[i][i]

            for k in range(i, n):
                A[j][k] = A[j][k] - wspolczynnik * A[i][k]

            b[j] = b[j] - wspolczynnik * b[i]

    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += A[i][j] * x[j]

        x[i] = (b[i] - suma) / A[i][i]

    return x

def aproksymacja_najmniejszych_kwadratow(punkty, stopien):
    n = stopien + 1 # liczba współczynników

    A = [] # macierz układu
    B = [] # wyrazy wolne

    for i in range(n):
        wiersz = []

        for j in range(n):
            suma = 0.0

            for x, y in punkty:
                suma += x ** (i + j)

            wiersz.append(suma)

        A.append(wiersz)

        suma = 0.0

        for x, y in punkty:
            suma += y * (x ** i)

        B.append(suma)

    A_kopia = []
    for wiersz in A:
        A_kopia.append(wiersz.copy())

    B_kopia = B.copy()

    wspolczynniki = rozwiaz_uklad_gaussa(A_kopia, B_kopia)

    h = 0.0 # błąd

    for x, y in punkty:
        y_aprox = 0.0

        for i in range(len(wspolczynniki)):
            y_aprox += wspolczynniki[i] * (x ** i)

        h += (y_aprox - y) ** 2

    return wspolczynniki, h

punkty = [(0.0, 2.0), (0.5, 2.48), (1.0, 2.84), (1.5, 3.0), (2.0, 2.91)]
stopien = 2

wspolczynniki, blad = aproksymacja_najmniejszych_kwadratow(punkty, stopien)

print("Współczynniki wielomianu:")
for i in range(len(wspolczynniki)):
    print(f"a{i} = {wspolczynniki[i]}")

print("\nSuma kwadratów błędów:")
print(blad)

#zad 4
import matplotlib.pyplot as plt

print("-------------------- ZADANIE 4 --------------------")

# ===== Zadanie 1: aproksymacja liniowa =====
punkty1 = [(1.1, 2.1), (1.4, 2.3), (1.8, 2.9), (2.5, 3.2), (2.8, 3.6), (3.0, 4.2)]

n1 = len(punkty1)
Sx = 0.0
Sy = 0.0
Sxx = 0.0
Sxy = 0.0

for x, y in punkty1:
    Sx += x
    Sy += y
    Sxx += x * x
    Sxy += x * y

a1 = (n1 * Sxy - Sx * Sy) / (n1 * Sxx - Sx * Sx)
b1 = (Sy - a1 * Sx) / n1

x1 = [p[0] for p in punkty1]
y1 = [p[1] for p in punkty1]

x1_wykres = []
y1_wykres = []

xmin1 = min(x1)
xmax1 = max(x1)

for i in range(200):
    X = xmin1 + (xmax1 - xmin1) * i / 199
    Y = a1 * X + b1
    x1_wykres.append(X)
    y1_wykres.append(Y)

plt.figure(figsize=(8, 5))
plt.scatter(x1, y1, label="Punkty wejściowe")
plt.plot(x1_wykres, y1_wykres, label="Aproksymacja liniowa")
plt.title("Zadanie 1 - aproksymacja liniowa")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


# ===== Zadanie 2: aproksymacja wielomianem 2 stopnia =====
punkty2 = [(0.0, 2.0), (0.5, 2.48), (1.0, 2.84), (1.5, 3.0), (2.0, 2.91)]

def rozwiaz_uklad_gaussa(A, b):
    n = len(b)

    for i in range(n):
        max_wiersz = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_wiersz][i]):
                max_wiersz = j

        A[i], A[max_wiersz] = A[max_wiersz], A[i]
        b[i], b[max_wiersz] = b[max_wiersz], b[i]

        for j in range(i + 1, n):
            wsp = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= wsp * A[i][k]
            b[j] -= wsp * b[i]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += A[i][j] * x[j]
        x[i] = (b[i] - suma) / A[i][i]

    return x

Sx = 0.0
Sx2 = 0.0
Sx3 = 0.0
Sx4 = 0.0
Sy = 0.0
Sxy = 0.0
Sx2y = 0.0

for x, y in punkty2:
    Sx += x
    Sx2 += x**2
    Sx3 += x**3
    Sx4 += x**4
    Sy += y
    Sxy += x * y
    Sx2y += x**2 * y

n2 = len(punkty2)

A = [
    [Sx4, Sx3, Sx2],
    [Sx3, Sx2, Sx],
    [Sx2, Sx, n2]
]

B = [Sx2y, Sxy, Sy]

a2, b2, c2 = rozwiaz_uklad_gaussa(A, B)

x2 = [p[0] for p in punkty2]
y2 = [p[1] for p in punkty2]

x2_wykres = []
y2_wykres = []

xmin2 = min(x2)
xmax2 = max(x2)

for i in range(200):
    X = xmin2 + (xmax2 - xmin2) * i / 199
    Y = a2 * X**2 + b2 * X + c2
    x2_wykres.append(X)
    y2_wykres.append(Y)

plt.figure(figsize=(8, 5))
plt.scatter(x2, y2, label="Punkty wejściowe")
plt.plot(x2_wykres, y2_wykres, label="Aproksymacja wielomianem 2 stopnia")
plt.title("Zadanie 2 - aproksymacja wielomianem 2 stopnia")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()