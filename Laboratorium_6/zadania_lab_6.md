# Zadanie 1

**Napisz program implementujący metodę Jacobiego iteracyjnego rozwiązywania układów równań liniowych, w której warunkiem zatrzymania będzie:**

a) liczba iteracji,  
b) norma wektora powstałego przez odjęcie wektorów określających kolejne przybliżenia,  
c) błąd uzyskanego przybliżenia.

---

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

wzór metody Jacobiego ma postać:

$$
x_i^{(k+1)} =
\frac{1}{a_{ii}}
\left(
b_i - \sum_{j \ne i} a_{ij}x_j^{(k)}
\right)
$$

To znaczy, że przy liczeniu nowej wartości \(x_i\):
- korzystasz z elementów macierzy \(A\),
- z prawej strony układu \(b\),
- i tylko ze **starego przybliżenia**.

---

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz wektor początkowy \(x^{(0)}\), na przykład:

$$
x^{(0)} = [0,0,0,0]
$$

### Krok 2

Dla każdej iteracji liczysz nowy wektor \(x^{(k+1)}\).

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

Jeżeli znasz dokładne rozwiązanie \(x^*\), możesz sprawdzać:

$$
\|x^{(k)} - x^*\| < \varepsilon
$$

---

## Kod — metoda Jacobiego

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
````

---

# Zadanie 2

**Napisz program implementujący metodę Gaussa-Seidla iteracyjnego rozwiązywania układów równań liniowych z analogicznymi warunkami zatrzymania jak w zadaniu 1.**

---

## Co to jest metoda Gaussa-Seidla?

Metoda Gaussa-Seidla jest podobna do metody Jacobiego, ale ma ważną różnicę:

podczas liczenia nowego przybliżenia wykorzystuje od razu te wartości, które zostały już policzone w bieżącej iteracji.

Wzór ma postać:

$$
x_i^{(k+1)} =
\frac{1}{a_{ii}}
\left(
b_i

* \sum_{j < i} a_{ij}x_j^{(k+1)}
* \sum_{j > i} a_{ij}x_j^{(k)}
  \right)
  $$

Czyli:

* dla wcześniejszych współrzędnych bierzesz już nowe wartości,
* dla późniejszych jeszcze stare.

Dzięki temu metoda Gaussa-Seidla zwykle zbiega szybciej niż metoda Jacobiego.

---

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz początkowe przybliżenie (x^{(0)}).

### Krok 2

Dla każdej iteracji przechodzisz po współrzędnych po kolei.

### Krok 3

Przy obliczaniu nowej wartości używasz:

* nowych wartości dla indeksów wcześniejszych,
* starych wartości dla indeksów późniejszych.

### Krok 4

Po każdej iteracji sprawdzasz warunek zatrzymania:

* liczba iteracji,
* norma różnicy,
* błąd przybliżenia.

---

## Kod — metoda Gaussa-Seidla

```python
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
```

---

# Zadanie 3

**Sprawdź uwarunkowanie układu pod kątem metod z zadania 1 oraz 2.**

Układ do testowania:

$$
\begin{cases}
4x_1 - 2x_2 = 0, \
-2x_1 + 5x_2 - x_3 = 2, \
-x_2 + 4x_3 + 2x_4 = 3, \
2x_3 + 3x_4 = -2.
\end{cases}
$$

---

## Zapis macierzowy układu

Macierz współczynników:

$$
A =
\begin{bmatrix}
4 & -2 & 0 & 0 \
-2 & 5 & -1 & 0 \
0 & -1 & 4 & 2 \
0 & 0 & 2 & 3
\end{bmatrix}
$$

Wektor prawej strony:

$$
b =
\begin{bmatrix}
0 \
2 \
3 \
-2
\end{bmatrix}
$$

Dokładne rozwiązanie tego układu jest równe:

$$
x^* =
\begin{bmatrix}
0.5 \
1 \
2 \
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