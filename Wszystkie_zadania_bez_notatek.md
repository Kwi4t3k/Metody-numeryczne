# Lab 1

## Zadanie 1
Sprawdź, czy suma dwóch liczb zmiennoprzecinkowych (zarówno w pojedynczej jak i podwójnej precyzji) jest zawsze równa oczekiwanej matematycznie wartości. Wyjaśnij, dlaczego odpowiedź może być błędna przy bezpośrednim porównaniu liczb zmiennoprzecinkowych.

```python
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
```

```
0.3
0.30000000000000004
Czy równe?:  False
```

## Zadanie 2
Sprawdź, co się stanie, gdy dodasz bardzo dużą liczbę do bardzo małej, a następnie odejmiesz dużą liczbę od wyniku.

```python
a = 10000000000000000
b = 0.000000000000001

wynik = (a + b) - a

print(wynik)
```

```
0.0
```

## Zadanie 3
Wyświetl liczbę zmiennoprzecinkową jako float i double z precyzją do 20 miejsc po przecinku.

```python
import numpy as np

liczba = 0.1

# float - pojedyncza precyzja
liczba_f = np.float32(liczba)

# double - podwójna precyzja
liczba_d = float(liczba)

print("float: ", format(liczba_f, ".20f"))
print("double: ", format(liczba_d, ".20f"))
```

```
float:  0.10000000149011611938
double:  0.10000000000000000555
```

## Zadanie 4
Oblicz 0,3 · 3 + 0,1 i porównaj wynik z jego wartościami zaokrąglonymi do dołu i do góry (floor i ceil).

```python
import math

wynik = 0.3 * 3 + 0.1

print("Wynik zwykły: ", wynik)
print("Wynik zaokrąglony w dół: ", math.floor(wynik))
print("Wynik zaokrąglony w górę: ", math.ceil(wynik))
```

```
Wynik zwykły:  0.9999999999999999
Wynik zaokrąglony w dół:  0
Wynik zaokrąglony w górę:  1
```

## Zadanie 5
Oblicz różnicę między 1,0000001 i 1,0000000 oraz między 1,0000002 i 1,0000001. Wyjaśnij, dlaczego wyniki mogą się różnić od teoretycznej różnicy.

```python
wynik1 = 1.0000001 - 1.0000000
wynik2 = 1.0000002 - 1.0000001

print("wynik1: ", wynik1)
print("wynik2: ", wynik2)
```

```
wynik1:  1.0000000005838672e-07
wynik2:  9.999999983634211e-08
```

## Zadanie 6
Podziel liczbę 1,0 przez 0,0 i liczbę 0,0 przez 0,0. Sprawdź, co zwrócą te operacje.

```python
# wynik1 = 1.0 / 0.0
wynik1 = np.divide(1.0, 0.0)
# wynik2 = 0.0 / 0.0
wynik2 = np.divide(0.0, 0.0)

print("wynik dzielenia pierwszego: ", wynik1)
print("wynik dzielenia drugiego: ", wynik2)
```
**Wynik z NumPy:**
```
zadania.py:80: RuntimeWarning: divide by zero encountered in divide
  wynik1 = np.divide(1.0, 0.0)
zadania.py:82: RuntimeWarning: invalid value encountered in divide
  wynik2 = np.divide(0.0, 0.0)
wynik dzielenia pierwszego:  inf
wynik dzielenia drugiego:  nan
```

**Wynik z czystego pythona:**
```
Traceback (most recent call last):
  File "zadania.py", line 79, in <module>
    wynik1 = 1.0 / 0.0
             ~~~~^~~~~
ZeroDivisionError: float division by zero

-----------------------------------------

Traceback (most recent call last):
  File "zadania.py", line 80, in <module>
    wynik2 = 0.0 / 0.0
             ~~~~^~~~~
ZeroDivisionError: float division by zero
```

## Zadanie 7
Oblicz maszynowy epsilon dla typów float i double i porównaj wyniki. Wyjaśnij, czym jest maszynowy epsilon i jak wpływa na dokładność obliczeń komputerowych.

```python
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

u32 = eps32 / np.float32(2.0)
u64 = eps64 / 2.0

print("Epsilon float32:", eps32)
print("Unit roundoff float32:", u32)

print("Epsilon float64 / double:", eps64)
print("Unit roundoff float64:", u64)

print("Porównanie:")
print("float32 ma dokładność około 7 cyfr dziesiętnych")
print("float64 / double ma dokładność około 16 cyfr dziesiętnych")
```

> W programie obliczono wartość epsilon jako najmniejszą liczbę dodatnią, dla której `1 + epsilon > 1`. W literaturze czasem przez maszynowy epsilon rozumie się tę wartość, a czasem połowę tej wartości, czyli tzw. unit roundoff $u$, zgodny ze wzorem ze slajdu. Dlatego dla zaokrąglania do najbliższej liczby maszynowej przyjmuje się $u \approx \varepsilon/2$.

```
Epsilon float32: 1.1920929e-07
Unit roundoff float32: 5.9604645e-08
Epsilon float64 / double: 2.220446049250313e-16
Unit roundoff float64: 1.1102230246251565e-16
Porównanie:
float32 ma dokładność około 7 cyfr dziesiętnych
float64 / double ma dokładność około 16 cyfr dziesiętnych
```

## Zadanie 8
Sumuj liczbę 0,0001 w pętli 1.000.000 razy i porównaj wynik z wynikiem uzyskanym przez mnożenie 1.000.000 przez 0,0001. Wyjaśnij, dlaczego mogą wystąpić różnice.

```python
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
```

```
Wynik sumowania w pętli: 100.00000000219612
Wynik mnożenia: 100.0
Różnica: 2.1961170659778873e-09
```

## Zadanie 9
Oblicz sumę odwrotności liczb od 1 do 1.000.000 w kolejności rosnącej i malejącej. Porównaj wyniki.

```python
n = 1_000_000

# Sumowanie w kolejności rosnącej (od 1 do 1_000_000)
suma_rosnaco = 0.0
for i in range(1, n + 1):
    suma_rosnaco += 1.0 / i

# Sumowanie w kolejności malejącej (od 1_000_000 do 1)
suma_malejaco = 0.0
for i in range(n, 0, -1):
    suma_malejaco += 1.0 / i

# Różnica
roznica = suma_rosnaco - suma_malejaco

print("Suma rosnąco:", suma_rosnaco)
print("Suma malejąco:", suma_malejaco)
print("Różnica:", roznica)
```

```
Suma rosnąco: 14.392726722864989
Suma malejąco: 14.392726722865772
Różnica: -7.833733661755105e-13
```

## Zadanie 10
Niech

$$
f(x) = \sqrt{x^2 + 1} - 1
$$

oraz

$$
g(x) = \frac{x^2}{\sqrt{x^2 + 1} + 1}.
$$

Łatwo zauważyć, że $g = f$. Oblicz i porównaj wartości funkcji $g$ i $f$ dla:

$$
x = 8^{-1},\; 8^{-2},\; 8^{-3},\; \dots
$$
```python
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
```

```
           x                 f(x)                 g(x)              różnica     
 1.25000e-01 7.782218537318641e-03 7.782218537318706e-03 -6.505213034913027e-17 
 1.56250e-02 1.220628628286757e-04 1.220628628287590e-04 -8.328027937404281e-17 
 1.95312e-03 1.907346813823096e-06 1.907346813826566e-06 -3.469446951953614e-18 
 2.44141e-04 2.980232194360610e-08 2.980232194360612e-08 -1.323488980084844e-23 
 3.05176e-05 4.656612873077393e-10 4.656612871993190e-10 1.084202172485504e-19  
 3.81470e-06 7.275957614183426e-12 7.275957614156956e-12 2.646977960169689e-23  
 4.76837e-07 1.136868377216160e-13 1.136868377216096e-13 6.462348535570529e-27  
 5.96046e-08 1.776356839400250e-15 1.776356839400249e-15 1.577721810442024e-30  
 7.45058e-09 0.000000000000000e+00 2.775557561562891e-17 -2.775557561562891e-17 
 9.31323e-10 0.000000000000000e+00 4.336808689942018e-19 -4.336808689942018e-19 
```

# Lab 2
## Zadanie 1
Napisz funkcję, która wygeneruje tablicę liczb zmiennoprzecinkowych pojedynczej precyzji reprezentujących elementy ciągu postaci:

$$
S_n = \sum_{k=0}^{n-1} a_k = \sum_{k=0}^{n-1} \frac{1}{(k \bmod m + 1)(k \bmod m + 2)},
$$

gdzie $n$ i $m$ są potęgami liczby $2$ oraz $n > m$.

**Uniwersalna funkcja na sprawdzenie czy $x$ jest potęgą $y$**
```python
def czy_potega(x, y):  # sprawdza, czy x jest potęgą liczby y
    if x < 1 or y <= 1:  # potęgi rozważamy dla dodatniego x i podstawy y większej od 1
        return False  # jeśli warunek nie jest spełniony, zwracamy False

    while x % y == 0:  # dopóki x dzieli się przez y bez reszty
        x = x // y  # dzielimy x przez y

    return x == 1  # jeśli na końcu zostało 1, to x było potęgą y
```
**Przykład użycia**
```python
print(czy_potega(64, 2))   # True, bo 64 = 2^6
print(czy_potega(81, 3))   # True, bo 81 = 3^4
print(czy_potega(100, 10)) # True, bo 100 = 10^2
print(czy_potega(12, 2))   # False
print(czy_potega(16, 4))   # True, bo 16 = 4^2
```

**Rozwiązanie zadania**
```python
import numpy as np

def czy_potega_dwojki(x):
    return x > 0 and x & (x - 1) == 0

def generuj_tablice(n, m):
    if czy_potega_dwojki(n) and czy_potega_dwojki(m) and n > m:
        tablica = []

        for k in range(n):
            licznik = 1
            mianownik = ((k % m) + 1) * ((k % m) + 2)

            element = licznik / mianownik

            tablica.append(np.float32(element))

        return tablica
    else:
        raise ValueError("n i m muszą być potęgami liczby 2 oraz musi być spełnione n > m")

n = 64
m = 16

tablica = generuj_tablice(n, m)

print("Elementy ciągu:")
for i, wartosc in enumerate(tablica):
    print("a_", i, "=", wartosc)
```

## Zadanie 2
Napisz funkcję sumującą elementy tablicy z zadania 1. Sprawdź dokładność otrzymanej sumy.

```python
import numpy as np

def czy_potega_dwojki(x):
    return x > 0 and x & (x - 1) == 0

def generuj_tablice(n, m):
    if czy_potega_dwojki(n) and czy_potega_dwojki(m) and n > m:
        tablica = []

        for k in range(n):
            licznik = 1
            mianownik = ((k % m) + 1) * ((k % m) + 2)

            element = licznik / mianownik

            tablica.append(np.float32(element))

        return tablica
    else:
        raise ValueError("n i m muszą być potęgami liczby 2 oraz musi być spełnione n > m")

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
print("\nSprawdzenie sumy: ", n / (m + 1))
```

## Zadanie 3
Napisz funkcję sumującą elementy tablicy z zadania 1 z wykorzystaniem algorytmu Gilla–Møllera. Sprawdź dokładność otrzymanej sumy.

```python
import numpy as np

def czy_potega_dwojki(x):
    return x > 0 and x & (x - 1) == 0

def generuj_tablice(n, m):
    if czy_potega_dwojki(n) and czy_potega_dwojki(m) and n > m:
        tablica = []

        for k in range(n):
            licznik = 1
            mianownik = ((k % m) + 1) * ((k % m) + 2)

            element = licznik / mianownik

            tablica.append(np.float32(element))

        return tablica
    else:
        raise ValueError("n i m muszą być potęgami liczby 2 oraz musi być spełnione n > m")
        
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

print("\nSuma:", suma)
print("Sprawdzenie sumy:", n / (m + 1))
```

## Zadanie 4
Napisz funkcję sumującą elementy tablicy z zadania 1 z wykorzystaniem algorytmu Kahana. Sprawdź dokładność otrzymanej sumy. Porównaj wyniki wszystkich omówionych metod sumowania.

```python
import numpy as np

def czy_potega_dwojki(x):
    return x > 0 and x & (x - 1) == 0

def generuj_tablice(n, m):
    if czy_potega_dwojki(n) and czy_potega_dwojki(m) and n > m:
        tablica = []

        for k in range(n):
            licznik = 1
            mianownik = ((k % m) + 1) * ((k % m) + 2)

            element = licznik / mianownik

            tablica.append(np.float32(element))

        return tablica
    else:
        raise ValueError("n i m muszą być potęgami liczby 2 oraz musi być spełnione n > m")
        
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
```

## Zadanie 5
Przeprowadź analogiczne działania dla danych w podwójnej precyzji.

```python
import numpy as np

def czy_potega_dwojki(x):
    return x > 0 and x & (x - 1) == 0

def generuj_tablice(n, m):
    if czy_potega_dwojki(n) and czy_potega_dwojki(m) and n > m:
        tablica = []

        for k in range(n):
            licznik = 1
            mianownik = ((k % m) + 1) * ((k % m) + 2)

            element = licznik / mianownik

            tablica.append(element)

        return tablica
    else:
        raise ValueError("n i m muszą być potęgami liczby 2 oraz musi być spełnione n > m")
        
def sumuj_tablice(tablica):
    suma = 0.0

    for element in tablica:
        suma = suma + element

    return suma

def sumuj_tablice_Møller(tablica):
    suma = 0.0
    poprawka = 0.0

    for element in tablica:
        t = suma + element
        poprawka = poprawka + (element - (t-suma))
        suma = t

    return suma + poprawka

def sumuj_tablice_Kahan(tablica):
    suma = 0.0
    c = 0.0

    for element in tablica:
        y = element - c
        t = suma + y
        c = (t-suma) - y
        suma = t

    return suma

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
```

# Lab 3
## Zadanie 1
Napisz program, który obliczy normę: euklidesową, Manhattan, maximum dla -wymiarowego wektora.

```python
import math

def normy_wektora(wektor):

    # norma euklidesowa
    suma_kwadratow = 0
    for x in wektor:
        suma_kwadratow += x**2
    norma_euklidesowa = math.sqrt(suma_kwadratow)

    # norma Manhattan
    norma_manhattan = 0
    for x in wektor:
        norma_manhattan += abs(x)

    # norma maximum
    # norma_max = max(abs(x) for x in wektor)
    norma_max = 0

    for x in wektor:
        wartosc_bezwzgledna = abs(x)

        if wartosc_bezwzgledna > norma_max:
            norma_max = wartosc_bezwzgledna

    return norma_euklidesowa, norma_manhattan, norma_max

wektor = [3, 4, 5]

euklidesowa, manhattan, maksimum = normy_wektora(wektor)

print("Norma euklidesowa:", euklidesowa)
print("Norma Manhattan:", manhattan)
print("Norma maximum:", maksimum)
```

```
Norma euklidesowa: 7.0710678118654755
Norma Manhattan: 12
Norma maximum: 5
```

## Zadanie 2
Napisz program, który będzie wyliczał odległość pomiędzy dwoma punktami przestrzeni dwuwymiarowej w metrykach: euklidesowej, Manhattan, rzece i kolejowej.

```python
import math

def odleglosci(P, Q):
    p1, p2 = P
    q1, q2 = Q

    # metryka euklidesowa
    euklidesowa = math.sqrt(math.pow((q1 - p1), 2) + math.pow((q2 - p2), 2))

    #matryka Manhattan
    manhattan = abs(p1 - q1) + abs(p2 - q2)

    #metryka rzeka
    if p1 == q1:
        rzeka = abs(p2 - q2)
    else:
        rzeka = abs(p1 - q1) + abs(p2) + abs(q2)

    # metryka kolejowa
    det = p1 * q2 - p2 * q1
    if det == 0:
        kolejowa = math.sqrt(math.pow((q1 - p1), 2) + math.pow((q2 - p2), 2))
    else:
        kolejowa = math.sqrt(math.pow((0 - p1), 2) + math.pow((0 - p2), 2)) + math.sqrt(math.pow((0 - q1), 2) + math.pow((0 - q2), 2))

    return euklidesowa, manhattan, rzeka, kolejowa

punktP = (2, 3)
punktQ = (5, 7)

euklidesowa, manhattan, rzeka, kolejowa = odleglosci(punktP, punktQ)

print("Metryka euklidesowa:", euklidesowa)
print("Metryka Manhattan:", manhattan)
print("Metryka rzeka:", rzeka)
print("Metryka kolejowa/centrum:", kolejowa)
```

```
Metryka euklidesowa: 5.0
Metryka Manhattan: 7
Metryka rzeka: 13
Metryka kolejowa/centrum: 12.207876542506616
```

**Lub**

```python
import math

def metryka_euklidesowa(P, Q):
    p1, p2 = P
    q1, q2 = Q

    return math.sqrt(math.pow(q1 - p1, 2) + math.pow(q2 - p2, 2))


def metryka_manhattan(P, Q):
    p1, p2 = P
    q1, q2 = Q

    return abs(p1 - q1) + abs(p2 - q2)


def metryka_rzeka(P, Q):
    p1, p2 = P
    q1, q2 = Q

    if abs(p1 - q1) < 1e-12:
        return abs(p2 - q2)
    else:
        return abs(p1 - q1) + abs(p2) + abs(q2)


def metryka_kolejowa(P, Q):
    p1, p2 = P
    q1, q2 = Q

    det = p1 * q2 - p2 * q1

    if abs(det) < 1e-12:
        return math.sqrt(math.pow(q1 - p1, 2) + math.pow(q2 - p2, 2))
    else:
        odleglosc_P_od_centrum = math.sqrt(math.pow(p1, 2) + math.pow(p2, 2))
        odleglosc_Q_od_centrum = math.sqrt(math.pow(q1, 2) + math.pow(q2, 2))

        return odleglosc_P_od_centrum + odleglosc_Q_od_centrum


punktP = (2.5, 3.1)
punktQ = (5.2, 7.4)

euklidesowa = metryka_euklidesowa(punktP, punktQ)
manhattan = metryka_manhattan(punktP, punktQ)
rzeka = metryka_rzeka(punktP, punktQ)
kolejowa = metryka_kolejowa(punktP, punktQ)

print("Metryka euklidesowa:", euklidesowa)
print("Metryka Manhattan:", manhattan)
print("Metryka rzeka:", rzeka)
print("Metryka kolejowa/centrum:", kolejowa)
```

## Zadanie 3
Napisz program, który obliczy normę: Frobeniusa, Manhattan, maximum dla -wymiarowej macierzy.

```python
import math

def normy_macierzy(macierz):
    wiersze = len(macierz)
    kolumny = len(macierz[0])

    # norma Frobeniusa
    suma_kwadratow = 0
    for i in range(wiersze):
        for j in range(kolumny):
            suma_kwadratow += math.pow(macierz[i][j], 2)
    Frobeniusa = math.sqrt(suma_kwadratow)

    # norma Manhattan
    suma_modulow = 0
    for i in range(wiersze):
        for j in range(kolumny):
            suma_modulow += abs(macierz[i][j])
    Manhattan = suma_modulow

    # norma maksimum
    maksimum = 0
    for i in range(wiersze):
        for j in range(kolumny):
            if abs(macierz[i][j]) > maksimum:
                maksimum = abs(macierz[i][j])

    return Frobeniusa, Manhattan, maksimum

macierz = [
    [1, -2, 3],
    [4, 5, -6]
]

Frobeniusa, Manhattan, maksimum = normy_macierzy(macierz)

print("Norma Frobeniusa:", Frobeniusa)
print("Norma Manhattan:", Manhattan)
print("Norma maksimum:", maksimum)
```

```
Norma Frobeniusa: 9.539392014169456
Norma Manhattan: 21
Norma maksimum: 6
```

**Każda funkcja oddzielnie**
```python
import math

def norma_Frobeniusa(macierz):
    wiersze = len(macierz)
    kolumny = len(macierz[0])

    suma_kwadratow = 0

    for i in range(wiersze):
        for j in range(kolumny):
            suma_kwadratow += math.pow(macierz[i][j], 2)

    return math.sqrt(suma_kwadratow)


def norma_Manhattan(macierz):
    wiersze = len(macierz)
    kolumny = len(macierz[0])

    suma_modulow = 0

    for i in range(wiersze):
        for j in range(kolumny):
            suma_modulow += abs(macierz[i][j])

    return suma_modulow


def norma_maksimum(macierz):
    wiersze = len(macierz)
    kolumny = len(macierz[0])

    maksimum = 0

    for i in range(wiersze):
        for j in range(kolumny):
            if abs(macierz[i][j]) > maksimum:
                maksimum = abs(macierz[i][j])

    return maksimum


macierz = [
    [1, -2, 3],
    [4, 5, -6]
]

Frobeniusa = norma_Frobeniusa(macierz)
Manhattan = norma_Manhattan(macierz)
maksimum = norma_maksimum(macierz)

print("Norma Frobeniusa:", Frobeniusa)
print("Norma Manhattan:", Manhattan)
print("Norma maksimum:", maksimum)
```

## Zadanie 4
Napisz program, który wykona mnożenie dwóch macierzy. Kiedy działanie takie nie może zostać przeprowadzone? Sprawdź czy mnożenie macierzy jest przemienne lub łączne?

```python
def mnozenie_macierzy(macierz1, macierz2):
    ilosc_wierszy_macierz1 = len(macierz1)
    ilosc_wierszy_macierz2 = len(macierz2)
    ilosc_kolumn_macierz1 = len(macierz1[0])
    ilosc_kolumn_macierz2 = len(macierz2[0])

    if ilosc_kolumn_macierz1 != ilosc_wierszy_macierz2:
        raise ValueError("Nie da się pomnożyć tych macierzy")
    
    wynik = []
    for i in range(ilosc_wierszy_macierz1):
        wiersz = []
        for j in range(ilosc_kolumn_macierz2):
            suma = 0
            for k in range(ilosc_kolumn_macierz1):
                suma += macierz1[i][k] * macierz2[k][j]
            wiersz.append(suma)
        wynik.append(wiersz)

    return wynik

macierz1 = [
    [1, 2],
    [3, 4]
]

macierz2 = [
    [5, 6],
    [7, 8]
]

wynik = mnozenie_macierzy(macierz1, macierz2)

print("Wynik mnożenia:")
for wiersz in wynik:
    print(wiersz)


macierzAB = mnozenie_macierzy(macierz1, macierz2)
macierzBA = mnozenie_macierzy(macierz2, macierz1)
# czy przemienne => nie jest
print("Czy AB == BA", macierzAB == macierzBA) 

C = [
	[2, 0],
	[0, 2]
]

macierzAB = mnozenie_macierzy(macierz1, macierz2)
lewa = mnozenie_macierzy(macierzAB, C)

macierzBC = mnozenie_macierzy(macierz2, C)
prawa = mnozenie_macierzy(macierz1, macierzBC)

# czy łączne => jest łączne
print("Czy (AB)C == A(BC)", lewa == prawa)
```

```
Wynik mnożenia:
[19, 22]
[43, 50]

Czy AB == BA False
Czy (AB)C = A(BC) True
```

## Zadanie 5
Zaprojektuj i utwórz klasę dla macierzy umożliwiającą tworzenie, wypisywanie i wykonywanie działań: mnożenie przez stałą, dodawanie, mnożenie.

```python
# definicja klasy Macierz
class Macierz:
    # funkcja uruchamiana przy tworzeniu nowego obiektu klasy
    def __init__(self, dane):
        # sprawdzamy, czy macierz nie jest pusta
        if len(dane) == 0:
            raise ValueError("Macierz nie może być pusta")

        # sprawdzamy, czy pierwszy wiersz nie jest pusty
        if len(dane[0]) == 0:
            raise ValueError("Macierz musi mieć co najmniej jedną kolumnę")

        # zapamiętujemy liczbę kolumn z pierwszego wiersza
        liczba_kolumn = len(dane[0])

        # sprawdzamy, czy wszystkie wiersze mają tyle samo kolumn
        for wiersz in dane:
            if len(wiersz) != liczba_kolumn:
                raise ValueError("Wszystkie wiersze macierzy muszą mieć tę samą długość")

        # zapisanie danych macierzy wewnątrz obiektu
        self.dane = dane

    # funkcja do wypisywania macierzy
    def wypisz(self):
        # przejście po wszystkich wierszach macierzy
        for wiersz in self.dane:
            # wypisanie jednego wiersza
            print(wiersz)

    # funkcja mnożąca macierz przez liczbę
    def mnozenie_przez_stala(self, stala):
        # pusta lista na wynik
        wynik = []

        # przejście po wszystkich wierszach macierzy
        for wiersz in self.dane:
            # nowy wiersz wynikowy
            nowy_wiersz = []

            # przejście po wszystkich elementach w danym wierszu
            for element in wiersz:
                # dodanie do nowego wiersza elementu pomnożonego przez stałą
                nowy_wiersz.append(element * stala)

            # dodanie gotowego wiersza do macierzy wynikowej
            wynik.append(nowy_wiersz)

        # zwrócenie nowej macierzy jako obiektu klasy Macierz
        return Macierz(wynik)

    # funkcja dodająca dwie macierze
    def dodawanie(self, inna):
        # sprawdzamy, czy macierze mają taką samą liczbę wierszy
        if len(self.dane) != len(inna.dane):
            raise ValueError("Macierze muszą mieć taką samą liczbę wierszy")

        # sprawdzamy, czy macierze mają taką samą liczbę kolumn
        if len(self.dane[0]) != len(inna.dane[0]):
            raise ValueError("Macierze muszą mieć taką samą liczbę kolumn")

        # pusta lista na wynik
        wynik = []

        # przejście po numerach wierszy
        for i in range(len(self.dane)):
            # nowy wiersz wynikowy
            wiersz = []

            # przejście po numerach kolumn
            for j in range(len(self.dane[0])):
                # dodanie do siebie elementów z obu macierzy o tych samych indeksach
                wiersz.append(self.dane[i][j] + inna.dane[i][j])

            # dodanie gotowego wiersza do macierzy wynikowej
            wynik.append(wiersz)

        # zwrócenie nowej macierzy jako obiektu klasy Macierz
        return Macierz(wynik)

    # funkcja mnożąca dwie macierze
    def mnozenie(self, inna):
        # sprawdzamy warunek mnożenia macierzy
        if len(self.dane[0]) != len(inna.dane):
            raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy")

        # pusta lista na wynik
        wynik = []

        # przejście po wierszach pierwszej macierzy
        for i in range(len(self.dane)):
            # nowy wiersz wynikowy
            wiersz = []

            # przejście po kolumnach drugiej macierzy
            for j in range(len(inna.dane[0])):
                # zmienna przechowująca sumę iloczynów
                suma = 0

                # przejście po elementach wiersza i kolumny
                for k in range(len(self.dane[0])):
                    # dodawanie kolejnych iloczynów do sumy
                    suma += self.dane[i][k] * inna.dane[k][j]

                # dodanie obliczonego elementu do wiersza wynikowego
                wiersz.append(suma)

            # dodanie gotowego wiersza do macierzy wynikowej
            wynik.append(wiersz)

        # zwrócenie nowej macierzy jako obiektu klasy Macierz
        return Macierz(wynik)


# utworzenie pierwszej macierzy A
A = Macierz([[1, 2], [3, 4]])

# utworzenie drugiej macierzy B
B = Macierz([[5, 6], [7, 8]])

print("Macierz A:")
A.wypisz()

print("Macierz B:")
B.wypisz()

print("A + B:")
A.dodawanie(B).wypisz()

print("A * 2:")
A.mnozenie_przez_stala(2).wypisz()

print("A * B:")
A.mnozenie(B).wypisz()
```

# Lab 4
## Zadanie 1
Napisz funkcję zwracającą wyznacznik macierzy kwadratowej dowolnego rozmiaru.

```python
import math

def czy_kwadratowa(A):
    if len(A) == 0:
        return False
    
    liczba_wierszy = len(A)

    for i in range(liczba_wierszy):
            if len(A[i]) != liczba_wierszy:
                return False
    return True

def minor(macierz, usuniety_wiersz, usunieta_kolumne):
    wynik = []

    for i in range(len(macierz)):
        if i == usuniety_wiersz:
            continue

        nowy_wiersz = []
        for j in range(len(macierz[i])):
            if j == usunieta_kolumne:
                continue
            nowy_wiersz.append(macierz[i][j])

        wynik.append(nowy_wiersz)

    return wynik

def wyznacznik_macierzy(macierz):
    n = len(macierz)
    
    # sprawdzenie czy jest kwadratowa macierz
    # for wiersz in macierz:
    #     if len(wiersz) != n:
    #         raise ValueError("Nie da się policzyc wyznacznika macierzy, która nie jest kwadratowa")

    if not czy_kwadratowa(macierz):
        raise ValueError("Nie da się policzyc wyznacznika macierzy, która nie jest kwadratowa")
        
    if n == 1:
        return macierz[0][0]
    
    if n == 2:
        return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]
    
    wyznacznik = 0

    for j in range(n):
        podmacierz = minor(macierz, 0, j)
        wyznacznik += math.pow((-1), 0+j) * macierz[0][j] * wyznacznik_macierzy(podmacierz)
        # wyznacznik += ((-1) ** j) * macierz[0][j] * wyznacznik_macierzy(podmacierz) # to żeby nie było float

    return wyznacznik

macierz = [
    [2, 4, 6],
    [0, 2, -1],
    [-3, 3, 3]
]

print("Wyznacznik macierzy: ", wyznacznik_macierzy(macierz))
```

```
Wyznacznik macierzy:  66.0
```

## Zadanie 2
Napisz funkcję zwracającą transpozycję macierzy dowolnego rozmiaru.

```python
def transpozycja(macierz):
    liczba_wierszy = len(macierz)
    liczba_kolumn = len(macierz[0])

    wynik = []

    for j in range(liczba_kolumn):
        nowy_wiersz = []
        for i in range(liczba_wierszy):
            nowy_wiersz.append(macierz[i][j])
        wynik.append(nowy_wiersz)

    return wynik


macierz = [
    [2, 4, 6],
    [0, 2, -1],
    [-3, 3, 3]
]

print("Przed transpozycją macierzy:")
for wiersz in macierz:
    print(wiersz)

wynik = transpozycja(macierz)

print("Po transpozycji macierzy:")
for wiersz in wynik:
    print(wiersz)
```

```
Przed transpozycją macierzy:
[2, 4, 6]
[0, 2, -1]
[-3, 3, 3]

Po transpozycji macierzy:
[2, 0, -3]
[4, 2, 3]
[6, -1, 3]
```

## Zadanie 3
Napisz funkcję znajdującą macierz odwrotną do macierzy kwadratowej dowolnego rozmiaru za pomocą:

- a) rozwinięcia Laplace’a
- b) metody Gaussa-Jordana

```python
import math

def minor(macierz, usun_wiersz, usun_kolumne):
    wynik = []

    for i in range(len(macierz)):
        if i == usun_wiersz:
            continue

        nowy_wiersz = []
        for j in range(len(macierz[i])):
            if j == usun_kolumne:
                continue
            nowy_wiersz.append(macierz[i][j])

        wynik.append(nowy_wiersz)

    return wynik

def wyznacznik_macierzy(macierz):
    n = len(macierz)
    
    for wiersz in macierz:
        if len(wiersz) != n:
            raise ValueError("Nie da się policzyc wyznacznika macierzy, która nie jest kwadratowa")
        
    if n == 1:
        return macierz[0][0]
    
    if n == 2:
        return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]
    
    det = 0
    for j in range(n):
        podmacierz = minor(macierz, 0, j)
        det += math.pow((-1), 0+j) * macierz[0][j] * wyznacznik_macierzy(podmacierz)

    return det

def transpozycja(macierz):
    liczba_wierszy = len(macierz)
    liczba_kolumn = len(macierz[0])

    wynik = []

    for j in range(liczba_kolumn):
        nowy_wiersz = []
        for i in range(liczba_wierszy):
            nowy_wiersz.append(macierz[i][j])
        wynik.append(nowy_wiersz)

    return wynik

def zeros(n,m):
    macierz = []

    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0)
        macierz.append(wiersz)

    return macierz

def macierz_odwrotna_Laplace(macierz): # punkt a
    n = len(macierz)
    d = wyznacznik_macierzy(macierz)

    if d == 0:
        raise ValueError("Macierz jest osobliwa, nie ma odwrotności")
    
    if n == 1:
        return [[1 / d]]
    
    C = zeros(n, n)

    for i in range(n):
        for j in range(n):
            M = minor(macierz, i, j)
            C[i][j] = math.pow(-1, i+j) * wyznacznik_macierzy(M)

    Adj = transpozycja(C)
    
    wynik = zeros(n, n)
    for i in range(n):
        for j in range(n):
            wynik[i][j] = Adj[i][j] / d

    return wynik

def macierz_odwrotna_Gaussa_Jordana(macierz): # punkt b
    n = len(macierz)

    for wiersz in macierz:
        if len(wiersz) != n:
            raise ValueError("Macierz musi być kwadratowa")

    # macierz rozszerzona [A | I]
    rozszerzona_macierz = []

    for i in range(n):
        wiersz = []

        # lewa strona: macierz A
        for j in range(n):
            wiersz.append(macierz[i][j])
            # wiersz.append(float(macierz[i][j]))
        
        # prawa strona: macierz jednostkowa I
        for j in range(n):
            if i == j:
                wiersz.append(1)
            else:
                wiersz.append(0)

        rozszerzona_macierz.append(wiersz)

    # algorytm Gaussa-Jordana
    for i in range(n):
        # jeśli na przekątnej jest 0, zamień wiersze
        if rozszerzona_macierz[i][i] == 0:
            znaleziono = False
            for k in range(i+1, n):
                if rozszerzona_macierz[k][i] != 0:
                    rozszerzona_macierz[i], rozszerzona_macierz[k] = rozszerzona_macierz[k], rozszerzona_macierz[i]
                    znaleziono = True
                    break
            if not znaleziono:
                raise ValueError("Macierz nie ma odwrotności")
            
        # dzielenie całego wiersza przez element główny
        element_glowny = rozszerzona_macierz[i][i]
        for j in range(2 * n):
            rozszerzona_macierz[i][j] = rozszerzona_macierz[i][j] / element_glowny

        # zerowanie pozostałych elementów w tej kolumnie
        for k in range(n):
            if k != i:
                wspolczynnik = rozszerzona_macierz[k][i]
                for j in range(2 * n):
                    rozszerzona_macierz[k][j] = rozszerzona_macierz[k][j] - wspolczynnik * rozszerzona_macierz[i][j]

    odwrotna = []
    for i in range(n):
        wiersz = []
        for j in range(n, 2 * n):
            wiersz.append(rozszerzona_macierz[i][j])
        odwrotna.append(wiersz)

    return odwrotna

macierz = [
    [2, 4, 6],
    [0, 2, -1],
    [-3, 3, 3]
]

wynik_Laplace = macierz_odwrotna_Laplace(macierz)
wynik_Gauss_Jordan = macierz_odwrotna_Gaussa_Jordana(macierz)

print("Macierz odwrotna Laplace:")
for wiersz in wynik_Laplace:
    print(wiersz)

print("Macierz odwrotna Gauss Jordan:")
for wiersz in wynik_Gauss_Jordan:
    print(wiersz)
```

```
Macierz odwrotna Laplace:
[0.13636363636363635, 0.09090909090909091, -0.24242424242424243]
[0.045454545454545456, 0.36363636363636365, 0.030303030303030304]
[0.09090909090909091, -0.2727272727272727, 0.06060606060606061]

Macierz odwrotna Gauss Jordan:
[0.13636363636363635, 0.09090909090909083, -0.24242424242424243]
[0.045454545454545456, 0.36363636363636365, 0.030303030303030304]
[0.09090909090909091, -0.2727272727272727, 0.06060606060606061]
```

**Gauss-Jordan do wyznacznika i odwrotnej**
```python
def macierz_odwrotna_Gaussa_Jordana(macierz):
    n = len(macierz)

    for wiersz in macierz:
        if len(wiersz) != n:
            raise ValueError("Macierz musi być kwadratowa")

    rozszerzona_macierz = []

    for i in range(n):
        wiersz = []

        for j in range(n):
            wiersz.append(macierz[i][j])

        for j in range(n):
            if i == j:
                wiersz.append(1)
            else:
                wiersz.append(0)

        rozszerzona_macierz.append(wiersz)

    wyznacznik = 1

    for i in range(n):
        if rozszerzona_macierz[i][i] == 0:
            znaleziono = False

            for k in range(i + 1, n):
                if rozszerzona_macierz[k][i] != 0:
                    rozszerzona_macierz[i], rozszerzona_macierz[k] = rozszerzona_macierz[k], rozszerzona_macierz[i]
                    wyznacznik *= -1
                    znaleziono = True
                    break

            if not znaleziono:
                raise ValueError("Macierz nie ma odwrotności")

        element_glowny = rozszerzona_macierz[i][i]

        wyznacznik *= element_glowny

        for j in range(2 * n):
            rozszerzona_macierz[i][j] = rozszerzona_macierz[i][j] / element_glowny

        for k in range(n):
            if k != i:
                wspolczynnik = rozszerzona_macierz[k][i]

                for j in range(2 * n):
                    rozszerzona_macierz[k][j] = rozszerzona_macierz[k][j] - wspolczynnik * rozszerzona_macierz[i][j]

    odwrotna = []

    for i in range(n):
        wiersz = []

        for j in range(n, 2 * n):
            wiersz.append(rozszerzona_macierz[i][j])

        odwrotna.append(wiersz)

    return odwrotna, wyznacznik
```

## Zadanie 4
Napisz funkcję, która wykona mnożenie dwóch macierzy.

```python
def mnozenie_macierzy(macierz1, macierz2):
    ilosc_wierszy_macierz1 = len(macierz1)
    ilosc_wierszy_macierz2 = len(macierz2)
    ilosc_kolumn_macierz1 = len(macierz1[0])
    ilosc_kolumn_macierz2 = len(macierz2[0])

    if ilosc_kolumn_macierz1 != ilosc_wierszy_macierz2:
        raise ValueError("Nie da się pomnożyć tych macierzy")
    
    wynik = []
    for i in range(ilosc_wierszy_macierz1):
        wiersz = []
        for j in range(ilosc_kolumn_macierz2):
            suma = 0
            for k in range(ilosc_kolumn_macierz1):
                suma += macierz1[i][k] * macierz2[k][j]
            wiersz.append(suma)
        wynik.append(wiersz)

    return wynik

macierz1 = [
    [1, 2],
    [3, 4]
]

macierz2 = [
    [5, 6],
    [7, 8]
]

wynik = mnozenie_macierzy(macierz1, macierz2)

print("Wynik mnożenia:")
for wiersz in wynik:
    print(wiersz)


macierzAB = mnozenie_macierzy(macierz1, macierz2)
macierzBA = mnozenie_macierzy(macierz2, macierz1)
```

```
Wynik mnożenia:
[19, 22]
[43, 50]
```

## Zadanie 5
Korzystając z rozwiązań poprzednich zadań wykonaj następujące mnożenia macierzowe: $A \cdot A^{-1}$ oraz $A^{-1} \cdot A$ i porównaj ich wyniki.

```python
def macierz_odwrotna_Gaussa_Jordana(macierz): # punkt b
    n = len(macierz)

    for wiersz in macierz:
        if len(wiersz) != n:
            raise ValueError("Macierz musi być kwadratowa")

    # macierz rozszerzona [A | I]
    rozszerzona_macierz = []

    for i in range(n):
        wiersz = []

        # lewa strona: macierz A
        for j in range(n):
            wiersz.append(macierz[i][j])
            # wiersz.append(float(macierz[i][j]))
        
        # prawa strona: macierz jednostkowa I
        for j in range(n):
            if i == j:
                wiersz.append(1)
            else:
                wiersz.append(0)

        rozszerzona_macierz.append(wiersz)

    # algorytm Gaussa-Jordana
    for i in range(n):
        # jeśli na przekątnej jest 0, zamień wiersze
        if rozszerzona_macierz[i][i] == 0:
            znaleziono = False
            for k in range(i+1, n):
                if rozszerzona_macierz[k][i] != 0:
                    rozszerzona_macierz[i], rozszerzona_macierz[k] = rozszerzona_macierz[k], rozszerzona_macierz[i]
                    znaleziono = True
                    break
            if not znaleziono:
                raise ValueError("Macierz nie ma odwrotności")
            
        # dzielenie całego wiersza przez element główny
        element_glowny = rozszerzona_macierz[i][i]
        for j in range(2 * n):
            rozszerzona_macierz[i][j] = rozszerzona_macierz[i][j] / element_glowny

        # zerowanie pozostałych elementów w tej kolumnie
        for k in range(n):
            if k != i:
                wspolczynnik = rozszerzona_macierz[k][i]
                for j in range(2 * n):
                    rozszerzona_macierz[k][j] = rozszerzona_macierz[k][j] - wspolczynnik * rozszerzona_macierz[i][j]

    odwrotna = []
    for i in range(n):
        wiersz = []
        for j in range(n, 2 * n):
            wiersz.append(rozszerzona_macierz[i][j])
        odwrotna.append(wiersz)

    return odwrotna
    
def mnozenie_macierzy(macierz1, macierz2):
    ilosc_wierszy_macierz1 = len(macierz1)
    ilosc_wierszy_macierz2 = len(macierz2)
    ilosc_kolumn_macierz1 = len(macierz1[0])
    ilosc_kolumn_macierz2 = len(macierz2[0])

    if ilosc_kolumn_macierz1 != ilosc_wierszy_macierz2:
        raise ValueError("Nie da się pomnożyć tych macierzy")
    
    wynik = []
    for i in range(ilosc_wierszy_macierz1):
        wiersz = []
        for j in range(ilosc_kolumn_macierz2):
            suma = 0
            for k in range(ilosc_kolumn_macierz1):
                suma += macierz1[i][k] * macierz2[k][j]
            wiersz.append(suma)
        wynik.append(wiersz)

    return wynik

macierz1 = [
    [1, 2],
    [3, 4]
]

macierz2 = [
    [5, 6],
    [7, 8]
]

wynik = mnozenie_macierzy(macierz1, macierz2)

print("Wynik mnożenia:")
for wiersz in wynik:
    print(wiersz)


macierzAB = mnozenie_macierzy(macierz1, macierz2)
macierzBA = mnozenie_macierzy(macierz2, macierz1)

macierz = [
    [2, 4, 6],
    [0, 2, -1],
    [-3, 3, 3]
]

macierz_odwrotna = macierz_odwrotna_Gaussa_Jordana(macierz)

wynik1 = mnozenie_macierzy(macierz, macierz_odwrotna)
wynik2 = mnozenie_macierzy(macierz_odwrotna, macierz)

print("Wynik mnożenia A * A^-1:")
for wiersz in wynik1:
    print(wiersz)

print("Wynik mnożenia A^-1 * A:")
for wiersz in wynik2:
    print(wiersz)
```

```
Wynik mnożenia A * A^-1:
[1.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[0.0, 2.220446049250313e-16, 1.0]

Wynik mnożenia A^-1 * A:
[1.0, -2.220446049250313e-16, 0.0]
[0.0, 1.0, -2.7755575615628914e-17]
[0.0, 5.551115123125783e-17, 1.0]
```

# Lab 5
## Zadanie 1