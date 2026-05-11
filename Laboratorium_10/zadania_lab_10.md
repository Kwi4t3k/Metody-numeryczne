# Zadanie 1

**Napisz program implementujący różniczkowanie numeryczne za pomocą metody Newtona dla następujących funkcji:**

a)

$
f(x)=2x^2+2
$

b)

$
f(x)=2x^4-x^2+3x-7
$

c)

$
f(x)=x^2e^x
$

Oblicz błąd względny otrzymanego rozwiązania dla:

$
h=10^{-2}
$

oraz

$
h=10^{-4}
$

W programie pochodną liczymy w punkcie:

$$
x=1
$$

## Co to jest różniczkowanie numeryczne?

Różniczkowanie numeryczne to metoda przybliżonego obliczania pochodnych funkcji na podstawie wartości tej funkcji w wybranych punktach.

Stosujemy je wtedy, gdy:

- trudno jest policzyć pochodną analitycznie,
- funkcja jest dana tylko przez wartości w punktach,
- chcemy szybko przybliżyć wartość pochodnej.

Różnice skończone można wyprowadzić z ilorazu różnicowego albo z rozwinięcia Taylora.

## Metoda Newtona — różnica w przód

W tym zadaniu mamy użyć metody Newtona, czyli **dwupunktowej różnicy w przód**.

Wzór ze slajdu:

$$
f'(x)\approx \frac{f(x+h)-f(x)}{h}, \space \space \space O(h)
$$

gdzie:

- $x$ — punkt, w którym liczymy pochodną,
- $h$ — mały krok,
- $f(x+h)$ — wartość funkcji w punkcie przesuniętym o $h$ w prawo,
- $f(x)$ — wartość funkcji w punkcie $x$.

Metoda nazywa się „w przód”, ponieważ korzysta z punktów:

$$
x
$$

oraz

$$
x+h
$$

czyli patrzy w prawą stronę od punktu $x$.

## Błąd względny

Na slajdzie błąd względny zapisano jako:

$$
\delta x=\frac{|x-\overline{x}|}{|x|}
$$

W tym zadaniu nie porównujemy zwykłych liczb, tylko wartości pochodnych.

Dlatego przyjmujemy:

$$
x=f'_{\text{dokładna}}(x)
$$

oraz:

$$
\overline{x}=f'_{\text{przybliżona}}(x)
$$

Zatem błąd względny liczymy ze wzoru:

$$
\delta=
\frac{
\left|f'_{\text{dokładna}}(x)-f'_{\text{przybliżona}}(x)\right|
}{
\left|f'_{\text{dokładna}}(x)\right|
}
$$

## Pochodne dokładne funkcji

Aby policzyć błąd względny, musimy znać dokładne wartości pochodnych.

### Funkcja a)

$$
f(x)=2x^2+2
$$

Pochodna dokładna:

$$
f'(x)=4x
$$

### Funkcja b)

$$
f(x)=2x^4-x^2+3x-7
$$

Pochodna dokładna:

$$
f'(x)=8x^3-2x+3
$$

### Funkcja c)

$$
f(x)=x^2e^x
$$

Korzystamy z reguły iloczynu:

$$
(x^2e^x)'=(x^2)'e^x+x^2(e^x)'
$$

czyli:

$$
f'(x)=2xe^x+x^2e^x
$$

Po wyłączeniu $e^x$:

$$
f'(x)=e^x(x^2+2x)
$$

## Co robi program?

Program:

1. Definiuje funkcję do liczenia pochodnej metodą różnicy w przód.
2. Definiuje funkcję do liczenia błędu względnego.
3. Definiuje funkcje z zadania oraz ich pochodne dokładne.
4. Dla każdej funkcji liczy pochodną numeryczną dla:
   $$
   h=10^{-2}
   $$
   oraz:
   $$
   h=10^{-4}
   $$
5. Porównuje pochodną numeryczną z pochodną dokładną.
6. Wypisuje błąd względny.

## Kod

```python
import math  # importujemy moduł math, ponieważ potrzebujemy funkcji exp do obliczania e^x

print("------------------------ZADANIE 1--------------------------")  # wypisujemy nagłówek zadania

def roznica_w_przod(f, x, h):  # definiujemy funkcję liczącą pochodną metodą różnicy w przód
    return (f(x + h) - f(x)) / h  # zwracamy przybliżenie pochodnej ze wzoru: f'(x) ≈ (f(x+h)-f(x))/h

def blad_wzgledny(wartosc_dokladna, wartosc_przyblizona):  # definiujemy funkcję liczącą błąd względny
    if wartosc_dokladna != 0:  # sprawdzamy, czy wartość dokładna nie jest zerem, żeby nie dzielić przez zero
        return abs(wartosc_dokladna - wartosc_przyblizona) / abs(wartosc_dokladna)  # zwracamy błąd względny zgodnie ze wzorem ze slajdu
    else:  # obsługujemy przypadek, gdy wartość dokładna jest równa zero
        raise ValueError("Nie można policzyć błędu względnego, gdy wartość dokładna jest równa 0.")  # zgłaszamy błąd, ponieważ dzielenie przez zero jest niemożliwe

def f1(x):  # definiujemy pierwszą funkcję z zadania
    return 2 * x**2 + 2  # zwracamy wartość funkcji f(x)=2x^2+2

def df1(x):  # definiujemy dokładną pochodną pierwszej funkcji
    return 4 * x  # zwracamy wartość pochodnej f'(x)=4x

def f2(x):  # definiujemy drugą funkcję z zadania
    return 2 * x**4 - x**2 + 3*x - 7  # zwracamy wartość funkcji f(x)=2x^4-x^2+3x-7

def df2(x):  # definiujemy dokładną pochodną drugiej funkcji
    return 8 * x**3 - 2 * x + 3  # zwracamy wartość pochodnej f'(x)=8x^3-2x+3

def f3(x):  # definiujemy trzecią funkcję z zadania
    return x**2 * math.exp(x)  # zwracamy wartość funkcji f(x)=x^2e^x

def df3(x):  # definiujemy dokładną pochodną trzeciej funkcji
    return math.exp(x) * (x**2 + 2 * x)  # zwracamy wartość pochodnej f'(x)=e^x(x^2+2x)

def porownaj_pochodna(nazwa, f, df, x, h_lista):  # definiujemy funkcję porównującą pochodną numeryczną z dokładną
    print("\n" + nazwa)  # wypisujemy nazwę aktualnie badanej funkcji
    print("x =", x)  # wypisujemy punkt, w którym liczymy pochodną
    print("h              pochodna numeryczna        pochodna dokładna          błąd względny")  # wypisujemy nagłówek tabeli wyników

    for h in h_lista:  # przechodzimy po kolejnych wartościach kroku h
        pochodna_numeryczna = roznica_w_przod(f, x, h)  # liczymy pochodną numeryczną metodą różnicy w przód
        pochodna_dokladna = df(x)  # liczymy dokładną wartość pochodnej w punkcie x
        blad = blad_wzgledny(pochodna_dokladna, pochodna_numeryczna)  # liczymy błąd względny między wartością dokładną i przybliżoną

        print(f"{h:<14} {pochodna_numeryczna:<25} {pochodna_dokladna:<25} {blad}")  # wypisujemy jeden wiersz tabeli z wynikami

x0 = 1.0  # ustalamy punkt x, w którym obliczamy pochodną

h_lista = [10**(-2), 10**(-4)]  # tworzymy listę wartości h podanych w treści zadania

porownaj_pochodna("a) f(x) = 2x^2 + 2", f1, df1, x0, h_lista)  # wykonujemy obliczenia dla funkcji a)
porownaj_pochodna("b) f(x) = 2x^4 - x^2 + 3x - 7", f2, df2, x0, h_lista)  # wykonujemy obliczenia dla funkcji b)
porownaj_pochodna("c) f(x) = x^2e^x", f3, df3, x0, h_lista)  # wykonujemy obliczenia dla funkcji c)
```

## Wyniki

Dla funkcji:

$$
f(x)=2x^2+2
$$

w punkcie:

$$
x=1
$$

pochodna dokładna wynosi:

$$
f'(1)=4
$$

Dla $h=10^{-2}$ program otrzymuje wynik około:

$$
4.02
$$

a dla $h=10^{-4}$:

$$
4.0002
$$

Widać więc, że mniejszy krok daje wynik bliższy wartości dokładnej.

---

Dla funkcji:

$$
f(x)=2x^4-x^2+3x-7
$$

pochodna dokładna wynosi:

$$
f'(x)=8x^3-2x+3
$$

W punkcie:

$$
x=1
$$

mamy:

$$
f'(1)=9
$$

Program porównuje wartości otrzymane metodą różnicy w przód z wartością dokładną i oblicza błąd względny.

---

Dla funkcji:

$$
f(x)=x^2e^x
$$

pochodna dokładna wynosi:

$$
f'(x)=e^x(x^2+2x)
$$

Dla:

$$
x=1
$$

otrzymujemy:

$$
f'(1)=3e\approx 8.154845485
$$

Program liczy przybliżenia tej wartości dla dwóch różnych kroków $h$.

---

## Wnioski

W zadaniu zastosowano metodę Newtona, czyli dwupunktową różnicę w przód:

$$
f'(x)\approx \frac{f(x+h)-f(x)}{h}
$$

Dla każdej funkcji porównano wynik numeryczny z dokładną pochodną analityczną.

Błąd względny policzono ze wzoru:

$$
\delta=
\frac{
\left|f'_{\text{dokładna}}(x)-f'_{\text{przybliżona}}(x)\right|
}{
\left|f'_{\text{dokładna}}(x)\right|
}
$$

Z wyników widać, że dla mniejszego kroku:

$$
h=10^{-4}
$$

błąd względny jest mniejszy niż dla:

$$
h=10^{-2}
$$

Oznacza to, że zmniejszenie kroku $h$ poprawia dokładność przybliżenia pochodnej metodą różnicy w przód.

Trzeba jednak pamiętać, że dla bardzo małych wartości $h$ mogą pojawić się błędy zaokrągleń wynikające z ograniczonej precyzji obliczeń komputerowych.

# Zadanie 2

**Przeprowadź obliczenia analogiczne jak w zadaniu 1 dla metod różnic skończonych: wstecznej i centralnej dwupunktowej.**

W zadaniu korzystamy z tych samych funkcji co w zadaniu 1:

a)

$
f(x)=2x^2+2
$

b)

$
f(x)=2x^4-x^2+3x-7
$

c)

$
f(x)=x^2e^x
$

Obliczenia wykonujemy dla:

$$
h=10^{-2}
$$

oraz:

$$
h=10^{-4}
$$

W programie pochodną liczymy w punkcie:

$$
x=1
$$

## Cel zadania

W zadaniu 1 używaliśmy różnicy w przód, czyli metody Newtona:

$$
f'(x)\approx \frac{f(x+h)-f(x)}{h}
$$

W zadaniu 2 mamy wykonać podobne obliczenia, ale dla dwóch innych metod różnic skończonych:

- różnicy wstecznej,
- różnicy centralnej dwupunktowej.

Dla każdej metody porównujemy wynik numeryczny z pochodną dokładną i obliczamy błąd względny.

## Różnica wsteczna

Na slajdzie podano wzór:

$$
f'(x)\approx \frac{f(x)-f(x-h)}{h}
$$

Ta metoda korzysta z wartości funkcji w punktach:

$$
x
$$

oraz:

$$
x-h
$$

czyli patrzy „wstecz” względem punktu $x$.

Błąd tej metody jest rzędu:

$$
O(h)
$$

To oznacza, że zmniejszenie kroku $h$ powinno poprawiać dokładność wyniku.

## Różnica centralna dwupunktowa

Na slajdzie podano wzór:

$$
f'(x)\approx \frac{f(x+h)-f(x-h)}{2h}
$$

Ta metoda korzysta z dwóch punktów położonych symetrycznie względem punktu $x$:

$$
x-h
$$

oraz:

$$
x+h
$$

Dlatego nazywa się metodą centralną.

Błąd tej metody jest rzędu:

$$
O(h^2)
$$

Oznacza to, że zwykle jest dokładniejsza niż różnica wsteczna oraz różnica w przód.

## Błąd względny

Ze slajdu o błędzie względnym mamy wzór:

$$
\delta x=\frac{|x-\overline{x}|}{|x|}
$$

W tym zadaniu porównujemy pochodną dokładną z pochodną przybliżoną.

Dlatego podstawiamy:

$$
x=f'_{\text{dokładna}}(x)
$$

oraz:

$$
\overline{x}=f'_{\text{przybliżona}}(x)
$$

Otrzymujemy:

$$
\delta=
\frac{
\left|f'_{\text{dokładna}}(x)-f'_{\text{przybliżona}}(x)\right|
}{
\left|f'_{\text{dokładna}}(x)\right|
}
$$

## Pochodne dokładne funkcji

Tak jak w zadaniu 1, do policzenia błędu względnego potrzebujemy pochodnych dokładnych.

### Funkcja a)

$$
f(x)=2x^2+2
$$

Pochodna:

$$
f'(x)=4x
$$

---

### Funkcja b)

$$
f(x)=2x^4-x^2+3x-7
$$

Pochodna:

$$
f'(x)=8x^3-2x+3
$$

---

### Funkcja c)

$$
f(x)=x^2e^x
$$

Pochodna:

$$
f'(x)=e^x(x^2+2x)
$$

## Co robi program?

Program:

1. Definiuje funkcję liczącą pochodną metodą różnicy wstecznej.
2. Definiuje funkcję liczącą pochodną metodą różnicy centralnej dwupunktowej.
3. Definiuje funkcję liczącą błąd względny.
4. Definiuje funkcje z zadania oraz ich pochodne dokładne.
5. Dla każdej funkcji i dla każdego kroku $h$ liczy:
   - pochodną metodą wsteczną,
   - pochodną metodą centralną,
   - błąd względny dla obu metod.
6. Wypisuje wyniki w tabeli.

## Kod

```python
print("------------------------ZADANIE 2--------------------------")  # wypisujemy nagłówek zadania

def roznica_wsteczna(f, x, h):  # definiujemy funkcję liczącą pochodną metodą różnicy wstecznej
    return (f(x) - f(x - h)) / h  # zwracamy przybliżenie pochodnej ze wzoru: f'(x) ≈ (f(x)-f(x-h))/h
    
def roznica_centralna_dwupunktowa(f, x, h):  # definiujemy funkcję liczącą pochodną metodą różnicy centralnej dwupunktowej
    return (f(x + h) - f(x - h)) / (2 * h)  # zwracamy przybliżenie pochodnej ze wzoru: f'(x) ≈ (f(x+h)-f(x-h))/(2h)

def blad_wzgledny(wartosc_dokladna, wartosc_przyblizona):  # definiujemy funkcję liczącą błąd względny
    if wartosc_dokladna != 0:  # sprawdzamy, czy wartość dokładna nie jest równa zero
        return abs(wartosc_dokladna - wartosc_przyblizona) / abs(wartosc_dokladna)  # zwracamy błąd względny zgodny ze wzorem ze slajdu
    else:  # obsługujemy przypadek, gdy wartość dokładna jest równa zero
        raise ValueError("Nie można policzyć błędu względnego, gdy wartość dokładna jest równa 0.")  # zgłaszamy błąd, bo nie można dzielić przez zero

def f1(x):  # definiujemy pierwszą funkcję z zadania
    return 2 * x**2 + 2  # zwracamy wartość funkcji f(x)=2x^2+2

def df1(x):  # definiujemy dokładną pochodną pierwszej funkcji
    return 4 * x  # zwracamy wartość pochodnej f'(x)=4x

def f2(x):  # definiujemy drugą funkcję z zadania
    return 2 * x**4 - x**2 + 3*x - 7  # zwracamy wartość funkcji f(x)=2x^4-x^2+3x-7

def df2(x):  # definiujemy dokładną pochodną drugiej funkcji
    return 8 * x**3 - 2 * x + 3  # zwracamy wartość pochodnej f'(x)=8x^3-2x+3

def f3(x):  # definiujemy trzecią funkcję z zadania
    return x**2 * math.exp(x)  # zwracamy wartość funkcji f(x)=x^2e^x

def df3(x):  # definiujemy dokładną pochodną trzeciej funkcji
    return math.exp(x) * (x**2 + 2 * x)  # zwracamy wartość pochodnej f'(x)=e^x(x^2+2x)

def porownaj_metody(nazwa, f, df, x, h_lista):  # definiujemy funkcję porównującą metody dla jednej funkcji
    print("\n" + nazwa)  # wypisujemy nazwę aktualnie badanej funkcji
    print("x =", x)  # wypisujemy punkt, w którym liczymy pochodną
    print("h              metoda          pochodna numeryczna        pochodna dokładna          błąd względny")  # wypisujemy nagłówek tabeli

    for h in h_lista:  # przechodzimy po kolejnych wartościach kroku h
        pochodna_dokladna = df(x)  # liczymy dokładną wartość pochodnej w punkcie x

        pochodna_wsteczna = roznica_wsteczna(f, x, h)  # liczymy pochodną numeryczną metodą różnicy wstecznej
        blad_wsteczny = blad_wzgledny(pochodna_dokladna, pochodna_wsteczna)  # liczymy błąd względny dla metody wstecznej

        print(f"{h:<14} {'wsteczna':<15} {pochodna_wsteczna:<25} {pochodna_dokladna:<25} {blad_wsteczny}")  # wypisujemy wyniki dla różnicy wstecznej

        pochodna_centralna = roznica_centralna_dwupunktowa(f, x, h)  # liczymy pochodną numeryczną metodą różnicy centralnej
        blad_centralny = blad_wzgledny(pochodna_dokladna, pochodna_centralna)  # liczymy błąd względny dla metody centralnej

        print(f"{h:<14} {'centralna':<15} {pochodna_centralna:<25} {pochodna_dokladna:<25} {blad_centralny}")  # wypisujemy wyniki dla różnicy centralnej

x0 = 1.0  # ustalamy punkt x, w którym obliczamy pochodną

h_lista = [10**(-2), 10**(-4)]  # zapisujemy wartości h podane w treści zadania

porownaj_metody("a) f(x) = 2x^2 + 2", f1, df1, x0, h_lista)  # wykonujemy obliczenia dla funkcji a)
porownaj_metody("b) f(x) = 2x^4 - x^2 + 3x - 7", f2, df2, x0, h_lista)  # wykonujemy obliczenia dla funkcji b)
porownaj_metody("c) f(x) = x^2e^x", f3, df3, x0, h_lista)  # wykonujemy obliczenia dla funkcji c)
```

## Wyniki i interpretacja

Dla funkcji:

$$
f(x)=2x^2+2
$$

w punkcie:

$$
x=1
$$

pochodna dokładna wynosi:

$$
f'(1)=4
$$

Metoda wsteczna daje wynik trochę mniejszy od wartości dokładnej, a metoda centralna daje wynik praktycznie równy wartości dokładnej.

---

Dla funkcji:

$$
f(x)=2x^4-x^2+3x-7
$$

w punkcie:

$$
x=1
$$

pochodna dokładna wynosi:

$$
f'(1)=9
$$

Metoda centralna daje wyraźnie mniejszy błąd niż metoda wsteczna.

---

Dla funkcji:

$$
f(x)=x^2e^x
$$

w punkcie:

$$
x=1
$$

pochodna dokładna wynosi:

$$
f'(1)=3e\approx 8.154845485
$$

Także tutaj metoda centralna daje dokładniejszy wynik niż metoda wsteczna.

## Wnioski

W zadaniu zastosowano dwie metody różnic skończonych:

### Różnicę wsteczną

$$
f'(x)\approx \frac{f(x)-f(x-h)}{h}
$$

oraz różnicę centralną dwupunktową:

$$
f'(x)\approx \frac{f(x+h)-f(x-h)}{2h}
$$

Wyniki pokazują, że dla mniejszego kroku:

$$
h=10^{-4}
$$

błędy są zwykle mniejsze niż dla:

$$
h=10^{-2}
$$

Dodatkowo metoda centralna jest dokładniejsza od metody wstecznej, ponieważ jej błąd jest rzędu:

$$
O(h^2)
$$

a błąd metody wstecznej jest rzędu:

$$
O(h)
$$

Oznacza to, że różnica centralna szybciej poprawia dokładność przy zmniejszaniu kroku $h$.

# Zadanie 3

**Przeprowadź obliczenia analogiczne jak w zadaniu 1 dla metod różnic skończonych: w przód i wstecznej trzypunktowej oraz centralnej czteropunktowej.**

W zadaniu korzystamy z tych samych funkcji co wcześniej:

a)

$
f(x)=2x^2+2
$

b)

$
f(x)=2x^4-x^2+3x-7
$

c)

$
f(x)=x^2e^x
$

Obliczenia wykonujemy dla:

$$
h=10^{-2}
$$

oraz:

$$
h=10^{-4}
$$

W programie pochodną liczymy w punkcie:

$$
x=1
$$

## Cel zadania

W poprzednich zadaniach używaliśmy prostszych wzorów różnic skończonych:

- różnicy w przód,
- różnicy wstecznej,
- różnicy centralnej dwupunktowej.

W tym zadaniu stosujemy dokładniejsze wzory:

- trzypunktową różnicę w przód,
- trzypunktową różnicę wsteczną,
- czteropunktową różnicę centralną.

Dla każdej metody porównujemy wynik numeryczny z pochodną dokładną i obliczamy błąd względny.

## Trzypunktowa różnica w przód

Ze slajdu mamy wzór:

$$
f'(x)\approx \frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}
$$

Ta metoda korzysta z trzech punktów:

$$
x,\quad x+h,\quad x+2h
$$

czyli używa punktów położonych „w przód” od punktu $x$.

Błąd tej metody jest rzędu:

$$
O(h^2)
$$

czyli metoda jest dokładniejsza od zwykłej dwupunktowej różnicy w przód, która miała błąd rzędu $O(h)$.

## Trzypunktowa różnica wsteczna

Ze slajdu mamy wzór:

$$
f'(x)\approx \frac{3f(x)-4f(x-h)+f(x-2h)}{2h}
$$

Ta metoda korzysta z trzech punktów:

$$
x,\quad x-h,\quad x-2h
$$

czyli używa punktów położonych „wstecz” od punktu $x$.

Błąd tej metody również jest rzędu:

$$
O(h^2)
$$

## Czteropunktowa różnica centralna

Ze slajdu mamy wzór:

$$
f'(x)\approx
\frac{
f(x-2h)-8f(x-h)+8f(x+h)-f(x+2h)
}{12h}
$$

Ta metoda korzysta z punktów położonych symetrycznie wokół $x$:

$$
x-2h,\quad x-h,\quad x+h,\quad x+2h
$$

Jest to metoda centralna, ponieważ wykorzystuje wartości funkcji po obu stronach punktu $x$.

Błąd tej metody jest rzędu:

$$
O(h^4)
$$

czyli powinna być najdokładniejsza spośród metod użytych w tym zadaniu.

## Błąd względny

Ze slajdu o błędzie względnym:

$$
\delta x=\frac{|x-\overline{x}|}{|x|}
$$

W tym zadaniu wartością dokładną jest pochodna dokładna, a wartością przybliżoną jest pochodna obliczona numerycznie.

Dlatego używamy wzoru:

$$
\delta=
\frac{
\left|f'_{\text{dokładna}}(x)-f'_{\text{przybliżona}}(x)\right|
}{
\left|f'_{\text{dokładna}}(x)\right|
}
$$

## Pochodne dokładne funkcji

Do obliczenia błędu względnego potrzebujemy pochodnych dokładnych.

### Funkcja a)

$$
f(x)=2x^2+2
$$

Pochodna:

$$
f'(x)=4x
$$

---

### Funkcja b)

$$
f(x)=2x^4-x^2+3x-7
$$

Pochodna:

$$
f'(x)=8x^3-2x+3
$$

---

### Funkcja c)

$$
f(x)=x^2e^x
$$

Korzystamy z reguły iloczynu:

$$
f'(x)=2xe^x+x^2e^x
$$

czyli:

$$
f'(x)=e^x(x^2+2x)
$$

## Co robi program?

Program:

1. Definiuje funkcję dla trzypunktowej różnicy w przód.
2. Definiuje funkcję dla trzypunktowej różnicy wstecznej.
3. Definiuje funkcję dla czteropunktowej różnicy centralnej.
4. Definiuje funkcję liczącą błąd względny.
5. Definiuje funkcje z zadania oraz ich pochodne dokładne.
6. Dla każdej funkcji i dla każdego kroku $h$ oblicza pochodną trzema metodami.
7. Porównuje wyniki z pochodną dokładną.
8. Wypisuje błąd względny.

## Kod

```python
import math  # importujemy moduł math, ponieważ potrzebujemy funkcji exp do obliczania e^x

print("------------------------ZADANIE 3--------------------------")  # wypisujemy nagłówek zadania

def roznica_w_przod_trzypunktowa(f, x, h):  # definiujemy funkcję liczącą pochodną trzypunktową różnicą w przód
    return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)  # zwracamy wynik ze wzoru: [-3f(x)+4f(x+h)-f(x+2h)]/(2h)

def roznica_wsteczna_trzypunktowa(f, x, h):  # definiujemy funkcję liczącą pochodną trzypunktową różnicą wsteczną
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)  # zwracamy wynik ze wzoru: [3f(x)-4f(x-h)+f(x-2h)]/(2h)
    
def roznica_centralna_czteropunktowa(f, x, h):  # definiujemy funkcję liczącą pochodną czteropunktową różnicą centralną
    return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h)  # zwracamy wynik ze wzoru centralnego czteropunktowego

def blad_wzgledny(wartosc_dokladna, wartosc_przyblizona):  # definiujemy funkcję liczącą błąd względny
    if wartosc_dokladna != 0:  # sprawdzamy, czy wartość dokładna nie jest równa zero
        return abs(wartosc_dokladna - wartosc_przyblizona) / abs(wartosc_dokladna)  # zwracamy błąd względny zgodnie ze wzorem ze slajdu
    else:  # obsługujemy przypadek, gdy wartość dokładna jest równa zero
        raise ValueError("Nie można policzyć błędu względnego, gdy wartość dokładna jest równa 0.")  # zgłaszamy błąd, ponieważ nie można dzielić przez zero

def f1(x):  # definiujemy pierwszą funkcję z zadania
    return 2 * x**2 + 2  # zwracamy wartość funkcji f(x)=2x^2+2

def df1(x):  # definiujemy dokładną pochodną pierwszej funkcji
    return 4 * x  # zwracamy wartość pochodnej f'(x)=4x

def f2(x):  # definiujemy drugą funkcję z zadania
    return 2 * x**4 - x**2 + 3*x - 7  # zwracamy wartość funkcji f(x)=2x^4-x^2+3x-7

def df2(x):  # definiujemy dokładną pochodną drugiej funkcji
    return 8 * x**3 - 2 * x + 3  # zwracamy wartość pochodnej f'(x)=8x^3-2x+3

def f3(x):  # definiujemy trzecią funkcję z zadania
    return x**2 * math.exp(x)  # zwracamy wartość funkcji f(x)=x^2e^x

def df3(x):  # definiujemy dokładną pochodną trzeciej funkcji
    return math.exp(x) * (x**2 + 2 * x)  # zwracamy wartość pochodnej f'(x)=e^x(x^2+2x)

def porownaj_metody(nazwa, f, df, x, h_lista):  # definiujemy funkcję porównującą wszystkie metody dla jednej funkcji
    print("\n" + nazwa)  # wypisujemy nazwę aktualnie badanej funkcji
    print("x =", x)  # wypisujemy punkt, w którym obliczamy pochodną
    print("h              metoda                    pochodna numeryczna        pochodna dokładna          błąd względny")  # wypisujemy nagłówek tabeli

    for h in h_lista:  # przechodzimy po kolejnych wartościach kroku h
        pochodna_dokladna = df(x)  # liczymy dokładną wartość pochodnej w punkcie x

        pochodna_przod = roznica_w_przod_trzypunktowa(f, x, h)  # liczymy pochodną metodą trzypunktowej różnicy w przód
        blad_przod = blad_wzgledny(pochodna_dokladna, pochodna_przod)  # liczymy błąd względny dla metody w przód

        print(f"{h:<14} {'w przód 3-punktowa':<25} {pochodna_przod:<25} {pochodna_dokladna:<25} {blad_przod}")  # wypisujemy wynik metody w przód

        pochodna_wsteczna = roznica_wsteczna_trzypunktowa(f, x, h)  # liczymy pochodną metodą trzypunktowej różnicy wstecznej
        blad_wsteczny = blad_wzgledny(pochodna_dokladna, pochodna_wsteczna)  # liczymy błąd względny dla metody wstecznej

        print(f"{h:<14} {'wsteczna 3-punktowa':<25} {pochodna_wsteczna:<25} {pochodna_dokladna:<25} {blad_wsteczny}")  # wypisujemy wynik metody wstecznej

        pochodna_centralna = roznica_centralna_czteropunktowa(f, x, h)  # liczymy pochodną metodą czteropunktowej różnicy centralnej
        blad_centralny = blad_wzgledny(pochodna_dokladna, pochodna_centralna)  # liczymy błąd względny dla metody centralnej

        print(f"{h:<14} {'centralna 4-punktowa':<25} {pochodna_centralna:<25} {pochodna_dokladna:<25} {blad_centralny}")  # wypisujemy wynik metody centralnej

x0 = 1.0  # ustalamy punkt x, w którym obliczamy pochodną

h_lista = [10**(-2), 10**(-4)]  # zapisujemy wartości h podane w treści zadania

porownaj_metody("a) f(x) = 2x^2 + 2", f1, df1, x0, h_lista)  # wykonujemy obliczenia dla funkcji a)
porownaj_metody("b) f(x) = 2x^4 - x^2 + 3x - 7", f2, df2, x0, h_lista)  # wykonujemy obliczenia dla funkcji b)
porownaj_metody("c) f(x) = x^2e^x", f3, df3, x0, h_lista)  # wykonujemy obliczenia dla funkcji c)
```

## Interpretacja wyników

Dla funkcji:

$$
f(x)=2x^2+2
$$

pochodna dokładna w punkcie:

$$
x=1
$$

wynosi:

$$
f'(1)=4
$$

Wszystkie metody dają wynik bardzo bliski wartości dokładnej.

---

Dla funkcji:

$$
f(x)=2x^4-x^2+3x-7
$$

pochodna dokładna to:

$$
f'(x)=8x^3-2x+3
$$

Dla:

$$
x=1
$$

otrzymujemy:

$$
f'(1)=9
$$

Metoda centralna czteropunktowa daje najmniejszy błąd, ponieważ ma błąd rzędu $O(h^4)$.

---

Dla funkcji:

$$
f(x)=x^2e^x
$$

pochodna dokładna wynosi:

$$
f'(x)=e^x(x^2+2x)
$$

Dla:

$$
x=1
$$

otrzymujemy:

$$
f'(1)=3e\approx 8.154845485
$$

Również tutaj metoda centralna czteropunktowa daje najdokładniejszy wynik.

## Wnioski

W zadaniu zastosowano trzy metody różnic skończonych:

### Trzypunktową różnicę w przód

$$
f'(x)\approx \frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}
$$

### Trzypunktową różnicę wsteczną

$$
f'(x)\approx \frac{3f(x)-4f(x-h)+f(x-2h)}{2h}
$$

### Czteropunktową różnicę centralną

$$
f'(x)\approx
\frac{
f(x-2h)-8f(x-h)+8f(x+h)-f(x+2h)
}{12h}
$$

Trzypunktowe metody w przód i wstecz mają dokładność rzędu:

$$
O(h^2)
$$

Natomiast metoda centralna czteropunktowa ma dokładność rzędu:

$$
O(h^4)
$$

Dlatego metoda centralna czteropunktowa zwykle daje najlepsze wyniki.

Z wyników programu widać, że dla mniejszego kroku:

$$
h=10^{-4}
$$

błąd jest zazwyczaj mniejszy niż dla:

$$
h=10^{-2}
$$

Trzeba jednak pamiętać, że przy bardzo małych wartościach $h$ mogą pojawić się błędy zaokrągleń związane z ograniczoną precyzją obliczeń komputerowych.

# Zadanie 4

**Zaimplementuj różniczkowanie za pomocą wielomianów Lagrange’a. Wyznacz pochodną w punkcie**

$$
x=3.5
$$

**przy następujących węzłach interpolacji:**

$$
\{ (1,4),\ (2,10),\ (3,20),\ (4,34),\ (5,52) \}
$$

## Na czym polega metoda?

W tym zadaniu najpierw budujemy **wielomian interpolacyjny Lagrange’a** przechodzący przez podane punkty, a potem przybliżamy jego pochodną metodą różnicy centralnej.

Na tablicy zapisano:

$$
L_n(x)=\sum_{i=0}^{n} y_i l_i(x)
$$

gdzie $l_i(x)$ to wielomiany bazowe Lagrange’a.

Każdy wielomian bazowy ma postać:

$$
l_i(x)=
\prod_{\substack{j=0 \\ j\ne i}}^{n}
\frac{x-x_j}{x_i-x_j}
$$

Czyli dla każdego punktu budujemy osobny składnik, który potem mnożymy przez odpowiadającą mu wartość $y_i$.

## Dane z zadania

Mamy punkty:

$$
(1,4),\ (2,10),\ (3,20),\ (4,34),\ (5,52)
$$

czyli:

- $x_0=1,\ y_0=4$
- $x_1=2,\ y_1=10$
- $x_2=3,\ y_2=20$
- $x_3=4,\ y_3=34$
- $x_4=5,\ y_4=52$

Chcemy policzyć pochodną w punkcie:

$$
X=3.5
$$

Przyjmujemy krok zgodnie z ustaleniem:

$$
h=10^{-4}
$$

## Budowa wielomianu Lagrange’a

Wielomian interpolacyjny ma postać:

$$
L_n(x)=y_0l_0(x)+y_1l_1(x)+y_2l_2(x)+y_3l_3(x)+y_4l_4(x)
$$

Dla naszych danych:

$$
L_n(x)=4l_0(x)+10l_1(x)+20l_2(x)+34l_3(x)+52l_4(x)
$$

Każda funkcja bazowa $l_i(x)$ jest liczona ze wzoru:

$$
l_i(x)=
\prod_{\substack{j=0 \\ j\ne i}}^{n}
\frac{x-x_j}{x_i-x_j}
$$

W programie odpowiada za to funkcja:

```python
baza_lagrange(punkty, i, x)
```

## Różniczkowanie wielomianu Lagrange’a

Na tablicy pojawia się pomysł użycia różnicy centralnej dla wielomianu interpolacyjnego:

$$
f'(x)\approx \frac{L_n(x+h)-L_n(x-h)}{2h}
$$

W naszym zadaniu:

$$
f'(3.5)\approx \frac{L_n(3.5+h)-L_n(3.5-h)}{2h}
$$

dla:

$$
h=10^{-4}
$$

Czyli program:

1. Liczy wartość wielomianu Lagrange’a w punkcie $x+h$.
2. Liczy wartość wielomianu Lagrange’a w punkcie $x-h$.
3. Podstawia te wartości do wzoru różnicy centralnej.


## Kod

```python
print("-------------------- ZADANIE 4 --------------------")  # wypisujemy nagłówek zadania

def baza_lagrange(punkty, i, x):  # definiujemy funkcję liczącą i-tą bazę Lagrange'a l_i(x)
    xi =  punkty[i][0]  # pobieramy wartość x_i z i-tego punktu

    wynik = 1.0  # zaczynamy iloczyn od 1, bo będziemy mnożyć kolejne czynniki

    for j in range(len(punkty)):  # przechodzimy po wszystkich punktach
        if j != i:  # pomijamy przypadek j = i, ponieważ we wzorze jest warunek j różne od i
            xj = punkty[j][0]  # pobieramy wartość x_j z j-tego punktu
            wynik *= (x - xj) / (xi - xj)  # mnożymy przez kolejny czynnik wzoru Lagrange'a

    return wynik  # zwracamy wartość i-tej funkcji bazowej Lagrange'a

def wielomian_lagrange(punkty, x):  # definiujemy funkcję liczącą wartość wielomianu Lagrange'a L_n(x)
    suma = 0.0  # tworzymy zmienną, w której będziemy sumować składniki wielomianu

    for i in range(len(punkty)):  # przechodzimy po wszystkich punktach interpolacji
        yi = punkty[i][1]  # pobieramy wartość y_i z i-tego punktu
        suma += yi * baza_lagrange(punkty, i, x)  # dodajemy składnik y_i * l_i(x) do sumy

    return suma  # zwracamy wartość wielomianu interpolacyjnego L_n(x)

def pochodna_lagrange_centralna(punkty, x, h):  # definiujemy funkcję liczącą pochodną metodą różnicy centralnej
    return (wielomian_lagrange(punkty, x + h) - wielomian_lagrange(punkty, x - h)) / (2 * h)  # stosujemy wzór: [L_n(x+h)-L_n(x-h)]/(2h)

punkty = [(1, 4), (2, 10), (3, 20), (4, 34), (5, 52)]  # zapisujemy węzły interpolacji z zadania

X = 3.5  # zapisujemy punkt, w którym chcemy policzyć pochodną
h = 10**(-4)  # zapisujemy krok h = 10^-4

wynik = pochodna_lagrange_centralna(punkty, X, h)  # obliczamy przybliżoną wartość pochodnej w punkcie X

print("Węzły interpolacji:")  # wypisujemy opis danych wejściowych
print(punkty)  # wypisujemy listę punktów interpolacji

print("\nPunkt, w którym liczymy pochodną:")  # wypisujemy opis punktu obliczeń
print("x =", X)  # wypisujemy wartość punktu X

print("\nKrok:")  # wypisujemy opis kroku
print("h =", h)  # wypisujemy wartość kroku h

print("\nPrzybliżona wartość pochodnej:")  # wypisujemy opis wyniku
print("f'(", X, ") =", wynik)  # wypisujemy przybliżoną wartość pochodnej
```

## Wynik programu

Program zwraca wartość bardzo bliską:

$$
14
$$

czyli:

$$
f'(3.5)\approx 14
$$

Przykładowy wynik:

```text
f'( 3.5 ) = 14.000000000020663
```

Różnica od dokładnej wartości wynika tylko z zaokrągleń numerycznych.

## Sprawdzenie wyniku

Dane punkty:

$$
(1,4),\ (2,10),\ (3,20),\ (4,34),\ (5,52)
$$

leżą na funkcji:

$$
f(x)=2x^2+2
$$

Sprawdzenie:

$$
f(1)=2\cdot1^2+2=4
$$

$$
f(2)=2\cdot2^2+2=10
$$

$$
f(3)=2\cdot3^2+2=20
$$

$$
f(4)=2\cdot4^2+2=34
$$

$$
f(5)=2\cdot5^2+2=52
$$

Pochodna tej funkcji wynosi:

$$
f'(x)=4x
$$

Dla:

$$
x=3.5
$$

otrzymujemy:

$$
f'(3.5)=4\cdot3.5=14
$$

Dlatego wynik programu:

$$
f'(3.5)\approx 14
$$

jest poprawny.

## Wnioski

W zadaniu zbudowano wielomian interpolacyjny Lagrange’a:

$$
L_n(x)=\sum_{i=0}^{n} y_i l_i(x)
$$

gdzie:

$$
l_i(x)=
\prod_{\substack{j=0 \\ j\ne i}}^{n}
\frac{x-x_j}{x_i-x_j}
$$

Następnie pochodną obliczono metodą różnicy centralnej zastosowanej do wielomianu interpolacyjnego:

$$
f'(x)\approx \frac{L_n(x+h)-L_n(x-h)}{2h}
$$

Dla:

$$
X=3.5
$$

oraz:

$$
h=10^{-4}
$$

otrzymano:

$$
f'(3.5)\approx 14
$$

Wynik jest zgodny z wartością dokładną, ponieważ podane punkty pochodzą z funkcji:

$$
f(x)=2x^2+2
$$

a jej pochodna w punkcie $3.5$ wynosi:

$$
14.
$$