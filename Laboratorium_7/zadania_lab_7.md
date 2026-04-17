**Zadanie 1. Napisz program implementujący metodę bisekcji. Program przetestuj dla
następujących funkcji:**

a)
$
f(x) = x^2 - 4, x \isin <0; 2.2>
$

b)
$
f(x) = \sin x - \frac{1}{2}, x \isin <0; 2.2>
$

## Co to jest metoda bisekcji?

Metoda bisekcji służy do wyznaczania miejsca zerowego funkcji w przedziale $[a,b]$, w którym funkcja zmienia znak.

Zakładamy więc, że:

$$
f(a)\cdot f(b)<0
$$

co oznacza, że w przedziale $[a,b]$ znajduje się co najmniej jedno miejsce zerowe.

Metoda polega na wielokrotnym dzieleniu przedziału na połowy i wybieraniu tej części, w której nadal występuje zmiana znaku.

## Obliczanie kolejnych przybliżeń

W prezentacji przyjęto, że:

- początkowo mamy dwa końce przedziału izolacji pierwiastka,
- dla kolejnych kroków iteracji $i=3,4,\dots$ nowe przybliżenie wyznaczamy jako średnią dwóch wybranych punktów.

Nową wartość obliczamy ze wzoru:

$$
x_i=\frac{x_{i-1}+x_k}{2}
$$

gdzie $k$ jest jedną z wartości $\{i-3, i-2\}$, a wybór $k$ jest taki, aby spełnione były warunki:

$$
|x_i-x_{i-1}|=|x_i-x_k|
$$

oraz

$$
f(x_{i-1})\cdot f(x_k)<0
$$

co wskazuje na obecność pierwiastka w tym przedziale.

W praktyce oznacza to, że w każdym kroku bierzemy **punkt środkowy aktualnego przedziału**:

$$
x_i=\frac{a+b}{2}
$$

albo równoważnie, zgodnie z praktyczną uwagą ze slajdów:

$$
x_i=a+\frac{b-a}{2}
$$

Ten drugi zapis jest wygodniejszy numerycznie.

## Jak działa metoda krok po kroku?

1. Wybieramy przedział $[a,b]$, w którym funkcja zmienia znak.
2. Obliczamy punkt środkowy:
   $$
   x=\frac{a+b}{2}
   $$
3. Sprawdzamy znak funkcji w punkcie środkowym.
4. Jeśli znak funkcji w $a$ i w $x$ jest różny, to nowym przedziałem jest $[a,x]$.
5. W przeciwnym razie nowym przedziałem jest $[x,b]$.
6. Powtarzamy kroki aż do spełnienia wybranego warunku stopu.

W każdej iteracji przedział izolacji pierwiastka zmniejsza się o połowę, więc z każdym krokiem przybliżenie staje się dokładniejsze.

## Kryteria zakończenia iteracji

W prezentacji podano trzy możliwe kryteria zakończenia obliczeń metodą bisekcji:

### 1. Zadana liczba kroków — iteracji

Program kończy działanie po wykonaniu określonej liczby iteracji.

### 2. Dostatecznie mały błąd

Program kończy działanie, gdy oszacowanie błędu przybliżenia jest wystarczająco małe.

Na slajdzie błąd zapisano jako:

$$
|x_i-x^*|<\frac{b-a}{2^{i-2}}
$$

co pokazuje, że wraz z kolejnymi iteracjami przybliżenie jest coraz dokładniejsze.

### 3. Wartość funkcji dostatecznie bliska zeru

Program kończy działanie, gdy:

$$
|f(x_i)|<\varepsilon
$$

czyli gdy wartość funkcji w aktualnym punkcie jest już bardzo bliska zeru.

## Wyznaczanie błędu metody bisekcji

Na slajdach dokładność przybliżenia w $i$-tym kroku określono wzorem:

$$
|x_i-x^*|<\frac{b-a}{2^{i-2}}
$$

Oznacza to, że błąd maleje wraz z liczbą iteracji.

Na przykład po 12 krokach:

$$
|x_{12}-x^*|<\frac{b-a}{2^{12-2}}
$$

## Praktyczne uwagi

W prezentacji podano też kilka praktycznych wskazówek:

- metoda bisekcji daje **jedno miejsce zerowe**, a nie wszystkie miejsca zerowe w całym przedziale,
- przez błędy zaokrągleń otrzymanie dokładnie \(f(x)=0\) jest mało prawdopodobne, więc nie powinno to być jedyne kryterium zakończenia,
- punkt środkowy lepiej liczyć ze wzoru
  $$
  a+\frac{b-a}{2}
  $$
  niż
  $$
  \frac{a+b}{2}
  $$
- zmianę znaku wygodnie sprawdzać przez porównanie znaków:
  $$
  sgn(f(x_i)) \ne sgn(f(x_j))
  $$
  zamiast przez mnożenie:
  $$
  f(x_i)\cdot f(x_j)<0
  $$

## Program

```python
import math  # importujemy moduł math, ponieważ będzie potrzebny do funkcji sin

def sgn(x):  # definiujemy funkcję zwracającą znak liczby
    if x > 0:  # sprawdzamy, czy liczba jest dodatnia
        return 1  # jeśli tak, zwracamy 1
    elif x < 0:  # sprawdzamy, czy liczba jest ujemna
        return -1  # jeśli tak, zwracamy -1
    else:  # w przeciwnym razie liczba jest równa zero
        return 0  # zwracamy 0

def bisekcja(f, a, b, max_iter=100, epsilon=1e-3, warunek_stopu="iteracje"):  # definiujemy funkcję realizującą metodę bisekcji
    if f(b) * f(a) > 0:  # sprawdzamy, czy na końcach przedziału nie ma takiego samego znaku
        raise ValueError("Na krańcach przedziału funkcja musi mieć przeciwne znaki.")  # jeśli znak się nie zmienia, zgłaszamy błąd

    a0 = a  # zapamiętujemy początkowy lewy koniec przedziału do wzoru na błąd
    b0 = b  # zapamiętujemy początkowy prawy koniec przedziału do wzoru na błąd
    historia = []  # tworzymy pustą listę, w której będziemy zapisywać kolejne kroki metody

    x1 = a  # zgodnie z numeracją ze slajdów przyjmujemy pierwszy punkt jako lewy koniec przedziału
    x2 = b  # zgodnie z numeracją ze slajdów przyjmujemy drugi punkt jako prawy koniec przedziału

    historia.append([1, a, b, x1, f(x1), None])  # zapisujemy do historii krok 1
    historia.append([2, a, b, x2, f(x2), None])  # zapisujemy do historii krok 2

    if warunek_stopu == "iteracje" and max_iter == 1:  # sprawdzamy, czy użytkownik chce zakończyć po pierwszym kroku
        return x1, historia  # zwracamy pierwszy punkt i historię
    if warunek_stopu == "iteracje" and max_iter == 2:  # sprawdzamy, czy użytkownik chce zakończyć po drugim kroku
        return x2, historia  # zwracamy drugi punkt i historię

    for i in range(3, max_iter + 1):  # wykonujemy kolejne kroki od i=3 zgodnie z numeracją ze slajdów
        miejsce_zerowe = a + ((b - a) / 2.0)  # obliczamy punkt środkowy przedziału w postaci zalecanej na slajdach

        fa = f(a)  # obliczamy wartość funkcji w lewym końcu przedziału
        fc = f(miejsce_zerowe)  # obliczamy wartość funkcji w punkcie środkowym

        blad = (b0 - a0) / (2 ** (i - 2))  # obliczamy oszacowanie błędu dokładnie według wzoru ze slajdu

        historia.append([i, a, b, miejsce_zerowe, fc, blad])  # zapisujemy aktualny krok do historii

        if warunek_stopu == "iteracje":  # sprawdzamy, czy wybrano warunek stopu oparty na liczbie iteracji
            if i == max_iter:  # jeśli osiągnięto zadaną liczbę iteracji
                return miejsce_zerowe, historia  # zwracamy aktualne przybliżenie i historię

        elif warunek_stopu == "blad":  # sprawdzamy, czy wybrano warunek stopu oparty na błędzie
            if blad < epsilon:  # jeśli oszacowanie błędu jest mniejsze od zadanej tolerancji
                return miejsce_zerowe, historia  # zwracamy aktualne przybliżenie i historię

        elif warunek_stopu == "wartosc":  # sprawdzamy, czy wybrano warunek stopu oparty na wartości funkcji
            if abs(fc) < epsilon:  # jeśli wartość funkcji jest dostatecznie bliska zeru
                return miejsce_zerowe, historia  # zwracamy aktualne przybliżenie i historię

        else:  # jeśli podano niepoprawny napis określający warunek stopu
            raise ValueError("Niepoprawny warunek stopu.")  # zgłaszamy błąd

        if fc == 0:  # sprawdzamy, czy udało się trafić dokładnie w miejsce zerowe
            return miejsce_zerowe, historia  # jeśli tak, od razu kończymy działanie

        if sgn(fa) != sgn(fc):  # sprawdzamy zgodnie ze slajdem, czy między a i punktem środkowym następuje zmiana znaku
            b = miejsce_zerowe  # jeśli tak, nowym prawym końcem przedziału staje się punkt środkowy
        else:  # w przeciwnym razie pierwiastek znajduje się w drugiej połowie przedziału
            a = miejsce_zerowe  # nowym lewym końcem przedziału staje się punkt środkowy

    return miejsce_zerowe, historia  # jeśli pętla się zakończy, zwracamy ostatnie przybliżenie i historię

def wypisz_historie(historia):  # definiujemy funkcję wypisującą historię działania metody
    print("i         a           b           x          f(x)        blad")  # wypisujemy nagłówek tabeli
    for krok in historia:  # przechodzimy po wszystkich zapisanych krokach
        print(  # wypisujemy pojedynczy wiersz historii
            f"{krok[0]} "  # wypisujemy numer iteracji
            f"{krok[1]} "  # wypisujemy lewy koniec przedziału
            f"{krok[2]} "  # wypisujemy prawy koniec przedziału
            f"{krok[3]} "  # wypisujemy aktualne przybliżenie
            f"{krok[4]} "  # wypisujemy wartość funkcji w punkcie przybliżonym
            f"{krok[5]}"  # wypisujemy oszacowanie błędu
        )  # kończymy wypisywanie jednego wiersza

def f1(x):  # definiujemy pierwszą funkcję testową
    return x**2 - 4  # zwracamy wartość funkcji x^2 - 4

def f2(x):  # definiujemy drugą funkcję testową
    return math.sin(x) - 0.5  # zwracamy wartość funkcji sin(x) - 1/2

print("-------------------- ZADANIE 1 --------------------")  # wypisujemy nagłówek zadania

print("\n==================== FUNKCJA a) ====================")  # wypisujemy nagłówek dla funkcji a)
print("f(x) = x^2 - 4, przedział [0, 2.2]")  # wypisujemy opis funkcji i przedziału

wynik_a_iter, historia_a_iter = bisekcja(f1, 0.0, 2.2, max_iter=12, warunek_stopu="iteracje")  # uruchamiamy metodę bisekcji dla funkcji a) z warunkiem liczby iteracji
print("\nWarunek stopu: liczba iteracji")  # wypisujemy nazwę wybranego warunku stopu
wypisz_historie(historia_a_iter)  # wypisujemy pełną historię iteracji
print("Przybliżony pierwiastek:", wynik_a_iter)  # wypisujemy wyznaczone przybliżenie miejsca zerowego
print("f(x) =", f1(wynik_a_iter))  # wypisujemy wartość funkcji w znalezionym punkcie

wynik_a_blad, historia_a_blad = bisekcja(f1, 0.0, 2.2, epsilon=1e-3, warunek_stopu="blad")  # uruchamiamy metodę bisekcji dla funkcji a) z warunkiem małego błędu
print("\nWarunek stopu: dostatecznie mały błąd")  # wypisujemy nazwę wybranego warunku stopu
print("Przybliżony pierwiastek:", wynik_a_blad)  # wypisujemy wyznaczone przybliżenie miejsca zerowego
print("f(x) =", f1(wynik_a_blad))  # wypisujemy wartość funkcji w znalezionym punkcie
print("Liczba iteracji:", len(historia_a_blad))  # wypisujemy liczbę zapisanych kroków

wynik_a_wartosc, historia_a_wartosc = bisekcja(f1, 0.0, 2.2, epsilon=1e-3, warunek_stopu="wartosc")  # uruchamiamy metodę bisekcji dla funkcji a) z warunkiem małej wartości funkcji
print("\nWarunek stopu: wartość funkcji bliska zeru")  # wypisujemy nazwę wybranego warunku stopu
print("Przybliżony pierwiastek:", wynik_a_wartosc)  # wypisujemy wyznaczone przybliżenie miejsca zerowego
print("f(x) =", f1(wynik_a_wartosc))  # wypisujemy wartość funkcji w znalezionym punkcie
print("Liczba iteracji:", len(historia_a_wartosc))  # wypisujemy liczbę zapisanych kroków

print("\n==================== FUNKCJA b) ====================")  # wypisujemy nagłówek dla funkcji b)
print("f(x) = sin(x) - 1/2, przedział [0, 2.2]")  # wypisujemy opis funkcji i przedziału

wynik_b_iter, historia_b_iter = bisekcja(f2, 0.0, 2.2, max_iter=12, warunek_stopu="iteracje")  # uruchamiamy metodę bisekcji dla funkcji b) z warunkiem liczby iteracji
print("\nWarunek stopu: liczba iteracji")  # wypisujemy nazwę wybranego warunku stopu
wypisz_historie(historia_b_iter)  # wypisujemy pełną historię iteracji
print("Przybliżony pierwiastek:", wynik_b_iter)  # wypisujemy wyznaczone przybliżenie miejsca zerowego
print("f(x) =", f2(wynik_b_iter))  # wypisujemy wartość funkcji w znalezionym punkcie

wynik_b_blad, historia_b_blad = bisekcja(f2, 0.0, 2.2, epsilon=1e-3, warunek_stopu="blad")  # uruchamiamy metodę bisekcji dla funkcji b) z warunkiem małego błędu
print("\nWarunek stopu: dostatecznie mały błąd")  # wypisujemy nazwę wybranego warunku stopu
print("Przybliżony pierwiastek:", wynik_b_blad)  # wypisujemy wyznaczone przybliżenie miejsca zerowego
print("f(x) =", f2(wynik_b_blad))  # wypisujemy wartość funkcji w znalezionym punkcie
print("Liczba iteracji:", len(historia_b_blad))  # wypisujemy liczbę zapisanych kroków

wynik_b_wartosc, historia_b_wartosc = bisekcja(f2, 0.0, 2.2, epsilon=1e-3, warunek_stopu="wartosc")  # uruchamiamy metodę bisekcji dla funkcji b) z warunkiem małej wartości funkcji
print("\nWarunek stopu: wartość funkcji bliska zeru")  # wypisujemy nazwę wybranego warunku stopu
print("Przybliżony pierwiastek:", wynik_b_wartosc)  # wypisujemy wyznaczone przybliżenie miejsca zerowego
print("f(x) =", f2(wynik_b_wartosc))  # wypisujemy wartość funkcji w znalezionym punkcie
print("Liczba iteracji:", len(historia_b_wartosc))  # wypisujemy liczbę zapisanych kroków
```

---

## Wnioski

Metoda bisekcji polega na wielokrotnym dzieleniu przedziału na połowy i wybieraniu tej części, w której funkcja zmienia znak. Dzięki temu kolejne przybliżenia coraz bardziej zbliżają się do miejsca zerowego.

W programie zastosowano trzy warunki zakończenia obliczeń zgodne ze slajdami:

- zadana liczba iteracji,
- dostatecznie mały błąd,
- wartość funkcji dostatecznie bliska zeru.

Dla funkcji:

$$
f(x)=x^2-4
$$

w przedziale $[0,2.2]$ metoda prowadzi do pierwiastka bliskiego wartości:

$$
x=2
$$

Dla funkcji:

$$
f(x)=\sin x-\frac12
$$

w przedziale $[0,2.2]$ metoda prowadzi do pierwiastka bliskiego wartości:

$$
x\approx 0.5236
$$

czyli do wartości:

$$
x=\frac{\pi}{6}
$$

---

**Zadanie 2. Napisz program implementujący metodę Newtona (czyli metodę stycznych). Program przetestuj dla funkcji z zadania 1.**

---

**Zadanie 3. Napisz program impelemntujący metodę siecznych. Program przetestuj dla funkcji z zadania 1.**