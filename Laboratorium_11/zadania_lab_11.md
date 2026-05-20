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

Oznacza to, że dokładną wartość całki zastępujemy sumą wartości funkcji w wybranych punktach $x_i$, pomnożonych przez odpowiednie współczynniki $A_i$.

W zadaniu wykorzystujemy trzy metody:

- metodę prostokątów,
- metodę trapezów,
- metodę Simpsona.

Każda z metod polega na podzieleniu przedziału całkowania $[a,b]$ na mniejsze części.

Liczbę podprzedziałów oznaczamy jako:

$$
N
$$

W kodzie ta sama liczba jest zapisana jako zmienna:

```python
n
```

Krok całkowania, czyli długość jednego podprzedziału, wynosi:

$$
h=\frac{b-a}{N}
$$

Punkty podziału przedziału obliczamy ze wzoru:

$$
x_i=a+\frac{b-a}{N}i
$$

czyli równoważnie:

$$
x_i=a+ih
$$

Im większa liczba podprzedziałów $N$, tym mniejszy krok $h$, a wynik zwykle jest dokładniejszy.

---

# Zadanie 1 — metoda prostokątów

## Idea metody prostokątów

Metoda prostokątów polega na przybliżeniu pola pod wykresem funkcji za pomocą prostokątów.

Na pojedynczym podprzedziale $[x_i,x_{i+1}]$ funkcję $f(x)$ zastępujemy wartością stałą $y_i$. Oznacza to, że zamiast dokładnego pola pod wykresem liczymy pole prostokąta.

Dla jednego podprzedziału mamy:

$$
\sigma_i=\int_{x_i}^{x_{i+1}} f(x)\,dx
$$

Przybliżamy tę wartość przez:

$$
\sigma_i \approx \int_{x_i}^{x_{i+1}} y_i\,dx
$$

Ponieważ $y_i$ jest stałe, otrzymujemy:

$$
\sigma_i \approx y_i(x_{i+1}-x_i)
$$

Dla równoodległych punktów:

$$
x_{i+1}-x_i=h
$$

więc:

$$
\sigma_i \approx y_i h
$$

Po zsumowaniu wszystkich prostokątów otrzymujemy:

$$
\int_a^b f(x)\,dx \approx h\sum_{i=0}^{N-1}y_i
$$

## Metoda prostokątów środkowych

Na slajdach zaznaczono, że dla węzłów równoodległych często przyjmuje się:

$$
y_i=f\left(x_i+\frac{h}{2}\right)
$$

czyli wartość funkcji w środku podprzedziału.

Dlatego w programie zastosowano **metodę prostokątów środkowych**.

Dla tej metody:

$$
x_{\text{środek}}=x_i+\frac{h}{2}
$$

czyli:

$$
x_{\text{środek}}=a+\left(i+\frac12\right)h
$$

Wzór użyty w programie ma postać:

$$
\int_a^b f(x)\,dx \approx h\sum_{i=0}^{N-1} f\left(a+\left(i+\frac12\right)h\right)
$$

Po podstawieniu:

$$
h=\frac{b-a}{N}
$$

można zapisać:

$$
\int_a^b f(x)\,dx \approx
\frac{b-a}{N}
\sum_{i=0}^{N-1}
f\left(a+\left(i+\frac12\right)\frac{b-a}{N}\right)
$$

Ta wersja jest zgodna z metodą prostokątów ze slajdów, ponieważ przyjmuje wysokość prostokąta jako wartość funkcji w środku podprzedziału.

---

# Zadanie 2 — metoda trapezów

## Idea metody trapezów

Metoda trapezów polega na tym, że na każdym podprzedziale funkcję zastępujemy prostą przechodzącą przez dwa punkty:

$$
(x_i,f(x_i))
$$

oraz:

$$
(x_{i+1},f(x_{i+1}))
$$

Wtedy pole pod wykresem na danym podprzedziale przybliżamy polem trapezu.

Dla jednego podprzedziału pole trapezu wynosi:

$$
\sigma_i=\frac12 h(y_i+y_{i+1})
$$

gdzie:

$$
y_i=f(x_i)
$$

oraz:

$$
y_{i+1}=f(x_{i+1})
$$

Po zsumowaniu pól trapezów dla całego przedziału $[a,b]$ otrzymujemy wzór:

$$
\int_a^b f(x)\,dx
\approx
\frac12 h\sum_{i=0}^{N-1}(y_{i+1}+y_i)
$$

Po uporządkowaniu składników dostajemy:

$$
\int_a^b f(x)\,dx
\approx
h\left[
\frac12(y_0+y_N)+\sum_{i=1}^{N-1}y_i
\right]
$$

Ponieważ:

$$
y_i=f(x_i)
$$

możemy zapisać:

$$
\int_a^b f(x)\,dx
\approx
h\left[
\frac{f(a)+f(b)}{2}
+
\sum_{i=1}^{N-1}f(x_i)
\right]
$$

gdzie:

$$
x_i=a+ih
$$

oraz:

$$
h=\frac{b-a}{N}
$$

Jest to dokładnie wzór zastosowany w programie.

## Dokładność metody trapezów

Metoda trapezów jest dokładna, jeżeli funkcja $f$ jest wielomianem stopnia co najwyżej pierwszego, czyli funkcją liniową.

Dla innych funkcji pojawia się błąd przybliżenia, ponieważ wykres funkcji nie zawsze jest idealnie prostą linią na każdym podprzedziale.

---

# Zadanie 3 — metoda Simpsona

## Idea metody Simpsona

Metoda Simpsona jest dokładniejszą metodą całkowania numerycznego niż metoda prostokątów i metoda trapezów.

W metodzie tej pole pod wykresem przybliżamy za pomocą fragmentów paraboli.

Dla jednego przedziału wzór Simpsona ma postać:

$$
I \approx \frac{b-a}{6}
\left(
f(a)+4f\left(\frac{a+b}{2}\right)+f(b)
\right)
$$

Widzimy, że metoda wykorzystuje trzy wartości funkcji:

- wartość na początku przedziału,
- wartość w środku przedziału,
- wartość na końcu przedziału.

Środkowy punkt ma wagę $4$, dlatego ma większy wpływ na wynik.

---

## Złożona metoda Simpsona

Dla wielu podprzedziałów stosujemy złożoną metodę Simpsona.

Liczba podprzedziałów $N$ musi być parzysta.

Krok wynosi:

$$
h=\frac{b-a}{N}
$$

Punkty podziału:

$$
x_i=a+ih
$$

dla:

$$
i=0,1,\dots,N
$$

Wzór ze slajdu ma postać:

$$
S_N=
\frac{h}{3}
\left[
f(x_0)
+
4\left(f(x_1)+f(x_3)+\dots+f(x_{N-1})\right)
+
2\left(f(x_2)+f(x_4)+\dots+f(x_{N-2})\right)
+
f(x_N)
\right]
$$

Można go też zapisać w formie sum:

$$
S_N=
\frac{h}{3}
\left[
f(a)+f(b)
+4\sum_{\substack{i=1 \\ i\ \text{nieparzyste}}}^{N-1} f(x_i)
+2\sum_{\substack{i=2 \\ i\ \text{parzyste}}}^{N-2} f(x_i)
\right]
$$

W programie działa to tak:

- pierwszy punkt $f(a)$ ma wagę $1$,
- ostatni punkt $f(b)$ ma wagę $1$,
- punkty o indeksach nieparzystych mają wagę $4$,
- punkty o indeksach parzystych mają wagę $2$.

Metoda Simpsona jest dokładna dla wielomianów stopnia co najwyżej trzeciego.

---

## Błąd metody Simpsona

Na slajdach podano, że błąd przybliżenia w metodzie Simpsona zależy od czwartej pochodnej funkcji.

Ma postać:

$$
\varepsilon=
\left|f^{(4)}(\xi)\right|
\frac{(b-a)h^4}{180}
$$

gdzie:

- $f^{(4)}(\xi)$ oznacza czwartą pochodną funkcji w pewnym punkcie $\xi\in(a,b)$,
- $h=\frac{b-a}{N}$.

Oznacza to, że dla mniejszego kroku $h$ metoda Simpsona bardzo szybko zwiększa dokładność.

---

# Zadanie 4 — testowane całki

Program testuje wszystkie trzy metody dla trzech całek.

---

## Całka a)

$$
\int_0^1 x^2\,dx
$$

Funkcja podcałkowa:

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
\int_0^1 x^2\,dx=
\frac{1^3}{3}-\frac{0^3}{3}
$$

$$
\int_0^1 x^2\,dx=\frac13
$$

---

## Całka b)

$$
\int_0^{\frac{\pi}{2}}\cos x\,dx
$$

Funkcja podcałkowa:

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

Funkcja podcałkowa:

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

Aby sprawdzić dokładność otrzymanych rozwiązań, porównujemy wynik numeryczny z wartością dokładną.

## Błąd bezwzględny

Błąd bezwzględny liczymy ze wzoru:

$$
\Delta=
\left|I_{\text{dokładne}}-I_{\text{przybliżone}}\right|
$$

gdzie:

- $I_{\text{dokładne}}$ — dokładna wartość całki,
- $I_{\text{przybliżone}}$ — wartość całki obliczona metodą numeryczną.

## Błąd względny

Błąd względny liczymy ze wzoru:

$$
\delta=
\frac{
\left|I_{\text{dokładne}}-I_{\text{przybliżone}}\right|
}{
\left|I_{\text{dokładne}}\right|
}
$$

Błąd względny pokazuje, jak duży jest błąd w stosunku do wartości dokładnej.

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


n = 100  # ustalamy liczbę podprzedziałów; w teorii oznaczamy ją jako N; jest parzysta, więc metoda Simpsona może działać

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
```

# Wnioski

W programie zaimplementowano trzy metody całkowania numerycznego:

- metodę prostokątów środkowych,
- metodę trapezów,
- metodę Simpsona.

Metoda prostokątów środkowych przybliża pole pod wykresem za pomocą prostokątów o wysokości równej wartości funkcji w środku każdego podprzedziału.

Metoda trapezów przybliża funkcję na każdym podprzedziale odcinkiem prostej i oblicza pole trapezów.

Metoda Simpsona przybliża funkcję fragmentami paraboli i wykorzystuje wagi:

$$
1,\ 4,\ 2,\ 4,\ 2,\dots,\ 4,\ 1
$$

Wszystkie metody zostały przetestowane dla całek:

$$
\int_0^1 x^2\,dx
$$

$$
\int_0^{\frac{\pi}{2}}\cos x\,dx
$$

$$
\int_e^{e^2}\frac{1}{x}\,dx
$$

Dla każdej całki znana jest wartość dokładna, dlatego można było obliczyć błąd bezwzględny i względny.

Najprostszą metodą jest metoda prostokątów. Metoda trapezów jest zwykle dokładniejsza, ponieważ uwzględnia wartości funkcji na obu końcach podprzedziału. Metoda Simpsona zwykle daje najlepszą dokładność, ponieważ przybliża funkcję parabolą.

Zwiększenie liczby podprzedziałów $N$ powoduje zmniejszenie kroku:

$$
h=\frac{b-a}{N}
$$

a więc zwykle poprawia dokładność obliczeń.