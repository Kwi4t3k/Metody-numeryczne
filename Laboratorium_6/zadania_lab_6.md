# Zadanie 1

**Napisz program implementujący metodę Jacobiego iteracyjnego rozwiązywania układów równań liniowych, w której warunkiem zatrzymania będzie:**

a) liczba iteracji,  
b) norma wektora powstałego przez odjęcie wektorów określających kolejne przybliżenia,  
c) błąd uzyskanego przybliżenia.

## Co to jest metoda Jacobiego?

Metoda Jacobiego jest metodą iteracyjną, czyli nie liczy rozwiązania od razu, tylko buduje kolejne przybliżenia:

$$
x^{(0)}, x^{(1)}, x^{(2)}, \dots
$$

Każde nowe przybliżenie oblicza się wyłącznie na podstawie poprzedniego.

Dla układu:

$$
Ax = b
$$

każdą niewiadomą w iteracji $k$ obliczamy na podstawie wartości z iteracji poprzedniej, czyli $x^{(k-1)}$.

wzór metody Jacobiego ma postać:

$$
x_i^{(k)} =
\frac{1}{a_{ii}}
\left(
b_i - \sum_{j \ne i} a_{ij}x_j^{(k-1)}
\right)
$$

gdzie:

- $a_{ii}$ - element na przekątnej macierzy,
- $b_i$ - odpowiedni element wektora prawej strony,
- $x_j^{(k-1)}$ - wartości z poprzedniej iteracji.

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz wektor początkowy $x^{(0)}$, na przykład:

$$
x^{(0)} = [0,0,0,0]
$$

### Krok 2

Dla każdej iteracji liczysz nowy wektor $x^{(k)}$ na podstawie poprzedniego wektora $x^{(k-1)}$.

### Krok 3

Po każdej iteracji sprawdzasz warunek zatrzymania.

### Krok 4

Jeśli warunek jest spełniony, kończysz obliczenia.

---

## Warunki zatrzymania

### a) Liczba iteracji

Program kończy działanie po zadanej liczbie kroków.

### b) Norma różnicy kolejnych przybliżeń

Sprawdzasz, czy:

$$
\|x^{(k+1)} - x^{(k)}\| < \varepsilon
$$

Jeżeli różnica między kolejnymi przybliżeniami jest bardzo mała, uznajesz, że rozwiązanie już się ustabilizowało.

### c) Błąd uzyskanego przybliżenia

Jeżeli znasz dokładne rozwiązanie $x^*$, możesz sprawdzać:

$$
\|x^{(k)} - x^*\| < \varepsilon
$$

---

## Kod

```python
def norma_max(wektor):
    maksimum = abs(wektor[0])
    for i in range(1, len(wektor)):
        if abs(wektor[i]) > maksimum:
            maksimum = abs(wektor[i])
    return maksimum


def odejmij_wektory(wektor1, wektor2):
    wynik = []
    for i in range(len(wektor1)):
        wynik.append(wektor1[i] - wektor2[i])
    return wynik

def wypisz_wektor(wektor, nazwa="x"):
    for i in range(len(wektor)):
        print(f"{nazwa}{i+1} = {wektor[i]}")

def jacobi(A, b, x0, max_iter=100, epsilon=1e-8, warunek_stopu="iteracje", rozwiazanie_dokladne=None):
    n = len(A)
    x_stare = x0[:]

    for krok in range(1, max_iter + 1):
        x_nowe = [0.0] * n

        for i in range(n):
            suma = 0.0
            for j in range(n):
                if j != i:
                    suma += A[i][j] * x_stare[j]

            x_nowe[i] = (b[i] - suma) / A[i][i]

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x_nowe, krok

        elif warunek_stopu == "roznica":
            roznica = odejmij_wektory(x_nowe, x_stare)
            if norma_max(roznica) < epsilon:
                return x_nowe, krok

        elif warunek_stopu == "blad":
            if rozwiazanie_dokladne is None:
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")
            blad = odejmij_wektory(x_nowe, rozwiazanie_dokladne)
            if norma_max(blad) < epsilon:
                return x_nowe, krok

        x_stare = x_nowe[:]

    return x_stare, max_iter

print("--------------------ZADANIE 1--------------------")

# Przykładowy układ:
# 10x1 - x2 + 2x3 = 6
# -x1 + 11x2 - x3 + 3x4 = 25
# 2x1 - x2 + 10x3 - x4 = -11
# 3x2 - x3 + 8x4 = 15

A = [
    [10.0, -1.0,  2.0,  0.0],
    [-1.0, 11.0, -1.0,  3.0],
    [2.0, -1.0, 10.0, -1.0],
    [0.0,  3.0, -1.0,  8.0]
]

b = [6.0, 25.0, -11.0, 15.0]

# Przybliżenie początkowe
x0 = [0.0, 0.0, 0.0, 0.0]

# Dokładne rozwiązanie tego układu:
# x = [1, 2, -1, 1]
x_dokladne = [1.0, 2.0, -1.0, 1.0]

print("\nDane:")
print("Macierz A:")
for wiersz in A:
    print(wiersz)

print("\nWektor b:")
print(b)

print("\nPrzybliżenie początkowe x^(0):")
print(x0)

print("\nDokładne rozwiązanie:")
print(x_dokladne)

# --------------------------------------------------
# a) Warunek stopu: liczba iteracji
# --------------------------------------------------
print("\n-------------------- a) LICZBA ITERACJI --------------------")
wynik_a, iteracje_a = jacobi(
    A, b, x0,
    max_iter=10,
    warunek_stopu="iteracje"
)

print("\nWynik końcowy po zadanej liczbie iteracji:")
wypisz_wektor(wynik_a)
print("Liczba iteracji:", iteracje_a)

roznica_a = odejmij_wektory(wynik_a, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(roznica_a))

# --------------------------------------------------
# b) Warunek stopu: norma różnicy kolejnych przybliżeń
# --------------------------------------------------
print("\n-------------------- b) NORMA RÓŻNICY KOLEJNYCH PRZYBLIŻEŃ --------------------")
wynik_b, iteracje_b = jacobi(
    A, b, x0,
    max_iter=100,
    epsilon=1e-6,
    warunek_stopu="roznica"
)

print("\nWynik końcowy:")
wypisz_wektor(wynik_b)
print("Liczba iteracji:", iteracje_b)

roznica_b = odejmij_wektory(wynik_b, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(roznica_b))

# --------------------------------------------------
# c) Warunek stopu: błąd uzyskanego przybliżenia
# --------------------------------------------------
print("\n-------------------- c) BŁĄD UZYSKANEGO PRZYBLIŻENIA --------------------")
wynik_c, iteracje_c = jacobi(
    A, b, x0,
    max_iter=100,
    epsilon=1e-6,
    warunek_stopu="blad",
    rozwiazanie_dokladne=x_dokladne
)

print("\nWynik końcowy:")
wypisz_wektor(wynik_c)
print("Liczba iteracji:", iteracje_c)

roznica_c = odejmij_wektory(wynik_c, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(roznica_c))

print("\n-------------------- WNIOSEK --------------------")
print("Jeżeli wyniki są coraz bliższe [1, 2, -1, 1], to program działa poprawnie.")
````

---

# Zadanie 2

**Napisz program implementujący metodę Gaussa-Seidla iteracyjnego rozwiązywania układów równań liniowych z analogicznymi warunkami zatrzymania jak w zadaniu 1.**

---

## Co to jest metoda Gaussa-Seidla?

Metoda Gaussa-Seidla jest podobna do metody Jacobiego, ale ma ważną różnicę:

podczas liczenia nowego przybliżenia wykorzystuje od razu te wartości, które zostały już policzone w bieżącej iteracji.

Każdą niewiadomą w iteracji \(k\) obliczamy ze wzoru:

$$
x_i^{(k)} =
\frac{1}{a_{ii}}
\left(
b_i
- \sum_{j=1}^{i-1} a_{ij}x_j^{(k)}
- \sum_{j=i+1}^{n} a_{ij}x_j^{(k-1)}
\right),
\quad i=1,2,\dots,n
$$

dla $i = 1,2,...,n$.

Czyli:

- dla wcześniejszych współrzędnych używamy już **nowych wartości** z iteracji $k$,
- dla późniejszych współrzędnych używamy jeszcze **starych wartości** z iteracji $k-1$.

Dzięki temu metoda Gaussa-Seidla zwykle zbiega szybciej niż metoda Jacobiego.

---

## Różnica względem metody Jacobiego

W metodzie Jacobiego wszystkie nowe wartości obliczane są wyłącznie na podstawie poprzedniego przybliżenia.

W metodzie Gaussa-Seidla:

- korzystamy z najnowszych dostępnych wartości,
- wartości są aktualizowane **sekwencyjnie**,
- po obliczeniu $x_1^{(k)}$ można od razu użyć go do wyznaczenia $x_2^{(k)}$, potem $x_3^{(k)}$ itd.

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz początkowe przybliżenie $x^{(0)}$.

### Krok 2

Dla każdej iteracji przechodzisz po współrzędnych po kolei: $i=1,2,\dots,n$.

### Krok 3

Przy obliczaniu nowej wartości $x_i^{(k)}$ używasz:

- nowych wartości $x_1^{(k)}, x_2^{(k)}, \dots, x_{i-1}^{(k)}$,
- starych wartości $x_{i+1}^{(k-1)}, x_{i+2}^{(k-1)}, \dots, x_n^{(k-1)}$.

### Krok 4

Po zakończeniu całej iteracji sprawdzasz warunek zatrzymania:

- liczba iteracji,
- norma różnicy kolejnych przybliżeń,
- błąd przybliżenia.

## Warunek stosowalności

Aby metoda mogła być wykonywana, na przekątnej macierzy nie może być zera, czyli:

$$
a_{ii} \ne 0 \quad \text{dla wszystkich } i=1,2,\dots,n
$$

## Kod

```python
def norma_max(wektor):
    maksimum = abs(wektor[0])
    for i in range(1, len(wektor)):
        if abs(wektor[i]) > maksimum:
            maksimum = abs(wektor[i])
    return maksimum


def odejmij_wektory(wektor1, wektor2):
    wynik = []
    for i in range(len(wektor1)):
        wynik.append(wektor1[i] - wektor2[i])
    return wynik


def wypisz_wektor(wektor, nazwa="x"):
    for i in range(len(wektor)):
        print(f"{nazwa}{i+1} = {wektor[i]}")


def gauss_seidel(A, b, x0, max_iter=100, epsilon=1e-8, warunek_stopu="iteracje", rozwiazanie_dokladne=None):
    n = len(A)
    x = x0[:]

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("Na przekątnej macierzy nie może być zera")

    for krok in range(1, max_iter + 1):
        x_stare = x[:]

        for i in range(n):
            suma1 = 0.0
            for j in range(i):
                suma1 += A[i][j] * x[j]

            suma2 = 0.0
            for j in range(i + 1, n):
                suma2 += A[i][j] * x_stare[j]

            x[i] = (b[i] - suma1 - suma2) / A[i][i]

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x, krok

        elif warunek_stopu == "roznica":
            roznica = odejmij_wektory(x, x_stare)
            if norma_max(roznica) < epsilon:
                return x, krok

        elif warunek_stopu == "blad":
            if rozwiazanie_dokladne is None:
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")
            blad = odejmij_wektory(x, rozwiazanie_dokladne)
            if norma_max(blad) < epsilon:
                return x, krok

        else:
            raise ValueError("Niepoprawny warunek stopu")

    return x, max_iter


print("-------------------- ZADANIE 2 --------------------")

# Przykładowy układ:
# 10x1 - x2 + 2x3 = 6
# -x1 + 11x2 - x3 + 3x4 = 25
# 2x1 - x2 + 10x3 - x4 = -11
# 3x2 - x3 + 8x4 = 15

A = [
    [10.0, -1.0,  2.0,  0.0],
    [-1.0, 11.0, -1.0,  3.0],
    [2.0, -1.0, 10.0, -1.0],
    [0.0,  3.0, -1.0,  8.0]
]

b = [6.0, 25.0, -11.0, 15.0]

# Przybliżenie początkowe
x0 = [0.0, 0.0, 0.0, 0.0]

# Dokładne rozwiązanie
x_dokladne = [1.0, 2.0, -1.0, 1.0]

print("\nDane:")
print("Macierz A:")
for wiersz in A:
    print(wiersz)

print("\nWektor b:")
print(b)

print("\nPrzybliżenie początkowe x^(0):")
print(x0)

print("\nDokładne rozwiązanie:")
print(x_dokladne)

# a) liczba iteracji
print("\n-------------------- a) LICZBA ITERACJI --------------------")
wynik_a, iteracje_a = gauss_seidel(
    A, b, x0,
    max_iter=10,
    warunek_stopu="iteracje"
)

print("\nWynik końcowy po zadanej liczbie iteracji:")
wypisz_wektor(wynik_a)
print("Liczba iteracji:", iteracje_a)

blad_a = odejmij_wektory(wynik_a, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_a))

# b) norma różnicy kolejnych przybliżeń
print("\n-------------------- b) NORMA RÓŻNICY KOLEJNYCH PRZYBLIŻEŃ --------------------")
wynik_b, iteracje_b = gauss_seidel(
    A, b, x0,
    max_iter=100,
    epsilon=1e-6,
    warunek_stopu="roznica"
)

print("\nWynik końcowy:")
wypisz_wektor(wynik_b)
print("Liczba iteracji:", iteracje_b)

blad_b = odejmij_wektory(wynik_b, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_b))

# c) błąd uzyskanego przybliżenia
print("\n-------------------- c) BŁĄD UZYSKANEGO PRZYBLIŻENIA --------------------")
wynik_c, iteracje_c = gauss_seidel(
    A, b, x0,
    max_iter=100,
    epsilon=1e-6,
    warunek_stopu="blad",
    rozwiazanie_dokladne=x_dokladne
)

print("\nWynik końcowy:")
wypisz_wektor(wynik_c)
print("Liczba iteracji:", iteracje_c)

blad_c = odejmij_wektory(wynik_c, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_c))

print("\n-------------------- WNIOSEK --------------------")
print("Jeżeli wyniki są bliskie [1, 2, -1, 1], to program działa poprawnie.")
```

---

# Zadanie 3

**Sprawdź uwarunkowanie układu pod kątem metod z zadania 1 oraz 2.**

Układ do testowania:

$$
\begin{cases}
4x_1 - 2x_2 = 0, \\
-2x_1 + 5x_2 - x_3 = 2, \\
-x_2 + 4x_3 + 2x_4 = 3, \\
2x_3 + 3x_4 = -2.
\end{cases}
$$

---

## Zapis macierzowy układu

Macierz współczynników:

$$
A =
\begin{bmatrix}
4 & -2 & 0 & 0 \\
-2 & 5 & -1 & 0 \\
0 & -1 & 4 & 2 \\
0 & 0 & 2 & 3
\end{bmatrix}
$$

Wektor prawej strony:

$$
b =
\begin{bmatrix}
0 \\
2 \\
3 \\
-2
\end{bmatrix}
$$

Dokładne rozwiązanie tego układu jest równe:

$$
x^* =
\begin{bmatrix}
0.5 \\
1 \\
2 \\
-2
\end{bmatrix}
$$

---

## Jak sprawdzić, czy metody powinny być zbieżne?

Najprostsze kryterium to **ściśle diagonalna dominacja**.

Macierz jest ściśle diagonalnie dominująca, jeśli w każdym wierszu:

$$
|a_{ii}| > \sum_{j \ne i} |a_{ij}|
$$

Sprawdźmy:

### Wiersz 1

$$
|4| > |-2| \quad \Rightarrow \quad 4 > 2
$$

### Wiersz 2

$$
|5| > |-2| + |-1| \quad \Rightarrow \quad 5 > 3
$$

### Wiersz 3

$$
|4| > |-1| + |2| \quad \Rightarrow \quad 4 > 3
$$

### Wiersz 4

$$
|3| > |2| \quad \Rightarrow \quad 3 > 2
$$

W każdym przypadku warunek jest spełniony.

---

## Wniosek o uwarunkowaniu

Macierz jest **ściśle diagonalnie dominująca**, więc:

* metoda Jacobiego jest zbieżna,
* metoda Gaussa-Seidla również jest zbieżna.

---

# Funkcja sprawdzająca dominację diagonalną

```python
def sprawdz_dominacje_diagonalna(A):
    for i in range(len(A)):
        suma = 0.0
        for j in range(len(A[i])):
            if i != j:
                suma += abs(A[i][j])

        if abs(A[i][i]) <= suma:
            return False

    return True
```

---

# Program testujący cały układ

```python
def norma_max(wektor):
    maksimum = abs(wektor[0])
    for i in range(1, len(wektor)):
        if abs(wektor[i]) > maksimum:
            maksimum = abs(wektor[i])
    return maksimum


def odejmij_wektory(wektor1, wektor2):
    wynik = []
    for i in range(len(wektor1)):
        wynik.append(wektor1[i] - wektor2[i])
    return wynik


def jacobi(A, b, x0, max_iter=100, epsilon=1e-8, warunek_stopu="iteracje", rozwiazanie_dokladne=None):
    n = len(A)
    x_stare = x0[:]

    for krok in range(1, max_iter + 1):
        x_nowe = [0.0] * n

        for i in range(n):
            suma = 0.0
            for j in range(n):
                if j != i:
                    suma += A[i][j] * x_stare[j]

            x_nowe[i] = (b[i] - suma) / A[i][i]

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x_nowe, krok

        elif warunek_stopu == "roznica":
            roznica = odejmij_wektory(x_nowe, x_stare)
            if norma_max(roznica) < epsilon:
                return x_nowe, krok

        elif warunek_stopu == "blad":
            if rozwiazanie_dokladne is None:
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")
            blad = odejmij_wektory(x_nowe, rozwiazanie_dokladne)
            if norma_max(blad) < epsilon:
                return x_nowe, krok

        x_stare = x_nowe[:]

    return x_stare, max_iter


def gauss_seidel(A, b, x0, max_iter=100, epsilon=1e-8, warunek_stopu="iteracje", rozwiazanie_dokladne=None):
    n = len(A)
    x = x0[:]

    for krok in range(1, max_iter + 1):
        x_stare = x[:]

        for i in range(n):
            suma1 = 0.0
            for j in range(i):
                suma1 += A[i][j] * x[j]

            suma2 = 0.0
            for j in range(i + 1, n):
                suma2 += A[i][j] * x_stare[j]

            x[i] = (b[i] - suma1 - suma2) / A[i][i]

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x, krok

        elif warunek_stopu == "roznica":
            roznica = odejmij_wektory(x, x_stare)
            if norma_max(roznica) < epsilon:
                return x, krok

        elif warunek_stopu == "blad":
            if rozwiazanie_dokladne is None:
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")
            blad = odejmij_wektory(x, rozwiazanie_dokladne)
            if norma_max(blad) < epsilon:
                return x, krok

    return x, max_iter


def sprawdz_dominacje_diagonalna(A):
    for i in range(len(A)):
        suma = 0.0
        for j in range(len(A[i])):
            if i != j:
                suma += abs(A[i][j])

        if abs(A[i][i]) <= suma:
            return False

    return True


A = [
    [4.0, -2.0, 0.0, 0.0],
    [-2.0, 5.0, -1.0, 0.0],
    [0.0, -1.0, 4.0, 2.0],
    [0.0, 0.0, 2.0, 3.0]
]

b = [0.0, 2.0, 3.0, -2.0]

x0 = [0.0, 0.0, 0.0, 0.0]
x_dokladne = [0.5, 1.0, 2.0, -2.0]

print("Czy macierz jest ściśle diagonalnie dominująca?", sprawdz_dominacje_diagonalna(A))

print("\nJACOBI - warunek: liczba iteracji")
wynik, kroki = jacobi(A, b, x0, max_iter=10, warunek_stopu="iteracje")
print("Wynik:", wynik)
print("Liczba iteracji:", kroki)

print("\nJACOBI - warunek: norma różnicy")
wynik, kroki = jacobi(A, b, x0, epsilon=1e-8, warunek_stopu="roznica")
print("Wynik:", wynik)
print("Liczba iteracji:", kroki)

print("\nJACOBI - warunek: błąd przybliżenia")
wynik, kroki = jacobi(A, b, x0, epsilon=1e-8, warunek_stopu="blad", rozwiazanie_dokladne=x_dokladne)
print("Wynik:", wynik)
print("Liczba iteracji:", kroki)

print("\nGAUSS-SEIDEL - warunek: liczba iteracji")
wynik, kroki = gauss_seidel(A, b, x0, max_iter=10, warunek_stopu="iteracje")
print("Wynik:", wynik)
print("Liczba iteracji:", kroki)

print("\nGAUSS-SEIDEL - warunek: norma różnicy")
wynik, kroki = gauss_seidel(A, b, x0, epsilon=1e-8, warunek_stopu="roznica")
print("Wynik:", wynik)
print("Liczba iteracji:", kroki)

print("\nGAUSS-SEIDEL - warunek: błąd przybliżenia")
wynik, kroki = gauss_seidel(A, b, x0, epsilon=1e-8, warunek_stopu="blad", rozwiazanie_dokladne=x_dokladne)
print("Wynik:", wynik)
print("Liczba iteracji:", kroki)
```

---

# Wnioski

* Metoda Jacobiego wykorzystuje w każdej iteracji tylko poprzednie przybliżenie.
* Metoda Gaussa-Seidla wykorzystuje już nowe wartości obliczone w tej samej iteracji, dlatego zwykle działa szybciej.
* Dla badanego układu macierz jest ściśle diagonalnie dominująca, więc obie metody są zbieżne.
* W praktyce metoda Gaussa-Seidla zwykle potrzebuje mniej iteracji niż metoda Jacobiego, aby osiągnąć podobną dokładność.

```