**Zadanie 1.** Napisz funkcję, która wygeneruje tablicę liczb zmiennoprzecinkowych pojedynczej precyzji reprezentujących elementy ciągu postaci:

$$
S_n = \sum_{k=0}^{n-1} a_k = \sum_{k=0}^{n-1} \frac{1}{(k \bmod m + 1)(k \bmod m + 2)},
$$

gdzie $n$ i $m$ są potęgami liczby $2$ oraz $n > m$.

```python
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
```

---

**Zadanie 2.** Napisz funkcję sumującą elementy tablicy z zadania 1. Sprawdź dokładność otrzymanej sumy.

```python
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
```

---

**Zadanie 3.** Napisz funkcję sumującą elementy tablicy z zadania 1 z wykorzystaniem algorytmu Gilla–Møllera. Sprawdź dokładność otrzymanej sumy.

```python
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
        poprawka = np.float32(poprawka + (element - (t - suma)))
        suma = t

    return np.float32(suma + poprawka)


n = 64
m = 16

tablica = generuj_tablice(n, m)

suma = sumuj_tablice(tablica)

print("Suma:", suma)
```

---

**Zadanie 4.** Napisz funkcję sumującą elementy tablicy z zadania 1 z wykorzystaniem algorytmu Kahana. Sprawdź dokładność otrzymanej sumy. Porównaj wyniki wszystkich omówionych metod sumowania.

```python
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
        poprawka = np.float32(poprawka + (element - (t - suma)))
        suma = t

    return np.float32(suma + poprawka)


def sumuj_tablice_Kahan(tablica):
    suma = np.float32(0.0)
    c = np.float32(0.0)

    for element in tablica:
        y = np.float32(element - c)
        t = np.float32(suma + y)
        c = np.float32((t - suma) - y)
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

print("Sprawdzenie dokładności:", n / (m + 1))
```

---

**Zadanie 5.** Przeprowadź analogiczne działania dla danych w podwójnej precyzji.

```python
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
        poprawka = float(poprawka + (element - (t - suma)))
        suma = t

    return float(suma + poprawka)


def sumuj_tablice_Kahan(tablica):
    suma = float(0.0)
    c = float(0.0)

    for element in tablica:
        y = float(element - c)
        t = float(suma + y)
        c = float((t - suma) - y)
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

print("Sprawdzenie dokładności:", n / (m + 1))
```