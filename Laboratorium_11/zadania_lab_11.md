# Całkowanie numeryczne

## Treść zadań

**Zadanie 1.** Zaimplementuj całkowanie numeryczne za pomocą metody prostokątów.

**Zadanie 2.** Zaimplementuj całkowanie numeryczne za pomocą metody trapezów.

**Zadanie 3.** Zaimplementuj całkowanie numeryczne za pomocą metody Simpsona.

**Zadanie 4.** Wyniki powyższych programów przetestuj dla następujących całek:

a)

$$
\int_0^1 x^2\,dx
$$

b)

$$
\int_0^{\frac{\pi}{2}}\cos x\,dx
$$

c)

$$
\int_e^{e^2}\frac{1}{x}\,dx
$$

**Zadanie 5.** Sprawdź dokładność otrzymanych rozwiązań.

---

# Wprowadzenie

Całkowanie numeryczne służy do przybliżonego obliczania wartości całek oznaczonych.

Całka oznaczona:

$$
\int_a^b f(x)\,dx
$$

oznacza pole pod wykresem funkcji $f(x)$ na przedziale $[a,b]$.

Na tablicy zapisano ogólną postać całkowania numerycznego:

$$
\int_a^b f(x)\,dx \approx \sum A_i f(x_i)
$$

Oznacza to, że całkę przybliżamy za pomocą sumy wartości funkcji $f(x_i)$, pomnożonych przez odpowiednie współczynniki $A_i$.

W zadaniu używamy trzech metod:

- metody prostokątów,
- metody trapezów,
- metody Simpsona.

Każda z tych metod polega na podzieleniu przedziału całkowania $[a,b]$ na mniejsze części.

Liczbę podprzedziałów oznaczamy jako:

$$
N
$$

Krok całkowania wynosi:

$$
h=\frac{b-a}{N}
$$

Punkty podziału przedziału obliczamy zgodnie ze wzorem z tablicy:

$$
x_i=a+\frac{b-a}{N}i
$$

czyli równoważnie:

$$
x_i=a+ih
$$

Im większa liczba $N$, tym mniejszy krok $h$, a wynik zwykle jest dokładniejszy.

---

# Zadanie 1 — metoda prostokątów

## Wzór dla jednego przedziału

Na tablicy dla metody prostokątów zapisano wzór:

$$
I \approx (b-a)f(a)
$$

Jest to najprostsza wersja metody prostokątów, w której pole pod wykresem przybliżamy jednym prostokątem o szerokości $b-a$ i wysokości $f(a)$.

Na tablicy dopisano też uwagę, że lepsze przybliżenie daje wartość funkcji w środku przedziału:

$$
f\left(\frac{a+b}{2}\right)
$$

Dlatego w programie zastosowano **metodę prostokątów środkowych**.

## Wzór dla $N$ części

Dla wielu podprzedziałów podstawowa metoda prostokątów ma postać:

$$
I \approx \frac{b-a}{N}\sum_{i=0}^{N-1} f(x_i)
$$

gdzie:

$$
x_i=a+\frac{b-a}{N}i
$$

W programie użyto wersji środkowej, dlatego zamiast punktu $x_i$ bierzemy środek każdego podprzedziału:

$$
x_i+\frac{h}{2}
$$

czyli:

$$
x_i+\frac{b-a}{2N}
$$

Wzór użyty w programie ma więc postać:

$$
I \approx h\sum_{i=0}^{N-1} f\left(x_i+\frac{h}{2}\right)
$$

albo po podstawieniu $h=\frac{b-a}{N}$:

$$
I \approx \frac{b-a}{N}
\sum_{i=0}^{N-1}
f\left(a+\left(i+\frac12\right)\frac{b-a}{N}\right)
$$

Ta wersja jest zgodna z uwagą z tablicy, że środek przedziału daje lepsze przybliżenie.

---

# Zadanie 2 — metoda trapezów

## Wzór dla jednego przedziału

Na tablicy dla metody trapezów zapisano wzór:

$$
I \approx \frac{b-a}{2}\left(f(a)+f(b)\right)
$$

Oznacza to, że pole pod wykresem przybliżamy trapezem.

W metodzie trapezów bierzemy wartości funkcji na obu końcach przedziału, czyli $f(a)$ i $f(b)$.

## Wzór dla $N$ części

Dla wielu podprzedziałów wzór ma postać:

$$
I \approx \frac{b-a}{2N}
\left(
f(a)+2\sum_{i=1}^{N-1}f(x_i)+f(b)
\right)
$$

gdzie:

$$
x_i=a+\frac{b-a}{N}i
$$

Ponieważ:

$$
h=\frac{b-a}{N}
$$

możemy zapisać ten wzór również tak:

$$
I \approx h\left(
\frac{f(a)+f(b)}{2}
+
\sum_{i=1}^{N-1}f(x_i)
\right)
$$

Właśnie ta równoważna postać została zastosowana w programie.

Wartości $f(a)$ i $f(b)$ są liczone z wagą $\frac12$, a punkty wewnętrzne z wagą $1$.

---

# Zadanie 3 — metoda Simpsona

## Wzór dla jednego przedziału

Na tablicy dla metody Simpsona zapisano wzór:

$$
I \approx \frac{b-a}{6}
\left(
f(a)+4f\left(\frac{a+b}{2}\right)+f(b)
\right)
$$

Metoda Simpsona przybliża pole pod wykresem za pomocą paraboli.

Wykorzystuje:

- wartość funkcji na początku przedziału,
- wartość funkcji w środku przedziału,
- wartość funkcji na końcu przedziału.

Środkowy punkt ma wagę $4$, dlatego metoda Simpsona często daje dokładniejsze wyniki niż metoda prostokątów i trapezów.

## Wzór dla wielu podprzedziałów

Dla wielu podprzedziałów metoda Simpsona wymaga, aby liczba podprzedziałów była parzysta.

W programie liczba podprzedziałów oznaczona jest jako $N$, a krok wynosi:

$$
h=\frac{b-a}{N}
$$

Wzór użyty w programie ma postać:

$$
I \approx \frac{h}{3}
\left[
f(a)+f(b)
+4\sum_{\substack{i=1 \\ i\ \text{nieparzyste}}}^{N-1} f(x_i)
+2\sum_{\substack{i=2 \\ i\ \text{parzyste}}}^{N-2} f(x_i)
\right]
$$

gdzie:

$$
x_i=a+ih
$$

W programie działa to tak:

- pierwszy punkt $f(a)$ ma wagę $1$,
- ostatni punkt $f(b)$ ma wagę $1$,
- punkty o indeksach nieparzystych mają wagę $4$,
- punkty o indeksach parzystych mają wagę $2$.

Jest to standardowa złożona metoda Simpsona, zgodna z ideą zapisaną na tablicy.

---

# Zadanie 4 — testowane całki

Program testuje wszystkie trzy metody dla trzech całek.

---

## Całka a)

$$
\int_0^1 x^2\,dx
$$

Funkcja:

$$
f(x)=x^2
$$

Przedział:

$$
[0,1]
$$

Wartość dokładna:

$$
\int x^2\,dx=\frac{x^3}{3}
$$

czyli:

$$
\int_0^1 x^2\,dx=\frac{1^3}{3}-\frac{0^3}{3}
$$

$$
\int_0^1 x^2\,dx=\frac13
$$

---

## Całka b)

$$
\int_0^{\frac{\pi}{2}}\cos x\,dx
$$

Funkcja:

$$
f(x)=\cos x
$$

Przedział:

$$
\left[0,\frac{\pi}{2}\right]
$$

Wartość dokładna:

$$
\int \cos x\,dx=\sin x
$$

czyli:

$$
\int_0^{\frac{\pi}{2}}\cos x\,dx=
\sin\frac{\pi}{2}-\sin 0
$$

$$
\int_0^{\frac{\pi}{2}}\cos x\,dx=1-0=1
$$

---

## Całka c)

$$
\int_e^{e^2}\frac{1}{x}\,dx
$$

Funkcja:

$$
f(x)=\frac{1}{x}
$$

Przedział:

$$
[e,e^2]
$$

Wartość dokładna:

$$
\int \frac{1}{x}\,dx=\ln x
$$

czyli:

$$
\int_e^{e^2}\frac{1}{x}\,dx=
\ln(e^2)-\ln(e)
$$

$$
\int_e^{e^2}\frac{1}{x}\,dx=2-1=1
$$

---

# Zadanie 5 — sprawdzenie dokładności

Aby sprawdzić dokładność metod, porównujemy wynik numeryczny z wartością dokładną.

## Błąd bezwzględny

Błąd bezwzględny liczymy ze wzoru:

$$
\Delta = |I_{\text{dokładne}}-I_{\text{przybliżone}}|
$$

gdzie:

- $I_{\text{dokładne}}$ — dokładna wartość całki,
- $I_{\text{przybliżone}}$ — wartość całki obliczona metodą numeryczną.

## Błąd względny

Błąd względny liczymy ze wzoru:

$$
\delta = \frac{|I_{\text{dokładne}}-I_{\text{przybliżone}}|}{|I_{\text{dokładne}}|}
$$

Błąd względny pokazuje, jak duży jest błąd w stosunku do wartości dokładnej.

---

# Kod programu

```python
import math  # importujemy moduł math, ponieważ potrzebujemy funkcji cos, liczby pi oraz liczby e

print("-------------------- CAŁKOWANIE NUMERYCZNE --------------------")  # wypisujemy główny nagłówek programu

def metoda_prostokatow(f, a, b, n):  # definiujemy funkcję liczącą całkę metodą prostokątów środkowych
    h = (b - a) / n  # obliczamy długość jednego podprzedziału, czyli h = (b-a)/N

    suma = 0.0  # tworzymy zmienną, w której będziemy sumować wartości funkcji

    for i in range(n):  # wykonujemy pętlę po wszystkich podprzedziałach od 0 do n-1
        x_srodek = a + (i + 0.5) * h  # obliczamy środek aktualnego podprzedziału, czyli x_i + h/2
        suma += f(x_srodek)  # dodajemy wartość funkcji w środku podprzedziału do sumy

    return h * suma  # mnożymy sumę przez h i zwracamy przybliżoną wartość całki


def metoda_trapezow(f, a, b, n):  # definiujemy funkcję liczącą całkę metodą trapezów
    h = (b - a) / n  # obliczamy długość jednego podprzedziału, czyli h = (b-a)/N

    suma = (f(a) + f(b)) / 2  # dodajemy wartości funkcji na końcach przedziału z wagą 1/2

    for i in range(1, n):  # przechodzimy po punktach wewnętrznych przedziału
        x = a + i * h  # obliczamy punkt x_i zgodnie ze wzorem x_i = a + ih
        suma += f(x)  # dodajemy wartość funkcji w punkcie x_i do sumy

    return h * suma  # mnożymy sumę przez h i zwracamy przybliżoną wartość całki


def metoda_simpsona(f, a, b, n):  # definiujemy funkcję liczącą całkę metodą Simpsona
    if n % 2 != 0:  # sprawdzamy, czy liczba podprzedziałów jest parzysta
        raise ValueError("W metodzie Simpsona liczba podprzedziałów n musi być parzysta.")  # zgłaszamy błąd, jeśli n jest nieparzyste

    h = (b - a) / n  # obliczamy długość jednego podprzedziału, czyli h = (b-a)/N

    suma = f(a) + f(b)  # pierwszy i ostatni punkt mają wagę 1

    for i in range(1, n):  # przechodzimy po punktach wewnętrznych przedziału
        x = a + i * h  # obliczamy punkt x_i

        if i % 2 == 0:  # sprawdzamy, czy indeks punktu jest parzysty
            suma += 2 * f(x)  # punkty parzyste mają wagę 2
        else:  # jeśli indeks nie jest parzysty, to jest nieparzysty
            suma += 4 * f(x)  # punkty nieparzyste mają wagę 4

    return (h / 3) * suma  # mnożymy sumę przez h/3 i zwracamy przybliżoną wartość całki


def blad_bezwzgledny(wartosc_dokladna, wartosc_przyblizona):  # definiujemy funkcję liczącą błąd bezwzględny
    return abs(wartosc_dokladna - wartosc_przyblizona)  # zwracamy wartość bezwzględną różnicy wyniku dokładnego i przybliżonego


def blad_wzgledny(wartosc_dokladna, wartosc_przyblizona):  # definiujemy funkcję liczącą błąd względny
    if wartosc_dokladna == 0:  # sprawdzamy, czy wartość dokładna nie jest zerem
        raise ValueError("Nie można policzyć błędu względnego, gdy wartość dokładna jest równa 0.")  # zabezpieczamy się przed dzieleniem przez zero

    return abs(wartosc_dokladna - wartosc_przyblizona) / abs(wartosc_dokladna)  # zwracamy błąd względny


def f1(x):  # definiujemy funkcję z całki a)
    return x**2  # zwracamy wartość funkcji f(x)=x^2


def f2(x):  # definiujemy funkcję z całki b)
    return math.cos(x)  # zwracamy wartość funkcji f(x)=cos(x)


def f3(x):  # definiujemy funkcję z całki c)
    return 1 / x  # zwracamy wartość funkcji f(x)=1/x


def testuj_calke(nazwa, f, a, b, wartosc_dokladna, n):  # definiujemy funkcję testującą wszystkie metody dla jednej całki
    print("\n" + nazwa)  # wypisujemy nazwę aktualnie badanej całki
    print("Przedział całkowania:", "[", a, ",", b, "]")  # wypisujemy przedział całkowania
    print("Liczba podprzedziałów n =", n)  # wypisujemy liczbę podprzedziałów
    print("Wartość dokładna =", wartosc_dokladna)  # wypisujemy dokładną wartość całki

    wynik_prostokaty = metoda_prostokatow(f, a, b, n)  # obliczamy całkę metodą prostokątów środkowych
    wynik_trapezy = metoda_trapezow(f, a, b, n)  # obliczamy całkę metodą trapezów
    wynik_simpson = metoda_simpsona(f, a, b, n)  # obliczamy całkę metodą Simpsona

    print("\nMetoda prostokątów:")  # wypisujemy nagłówek dla metody prostokątów
    print("Wynik =", wynik_prostokaty)  # wypisujemy wynik metody prostokątów
    print("Błąd bezwzględny =", blad_bezwzgledny(wartosc_dokladna, wynik_prostokaty))  # wypisujemy błąd bezwzględny metody prostokątów
    print("Błąd względny =", blad_wzgledny(wartosc_dokladna, wynik_prostokaty))  # wypisujemy błąd względny metody prostokątów

    print("\nMetoda trapezów:")  # wypisujemy nagłówek dla metody trapezów
    print("Wynik =", wynik_trapezy)  # wypisujemy wynik metody trapezów
    print("Błąd bezwzględny =", blad_bezwzgledny(wartosc_dokladna, wynik_trapezy))  # wypisujemy błąd bezwzględny metody trapezów
    print("Błąd względny =", blad_wzgledny(wartosc_dokladna, wynik_trapezy))  # wypisujemy błąd względny metody trapezów

    print("\nMetoda Simpsona:")  # wypisujemy nagłówek dla metody Simpsona
    print("Wynik =", wynik_simpson)  # wypisujemy wynik metody Simpsona
    print("Błąd bezwzględny =", blad_bezwzgledny(wartosc_dokladna, wynik_simpson))  # wypisujemy błąd bezwzględny metody Simpsona
    print("Błąd względny =", blad_wzgledny(wartosc_dokladna, wynik_simpson))  # wypisujemy błąd względny metody Simpsona


n = 100  # ustalamy liczbę podprzedziałów; jest parzysta, więc metoda Simpsona może działać

testuj_calke(  # uruchamiamy test dla całki a)
    "a) całka od 0 do 1 z x^2 dx",  # nazwa całki
    f1,  # funkcja podcałkowa
    0,  # dolna granica całkowania
    1,  # górna granica całkowania
    1 / 3,  # dokładna wartość całki
    n  # liczba podprzedziałów
)

testuj_calke(  # uruchamiamy test dla całki b)
    "b) całka od 0 do pi/2 z cos(x) dx",  # nazwa całki
    f2,  # funkcja podcałkowa
    0,  # dolna granica całkowania
    math.pi / 2,  # górna granica całkowania
    1,  # dokładna wartość całki
    n  # liczba podprzedziałów
)

testuj_calke(  # uruchamiamy test dla całki c)
    "c) całka od e do e^2 z 1/x dx",  # nazwa całki
    f3,  # funkcja podcałkowa
    math.e,  # dolna granica całkowania
    math.e**2,  # górna granica całkowania
    1,  # dokładna wartość całki
    n  # liczba podprzedziałów
)