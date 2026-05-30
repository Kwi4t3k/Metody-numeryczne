# Wykład 1: Dokładność (do lab1 i lab2)

## 1. Czym są metody numeryczne?

**Metody numeryczne** są działem matematyki stosowanej. Zajmują się sposobami rozwiązywania zadań matematycznych za pomocą działań arytmetycznych.

W informatyce i naukach technicznych często pojawiają się problemy typu:

$$
f(x)=0, \space\space\space\space Ax=b, \space\space\space\space \int_a^b f(x)\,dx, \space\space\space\space  y'=f(x,y)
$$

W praktyce rozwiązanie analityczne często:

- nie istnieje,
    
- jest zbyt kosztowne obliczeniowo,
    
- opiera się na danych obarczonych błędami,
    
- jest liczone na komputerze, który ma skończoną precyzję.
    

Celem metod numerycznych jest:

- obliczenie przybliżenia rozwiązania,
    
- oszacowanie błędu,
    
- kontrolowanie stabilności obliczeń.
    

---

## 2. Najważniejsze pojęcia

### Dokładność

**Dokładność** oznacza dopuszczalny błąd wyniku. W praktyce dobiera się ją zależnie od problemu.

Przykład interpretacji:

Jeżeli wynik ma być podany z dokładnością do `0.01`, to interesuje nas błąd nie większy niż jedna setna.

---

### Zbieżność iteracji

**Zbieżność iteracji** oznacza stopniowe zbliżanie się do wartości poszukiwanej.

Iteracje kończy się wtedy, gdy osiągnięta zostanie zadana dokładność.

Przykład:

Jeżeli kolejne przybliżenia rozwiązania wyglądają tak:

```text
1.4
1.41
1.414
1.4142
```

to widać, że wartości zbliżają się do pewnego wyniku. Można zakończyć obliczenia, gdy różnica między kolejnymi przybliżeniami jest wystarczająco mała.

---

### Dyskretyzacja

**Dyskretyzacja** to zastąpienie obiektu ciągłego obiektem o skończonej liczbie węzłów.

Przykład:

Zamiast analizować funkcję na całym przedziale, wybieramy kilka punktów, np.:

```text
x = 0, 1, 2, 3, 4
```

i liczymy wartości funkcji tylko w tych punktach.

---

### Model

**Model** to celowo uproszczona reprezentacja rzeczywistości.

---

### Model matematyczny

**Model matematyczny** to reprezentacja fragmentu rzeczywistości za pomocą symboli i operatorów matematycznych, z interpretacją odnoszącą się do danego zjawiska.

Schemat z wykładu:

```text
Model fizyczny(doświadczenie) | teoria
                ↓
        Model matematyczny
                ↓
    Metody analityczne | Model numeryczny(metody numeryczne)
```

---

## 3. Plan wykładu nr 1 — dokładność

Wykład dotyczył następujących tematów:

1. miary błędu: błąd bezwzględny, błąd względny, cyfry znaczące,
    
2. liczby maszynowe: `float`, `double`, IEEE 754, epsilon,
    
3. porównywanie liczb, `Inf`, `NaN`, utrata cyfr znaczących,
    
4. wpływ kolejności działań: gubienie składnika, sumowanie, algorytm Kahana,
    
5. uwarunkowanie i stabilność algorytmów, np. na przykładzie `a² - b²`.
    

---

# 4. Błąd bezwzględny

Niech:

- `x` — wartość dokładna,
    
- `x̄` — przybliżenie wartości dokładnej.
    

**Błąd bezwzględny**:

$$
\Delta x = |x - \bar{x}|
$$

Błąd bezwzględny mówi, o ile przybliżenie różni się od wartości dokładnej.

Jeżeli `x` nie jest znane, zamiast dokładnego błędu oblicza się jego oszacowanie, czyli kres górny.

### Ważne

Błąd bezwzględny zależy od skali liczby.

Przykład:

Jeżeli błąd wynosi:

```text
Δx = 0.01
```

to dla liczby bliskiej `1` może być to istotny błąd, ale dla liczby bliskiej `1000` jest to bardzo mały błąd.

### Przykład
```python
def blad_bezwzgledny(x, x_przyblizone):
    return abs(x - x_przyblizone)


# przykład
x = 10          # wartość dokładna
x_bar = 9.8     # wartość przybliżona

delta_x = blad_bezwzgledny(x, x_bar)

print("Błąd bezwzględny:", delta_x)
```

---

# 5. Błąd względny

Dla `x ≠ 0` błąd względny definiuje się jako:

$$
\delta x = \frac{|x - \bar{x}|}{|x|}
$$

Błąd względny mierzy dokładność niezależnie od rzędu wielkości liczby.

### Przykład z wykładu

Jeżeli:

```text
Δx = 0.01
```

to:

dla `x = 1`:

$$
δx=1%\delta x = 1\%
$$

dla `x = 1000`:

$$
δx=0.001%\delta x = 0.001\%
$$

### Wniosek

W analizie numerycznej kluczowy jest **błąd względny**, ponieważ lepiej pokazuje, czy wynik jest dokładny względem skali problemu.

### Przykład
```python
def blad_wzgledny(x, x_przyblizone):
    if x == 0:
        raise ValueError("Błąd względny nie jest określony dla x = 0")
    
    return abs(x - x_przyblizone) / abs(x)


# przykład
x = 1000
x_bar = 999.99

delta_x = blad_wzgledny(x, x_bar)

print("Błąd względny:", delta_x)
print("Błąd względny w procentach:", delta_x * 100, "%")
```

---

# 6. Źródła błędów w obliczeniach numerycznych

W obliczeniach numerycznych mogą pojawiać się różne błędy:

## 6.1. Błędy zaokrągleń

Wynikają z arytmetyki komputera, ponieważ komputer nie potrafi dokładnie zapisać wszystkich liczb rzeczywistych.

Przykład:

Liczba `0.1` nie ma skończonej reprezentacji binarnej, więc komputer przechowuje tylko jej przybliżenie.

---

## 6.2. Błędy obcięcia

Pojawiają się np. wtedy, gdy zatrzymujemy proces nieskończony.

Przykład:

Zamiast liczyć nieskończony szereg do końca, obcinamy go po określonej liczbie wyrazów.

---

## 6.3. Błędy programisty

Wynikają z niepoprawnego programu, np. złej kolejności działań, błędnego wzoru lub niewłaściwych warunków zakończenia pętli.

---

## 6.4. Błędy danych wejściowych

Dane wejściowe mogą pochodzić z pomiarów, zaokrągleń lub stałych fizycznych, które same są tylko przybliżone.

---

## 6.5. Błędy modelu

Wynikają z uproszczeń modelu matematycznego.

Model nie zawsze idealnie opisuje rzeczywistość.

---

## 6.6. Błędy metody

Niektóre metody mogą dawać duże błędy dla pewnych danych.

---

# 7. Błędy zaokrągleń

Komputer potrafi dokładnie reprezentować tylko:

- liczby całkowite z pewnego zakresu,
    
- liczby wymierne o skończonym rozwinięciu binarnym, również z pewnego zakresu.
    

Wiele ułamków dziesiętnych nie ma skończonego rozwinięcia binarnego.

Przykłady z wykładu:

$$
\frac{1}{5} = 0.(0011)_2, \space\space\space\space \frac{1}{10} = 0.0(0011)_2
$$

Oznacza to, że liczby takie jak `0.1` nie są przechowywane dokładnie, tylko jako przybliżenia.

---

# 8. Cyfry znaczące

Niech `x ≠ 0` ma postać:

$$
x = \pm 0.d_1d_2d_3 \ldots \times 10^k
$$

gdzie:

$$d_1 \neq 0$$

Przybliżenie `x̄` ma `p` cyfr znaczących, jeśli:

$$\frac{|x-\bar{x}|}{|x|} \leq \frac{1}{2} \cdot 10^{-p}$$

Liczba cyfr znaczących jest miarą błędu względnego.

### Przykład
```python
import math

def blad_wzgledny(x, x_bar):
    if x == 0:
        raise ValueError("x nie może być równe 0")
    return abs(x - x_bar) / abs(x)


def liczba_cyfr_znaczacych(x, x_bar):
    delta = blad_wzgledny(x, x_bar)

    if delta == 0:
        return "nieskończenie wiele, bo wynik jest dokładny"

    p = -math.log10(delta)
    return int(p)


x = 123.456789
x_bar = 123.457

delta = blad_wzgledny(x, x_bar)
p = liczba_cyfr_znaczacych(x, x_bar)

print("Błąd względny:", delta)
print("Około tyle cyfr znaczących:", p)
```
Idea:
```
mały błąd względny = dużo poprawnych cyfr znaczących
duży błąd względny = mało poprawnych cyfr znaczących
```

---

## Interpretacja cyfr znaczących

Jeżeli:

$$\delta x \approx 10^{-p}$$

to wynik ma około `p` poprawnych cyfr znaczących.

Przykład z wykładu:

$$\delta x \approx 10^{-6}$$

oznacza około `6` poprawnych cyfr znaczących.

W obliczeniach maszynowych liczba cyfr znaczących jest ograniczona długością mantysy.

---

# 9. Typy całkowite

Dowolną liczbę całkowitą `x` można przedstawić w systemie dwójkowym:

$$x = s \sum_{i=0}^{n} e_i 2^i$$

gdzie:

$$s \in \{−1,1\}$$

oraz:

$$e_i \in \{0,1\}$$

Obliczenia na liczbach całkowitych są zwykle dokładne do momentu przepełnienia.

### Wzór
liczba = znak · suma wybranych potęg liczby 2

### Przykład: liczba 13

W systemie dziesiętnym:

```text
13
```

Można ją zapisać jako sumę potęg dwójki:

```text
13 = 8 + 4 + 1
```

czyli:

```text
13 = 1·2³ + 1·2² + 0·2¹ + 1·2⁰
```

bo:

```text
2³ = 8
2² = 4
2¹ = 2
2⁰ = 1
```

Zatem binarnie:

```text
13 = 1101₂
```

Czytamy to tak:

```text
1·8 + 1·4 + 0·2 + 1·1 = 13
```

---

### Przykład: liczba -13

Tutaj wartość jest taka sama, tylko znak jest ujemny:

```text
-13 = -1 · (8 + 4 + 1)
```

czyli:

```text
-13 = -1 · (1·2³ + 1·2² + 0·2¹ + 1·2⁰)
```

Na slajdzie to właśnie oznacza `s ∈ {-1, 1}`.

---

### Jak to wygląda w Pythonie?

```python
x = 13

print(bin(x))
```

Wynik:

```text
0b1101
```

`0b` oznacza, że liczba jest zapisana binarnie.

Możesz też sprawdzić kilka liczb:

```python
liczby = [1, 2, 3, 4, 5, 13, 25]

for x in liczby:
    print(x, "=", bin(x))
```

Wynik będzie np.:

```text
1 = 0b1
2 = 0b10
3 = 0b11
4 = 0b100
5 = 0b101
13 = 0b1101
25 = 0b11001
```

---

## Zakres typów całkowitych

Zakres z wykładu:

$$[-2^d, 2^d - 1]$$

Wyjątki od dokładności:

- dzielenie całkowitoliczbowe,
    
- przepełnienie zakresu.
    

### Przykład dzielenia całkowitoliczbowego

Jeżeli w języku programowania wykonamy dzielenie całkowite:

```text
5 / 2
```

to wynik może być:

```text
2
```

a nie:

```text
2.5
```

czyli tracona jest część ułamkowa.

---

# 10. Typy zmiennopozycyjne

Liczba zmiennopozycyjna ma postać:

$$x = m \cdot p^c$$

gdzie:

- `m` — mantysa,
    
- `c` — wykładnik,
    
- `p` — podstawa, zwykle `2`.
    

W komputerze liczba rzeczywista jest kodowana przez mantysę i wykładnik.

---

## Reprezentacja liczby zmiennopozycyjnej

Zamiast nieskończonego rozwinięcia mantysy:

$$m = \sum_{i=1}^{\infty} e_{-i}2^{-i}$$

```python
def mantysa(e):  
"""  
Liczy:  
m = suma e_i * 2^(-i)  
  
e - lista bitów mantysy, np. [1, 0, 1, 1]  
"""  
suma = 0  
  
for i in range(1, len(e) + 1):  
suma += e[i - 1] * 2 ** (-i)  
  
return suma
```

używa się przybliżenia obciętego do `t` bitów:

$$m_t = \sum_{i=1}^{t} e_{-i}2^{-i}$$

```python
def mantysa_obcieta(e, t):
    """
    Liczy:
    m_t = suma od i=1 do t: e_i * 2^(-i)

    e - lista bitów mantysy
    t - liczba bitów, do których obcinamy
    """
    suma = 0

    for i in range(1, t + 1):
        suma += e[i - 1] * 2 ** (-i)

    return suma
```

z ograniczeniem:

$$|m - m_t| \leq \frac{1}{2}2^{-t}$$

```python
def ograniczenie_bledu(t):
    """
    Liczy:
    1/2 * 2^(-t)
    """
    return 0.5 * 2 ** (-t)
```

Reprezentacja liczby:

$$x = (-1)^s \cdot 2^c \cdot m_t$$

**Przykład użycia tych wyżej**
```python
e = [1, 0, 1, 1, 0, 1]  # bity mantysy
t = 4

m = mantysa(e)
m_t = mantysa_obcieta(e, t)
blad_graniczny = ograniczenie_bledu(t)

print("m =", m)
print("m_t =", m_t)
print("ograniczenie błędu =", blad_graniczny)
print("|m - m_t| =", abs(m - m_t))
```

---

# 11. `float` i `double`

Z wykładu:

|Typ|`digits10`|`max_digits10`|epsilon|zakres|
|---|--:|--:|--:|---|
|`float`|6|9|około `1.19 · 10⁻⁷`|około `10⁻³⁸ ... 10³⁸`|
|`double`|15|17|około `2.22 · 10⁻¹⁶`|około `10⁻³⁰⁸ ... 10³⁰⁸`|

### Ważna uwaga

`setprecision(20)` dla typu `float` nie zwiększa dokładności.

To znaczy, że wypisanie większej liczby cyfr nie sprawia, że wynik staje się dokładniejszy. Program wypisuje tylko więcej cyfr przechowywanego przybliżenia.

Do wiernego wypisywania używa się zwykle `max_digits10`.

### Notatka — Python

W języku Python typ `float` jest domyślnie liczbą zmiennoprzecinkową podwójnej precyzji, czyli odpowiada typowi `double` z języka C/C++.

Python nie ma osobnego podstawowego typu `float` i `double` tak jak C++. Zwykły `float` w Pythonie przechowuje około **15–17 cyfr znaczących**.

```python
import sys

print(sys.float_info.dig)      # liczba cyfr znaczących
print(sys.float_info.max)      # największa wartość
print(sys.float_info.epsilon)  # epsilon maszynowy
```

Przykład:

```python
x = 0.1 + 0.2

print(x)
print(f"{x:.20f}")
```

Wynik:

```text
0.30000000000000004
0.30000000000000004441
```

Oznacza to, że wypisanie większej liczby cyfr nie zwiększa dokładności wyniku. Program pokazuje jedynie więcej cyfr już zapisanego przybliżenia.

W Pythonie:

```python
print(f"{x:.20f}")
```

działa podobnie jak `setprecision(20)` w C++ — zmienia tylko sposób wyświetlania liczby, ale nie zwiększa dokładności obliczeń.

Do większej dokładności można użyć modułu `decimal`:

```python
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)
```

Wynik:

```text
0.3
```

Czyli najważniejsze:

```text
Python float ≈ C++ double
około 15–17 cyfr znaczących
większa liczba wypisanych cyfr nie oznacza większej dokładności
```

**Można użyć typu 32-bit jako:**
```python
import numpy as np

def suma_pojedyncza_precyzja(a, b):
    a32 = np.float32(a)
    b32 = np.float32(b)
    return np.float32(a32 + b32)
```

---

# 12. Standard IEEE 754

Według slajdu z wykładu:

|Typ|Rozmiar|Mantysa|Wykładnik|Przesunięcie wykładnika|
|---|--:|--:|--:|--:|
|Single Precision|32 bity = 4 bajty|23 bity|8 bitów|`2⁷ - 1 = 127`|
|Double Precision|64 bity = 8 bajtów|52 bity|11 bitów|`2¹⁰ - 1 = 1023`|

---

# 13. Reprezentacja zmiennopozycyjna i błąd względny

Niech `rd(x)` oznacza maszynową reprezentację liczby `x`, czyli zaokrąglenie do najbliższej liczby maszynowej.

Dla `x ≠ 0` zachodzi model:

$$rd(x) = x(1+\epsilon)$$

gdzie:

$$|\epsilon| \leq u
$$
`u` to jednostka zaokrąglenia, czyli **unit roundoff**.

W arytmetyce binarnej:

$$u = \frac{1}{2} \cdot 2^{-p}$$

gdzie `p` jest liczbą bitów mantysy.

### Wniosek

- mantysa decyduje o dokładności,
    
- wykładnik decyduje o zakresie.
    

---

# 14. Maszynowy epsilon

**Maszynowy epsilon**:

$$\epsilon_{mach} = \min\{\epsilon > 0 : 1 + \epsilon > 1\}$$

W praktyce dla IEEE 754 przy zaokrągleniu do najbliższej:

$$\epsilon_{mach} \approx \frac{1}{2} \cdot 2^{-p} = u$$

Typowo:

```text
float  ≈ 10⁻⁷
double ≈ 10⁻¹⁶
```

Przykład w Pythonie możesz dać taki:

```python
epsilon = 1.0

while 1.0 + epsilon > 1.0:
    epsilon = epsilon / 2

epsilon = epsilon * 2

print("Maszynowy epsilon:", epsilon)
print("1 + epsilon =", 1.0 + epsilon)
print("1 + epsilon/2 =", 1.0 + epsilon / 2)
```

Wynik będzie mniej więcej:

```text
Maszynowy epsilon: 2.220446049250313e-16
1 + epsilon = 1.0000000000000002
1 + epsilon/2 = 1.0
```

Czyli interpretacja jest taka:

```text
epsilon to najmniejsza liczba, którą można dodać do 1,
żeby komputer jeszcze zauważył zmianę.
```

Dla Pythona typ `float` działa jak `double`, więc epsilon jest około:

```text
2.22 · 10^-16
```

Możesz też użyć gotowej wartości z Pythona:

```python
import sys

print(sys.float_info.epsilon)
```

Wynik:

```text
2.220446049250313e-16
```

### Wniosek
> Maszynowy epsilon określa najmniejszą różnicę między liczbą `1` a najbliższą większą liczbą możliwą do zapisania w danym typie zmiennoprzecinkowym. W Pythonie dla typu `float` wynosi około `2.22 · 10^-16`. Oznacza to, że `1 + epsilon` jest już rozróżnialne od `1`, ale `1 + epsilon/2` zostaje zaokrąglone z powrotem do `1`.

---

# 15. Model arytmetyki zmiennopozycyjnej

Zakładany model:

$$fl(x \circ y) = (x \circ y)(1+\epsilon)$$

gdzie:

$$|\epsilon| \leq \epsilon_{mach}$$

oraz:

$$\circ \in \{+, -, \cdot, /\}$$

Każda operacja wprowadza błąd względny rzędu:

$$O(\epsilon_{mach})$$

Błędy mogą kumulować się w dłuższych obliczeniach.

### Przykład
Dobry przykład do tego slajdu: **wielokrotne dodawanie małej liczby**.

```python
suma = 0.0

for i in range(10):
    suma += 0.1

print(suma)
print(suma == 1.0)
```

Wynik:

```text
0.9999999999999999
False
```

Matematycznie powinno być:

```text
0.1 + 0.1 + ... + 0.1 = 1.0
```

ale komputer dostaje trochę inny wynik, bo `0.1` nie jest dokładnie reprezentowane binarnie. Każde dodanie wprowadza mały błąd zaokrąglenia.

Czyli ten slajd mówi mniej więcej:

```text
wynik w komputerze = wynik dokładny · (1 + mały błąd)
```

W kodzie można to zapisać jako notatkę:

```python
# Każda operacja zmiennoprzecinkowa może wprowadzać mały błąd.
# Przy wielu operacjach te błędy mogą się kumulować.

suma = 0.0

for i in range(1000000):
    suma += 0.1

dokladny_wynik = 100000.0

print("Wynik obliczony:", suma)
print("Wynik dokładny:", dokladny_wynik)
print("Błąd:", abs(suma - dokladny_wynik))
```

Przykładowy wynik:

```text
Wynik obliczony: 100000.00000133288
Wynik dokładny: 100000.0
Błąd: 0.0000013328826753422618
```

Najprostszy opis pod przykład:

> W arytmetyce zmiennoprzecinkowej każda operacja może wprowadzić niewielki błąd zaokrąglenia. Przy dłuższych obliczeniach błędy te mogą się sumować, dlatego wynik wielu operacji na liczbach `float` może nie być dokładnie równy wynikowi matematycznemu.

---

# 16. Porównywanie liczb zmiennopozycyjnych

Porównywanie przez `==` jest zwykle błędem dla `float` i `double`.

Zamiast tego stosuje się test mieszany, uwzględniający tolerancję absolutną i względną:

$$|a-b| \leq \epsilon \cdot \max(1, |a|, |b|)$$

Przykład z wykładu w C++:

```cpp
double eps = 1e-12;

bool equal = std::fabs(a-b) <= eps * std::max(1.0,
              std::max(std::fabs(a), std::fabs(b)));
```

### Interpretacja

- dla wartości bliskich zera dominuje część absolutna,
    
- dla dużych wartości dominuje część względna.
    

### Przykład
Przykład w Pythonie do tych slajdów:

```python
def prawie_rowne(a, b, eps=1e-12):
    return abs(a - b) <= eps * max(1, abs(a), abs(b))


a = 0.1 + 0.2
b = 0.3

print("a =", a)
print("b =", b)

print("Porównanie przez ==:", a == b)
print("Porównanie z tolerancją:", prawie_rowne(a, b))
```

Wynik:

```text
a = 0.30000000000000004
b = 0.3
Porównanie przez ==: False
Porównanie z tolerancją: True
```

Czyli zamiast pisać:

```python
if a == b:
    print("równe")
```

dla liczb `float` lepiej pisać:

```python
if prawie_rowne(a, b):
    print("prawie równe")
```

Całość działa według wzoru ze slajdu:

```python
abs(a - b) <= eps * max(1, abs(a), abs(b))
```

Przykład z większymi liczbami:

```python
a = 1000000.0000001
b = 1000000.0000002

print(a == b)
print(prawie_rowne(a, b))
```

Tutaj ważna jest tolerancja względna, bo dla dużych liczb mała różnica bezwzględna może być nieistotna.

Dobry opis do notatki:

> Liczb zmiennoprzecinkowych nie powinno się porównywać bezpośrednio przez `==`, ponieważ mogą zawierać małe błędy zaokrągleń. Zamiast tego sprawdza się, czy różnica między liczbami jest mniejsza od ustalonej tolerancji.

---

# 17. Dlaczego `0.1 + 0.2 != 0.3`?

Liczba `0.1` nie ma skończonej reprezentacji binarnej.

Dlatego wynik może wyglądać tak:

```text
0.1 + 0.2 = 0.30000000000000004
```

Nie powinno się więc pisać:

```cpp
if (a == b)
```

lecz stosować porównywanie z tolerancją.

---

# 18. Gubienie małego składnika

Przykład z wykładu:

$$(10^{20} + 10^{-10}) - 10^{20}$$

W arytmetyce rzeczywistej wynik to:

$$10^{-10}$$

Ale w arytmetyce zmiennoprzecinkowej często:

$$fl(10^{20} + 10^{-10}) = 10^{20}$$

Dzieje się tak, ponieważ `10⁻¹⁰` jest mniejsze niż odstęp między liczbami maszynowymi w okolicy `10²⁰`.

### Wniosek

Skala liczb i kolejność działań wpływają na wynik.

### Przykład
Tutaj najlepszy przykład w Pythonie:

```python
a = 10**20
b = 10**-10

wynik = (a + b) - a

print(wynik)
```

Wynik:

```text
0.0
```

A matematycznie powinno być:

```text
0.0000000001
```

czyli:

```text
10^-10
```

Dlaczego tak się dzieje?

```python
a = 10**20
b = 10**-10

print(a + b)
print(a)
print(a + b == a)
```

Wynik:

```text
1e+20
100000000000000000000
True
```

Czyli Python „zgubił” bardzo małą liczbę `10^-10`, bo przy liczbie `10^20` jest ona za mała, żeby zmienić zapis liczby typu `float`.

Możesz też pokazać, że **kolejność działań ma znaczenie**:

```python
a = 10**20
b = 10**-10

wynik1 = (a + b) - a
wynik2 = (a - a) + b

print(wynik1)
print(wynik2)
```

Wynik:

```text
0.0
1e-10
```

Opis do notatki:

> W arytmetyce zmiennoprzecinkowej bardzo mały składnik dodany do bardzo dużej liczby może zostać utracony. Dzieje się tak, ponieważ odstęp między kolejnymi liczbami maszynowymi w pobliżu dużych wartości jest większy niż dodawany mały składnik. Dlatego kolejność wykonywania działań może wpływać na wynik.

Możesz jeszcze dodać wersję z dokładniejszym typem `Decimal`:

```python
from decimal import Decimal, getcontext

getcontext().prec = 50

a = Decimal("1e20")
b = Decimal("1e-10")

wynik = (a + b) - a

print(wynik)
```

Wynik:

```text
1E-10
```

---

# 19. `Inf`, `NaN`, overflow i underflow

Standard IEEE 754 przewiduje wartości specjalne.

Przykłady:

```text
1.0 / 0.0 → ∞
0.0 / 0.0 → NaN
```

W C++:

```cpp
double x = 1.0/0.0; // inf
double y = 0.0/0.0; // nan

std::isinf(x);
std::isnan(y);
```

## Overflow

**Overflow** występuje, gdy wynik jest poza zakresem reprezentacji.

Wtedy wynik może przejść w:

```text
+∞ lub -∞
```

## Underflow

**Underflow** występuje dla bardzo małych liczb.

Wynik może zostać zapisany jako:

```text
0
```

albo jako liczba zdenormalizowana.

### Przykład

```python
import math

# wartości specjalne
x = float("inf")
y = float("nan")

print("x =", x)
print("y =", y)

print("Czy x to nieskończoność?", math.isinf(x))
print("Czy y to NaN?", math.isnan(y))
```

Wynik:

```text
x = inf
y = nan
Czy x to nieskończoność? True
Czy y to NaN? True
```

Ważna różnica względem C++:

```python
# W Pythonie to da błąd:
# print(1.0 / 0.0)
```

Python nie zwróci tutaj `inf`, tylko zgłosi:

```text
ZeroDivisionError: float division by zero
```

Dlatego w Pythonie `inf` i `nan` najprościej tworzyć tak:

```python
inf = float("inf")
nan = float("nan")
```

---

### Overflow — wynik za duży

```python
a = 1e308

wynik = a * 10

print(wynik)
print(math.isinf(wynik))
```

Wynik:

```text
inf
True
```

Czyli liczba była za duża, żeby zmieścić się w typie `float`, więc Python zapisał ją jako nieskończoność.

---

### Underflow — wynik za mały

```python
b = 1e-323

wynik = b / 10

print(wynik)
```

Wynik:

```text
0.0
```

Czyli liczba była tak mała, że została zaokrąglona do zera.

---

### NaN — wynik nieokreślony

```python
nan = float("nan")

print(nan)
print(math.isnan(nan))
print(nan == nan)
```

Wynik:

```text
nan
True
False
```

Ważne: `NaN` nie jest równy nawet samemu sobie, dlatego sprawdzamy go przez:

```python
math.isnan(nan)
```

Do notatki możesz wpisać:

> W Pythonie wartości specjalne można utworzyć przez `float("inf")` oraz `float("nan")`. Do ich sprawdzania służą funkcje `math.isinf()` i `math.isnan()`. Overflow oznacza wynik zbyt duży dla typu `float`, a underflow oznacza wynik tak mały, że zostaje zapisany jako `0.0` lub liczba zdenormalizowana.

---

# 20. Utrata cyfr znaczących
Przykład funkcji z wykładu:

$$  
f(x)=\sqrt{x^2+1}-1  
$$

Dla małych wartości `x` mamy:

$$  
\sqrt{x^2+1}\approx 1  
$$

więc w wyrażeniu:

$$  
\sqrt{x^2+1}-1  
$$

odejmujemy dwie prawie równe liczby. Może to powodować **utratę cyfr znaczących**, ponieważ wynik jest bardzo mały, a część dokładności zostaje utracona podczas odejmowania.

Aby uniknąć tego problemu, stosujemy racjonalizację:

$$  
f(x)=\sqrt{x^2+1}-1  
$$

Mnożymy przez wyrażenie sprzężone:

$$  
f(x)=  
\frac{(\sqrt{x^2+1}-1)(\sqrt{x^2+1}+1)}  
{\sqrt{x^2+1}+1}  
$$

Po uproszczeniu:

$$  
f(x)=  
\frac{x^2}{\sqrt{x^2+1}+1}  
$$

Druga postać jest **numerycznie stabilniejsza**, ponieważ nie odejmujemy już dwóch prawie równych liczb.

Przykład w Pythonie:

```python
import math

def f_naiwna(x):
    return math.sqrt(x**2 + 1) - 1

def f_stabilna(x):
    return x**2 / (math.sqrt(x**2 + 1) + 1)

x = 1e-8

print("Postać zwykła:", f_naiwna(x))
print("Postać stabilna:", f_stabilna(x))
```

Przykładowy wynik:

```text
Postać zwykła: 0.0
Postać stabilna: 5.0000000000000005e-17
```

Wniosek:

> Przy odejmowaniu dwóch prawie równych liczb może dojść do utraty cyfr znaczących. Dlatego wyrażenie warto przekształcić do postaci numerycznie stabilniejszej.

---

## Stabilniejsza postać przez racjonalizację

Zamiast liczyć:

f(x)=x2+1−1f(x) = \sqrt{x^2+1} - 1

można zastosować postać:

f(x)=x2x2+1+1f(x) = \frac{x^2}{\sqrt{x^2+1}+1}

Druga postać jest numerycznie stabilniejsza.

### Dlaczego?

Bo nie odejmujemy dwóch liczb prawie równych. Dzięki temu zmniejszamy ryzyko utraty cyfr znaczących.

---

# 21. Propagacja błędu

Dla funkcji jednej zmiennej, korzystając z aproksymacji liniowej:

$$\Delta f \approx |f'(x)|\Delta x$$

Małe błędy danych mogą zostać:

- wzmocnione,
    
- osłabione,
    
- zachowane.
    

### Interpretacja

Jeżeli `|f'(x)|` jest duże, to mały błąd wejścia może dać większy błąd wyniku.

Jeżeli `|f'(x)|` jest małe, to błąd może zostać osłabiony.

### Przykład
Jasne — przykład do slajdu **„Propagacja błędu”** można zrobić na funkcji:

$$  
f(x)=x^2  
$$

Wtedy pochodna to:

$$ 
f'(x)=2x  
$$

A błąd propaguje się w przybliżeniu tak:

$$  
\Delta f \approx |f'(x)|\Delta x  
$$

Czyli:

$$  
\Delta f \approx |2x|\Delta x  
$$

Przykład w Pythonie:

```python
def f(x):
    return x**2

def pochodna_f(x):
    return 2 * x


x = 10
delta_x = 0.01

x_przyblizone = x + delta_x

# dokładna zmiana wartości funkcji
delta_f_rzeczywiste = abs(f(x_przyblizone) - f(x))

# przybliżenie z propagacji błędu
delta_f_przyblizone = abs(pochodna_f(x)) * delta_x

print("x =", x)
print("Błąd danych Δx =", delta_x)

print("f(x) =", f(x))
print("f(x + Δx) =", f(x_przyblizone))

print("Rzeczywisty błąd Δf =", delta_f_rzeczywiste)
print("Przybliżony błąd Δf ≈ |f'(x)|Δx =", delta_f_przyblizone)
```

Przykładowy wynik:

```text
x = 10
Błąd danych Δx = 0.01
f(x) = 100
f(x + Δx) = 100.2001
Rzeczywisty błąd Δf = 0.2001000000000066
Przybliżony błąd Δf ≈ |f'(x)|Δx = 0.2
```

Wniosek:

> Mały błąd wejściowy `Δx = 0.01` spowodował błąd wyniku około `Δf = 0.2`.  
> Błąd został wzmocniony, ponieważ pochodna funkcji w punkcie `x = 10` wynosi `20`.

Możesz też dopisać krótką notatkę:

```text
Jeżeli |f'(x)| > 1, błąd danych jest wzmacniany.
Jeżeli |f'(x)| < 1, błąd danych jest osłabiany.
Jeżeli |f'(x)| ≈ 1, błąd jest mniej więcej zachowany.
```

---

# 22. Stabilność i niestabilność numeryczna

**Niestabilność numeryczna** występuje wtedy, gdy błędy zaokrągleń lub błędy danych są wzmacniane w trakcie obliczeń.

Źródła niestabilności:

- odejmowanie liczb bliskich,
    
- utrata cyfr znaczących,
    
- niekorzystna kolejność działań,
    
- źle dobrany wzór lub postać obliczeń,
    
- kumulacja błędów w długich obliczeniach.
    

---

# 23. Stabilność algorytmu

Algorytm jest **stabilny**, jeśli nie wzmacnia nieuniknionych błędów zaokrągleń.

Jeżeli błąd końcowy jest rzędu:

$$O(\epsilon_{mach})$$

to algorytm jest stabilny.

Jeżeli błędy rosną znacząco bardziej, algorytm jest niestabilny.

---

# 24. Uwarunkowanie zadania numerycznego

**Uwarunkowanie** określa wrażliwość rozwiązania na zaburzenia danych wejściowych.

Zadanie jest **źle uwarunkowane**, gdy nawet niewielkie błędy danych mogą powodować duże błędy wyniku, niezależnie od algorytmu.

### Ważne

Uwarunkowanie jest własnością problemu, a nie algorytmu.

---

# 25. Liczba uwarunkowania

Z propagacji błędu:

$$\Delta f \approx f'(x)\Delta x$$

Wersja względna:

$$\frac{|\Delta f|}{|f(x)|} \approx \left|\frac{x f'(x)}{f(x)}\right| \cdot \frac{|\Delta x|}{|x|}$$

Definicja liczby uwarunkowania:

$$\kappa(x) = \left|\frac{x f'(x)}{f(x)}\right|$$

Interpretacja:

```text
względny błąd wyjścia ≈ κ(x) · względny błąd wejścia
```

### Przykład
Przykład do slajdu w Pythonie, np. dla funkcji:

$$  
f(x)=x^2  
$$

Wtedy:

$$  
f'(x)=2x  
$$

Liczba uwarunkowania:

$$ 
\kappa(x)=\left|\frac{x f'(x)}{f(x)}\right|

\left|\frac{x \cdot 2x}{x^2}\right|  
=2  
$$

Czyli **błąd względny wyniku jest około 2 razy większy niż błąd względny wejścia**.

```python
def f(x):
    return x**2

def df(x):
    return 2*x

def kappa(x):
    return abs(x * df(x) / f(x))


x = 10
delta_x = 0.1

x_przyblizone = x + delta_x

blad_wzgledny_wejscia = abs(delta_x) / abs(x)

blad_wzgledny_wyjscia = abs(f(x_przyblizone) - f(x)) / abs(f(x))

przewidywany_blad = kappa(x) * blad_wzgledny_wejscia

print("x =", x)
print("x przybliżone =", x_przyblizone)

print("f(x) =", f(x))
print("f(x przybliżone) =", f(x_przyblizone))

print("Liczba uwarunkowania κ(x) =", kappa(x))

print("Błąd względny wejścia =", blad_wzgledny_wejscia)
print("Rzeczywisty błąd względny wyjścia =", blad_wzgledny_wyjscia)
print("Przewidywany błąd względny wyjścia ≈", przewidywany_blad)
```

Przykładowy wynik:

```text
x = 10
x przybliżone = 10.1
f(x) = 100
f(x przybliżone) = 102.01
Liczba uwarunkowania κ(x) = 2.0
Błąd względny wejścia = 0.01
Rzeczywisty błąd względny wyjścia = 0.0201
Przewidywany błąd względny wyjścia ≈ 0.02
```

Wniosek do notatki:

> Liczba uwarunkowania mówi, ile razy błąd względny danych wejściowych może zostać powiększony w wyniku.  
> Dla funkcji $( f(x)=x^2 )$ mamy $( \kappa(x)=2 )$, więc błąd względny wyniku jest około 2 razy większy niż błąd względny wejścia.

---

# 26. Źle uwarunkowany problem

Jeżeli:

$$\kappa(x) \gg 1$$

to mały błąd danych może powodować duży błąd wyniku.

---

# 27. Przykład liczby uwarunkowania: `f(x) = x²`

Dana jest funkcja:

$$f(x) = x^2$$

Pochodna:

$$f'(x) = 2x$$

Liczba uwarunkowania:

$$\kappa(x) = \left|\frac{x f'(x)}{f(x)}\right|$$

Po podstawieniu:

$$\kappa(x) = \left|\frac{x \cdot 2x}{x^2}\right| = 2$$

### Wniosek

Względny błąd wyniku jest około `2` razy większy niż względny błąd wejścia.

Problem jest dobrze uwarunkowany.

---

# 28. Przykład liczby uwarunkowania: `f(x) = sin(x)`

Dana jest funkcja:

$$f(x) = \sin x$$

Pochodna:

$$f'(x) = \cos x$$

Liczba uwarunkowania:

$$\kappa(x) = \left|\frac{x\cos x}{\sin x}\right|$$

Dla małych `x`:

$$x\sin x \approx x, \space\space\space\space\space \cos x \approx 1$$

więc:

$$\kappa(x) \approx \left|\frac{x}{x}\right| = 1$$

### Wniosek

W pobliżu zera problem jest dobrze uwarunkowany.

### Uwaga

Gdy `f(x)` jest bardzo małe, np. blisko miejsca zerowego, liczba uwarunkowania może być bardzo duża. Wtedy problem staje się źle uwarunkowany.

---

# 29. Uwarunkowanie a stabilność

## Uwarunkowanie

Uwarunkowanie jest własnością problemu:

$$w = \Phi(d)$$

Oznacza, jak bardzo wynik reaguje na zmianę danych wejściowych.

## Stabilność

Stabilność jest własnością algorytmu, czyli sposobu obliczania.

## Cel

Chcemy mieć stabilny algorytm dla możliwie dobrze uwarunkowanego problemu.

### Przykład
## Uwarunkowanie vs stabilność

**Uwarunkowanie** mówi, czy sam problem jest wrażliwy na małe błędy danych wejściowych.

**Stabilność** mówi, czy wybrany algorytm dobrze radzi sobie z błędami zaokrągleń.

Czyli:

```text
uwarunkowanie = cecha problemu
stabilność = cecha sposobu liczenia
```

Dobry przykład na podstawie wcześniejszego slajdu:

```python
import math

def f_naiwna(x):
    return math.sqrt(x**2 + 1) - 1

def f_stabilna(x):
    return x**2 / (math.sqrt(x**2 + 1) + 1)

x = 1e-8

print("x =", x)
print("Algorytm naiwny:", f_naiwna(x))
print("Algorytm stabilny:", f_stabilna(x))
```

Przykładowy wynik:

```text
x = 1e-08
Algorytm naiwny: 0.0
Algorytm stabilny: 5.0000000000000005e-17
```

Obie funkcje liczą matematycznie to samo:

```text
sqrt(x² + 1) - 1 = x² / (sqrt(x² + 1) + 1)
```

ale pierwszy sposób jest **niestabilny numerycznie**, bo odejmuje dwie prawie równe liczby:

```text
sqrt(x² + 1) ≈ 1
```

czyli komputer liczy coś w stylu:

```text
1.0000000000000000 - 1.0000000000000000
```

i wynik wychodzi `0.0`.

Drugi sposób jest **stabilniejszy**, bo nie odejmuje prawie równych liczb.

Notatka do slajdu:

> Problem może być dobrze uwarunkowany, ale źle dobrany algorytm może być niestabilny. Dlatego nie wystarczy znać wzoru matematycznego — ważny jest też sposób jego obliczania.

---

# 30. Relacja między uwarunkowaniem i stabilnością

Z wykładu:

|Uwarunkowanie|Algorytm|Efekt|
|---|---|---|
|dobre|stabilny|wynik dokładny|
|dobre|niestabilny|duży błąd|
|złe|stabilny|błąd wynika z natury problemu|
|złe|niestabilny|katastrofa numeryczna|

---

# 31. Przykład: `a² - b²`

Rozważamy problem:

$$\Phi(a,b) = a^2 - b^2$$

Dwa algorytmy:

## Algorytm A1

$$A1: a \cdot a - b \cdot b$$

## Algorytm A2

$$A2: (a+b)(a-b)$$

Algebraicznie oba wzory są równoważne.

Numerycznie niekoniecznie.

---

## Dlaczego A1 może być niestabilny?

Gdy:

$$a \approx b$$

to:

$$a^2 \approx b^2$$

Wtedy w algorytmie A1 odejmujemy liczby bliskie:

$$a^2 - b^2$$

Wynik jest małą różnicą dużych liczb.

To sprzyja utracie cyfr znaczących i wzmacnianiu błędu względnego.

---

## Dlaczego A2 może być stabilniejszy?

W algorytmie A2:

$$(a+b)(a-b)$$

mały czynnik:

$$a-b$$

występuje bezpośrednio.

Dlatego ta postać zwykle jest stabilniejsza, gdy `a ≈ b`.

---

## Wniosek

Równoważność algebraiczna nie oznacza równoważności numerycznej.

Wzór:

$$(a+b)(a-b)$$

bywa stabilniejszy niż:

$$a^2-b^2$$

gdy `a ≈ b`.

To klasyczny przykład katastrofalnej utraty cyfr znaczących.

---

# 32. Problem sumowania

Rozważamy ogólną sumę:

$$S_n = \sum_{k=1}^{n} a_k$$

Sumowanie jest jedną z najczęstszych operacji w obliczeniach numerycznych.

Celem analizy jest:

- porównanie różnych algorytmów sumowania,
    
- zbadanie wpływu precyzji, np. `float` i `double`,
    
- przeanalizowanie propagacji błędu numerycznego.
    

### Przykład

```python
import math

def suma_zwykla(liczby):
    suma = 0.0

    for x in liczby:
        suma += x

    return suma


liczby1 = [1e20, 1.0, -1e20]
liczby2 = [1e20, -1e20, 1.0]

print("Suma w kolejności 1:", suma_zwykla(liczby1))
print("Suma w kolejności 2:", suma_zwykla(liczby2))

print("Dokładniejsze sumowanie math.fsum:", math.fsum(liczby1))
```

Przykładowy wynik:

```text
Suma w kolejności 1: 0.0
Suma w kolejności 2: 1.0
Dokładniejsze sumowanie math.fsum: 1.0
```

Matematycznie suma powinna wynosić:

```text
10^20 + 1 - 10^20 = 1
```

ale w pierwszym przypadku Python najpierw liczy:

```text
10^20 + 1
```

Liczba `1` jest za mała względem `10^20`, więc zostaje „zgubiona”. Potem:

```text
10^20 - 10^20 = 0
```

Dlatego wynik wychodzi `0.0`.

Notatka do slajdu:

> Przy sumowaniu liczb zmiennoprzecinkowych kolejność działań może wpływać na wynik. Małe składniki mogą zostać utracone, gdy są dodawane do bardzo dużych liczb. Dlatego w obliczeniach numerycznych porównuje się różne algorytmy sumowania, np. zwykłe `sum()` i dokładniejsze `math.fsum()`.

---

# 33. Dlaczego sumowanie jest podchwytliwe?

Niech `a_k` będą liczbami zmiennoprzecinkowymi.

Możliwe trudności:

- składniki mają różne rzędy wielkości,
    
- składniki mogą zmieniać znak,
    
- składniki mogą być bardzo małe względem aktualnej sumy,
    
- liczba składników `n` może być bardzo duża.
    

Matematycznie suma jest dobrze określona.

Problem leży w arytmetyce zmiennoprzecinkowej.

---

# 34. Klasyczne sumowanie

Algorytm:

```text
s = 0
s ← s + a_k
```

Model błędu:

$$fl(x+y) = (x+y)(1+\epsilon)$$

gdzie:

$$|\epsilon| \leq \epsilon_{mach}$$

Po `n` krokach:

$$błąd \space względny = O(n\epsilon_{mach})$$

### Wniosek

Im większe `n`, tym większa kumulacja błędów.

### Przykład

```python
def sumowanie_klasyczne(liczby):
    s = 0.0

    for a_k in liczby:
        s = s + a_k

    return s
```

Czyli dokładnie według algorytmu ze slajdu:

$$  
s = 0  
$$

$$  
s \leftarrow s + a_k  
$$

Przykład pokazujący kumulację błędów:

```python
def sumowanie_klasyczne(liczby):
    s = 0.0

    for a_k in liczby:
        s = s + a_k

    return s


n = 1_000_000
liczby = [0.1] * n

wynik = sumowanie_klasyczne(liczby)
wynik_dokladny = n * 0.1

print("Wynik klasycznego sumowania:", wynik)
print("Wynik oczekiwany:", wynik_dokladny)
print("Błąd bezwzględny:", abs(wynik - wynik_dokladny))
```

Przykładowy wynik:

```text
Wynik klasycznego sumowania: 100000.00000133288
Wynik oczekiwany: 100000.0
Błąd bezwzględny: 1.3328826753422618e-06
```

Do notatki możesz dopisać:

> W klasycznym sumowaniu każda operacja dodawania może wprowadzić mały błąd zaokrąglenia. Po wielu krokach błędy mogą się kumulować, dlatego im większe `n`, tym większy może być błąd końcowy.

Można też porównać ze stabilniejszym sumowaniem w Pythonie:

```python
import math

n = 1_000_000
liczby = [0.1] * n

print("sum():", sum(liczby))
print("math.fsum():", math.fsum(liczby))
```

`math.fsum()` używa dokładniejszego algorytmu sumowania niż zwykłe dodawanie po kolei.

---

# 35. Algorytm Gilla–Møllera

Idea algorytmu:

- przechowywać sumę,
    
- przechowywać poprawkę, czyli kompensację.
    

Pseudokod z wykładu:

```text
s = 0
p = 0

for a_k:
    t = s + a_k
    p = p + (a_k - (t - s))
    s = t

return s + p
```

Algorytm zmniejsza utratę cyfr znaczących, ale błąd nadal rośnie z `n`.

---

# 36. Algorytm Kahana

Algorytm Kahana to algorytm kompensowanego sumowania.

Pseudokod z wykładu:

```text
sum = 0
c = 0

for a_k:
    y = a_k - c
    t = sum + y
    c = (t - sum) - y
    sum = t

return sum
```

Algorytm kompensuje utratę małych składników.

W wykładzie podano, że błąd nie narasta liniowo z `n`.

---

# 37. Co można badać przy sumowaniu?

Według wykładu można badać:

- porównanie błędów dla:
    
    - klasycznego sumowania,
        
    - algorytmu Gilla–Møllera,
        
    - algorytmu Kahana,
        
- wpływ liczby składników `n`,
    
- wpływ precyzji obliczeń,
    
- związek z:
    
    - propagacją błędu,
        
    - `εmach`,
        
    - stabilnością algorytmów.
        

---

# 38. Najważniejsze wnioski z wykładu

1. Każde obliczenie numeryczne jest przybliżeniem.
    
2. Źródłem błędów jest reprezentacja maszynowa.
    
3. Algorytmy mogą być stabilne albo niestabilne.
    
4. Problemy mogą być dobrze albo źle uwarunkowane.
    
5. Sposób liczenia ma znaczenie.
    
6. Dwa wzory algebraicznie równoważne mogą zachowywać się inaczej numerycznie.
    
7. Przy liczbach zmiennoprzecinkowych nie należy bezpośrednio porównywać wartości przez `==`.
    
8. Błędy mogą się kumulować, szczególnie w długich obliczeniach.
    
9. Odejmowanie liczb bardzo bliskich może prowadzić do utraty cyfr znaczących.
    
10. Algorytmy kompensowane, np. Kahana, pomagają ograniczyć błędy sumowania.
    

---

# 39. Szybka ściąga pojęć

|Pojęcie|Znaczenie|
|---|---|
|Błąd bezwzględny|Różnica między wartością dokładną a przybliżeniem|
|Błąd względny|Błąd odniesiony do skali wartości dokładnej|
|Cyfry znaczące|Miara dokładności związana z błędem względnym|
|Błąd zaokrąglenia|Błąd wynikający ze skończonej reprezentacji liczby w komputerze|
|`εmach`|Najmniejsza liczba dodatnia, dla której `1 + ε > 1`|
|Mantysa|Część liczby zmiennopozycyjnej decydująca o dokładności|
|Wykładnik|Część liczby zmiennopozycyjnej decydująca o zakresie|
|Overflow|Wynik poza zakresem, np. przejście do `∞`|
|Underflow|Wynik zbyt mały, przejście do `0` lub liczby zdenormalizowanej|
|`NaN`|Wynik nieokreślony, np. `0.0/0.0`|
|`Inf`|Nieskończoność, np. `1.0/0.0`|
|Stabilność algorytmu|Algorytm nie wzmacnia znacząco błędów zaokrągleń|
|Uwarunkowanie problemu|Wrażliwość wyniku na zaburzenia danych wejściowych|
|Katastrofalna utrata cyfr znaczących|Utrata dokładności przy odejmowaniu liczb bliskich|
|Algorytm Kahana|Metoda kompensowanego sumowania ograniczająca utratę małych składników|

---

# Metody numeryczne — wykład 2: Macierze

## 1. Definicja macierzy

**Macierzą** nazywamy prostokątną tablicę liczb o wymiarze `m × n`, czyli mającą `m` wierszy i `n` kolumn.

Ogólny zapis macierzy:

$$  
A =  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & \dots & a_{1,n} \\  
a_{2,1} & a_{2,2} & \dots & a_{2,n} \\  
\vdots & \vdots & \ddots & \vdots \\  
a_{m,1} & a_{m,2} & \dots & a_{m,n}  
\end{bmatrix}  
$$

W skrócie macierz zapisujemy jako:

$$  
A = [a_{i,j}]  
$$

gdzie `a_{i,j}` oznacza element leżący w `i`-tym wierszu i `j`-tej kolumnie.

### Przykład

Macierz:

$$  
A =  
\begin{bmatrix}  
1 & 2 & 3 \\  
4 & 5 & 6  
\end{bmatrix}  
$$

ma wymiar `2 × 3`, ponieważ ma 2 wiersze i 3 kolumny.

### Przykład w Pythonie

```python
A = [
    [1, 2, 3],
    [4, 5, 6]
]

liczba_wierszy = len(A)
liczba_kolumn = len(A[0])

print("Macierz A:")
print(A)

print("Liczba wierszy:", liczba_wierszy)
print("Liczba kolumn:", liczba_kolumn)
print("Wymiar macierzy:", liczba_wierszy, "x", liczba_kolumn)
```

Wynik:

```text
Macierz A:
[[1, 2, 3], [4, 5, 6]]
Liczba wierszy: 2
Liczba kolumn: 3
Wymiar macierzy: 2 x 3
```

---

## 2. Oznaczenia w macierzy

Dla macierzy:

$$  
A = [a_{i,j}]  
$$

oznaczenia są następujące:

- `a_{i,j}` — element macierzy,
    
- `i` — numer wiersza,
    
- `j` — numer kolumny,
    
- `a_{1,1}, a_{2,2}, a_{3,3}, ...` — elementy diagonali,
    
- `m × n` — wymiar macierzy.
    

### Przykład

Dla macierzy:

$$  
A =  
\begin{bmatrix}  
7 & 8 \\  
9 & 10  
\end{bmatrix}  
$$

element:

$$  
a_{2,1} = 9  
$$

bo znajduje się w drugim wierszu i pierwszej kolumnie.

### Przykład w Pythonie

W Pythonie indeksowanie zaczyna się od `0`, więc element `a_{2,1}` matematycznie zapisujemy jako `A[1][0]`.

```python
A = [
    [7, 8],
    [9, 10]
]

element = A[1][0]

print("Element a_2,1 =", element)
```

Wynik:

```text
Element a_2,1 = 9
```

---

# 3. Normy wektorowe

Dla wektora:

$$  
x = (x_1, x_2, \dots, x_n) \in \mathbb{R}^n  
$$

najczęściej używane normy to:

## 3.1. Norma euklidesowa

$$  
|x|_2 = \sqrt{\sum_{i=1}^{n} x_i^2}  
$$

Norma euklidesowa odpowiada zwykłej długości wektora.

### Przykład

Dla wektora:

$$  
x = (3,4)  
$$

mamy:

$$  
|x|_2 = \sqrt{3^2 + 4^2} = 5  
$$

### Przykład w Pythonie

```python
import math

x = [3, 4]

suma = 0

for xi in x:
    suma += xi ** 2

norma_euklidesowa = math.sqrt(suma)

print(norma_euklidesowa)
```

Wynik:

```text
5.0
```

---

## 3.2. Norma Manhattan

$$  
|x|_1 = \sum_{i=1}^{n} |x_i|  
$$

Norma Manhattan to suma modułów wszystkich współrzędnych.

### Przykład

Dla wektora:

$$  
x = (-3,4)  
$$

mamy:

$$  
|x|_1 = |-3| + |4| = 7  
$$

### Przykład w Pythonie

```python
x = [-3, 4]

suma = 0

for xi in x:
    suma += abs(xi)

norma_manhattan = suma

print(norma_manhattan)
```

Wynik:

```text
7
```

---

## 3.3. Norma maksimum

$$  
|x|_\infty = \max_{1 \leq i \leq n} |x_i|  
$$

Norma maksimum wybiera największą wartość bezwzględną spośród współrzędnych.

W wykładzie zaznaczono, że do porównań liczbowych często używa się normy maksimum, bo jest szybka i pokazuje największy błąd.

### Przykład

Dla wektora:

$$  
x = (-3,4,10,-2)  
$$

mamy:

$$  
|x|_\infty = 10  
$$

### Przykład w Pythonie

```python
x = [-3, 4, 10, -2]

maksimum = abs(x[0])

for xi in x:
    if abs(xi) > maksimum:
        maksimum = abs(xi)

norma_maksimum = maksimum

print(norma_maksimum)
```

Wynik:

```text
10
```

---

# 4. Odległości w $\mathbb{R}^2$ (metryki)

Dla punktów:

$$  
p = (x_1, x_2)  
$$

oraz:

$$  
q = (y_1, y_2)  
$$

w wykładzie podano kilka metryk.

---

## 4.1. Odległość euklidesowa

$$  
d_2(p,q) = \sqrt{(x_1-y_1)^2 + (x_2-y_2)^2}  
$$

To standardowa odległość „po prostej”.

### Przykład

Dla punktów:

$$  
p = (1,2)  
$$

$$  
q = (4,6)  
$$

mamy:

$$  
d_2(p,q) = \sqrt{(1-4)^2 + (2-6)^2} = 5  
$$

### Przykład w Pythonie

```python
import math

p = (1, 2)
q = (4, 6)

d = math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

print(d)
```

Wynik:

```text
5.0
```

---

## 4.2. Odległość Manhattan

$$  
d_1(p,q) = |x_1-y_1| + |x_2-y_2|  
$$

To odległość liczona jako suma przesunięć poziomych i pionowych.

### Przykład

Dla punktów:

$$  
p = (1,2)  
$$

$$  
q = (4,6)  
$$

mamy:

$$  
d_1(p,q) = |1-4| + |2-6| = 7  
$$

### Przykład w Pythonie

```python
p = (1, 2)
q = (4, 6)

d = abs(p[0] - q[0]) + abs(p[1] - q[1])

print(d)
```

Wynik:

```text
7
```

---

## 4.3. Metryka rzeki

W wykładzie podano metrykę rzeki, gdzie rzeka jest osią `Ox`.

$$  
d_R(p,q) =  
\begin{cases}  
|x_2-y_2|, & x_1 = y_1 \\  
|x_1-y_1| + |x_2| + |y_2|, & x_1 \neq y_1  
\end{cases}  
$$

Interpretacja: jeżeli punkty są na tej samej pionowej prostej, przechodzimy bezpośrednio. W przeciwnym razie trzeba dojść do rzeki, przejść wzdłuż niej i odejść od rzeki.

### Przykład

Dla:

$$  
p = (1,2)  
$$

$$  
q = (4,6)  
$$

ponieważ:

$$  
x_1 \neq y_1  
$$

liczymy:

$$  
d_R(p,q) = |1-4| + |2| + |6| = 11  
$$

### Przykład w Pythonie

```python
p = (1, 2)
q = (4, 6)

if p[0] == q[0]:
    d = abs(p[1] - q[1])
else:
    d = abs(p[0] - q[0]) + abs(p[1]) + abs(q[1])

print(d)
```

Wynik:

```text
11
```

---

## 4.4. Metryka kolejowa / centrum

W wykładzie podano też metrykę kolejową, gdzie w razie potrzeby jedzie się przez punkt:

$$  
(0,0)  
$$

Definicja:

$$  
d_C(p,q) =  
\begin{cases}  
|p-q|_2, & p \text{ i } q \text{ leżą na jednej prostej przez } (0,0) \\  
|p|_2 + |q|_2, & \text{w przeciwnym razie}  
\end{cases}  
$$

### Przykład

Dla punktów:

$$  
p = (1,1)  
$$

$$  
q = (2,2)  
$$

punkty leżą na tej samej prostej przechodzącej przez środek układu, więc można liczyć zwykłą odległość euklidesową.

### Przykład w Pythonie

```python
import math

p = (1, 1)
q = (2, 2)

def norma_euklidesowa(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

# Sprawdzamy, czy punkty leżą na jednej prostej przez (0,0).
# Dla punktów p=(x1,x2), q=(y1,y2) warunek współliniowości z (0,0):
# x1*y2 - x2*y1 == 0
if p[0] * q[1] - p[1] * q[0] == 0:
    roznica = (p[0] - q[0], p[1] - q[1])
    d = norma_euklidesowa(roznica)
else:
    d = norma_euklidesowa(p) + norma_euklidesowa(q)

print(d)
```

Wynik:

```text
1.4142135623730951
```

---

# 5. Macierze szczególne

## 5.1. Macierz wierszowa

Macierz wierszowa ma wymiar:

$$  
1 \times n  
$$

czyli składa się z jednego wiersza.

Przykład:

$$  
A =  
\begin{bmatrix}  
1 & 2 & 3 & 4  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [[1, 2, 3, 4]]

print(A)
print("Liczba wierszy:", len(A))
print("Liczba kolumn:", len(A[0]))
```

Wynik:

```text
[[1, 2, 3, 4]]
Liczba wierszy: 1
Liczba kolumn: 4
```

---

## 5.2. Macierz kolumnowa

Macierz kolumnowa ma wymiar:

$$  
m \times 1  
$$

czyli składa się z jednej kolumny.

Przykład:

$$  
A =  
\begin{bmatrix}  
1 \\  
2 \\  
3  
\end{bmatrix}  
$$

Można ją zapisać jako transpozycję macierzy wierszowej:

$$  
A =  
\begin{bmatrix}  
1 & 2 & 3  
\end{bmatrix}^T  
$$

### Transpozycja
```python
A = [[1, 2, 3]]

A_T = []

for i in range(len(A[0])):
    A_T.append([A[0][i]])

print("Macierz wierszowa:")
print(A)

print("Transpozycja, czyli macierz kolumnowa:")
print(A_T)
```
wynik:
```
[1  2  3]^T = [[1],
               [2],
               [3]]
```

### Przykład w Pythonie

```python
A = [
    [1],
    [2],
    [3]
]

print(A)
print("Liczba wierszy:", len(A))
print("Liczba kolumn:", len(A[0]))
```

Wynik:

```text
[[1], [2], [3]]
Liczba wierszy: 3
Liczba kolumn: 1
```

---

## 5.3. Macierz zerowa

Macierz zerowa to macierz, która zawiera same zera.

Przykład:

$$  
A =  
\begin{bmatrix}  
0 & 0 \\  
0 & 0  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
m = 2
n = 3

A = []

for i in range(m): 
	wiersz = [] 
	
	for j in range(n): 
		wiersz.append(0) 
	
	A.append(wiersz)

print(A)
```

Wynik:

```text
[[0, 0, 0], [0, 0, 0]]
```
2 wiersze i 3 kolumny

m x n = 2 x 3

---

## 5.4. Macierz kwadratowa

Macierz kwadratowa to macierz, w której liczba wierszy i kolumn jest taka sama.

Jeżeli macierz ma wymiar:

$$  
n \times n  
$$

to mówimy, że jest macierzą stopnia `n`.

Przykład macierzy kwadratowej stopnia 3:

$$  
A =  
\begin{bmatrix}  
1 & 2 & 3 \\  
4 & 5 & 6 \\  
7 & 8 & 9  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

czy_kwadratowa = len(A) == len(A[0]) # sprawdza czy ma tyle samo wierszy co kolumn

print(czy_kwadratowa)
```

Wynik:

```text
True
```

---

## 5.5. Macierz symetryczna

Macierz symetryczna to macierz kwadratowa, której elementy spełniają warunek:

$$  
a_{i,j} = a_{j,i}  
$$

Równoważnie:

$$  
A^T = A  
$$

Przykład:

$$  
A =  
\begin{bmatrix}  
1 & 2 & 3 \\  
2 & 5 & 6 \\  
3 & 6 & 9  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

n = len(A)
czy_symetryczna = True

for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            czy_symetryczna = False

print(czy_symetryczna)
```

Wynik:

```text
True
```

---

## 5.6. Macierz diagonalna

Macierz diagonalna to macierz kwadratowa, w której wszystkie elementy poza diagonalą są równe zero.

Przykład:

$$  
A =  
\begin{bmatrix}  
2 & 0 & 0 \\  
0 & 5 & 0 \\  
0 & 0 & 7  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [2, 0, 0],
    [0, 5, 0],
    [0, 0, 7]
]

n = len(A)

#---------------------------------------

A = []  
  
for i in range(n):  
	wiersz = []  
  
	for j in range(n):  
		if i == j:  
			wiersz.append(i + 2)  
	else:  
		wiersz.append(0)  
  
	A.append(wiersz)

czy_diagonalna = True

for i in range(n):
    for j in range(n):
        if i != j and A[i][j] != 0:
            czy_diagonalna = False

print(czy_diagonalna)
```

Wynik:

```text
True
```

---

## 5.7. Macierz jednostkowa

Macierz jednostkowa to szczególny przypadek macierzy diagonalnej. Na diagonali ma same jedynki.

Przykład:

$$  
I =  
\begin{bmatrix}  
1 & 0 & 0 \\  
0 & 1 & 0 \\  
0 & 0 & 1  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
n = 3

I = []  
  
for i in range(n):  
	wiersz = []  
  
	for j in range(n):  
		wiersz.append(0)  
  
	I.append(wiersz)
	

for i in range(n):
    I[i][i] = 1

print(I)
```

Wynik:

```text
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

---

## 5.8. Macierz górna trójkątna

Macierz górna trójkątna to macierz kwadratowa, w której elementy poniżej diagonali są równe zero.

Przykład:

$$  
U =  
\begin{bmatrix}  
1 & 2 & 3 \\  
0 & 4 & 5 \\  
0 & 0 & 6  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
U = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

n = len(U)

# ------------------------------------------
n = 3  
  
U = [] 
  
	for i in range(n):  
		wiersz = []  
	  
	for j in range(n):  
		if i <= j:  
			wiersz.append(j + 1)  
	else:  
		wiersz.append(0)  
	  
	U.append(wiersz)

czy_gorna_trojkatna = True

for i in range(n):
    for j in range(n):
        if i > j and U[i][j] != 0:
            czy_gorna_trojkatna = False

print(U)
print(czy_gorna_trojkatna)
```

Wynik:

```text
[[1, 2, 3], [0, 2, 3], [0, 0, 3]]
True
```

---

## 5.9. Macierz dolna trójkątna

Macierz dolna trójkątna to macierz kwadratowa, w której elementy powyżej diagonali są równe zero.

Przykład:

$$  
L =  
\begin{bmatrix}  
1 & 0 & 0 \\  
2 & 3 & 0 \\  
4 & 5 & 6  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
L = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
]

n = len(L)

#--------------------------------------------
n = 3  
  
	L = []  
	  
	for i in range(n):  
		wiersz = []  
	  
	for j in range(n):  
		if i >= j:  
			wiersz.append(i + j + 1)  
	else:  
		wiersz.append(0)  
	  
	L.append(wiersz)

czy_dolna_trojkatna = True

for i in range(n):
    for j in range(n):
        if i < j and L[i][j] != 0:
            czy_dolna_trojkatna = False

print(czy_dolna_trojkatna)
```

Wynik:

```text
True
```

---

# 6. Dodawanie i odejmowanie macierzy

Aby dodać lub odjąć dwie macierze, muszą mieć one takie same wymiary.

Jeżeli:

$$  
A = [a_{i,j}]  
$$

oraz:

$$  
B = [b_{i,j}]  
$$

to:

$$  
A \pm B = [a_{i,j} \pm b_{i,j}]  
$$

Dodawanie i odejmowanie wykonuje się element po elemencie.

### Przykład

$$  
A =  
\begin{bmatrix}  
1 & 2 \\  
3 & 4  
\end{bmatrix}  
$$

$$  
B =  
\begin{bmatrix}  
5 & 6 \\  
7 & 8  
\end{bmatrix}  
$$

$$  
A + B =  
\begin{bmatrix}  
6 & 8 \\  
10 & 12  
\end{bmatrix}  
$$

### Przykład w Pythonie
```python
# wymiary macierzy A
m_A = 2  # liczba wierszy
n_A = 2  # liczba kolumn

# wymiary macierzy B
m_B = 2  # liczba wierszy
n_B = 2  # liczba kolumn


# tworzenie macierzy A od zera
A = []

liczba = 1

for i in range(m_A):
    wiersz = []

    for j in range(n_A):
        wiersz.append(liczba)
        liczba += 1

    A.append(wiersz)


# tworzenie macierzy B od zera
B = []

liczba = 5

for i in range(m_B):
    wiersz = []

    for j in range(n_B):
        wiersz.append(liczba)
        liczba += 1

    B.append(wiersz)


print("Macierz A:")
print(A)

print("Macierz B:")
print(B)


# sprawdzenie, czy można dodać macierze
if len(A) == len(B) and len(A[0]) == len(B[0]):

    C = []

    for i in range(len(A)):
        wiersz = []

        for j in range(len(A[0])):
            wiersz.append(A[i][j] + B[i][j])

        C.append(wiersz)

    print("Macierz C = A + B:")
    print(C)

else:
    print("Nie można dodać macierzy, ponieważ mają różne wymiary.")
```

```python
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = []

for i in range(len(A)):
    wiersz = []
    for j in range(len(A[0])):
        wiersz.append(A[i][j] + B[i][j])
    C.append(wiersz)

print(C)
```

Wynik:

```text
[[6, 8], [10, 12]]
```

---

# 7. Mnożenie macierzy przez liczbę rzeczywistą

Jeżeli macierz `A` mnożymy przez liczbę rzeczywistą `k`, to każdy element macierzy mnożymy przez `k`.

$$  
kA = [ka_{i,j}]  
$$

### Przykład

$$  
A =  
\begin{bmatrix}  
1 & 2 \\  
3 & 4  
\end{bmatrix}  
$$

Dla:

$$  
k = 3  
$$

otrzymujemy:

$$  
3A =  
\begin{bmatrix}  
3 & 6 \\  
9 & 12  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [1, 2],
    [3, 4]
]

k = 3

C = []

for i in range(len(A)):
    wiersz = []
    for j in range(len(A[0])):
        wiersz.append(k * A[i][j])
    C.append(wiersz)

print(C)
```

Wynik:

```text
[[3, 6], [9, 12]]
```

---

# 8. Transpozycja macierzy

Macierz transponowana do macierzy `A` to macierz:

$$  
A^T  
$$

która powstaje przez zamianę wierszy na kolumny i kolumn na wiersze.

### Przykład

$$  
A =  
\begin{bmatrix}  
1 & 2 & 3 \\  
4 & 5 & 6  
\end{bmatrix}  
$$

$$  
A^T =  
\begin{bmatrix}  
1 & 4 \\  
2 & 5 \\  
3 & 6  
\end{bmatrix}  
$$

### Własności transpozycji

$$  
(A^T)^T = A  
$$

$$  
(A \pm B)^T = A^T \pm B^T  
$$

$$  
(kA)^T = kA^T  
$$

$$  
(AB)^T = B^T A^T  
$$

$$  
\det(A^T) = \det(A)  
$$

### Przykład w Pythonie

```python
A = [
    [1, 2, 3],
    [4, 5, 6]
]

AT = []

# przechodzimy po kolumnach macierzy A
for j in range(len(A[0])):
    wiersz = []

    # przechodzimy po wierszach macierzy A
    for i in range(len(A)):
        wiersz.append(A[i][j])

    AT.append(wiersz)

print(AT)
```

Wynik:

```text
[[1, 4], [2, 5], [3, 6]]
```

---

# 9. Normy macierzy

Dla macierzy:

$$  
A = [a_{i,j}] \in \mathbb{R}^{n \times m}  
$$

w wykładzie podano kilka norm.

---

## 9.1. Norma Frobeniusa

$$  
|A|_F = \sqrt{\sum_{i=1}^{n}\sum_{j=1}^{m} a_{i,j}^2}  
$$

Jest to norma euklidesowa wektora otrzymanego przez „spłaszczenie” macierzy.

### Przykład

Dla macierzy:

$$  
A =  
\begin{bmatrix}  
1 & 2 \\  
3 & 4  
\end{bmatrix}  
$$

mamy:

$$  
|A|_F = \sqrt{1^2 + 2^2 + 3^2 + 4^2}  
$$

$$  
|A|_F = \sqrt{30}  
$$

### Przykład w Pythonie

```python
import math

A = [
    [1, 2],
    [3, 4]
]

suma = 0

for i in range(len(A)):
    for j in range(len(A[0])):
        suma += A[i][j] ** 2

norma_frobeniusa = math.sqrt(suma)

print(norma_frobeniusa)
```

Wynik:

```text
5.477225575051661
```

---

## 9.2. Norma Manhattan jako suma modułów elementów

W wykładzie oznaczona jako:

$$  
|A|_{1,sum} = \sum_{i=1}^{n}\sum_{j=1}^{m} |a_{i,j}|  
$$

To suma wartości bezwzględnych wszystkich elementów macierzy.

### Przykład w Pythonie

```python
A = [
    [1, -2],
    [-3, 4]
]

suma = 0

for i in range(len(A)):
    for j in range(len(A[0])):
        suma += abs(A[i][j])

print(suma)
```

Wynik:

```text
10
```

---

## 9.3. Norma maksimum elementowa

$$  
|A|_{max} = \max_{1 \leq i \leq n,\ 1 \leq j \leq m} |a_{i,j}|  
$$

To największy moduł elementu macierzy.

### Przykład w Pythonie

```python
A = [
    [1, -2],
    [-3, 4]
]

maksimum = 0

for i in range(len(A)):
    for j in range(len(A[0])):
        if abs(A[i][j]) > maksimum:
            maksimum = abs(A[i][j])

print(maksimum)
```

Wynik:

```text
4
```

---

## 9.4. Norma operatorowa $|A|_1$

W wykładzie podkreślono ważną uwagę: norma:

$$  
|A|_{1,sum}  
$$

nie jest normą operatorową indukowaną przez normę wektorową:

$$  
|\cdot|_1  
$$

Norma operatorowa ma postać:

$$  
|A|_1 = \max_{1 \leq j \leq m} \sum_{i=1}^{n} |a_{i,j}|  
$$

czyli jest maksymalną sumą modułów w kolumnie.

### Przykład

Dla macierzy:

$$  
A =  
\begin{bmatrix}  
1 & -2 \\  
3 & 4  
\end{bmatrix}  
$$

sumy kolumn wynoszą:

$$  
|1| + |3| = 4  
$$

$$  
|-2| + |4| = 6  
$$

więc:

$$  
|A|_1 = 6  
$$

### Przykład w Pythonie

```python
A = [
    [1, -2],
    [3, 4]
]

liczba_wierszy = len(A)
liczba_kolumn = len(A[0])

najwieksza_suma_kolumny = 0

for j in range(liczba_kolumn):
    suma_kolumny = 0
    for i in range(liczba_wierszy):
        suma_kolumny += abs(A[i][j])

    if suma_kolumny > najwieksza_suma_kolumny:
        najwieksza_suma_kolumny = suma_kolumny

print(najwieksza_suma_kolumny)
```

Wynik:

```text
6
```

### Przykład losowe wartości w macierzy
```python
import random

# wymiary macierzy
m = 2  # liczba wierszy
n = 2  # liczba kolumn

# tworzenie macierzy A z losowych wartości
A = []

for i in range(m):
    wiersz = []

    for j in range(n):
        liczba = random.randint(-10, 10) # osuje liczby całkowite od -10 do 10
        wiersz.append(liczba)

    A.append(wiersz)


print("Macierz A:")
print(A)


# obliczanie normy kolumnowej
norma_kolumnowa = 0

for j in range(n):
    suma_kolumny = 0

    for i in range(m):
        suma_kolumny += abs(A[i][j])

    print("Suma kolumny", j, "=", suma_kolumny)

    if suma_kolumny > norma_kolumnowa:
        norma_kolumnowa = suma_kolumny


print("Norma kolumnowa macierzy A:", norma_kolumnowa)
```

Przykładowy wynik:
```
Macierz A:
[[4, -7], [2, 5]]
Suma kolumny 0 = 6
Suma kolumny 1 = 12
Norma kolumnowa macierzy A: 12
```

---

# 10. Macierz ortogonalna

Macierz ortogonalna to macierz, dla której zachodzi:

$$  
A^T A = I  
$$

Jeżeli macierz jest kwadratowa, to:

$$  
A^T A = AA^T = I  
$$

oraz:

$$  
A^T = A^{-1}  
$$

czyli transpozycja macierzy jest jej macierzą odwrotną.

### Przykład

Macierz jednostkowa jest macierzą ortogonalną:

$$  
I =  
\begin{bmatrix}  
1 & 0 \\  
0 & 1  
\end{bmatrix}  
$$

ponieważ:

$$  
I^T I = I  
$$

### Przykład w Pythonie

```python
A = [
    [1, 0],
    [0, 1]
]

def transponuj(M):
    wynik = []
    for j in range(len(M[0])):
        wiersz = []
        for i in range(len(M)):
            wiersz.append(M[i][j])
        wynik.append(wiersz)
    return wynik

def mnoz_macierze(A, B):
    wynik = []
    for i in range(len(A)):
        wiersz = []
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(B)):
                suma += A[i][k] * B[k][j]
            wiersz.append(suma)
        wynik.append(wiersz)
    return wynik

AT = transponuj(A)
ATA = mnoz_macierze(AT, A)

print(ATA)
```

Wynik:

```text
[[1, 0], [0, 1]]
```

---

# 11. Mnożenie macierzy

Iloczyn macierzy:

$$  
C = AB  
$$

istnieje wtedy, gdy liczba kolumn macierzy `A` jest równa liczbie wierszy macierzy `B`.

Jeżeli:

$$  
A \in \mathbb{R}^{m_1 \times n_1}  
$$

oraz:

$$  
B \in \mathbb{R}^{m_2 \times n_2}  
$$

to iloczyn `AB` istnieje wtedy i tylko wtedy, gdy:

$$  
n_1 = m_2  
$$

Wynik ma wymiar:

$$  
AB \in \mathbb{R}^{m_1 \times n_2}  
$$

Elementy macierzy wynikowej liczymy ze wzoru:

$$  
c_{i,j} = \sum_{l=1}^{n} a_{i,l}b_{l,j}  
$$

Koszt obliczeń:

$$  
\Theta(m_1 \cdot n_1 \cdot n_2)  
$$

### Przykład

$$  
A =  
\begin{bmatrix}  
1 & 2 \\  
3 & 4  
\end{bmatrix}  
$$

$$  
B =  
\begin{bmatrix}  
5 & 6 \\  
7 & 8  
\end{bmatrix}  
$$

Pierwszy element wyniku:

$$  
c_{1,1} = 1 \cdot 5 + 2 \cdot 7 = 19  
$$

Cały wynik:

$$  
AB =  
\begin{bmatrix}  
19 & 22 \\  
43 & 50  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# liczba kolumn macierzy A
kolumny_A = len(A[0])

# liczba wierszy macierzy B
wiersze_B = len(B)

if kolumny_A == wiersze_B:
    C = []

    for i in range(len(A)):
        wiersz = []

        for j in range(len(B[0])):
            suma = 0

            for l in range(len(B)):
                suma += A[i][l] * B[l][j]

            wiersz.append(suma)

        C.append(wiersz)

    print("Macierz C = A * B:")
    print(C)

else:
    print("Nie można pomnożyć macierzy.")
    print("Liczba kolumn macierzy A musi być równa liczbie wierszy macierzy B.")
```

Wynik:

```text
[[19, 22], [43, 50]]
```

---

## 11.1. Własności mnożenia macierzy

Mnożenie macierzy nie jest przemienne:

$$  
AB \neq BA  
$$

Mnożenie macierzy jest łączne:

$$  
(AB)C = A(BC)  
$$

Mnożenie jest rozdzielne względem dodawania:

$$  
A(B+C) = AB + AC  
$$

Macierz jednostkowa jest elementem neutralnym:

$$  
AI = A  
$$

$$  
IA = A  
$$

### Przykład z wykładu: $AB \neq BA$

Dane są macierze:

$$  
A =  
\begin{bmatrix}  
1 & 2 \\  
0 & 1  
\end{bmatrix}  
$$

$$  
B =  
\begin{bmatrix}  
1 & 0 \\  
3 & 1  
\end{bmatrix}  
$$

Wtedy:

$$  
AB =  
\begin{bmatrix}  
7 & 2 \\  
3 & 1  
\end{bmatrix}  
$$

oraz:

$$  
BA =  
\begin{bmatrix}  
1 & 2 \\  
3 & 7  
\end{bmatrix}  
$$

czyli:

$$  
AB \neq BA  
$$

### Przykład w Pythonie

```python
def mnoz_macierze(A, B):
    if len(A[0]) != len(B):
        return None

    C = []

    for i in range(len(A)):
        wiersz = []

        for j in range(len(B[0])):
            suma = 0

            for k in range(len(B)):
                suma += A[i][k] * B[k][j]

            wiersz.append(suma)

        C.append(wiersz)

    return C


A = [
    [1, 2],
    [0, 1]
]

B = [
    [1, 0],
    [3, 1]
]

AB = mnoz_macierze(A, B)
BA = mnoz_macierze(B, A)

print("AB =", AB)
print("BA =", BA)

if AB is not None and BA is not None:
    print("Czy AB == BA?", AB == BA)
else:
    print("Nie można wykonać któregoś mnożenia.")
```

Wynik:

```text
AB = [[7, 2], [3, 1]]
BA = [[1, 2], [3, 7]]
Czy AB == BA? False
```

---

# 12. Przekształcenia elementarne

Elementarne przekształcenia macierzy dzielą się na przekształcenia pierwszego i drugiego rodzaju.

## 12.1. Przekształcenia pierwszego rodzaju

Dotyczą wierszy macierzy.

Są to:

1. przestawienie dwóch wierszy,
    
2. pomnożenie dowolnego wiersza przez liczbę różną od zera,
    
3. dodanie do wiersza krotności innego wiersza.
    

### Przykład w Pythonie

```python
A = [
    [1, 2],
    [3, 4]
]

# Zamiana dwóch wierszy
A[0], A[1] = A[1], A[0]

print(A)
```

Wynik:

```text
[[3, 4], [1, 2]]
```

---

## 12.2. Przekształcenia drugiego rodzaju

Dotyczą kolumn macierzy.

Są to:

1. przestawienie dwóch kolumn,
    
2. pomnożenie dowolnej kolumny przez liczbę różną od zera,
    
3. dodanie do kolumny krotności innej kolumny.
    

### Przykład w Pythonie

```python
A = [
    [1, 2],
    [3, 4]
]

# Zamiana kolumn 0 i 1
for i in range(len(A)):
    A[i][0], A[i][1] = A[i][1], A[i][0]

print(A)
```

Wynik:

```text
[[2, 1], [4, 3]]
```

---

# 13. Znaczenie przekształceń elementarnych

Przekształcenia elementarne są używane między innymi do:

- liczenia rzędu macierzy,
    
- liczenia wyznacznika macierzy kwadratowej,
    
- rozwiązywania układów równań liniowych,
    
- znajdowania macierzy odwrotnej.
    

## 13.1. Wpływ na rząd macierzy

Na rząd macierzy nie mają wpływu żadne operacje elementarne.

Czyli wszystkie przekształcenia elementarne można stosować przy liczeniu rzędu.

### Przykład w Pythonie

Poniżej przykład pokazuje, że po dodaniu wielokrotności jednego wiersza do drugiego macierz zmienia wygląd, ale operacja jest elementarna.

```python
A = [
    [1, 2],
    [3, 4]
]

# R2 := R2 - 3 * R1
for j in range(len(A[0])):
    A[1][j] = A[1][j] - 3 * A[0][j]

print(A)
```

Wynik:

```text
[[1, 2], [0, -2]]
```

---

## 13.2. Wpływ operacji elementarnych na wyznacznik

Przy liczeniu wyznacznika:

1. Dodanie wielokrotności jednego wiersza do drugiego nie zmienia wyznacznika.
    
2. Pomnożenie wiersza lub kolumny przez `k` mnoży wyznacznik przez `k`.
    
3. Zamiana miejscami dwóch wierszy lub kolumn zmienia znak wyznacznika.
    

### Przykład w Pythonie

```python
def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

A = [
    [1, 2],
    [3, 4]
]

print("det(A) =", det2(A))

# Zamiana wierszy
B = [
    [3, 4],
    [1, 2]
]

print("det(B) =", det2(B))
```

Wynik:

```text
det(A) = -2
det(B) = 2
```

Po zamianie wierszy znak wyznacznika się zmienił.

---

# 14. Wyznacznik macierzy

Wyznacznik to funkcja przyporządkowująca każdej macierzy kwadratowej pewną liczbę.

Wyznacznik macierzy `A` oznaczamy jako:

$$  
\det(A)  
$$

albo:

$$  
|A|  
$$

Jeżeli:

$$  
\det(A) \neq 0  
$$

to macierz `A` nazywa się **nieosobliwą**.

Jeżeli:

$$  
\det(A) = 0  
$$

to macierz `A` nazywa się **osobliwą**.

### Własności wyznacznika

$$  
\det(A) = \det(A^T)  
$$

$$  
\det(AB) = \det(A)\det(B)  
$$

### Przykład w Pythonie

```python
def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

A = [
    [1, 2],
    [3, 4]
]

d = det2(A)

print("det(A) =", d)

if d != 0:
    print("Macierz jest nieosobliwa")
else:
    print("Macierz jest osobliwa")
```

Wynik:

```text
det(A) = -2
Macierz jest nieosobliwa
```

### Wersja dla dowolnej macierzy kwadratowej n x n
```python
def czy_kwadratowa(A):
    liczba_wierszy = len(A)

    for i in range(liczba_wierszy):
        if len(A[i]) != liczba_wierszy:
            return False

    return True


def minor(A, wiersz_usuniety, kolumna_usunieta):
    M = []

    for i in range(len(A)):
        if i != wiersz_usuniety:
            nowy_wiersz = []

            for j in range(len(A[i])):
                if j != kolumna_usunieta:
                    nowy_wiersz.append(A[i][j])

            M.append(nowy_wiersz)

    return M


def det(A):
    if not czy_kwadratowa(A):
        return None

    n = len(A)

    if n == 1:
        return A[0][0]

    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    wyznacznik = 0

    for j in range(n):
        znak = (-1) ** j
        wyznacznik += znak * A[0][j] * det(minor(A, 0, j))

    return wyznacznik
```

---

# 15. Wyznacznik metodą Laplace'a

Rozwinięcie Laplace'a pozwala obliczać wyznacznik rekurencyjnie.

Dla macierzy stopnia 1:

$$  
A = [a_{1,1}]  
$$

$$  
\det(A) = a_{1,1}  
$$

Dla macierzy stopnia większego niż 1:

$$  
\det(A) = \sum_{i=1}^{n} (-1)^{i+j}a_{i,j}M_{i,j}  
$$

gdzie `M_{i,j}` to wyznacznik macierzy powstałej z `A` przez skreślenie `i`-tego wiersza i `j`-tej kolumny.

W wykładzie ta definicja jest oparta o rozwinięcie wzdłuż `j`-tej kolumny.

### Przypadek macierzy 2 × 2

Dla:

$$  
A =  
\begin{bmatrix}  
a_{1,1} & a_{1,2} \\  
a_{2,1} & a_{2,2}  
\end{bmatrix}  
$$

mamy:

$$  
\det(A) = a_{1,1}a_{2,2} - a_{1,2}a_{2,1}  
$$

### Przykład w Pythonie

```python
def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

A = [
    [2, 1],
    [5, 3]
]

print(det2(A))
```

Wynik:

```text
1
```

---

## 15.1. Wyznacznik macierzy 3 × 3

Dla macierzy:

$$  
A =  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & a_{1,3} \\  
a_{2,1} & a_{2,2} & a_{2,3} \\  
a_{3,1} & a_{3,2} & a_{3,3}  
\end{bmatrix}  
$$

wyznacznik ma postać:

$$  
\det(A) =  
a_{1,1}a_{2,2}a_{3,3}  
+ a_{1,2}a_{2,3}a_{3,1}  
+ a_{1,3}a_{2,1}a_{3,2}  
- a_{1,3}a_{2,2}a_{3,1}  
- a_{1,1}a_{2,3}a_{3,2}  
- a_{1,2}a_{2,1}a_{3,3}  
$$

### Przykład w Pythonie

```python
def det3(A):
    a = A[0][0]
    b = A[0][1]
    c = A[0][2]

    d = A[1][0]
    e = A[1][1]
    f = A[1][2]

    g = A[2][0]
    h = A[2][1]
    i = A[2][2]

    wyznacznik = (
        a * e * i
        + b * f * g
        + c * d * h
        - c * e * g
        - b * d * i
        - a * f * h
    )

    return wyznacznik


A = [
    [1, 2, 1],
    [2, 3, 1],
    [1, 1, 1]
]

print(det3(A))
```

Wynik:

```text
-1
```

---

## 15.2. Algorytm rekurencyjny Laplace'a

Algorytm z wykładu:

```text
det(A):
    n = size(A)

    if n == 1:
        return A[1][1]

    if n == 2:
        return A[1][1] * A[2][2] - A[1][2] * A[2][1]

    s = 0

    for j = 1..n:
        M = minor(A, row=1, col=j)
        s += (-1)^(1+j) * A[1][j] * det(M)

    return s
```

Wada: koszt rośnie bardzo szybko, więc dla dużych macierzy ta metoda jest niepraktyczna.

### Przykład w Pythonie

```python
def minor(A, wiersz_do_usuniecia, kolumna_do_usuniecia):
    M = []

    for i in range(len(A)):
        if i == wiersz_do_usuniecia:
            continue

        nowy_wiersz = []

        for j in range(len(A)):
            if j == kolumna_do_usuniecia:
                continue

            nowy_wiersz.append(A[i][j])

        M.append(nowy_wiersz)

    return M


def det_laplace(A):
    n = len(A)

    if n == 1:
        return A[0][0]

    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    suma = 0

    # rozwinięcie wzdłuż pierwszego wiersza
    for j in range(n):
        znak = (-1) ** j
        suma += znak * A[0][j] * det_laplace(minor(A, 0, j))

    return suma


A = [
    [1, 2, 1],
    [2, 3, 1],
    [1, 1, 1]
]

print(det_laplace(A))
```

Wynik:

```text
-1
```

---

# 16. Macierz odwrotna

Dla macierzy kwadratowej `A` macierzą odwrotną jest macierz:

$$  
A^{-1}  
$$

spełniająca warunek:

$$  
A \cdot A^{-1} = A^{-1} \cdot A = I  
$$

gdzie `I` to macierz jednostkowa.

Warunkiem koniecznym i wystarczającym istnienia macierzy odwrotnej jest:

$$  
\det(A) \neq 0  
$$

### Przykład w Pythonie

```python
def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

A = [
    [2, 1],
    [5, 3]
]

if det2(A) != 0:
    print("Macierz odwrotna istnieje")
else:
    print("Macierz odwrotna nie istnieje")
```

Wynik:

```text
Macierz odwrotna istnieje
```

---

## 16.1. Macierz odwrotna dla macierzy 2 × 2

Dla macierzy:

$$  
A =  
\begin{bmatrix}  
a & b \\  
c & d  
\end{bmatrix}  
$$

jeżeli:

$$  
\det(A) \neq 0  
$$

to:

$$  
A^{-1} =  
\frac{1}{ad-bc}  
\begin{bmatrix}  
d & -b \\  
-c & a  
\end{bmatrix}  
$$

### Przykład

Dla macierzy:

$$  
A =  
\begin{bmatrix}  
2 & 1 \\  
5 & 3  
\end{bmatrix}  
$$

wyznacznik wynosi:

$$  
\det(A) = 2 \cdot 3 - 1 \cdot 5 = 1  
$$

więc:

$$  
A^{-1} =  
\begin{bmatrix}  
3 & -1 \\  
-5 & 2  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
def inverse2(A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]

    det = a * d - b * c

    if det == 0:
        raise ValueError("Macierz osobliwa, brak macierzy odwrotnej")

    return [
        [d / det, -b / det],
        [-c / det, a / det]
    ]


A = [
    [2, 1],
    [5, 3]
]

A_inv = inverse2(A)

print(A_inv)
```

Wynik:

```text
[[3.0, -1.0], [-5.0, 2.0]]
```

---

## 16.2. Odwracanie macierzy przez dopełnienia

Niech `A` będzie nieosobliwą macierzą kwadratową, czyli:

$$  
\det(A) \neq 0  
$$

Dopełnienie algebraiczne elementu `a_{i,j}`:

$$  
A_{i,j} = (-1)^{i+j}M_{i,j}  
$$

gdzie `M_{i,j}` to wyznacznik macierzy powstałej przez usunięcie `i`-tego wiersza i `j`-tej kolumny.

Macierz odwrotną można otrzymać ze wzoru:

$$  
A^{-1} = \frac{1}{\det(A)}(A^D)^T  
$$

gdzie:

- `A^D` — macierz dopełnień algebraicznych,
    
- `(A^D)^T` — macierz dołączona.
    

```
inverse_cofactor(A): 
	n = size(A) 
	d = det(A) 
	if d == 0: error("singular") 
	C = zeros(n,n) # macierz dopełnień 
	for i = 1..n: 
		for j = 1..n: 
			M = minor(A, row=i, col=j) 
			C[i][j] = (-1)^(i+j) * det(M) 
Adj = transpose(C) # macierz dołączona 
return (1/d) * Adj
```

### Przykład w Pythonie

```python
def minor(A, wiersz_do_usuniecia, kolumna_do_usuniecia):
    M = []

    for i in range(len(A)):
        if i == wiersz_do_usuniecia:
            continue

        nowy_wiersz = []

        for j in range(len(A)):
            if j == kolumna_do_usuniecia:
                continue

            nowy_wiersz.append(A[i][j])

        M.append(nowy_wiersz)

    return M


def det_laplace(A):
    n = len(A)

    if n == 1:
        return A[0][0]

    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    suma = 0

    for j in range(n):
        suma += ((-1) ** j) * A[0][j] * det_laplace(minor(A, 0, j))

    return suma


def transponuj(A):
    AT = []

    for j in range(len(A[0])):
        wiersz = []
        for i in range(len(A)):
            wiersz.append(A[i][j])
        AT.append(wiersz)

    return AT


def inverse_cofactor(A):
    n = len(A)
    d = det_laplace(A)

    if d == 0:
        raise ValueError("Macierz osobliwa")

    C = []

    for i in range(n):
        wiersz = []
        for j in range(n):
            M = minor(A, i, j)
            dopelnienie = ((-1) ** (i + j)) * det_laplace(M)
            wiersz.append(dopelnienie)
        C.append(wiersz)

    Adj = transponuj(C)

    A_inv = []

    for i in range(n):
        wiersz = []
        for j in range(n):
            wiersz.append(Adj[i][j] / d)
        A_inv.append(wiersz)

    return A_inv


A = [
    [2, 1],
    [5, 3]
]

print(inverse_cofactor(A))
```

Wynik:

```text
[[3.0, -1.0], [-5.0, 2.0]]
```

Uwaga z wykładu: ta metoda jest w praktyce bardzo droga obliczeniowo, ponieważ wymaga liczenia wyznaczników minorów.

---

## 16.3. Zależności dla macierzy odwrotnej

W wykładzie podano następujące zależności:

$$  
(A^{-1})^{-1} = A  
$$

$$  
(kA)^{-1} = \frac{1}{k}A^{-1}  
$$

gdzie:

$$  
k \neq 0  
$$

$$  
(A^T)^{-1} = (A^{-1})^T  
$$

$$  
(AB)^{-1} = B^{-1}A^{-1}  
$$

$$  
\det(A^{-1}) = \frac{1}{\det(A)}  
$$

### Przykład w Pythonie

```python
def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

A = [
    [2, 1],
    [5, 3]
]

det_A = det2(A)

print("det(A) =", det_A)
print("det(A^-1) =", 1 / det_A)
```

Wynik:

```text
det(A) = 1
det(A^-1) = 1.0
```

---

# 17. Metoda Gaussa i metoda Gaussa-Jordana

## 17.1. Eliminacja Gaussa

Eliminacja Gaussa polega na sprowadzeniu macierzy `A` do postaci trójkątnej górnej.

Następnie układ równań można rozwiązać przez podstawianie wsteczne.

W wykładzie podano też, że prowadzi to do rozkładu:

$$  
A = LU  
$$

### Przykład w Pythonie

Poniżej sprowadzamy macierz do postaci trójkątnej górnej.

```python
A = [
    [1.0, 2.0, 1.0],
    [2.0, 3.0, 1.0],
    [1.0, 1.0, 1.0]
]

n = len(A)

for k in range(n - 1):
    for i in range(k + 1, n):
        m = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] = A[i][j] - m * A[k][j]

print(A)
```

Wynik:

```text
[[1.0, 2.0, 1.0], [0.0, -1.0, -1.0], [0.0, 0.0, 1.0]]
```

---

## 17.2. Metoda Gaussa-Jordana

Metoda Gaussa-Jordana sprowadza macierz do postaci jednostkowej.

Eliminowane są elementy zarówno poniżej, jak i powyżej pivota.

Można dzięki niej bezpośrednio wyznaczać:

- macierz odwrotną,
    
- wyznacznik.
    

### Schemat z wykładu

Dla:

$$  
k = 1, \dots, n  
$$

1. wybieramy pivot,
    
2. normalizujemy wiersz:
    

$$  
R_k := \frac{1}{a_{k,k}}R_k  
$$

3. dla wszystkich:
    

$$  
i \neq k  
$$

wykonujemy:

$$  
R_i := R_i - a_{i,k}R_k  
$$

Efekt końcowy:

$$  
A \to I  
$$

### Przykład w Pythonie

```python
A = [
    [2.0, 1.0],
    [5.0, 3.0]
]

n = len(A)

for k in range(n):
    pivot = A[k][k]

    # Normalizacja wiersza z pivotem
    for j in range(n):
        A[k][j] = A[k][j] / pivot

    # Zerowanie pozostałych elementów w kolumnie k
    for i in range(n):
        if i != k:
            wspolczynnik = A[i][k]
            for j in range(n):
                A[i][j] = A[i][j] - wspolczynnik * A[k][j]

print(A)
```

Wynik:

```text
[[1.0, 0.0], [0.0, 1.0]]
```

---

# 18. Operacje elementarne a wyznacznik w metodzie Gaussa

Dopuszczalne operacje wierszowe:

1. zamiana wierszy:
    

$$  
R_i \leftrightarrow R_j  
$$

2. mnożenie wiersza przez skalar:
    

$$  
\lambda  
$$

3. dodanie wielokrotności wiersza do innego wiersza.
    

Wpływ na wyznacznik:

- zamiana wierszy zmienia znak wyznacznika,
    
- mnożenie wiersza przez `λ` mnoży wyznacznik przez `λ`,
    
- dodanie wielokrotności wiersza nie zmienia wyznacznika.
    

Po sprowadzeniu do postaci trójkątnej:

$$  
\det(A) = (-1)^p \prod_{i=1}^{n} u_{i,i}  
$$

gdzie `p` to liczba zamian wierszy.

### Przykład z wykładu

Macierz:

$$  
A =  
\begin{bmatrix}  
1 & 2 & 1 \\  
2 & 3 & 1 \\  
1 & 1 & 1  
\end{bmatrix}  
$$

po eliminacji trójkątnej:

$$  
U =  
\begin{bmatrix}  
1 & 2 & 1 \\  
0 & -1 & -1 \\  
0 & 0 & 1  
\end{bmatrix}  
$$

Wyznacznik:

$$  
\det(A) = 1 \cdot (-1) \cdot 1 = -1  
$$

### Przykład w Pythonie

```python
A = [
    [1.0, 2.0, 1.0],
    [2.0, 3.0, 1.0],
    [1.0, 1.0, 1.0]
]

n = len(A)

for k in range(n - 1):
    for i in range(k + 1, n):
        m = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] = A[i][j] - m * A[k][j]

det = 1

for i in range(n):
    det *= A[i][i]

print("Macierz U:")
print(A)
print("det(A) =", det)
```

Wynik:

```text
Macierz U:
[[1.0, 2.0, 1.0], [0.0, -1.0, -1.0], [0.0, 0.0, 1.0]]
det(A) = -1.0
```

---

# 19. Eliminacja Gaussa bez pivotingu

Dla:

$$  
k = 1, \dots, n-1  
$$

wykonuje się kroki:

1. przyjmujemy pivot:
    

$$  
a_{k,k}  
$$

2. dla:
    

$$  
i = k+1, \dots, n  
$$

liczymy:

$$  
m_{i,k} = \frac{a_{i,k}}{a_{k,k}}  
$$

3. aktualizujemy wiersze:
    

$$  
R_i := R_i - m_{i,k}R_k  
$$

Wymaganie:

$$  
a_{k,k} \neq 0  
$$

Problem: metoda może być niestabilna numerycznie przy małych pivotach.

### Przykład w Pythonie

```python
A = [
    [2.0, 1.0],
    [4.0, 3.0]
]

n = len(A)

for k in range(n - 1):
    if A[k][k] == 0:
        raise ValueError("Pivot jest równy zero")

    for i in range(k + 1, n):
        m = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] = A[i][j] - m * A[k][j]

print(A)
```

Wynik:

```text
[[2.0, 1.0], [0.0, 1.0]]
```

---

# 20. Eliminacja Gaussa z pivotingiem częściowym

W pivotingu częściowym dla każdej kolumny `k` wybiera się wiersz `p`, taki że:

$$  
|a_{p,k}| = \max_{i=k,\dots,n}|a_{i,k}|  
$$

Następnie zamienia się wiersze:

$$  
R_k \leftrightarrow R_p  
$$

i wykonuje standardową eliminację.

### Zalety pivotingu

- poprawia stabilność numeryczną,
    
- ogranicza propagację błędów zaokrągleń.
    

### Przykład w Pythonie

```python
A = [
    [0.0001, 1.0],
    [1.0, 1.0]
]

n = len(A)

for k in range(n - 1):
    # Wybór wiersza z największym elementem w kolumnie k
    p = k

    for i in range(k + 1, n):
        if abs(A[i][k]) > abs(A[p][k]):
            p = i

    # Zamiana wierszy
    A[k], A[p] = A[p], A[k]

    # Eliminacja
    for i in range(k + 1, n):
        m = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] = A[i][j] - m * A[k][j]

print(A)
```

Wynik:

```text
[[1.0, 1.0], [0.0, 0.9999]]
```

---

# 21. Metoda Gaussa-Jordana – schemat postępowania

Metoda Gaussa-Jordana sprowadza macierz do postaci jednostkowej.

Dla:

$$  
k = 1, \dots, n  
$$

wykonuje się następujące kroki:

1. Wybór pivota, opcjonalnie z pivotingiem.
    
2. Normalizacja wiersza:
    

$$  
R_k := \frac{1}{a_{k,k}}R_k  
$$

czyli cały wiersz z pivotem dzielimy przez wartość pivota, aby na diagonali otrzymać `1`.

3. Dla wszystkich:
    

$$  
i \neq k  
$$

wykonujemy:

$$  
R_i := R_i - a_{i,k}R_k  
$$

czyli zerujemy wszystkie pozostałe elementy w kolumnie pivota.

Efekt końcowy:

$$  
A \to I  
$$

czyli macierz `A` zostaje sprowadzona do macierzy jednostkowej.

### Przykład

Weźmy macierz:

$$  
A =  
\begin{bmatrix}  
2 & 1 \\  
5 & 3  
\end{bmatrix}  
$$

Po zastosowaniu metody Gaussa-Jordana macierz zostanie sprowadzona do postaci:

$$  
I =  
\begin{bmatrix}  
1 & 0 \\  
0 & 1  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [2.0, 1.0],
    [5.0, 3.0]
]

n = len(A)

for k in range(n):
    # 1. Wybór pivota
    pivot = A[k][k]

    if pivot == 0:
        raise ValueError("Pivot jest równy zero")

    # 2. Normalizacja wiersza:
    # R_k := (1 / a_kk) * R_k
    for j in range(n):
        A[k][j] = A[k][j] / pivot

    # 3. Zerowanie pozostałych elementów w kolumnie k
    # R_i := R_i - a_ik * R_k
    for i in range(n):
        if i != k:
            wspolczynnik = A[i][k]

            for j in range(n):
                A[i][j] = A[i][j] - wspolczynnik * A[k][j]

print(A)
```

Wynik:

```text
[[1.0, 0.0], [0.0, 1.0]]
```

### Wersja z pivotingiem częściowym

Pivoting częściowy polega na tym, że w kolumnie `k` szukamy wiersza z największą wartością bezwzględną elementu w tej kolumnie, a potem zamieniamy ten wiersz z wierszem `k`.

```python
A = [
    [0.0001, 1.0],
    [1.0, 1.0]
]

n = len(A)

for k in range(n):
    # Wybór pivota z pivotingiem częściowym
    p = k
    najwiekszy = abs(A[k][k])

    for i in range(k + 1, n):
        if abs(A[i][k]) > najwiekszy:
            najwiekszy = abs(A[i][k])
            p = i

    # Zamiana wierszy, jeśli znaleziono lepszy pivot
    if p != k:
        A[k], A[p] = A[p], A[k]

    pivot = A[k][k]

    if pivot == 0:
        raise ValueError("Pivot jest równy zero")

    # Normalizacja wiersza z pivotem
    for j in range(n):
        A[k][j] = A[k][j] / pivot

    # Zerowanie pozostałych elementów w kolumnie k
    for i in range(n):
        if i != k:
            wspolczynnik = A[i][k]

            for j in range(n):
                A[i][j] = A[i][j] - wspolczynnik * A[k][j]

print(A)
```

Wynik:

```text
[[1.0, 0.0], [0.0, 1.0]]
```

### Ważne

Metoda Gaussa-Jordana eliminuje elementy zarówno poniżej, jak i powyżej pivota. Dzięki temu na końcu otrzymujemy bezpośrednio macierz jednostkową.

Przy wyznaczaniu macierzy odwrotnej stosuje się macierz rozszerzoną:

$$  
[A \mid I]  
$$

i wykonuje przekształcenia:

$$  
[A \mid I] \to [I \mid A^{-1}]  
$$

---

# 22. Wyznaczanie macierzy odwrotnej metodą Gaussa-Jordana

Tworzymy macierz rozszerzoną:

$$  
[A \mid I]  
$$

Następnie stosujemy metodę Gaussa-Jordana:

$$  
[A \mid I] \to [I \mid A^{-1}]  
$$

Warunek:

$$  
\det(A) \neq 0  
$$

Złożoność obliczeniowa:

$$  
O(n^3)  
$$

### Przykład z wykładu

Dla:

$$  
A =  
\begin{bmatrix}  
2 & 1 \\  
5 & 3  
\end{bmatrix}  
$$

tworzymy macierz rozszerzoną:

$$  
\begin{bmatrix}  
2 & 1 & 1 & 0 \\  
5 & 3 & 0 & 1  
\end{bmatrix}  
$$

Po eliminacji:

$$  
\begin{bmatrix}  
1 & 0 & 3 & -1 \\  
0 & 1 & -5 & 2  
\end{bmatrix}  
$$

czyli:

$$  
A^{-1} =  
\begin{bmatrix}  
3 & -1 \\  
-5 & 2  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [2.0, 1.0],
    [5.0, 3.0]
]

n = len(A)

# Tworzymy macierz rozszerzoną [A | I]
AI = []

for i in range(n):
    wiersz = []

    for j in range(n):
        wiersz.append(A[i][j])

    for j in range(n):
        if i == j:
            wiersz.append(1.0)
        else:
            wiersz.append(0.0)

    AI.append(wiersz)

# Gauss-Jordan
for k in range(n):
    pivot = AI[k][k]

    if pivot == 0:
        raise ValueError("Pivot równy zero")

    # Normalizacja wiersza
    for j in range(2 * n):
        AI[k][j] = AI[k][j] / pivot

    # Zerowanie kolumny
    for i in range(n):
        if i != k:
            wspolczynnik = AI[i][k]

            for j in range(2 * n):
                AI[i][j] = AI[i][j] - wspolczynnik * AI[k][j]

# Odczytujemy prawą część jako A^-1
A_inv = []

for i in range(n):
    A_inv.append(AI[i][n:])

print(A_inv)
```

Wynik:

```text
[[3.0, -1.0], [-5.0, 2.0]]
```

---

# 23. Uwagi praktyczne z wykładu

W wykładzie podano kilka ważnych uwag praktycznych:

1. Metoda Gaussa-Jordana jest rzadko używana do rozwiązywania układów równań, bo jest mniej efektywna niż metoda oparta o rozkład `LU`.
    
2. Metoda Gaussa-Jordana jest bardzo wygodna do:
    
    - obliczania macierzy odwrotnej,
        
    - analizy rzędu macierzy.
        
3. W praktyce zawsze stosuje się pivoting.
    

### Przykład w Pythonie

Poniższy fragment pokazuje sam wybór pivota, czyli najważniejszy element pivotingu częściowego:

```python
A = [
    [0.001, 2.0],
    [5.0, 3.0]
]

k = 0
p = k

for i in range(k + 1, len(A)):
    if abs(A[i][k]) > abs(A[p][k]):
        p = i

print("Najlepszy wiersz na pivot:", p)
print("Wartość pivota:", A[p][k])
```

Wynik:

```text
Najlepszy wiersz na pivot: 1
Wartość pivota: 5.0
```

---

# 24. Najważniejsze rzeczy do zapamiętania na kolosa

## 24.1. Macierz

Macierz to prostokątna tablica liczb o wymiarze:

$$  
m \times n  
$$

### Python

```python
A = [
    [1, 2],
    [3, 4]
]

print(len(A), "x", len(A[0]))
```

---

## 24.2. Element macierzy

Element:

$$  
a_{i,j}  
$$

leży w `i`-tym wierszu i `j`-tej kolumnie.

### Python

```python
A = [
    [1, 2],
    [3, 4]
]

print(A[1][0])
```

Wynik:

```text
3
```

---

## 24.3. Dodawanie macierzy

Macierze można dodać tylko wtedy, gdy mają takie same wymiary.

$$  
A+B = [a_{i,j}+b_{i,j}]  
$$

### Python

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

print(C)
```

---

## 24.4. Transpozycja

Transpozycja zamienia wiersze na kolumny.

$$  
(A^T)^T = A  
$$

### Python

```python
A = [[1, 2, 3], [4, 5, 6]]

AT = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

print(AT)
```

---

## 24.5. Mnożenie macierzy

Iloczyn `AB` istnieje, gdy liczba kolumn `A` jest równa liczbie wierszy `B`.

$$  
c_{i,j} = \sum_{l=1}^{n} a_{i,l}b_{l,j}  
$$

### Python

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = []

for i in range(len(A)):
    wiersz = []
    for j in range(len(B[0])):
        suma = 0
        for k in range(len(B)):
            suma += A[i][k] * B[k][j]
        wiersz.append(suma)
    C.append(wiersz)

print(C)
```

---

## 24.6. Mnożenie macierzy nie jest przemienne

Zwykle:

$$  
AB \neq BA  
$$

### Python

```python
A = [[1, 2], [0, 1]]
B = [[1, 0], [3, 1]]

def matmul(A, B):
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]

print(matmul(A, B))
print(matmul(B, A))
```

---

## 24.7. Wyznacznik macierzy 2 × 2

Dla:

$$  
A =  
\begin{bmatrix}  
a & b \  
c & d  
\end{bmatrix}  
$$

mamy:

$$  
\det(A) = ad - bc  
$$

### Python

```python
A = [[2, 1], [5, 3]]

det = A[0][0] * A[1][1] - A[0][1] * A[1][0]

print(det)
```

---

## 24.8. Macierz odwrotna

Macierz odwrotna istnieje wtedy, gdy:

$$  
\det(A) \neq 0  
$$

oraz spełnia:

$$  
A A^{-1} = A^{-1} A = I  
$$

### Python

```python
A = [[2, 1], [5, 3]]

det = A[0][0] * A[1][1] - A[0][1] * A[1][0]

if det != 0:
    print("Macierz odwrotna istnieje")
else:
    print("Macierz odwrotna nie istnieje")
```

---

## 24.9. Gauss bez pivotingu

W eliminacji Gaussa używamy pivota:

$$  
a_{k,k}  
$$

i mnożnika:

$$  
m_{i,k} = \frac{a_{i,k}}{a_{k,k}}  
$$

Potem wykonujemy:

$$  
R_i := R_i - m_{i,k}R_k  
$$

### Python

```python
A = [[2.0, 1.0], [4.0, 3.0]]

m = A[1][0] / A[0][0]

for j in range(2):
    A[1][j] = A[1][j] - m * A[0][j]

print(A)
```

---

## 24.10. Pivoting częściowy

Wybieramy największy element w danej kolumnie jako pivot:

$$  
|a_{p,k}| = \max_{i=k,\dots,n}|a_{i,k}|  
$$

### Python

```python
A = [[0.001, 2.0], [5.0, 3.0]]

k = 0
p = k

for i in range(k + 1, len(A)):
    if abs(A[i][k]) > abs(A[p][k]):
        p = i

A[k], A[p] = A[p], A[k]

print(A)
```

---

# Metody numeryczne — wykład 3: Układy równań liniowych — metody bezpośrednie

## 1. Układ równań liniowych

Układ `m` równań liniowych z `n` niewiadomymi ma postać:

$$  
a_{1,1}x_1 + a_{1,2}x_2 + a_{1,3}x_3 + \dots + a_{1,n}x_n = b_1  
$$

$$  
a_{2,1}x_1 + a_{2,2}x_2 + a_{2,3}x_3 + \dots + a_{2,n}x_n = b_2  
$$

$$  
\dots  
$$

$$  
a_{m,1}x_1 + a_{m,2}x_2 + a_{m,3}x_3 + \dots + a_{m,n}x_n = b_m  
$$

Można go też zapisać krócej:

$$  
\sum_{j=1}^{n} a_{i,j}x_j = b_i  
$$

dla:

$$  
i = 1,2,\dots,m  
$$

### Przykład

Układ:

$$  
2x_1 + x_2 = 5  
$$

$$  
x_1 + 3x_2 = 7  
$$

ma `2` równania i `2` niewiadome.

### Przykład w Pythonie

```python
# Przykładowy układ:
# 2x1 + 1x2 = 5
# 1x1 + 3x2 = 7

A = [
    [2, 1],
    [1, 3]
]

b = [5, 7]

print("Macierz współczynników A:")
print(A)

print("Wektor wyrazów wolnych b:")
print(b)
```

---

## 2. Zapis macierzowy układu równań

Układ równań liniowych można zapisać w postaci macierzowej:

$$  
Ax = b  
$$

gdzie:

- `A` — macierz główna układu, złożona ze współczynników,
    
- `x` — wektor niewiadomych,
    
- `b` — wektor wyrazów wolnych.
    

Macierz współczynników:

$$  
A =  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & \dots & a_{1,n} \\  
a_{2,1} & a_{2,2} & \dots & a_{2,n} \\  
\vdots & \vdots & \ddots & \vdots \\  
a_{m,1} & a_{m,2} & \dots & a_{m,n}  
\end{bmatrix}  
$$

Wektor niewiadomych:

$$  
x =  
\begin{bmatrix}  
x_1 \\  
x_2 \\  
\vdots \\  
x_n  
\end{bmatrix}  
$$

Wektor wyrazów wolnych:

$$  
b =  
\begin{bmatrix}  
b_1 \\  
b_2 \\  
\vdots \\  
b_m  
\end{bmatrix}  
$$

Cały układ:

$$  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & \dots & a_{1,n} \\  
a_{2,1} & a_{2,2} & \dots & a_{2,n} \\  
\vdots & \vdots & \ddots & \vdots \\  
a_{m,1} & a_{m,2} & \dots & a_{m,n}  
\end{bmatrix}  
\begin{bmatrix}  
x_1 \\  
x_2 \\  
\vdots \\  
x_n  
\end{bmatrix}

\begin{bmatrix}  
b_1 \\  
b_2 \\  
\vdots \\  
b_m  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [2, 1],
    [1, 3]
]

x = [1, 2]

b = []

for i in range(len(A)):
    suma = 0

    for j in range(len(A[0])):
        suma = suma + A[i][j] * x[j]

    b.append(suma)

print("Dla x =", x)
print("Ax =", b)
```

Wynik:

```text
Dla x = [1, 2]
Ax = [4, 7]
```

---

## 3. Macierz rozszerzona

Macierz rozszerzona powstaje przez dołączenie do macierzy głównej `A` wektora wyrazów wolnych `b` jako ostatniej kolumny.

Oznaczamy ją jako:

$$  
A_b  
$$

Macierz rozszerzona ma rozmiar:

$$  
m \times (n+1)  
$$

Jeżeli:

$$  
A =  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & \dots & a_{1,n} \  
a_{2,1} & a_{2,2} & \dots & a_{2,n} \  
\vdots & \vdots & \ddots & \vdots \  
a_{m,1} & a_{m,2} & \dots & a_{m,n}  
\end{bmatrix}  
$$

oraz:

$$  
b =  
\begin{bmatrix}  
b_1 \  
b_2 \  
\vdots \  
b_m  
\end{bmatrix}  
$$

to:

$$  
A_b =  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & \dots & a_{1,n} & b_1 \  
a_{2,1} & a_{2,2} & \dots & a_{2,n} & b_2 \  
\vdots & \vdots & \ddots & \vdots & \vdots \  
a_{m,1} & a_{m,2} & \dots & a_{m,n} & b_m  
\end{bmatrix}  
$$

### Przykład

Dla:

$$  
A =  
\begin{bmatrix}  
2 & 1 \  
1 & 3  
\end{bmatrix}  
$$

oraz:

$$  
b =  
\begin{bmatrix}  
5 \  
7  
\end{bmatrix}  
$$

macierz rozszerzona to:

$$  
A_b =  
\begin{bmatrix}  
2 & 1 & 5 \  
1 & 3 & 7  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [2, 1],
    [1, 3]
]

b = [5, 7]

Ab = []

for i in range(len(A)):
    wiersz = []

    for j in range(len(A[0])):
        wiersz.append(A[i][j])

    wiersz.append(b[i])

    Ab.append(wiersz)

print(Ab)
```

Wynik:

```text
[[2, 1, 5], [1, 3, 7]]
```

---

## 4. Rząd macierzy

Macierz można traktować jako zbiór wektorów kolumnowych albo wierszowych.

Największa liczba niezależnych liniowo wektorów kolumnowych w macierzy `A` jest równa największej liczbie niezależnych liniowo wektorów wierszowych w `A`.

Ta liczba nazywa się **rzędem macierzy**.

Oznaczenie:

$$  
rank(A) = r  
$$

### Przykład

Jeżeli jeden wiersz macierzy jest wielokrotnością innego wiersza, to wiersze są liniowo zależne.

Dla macierzy:

$$  
A =  
\begin{bmatrix}  
1 & 2 \  
2 & 4  
\end{bmatrix}  
$$

drugi wiersz jest dwa razy większy od pierwszego, więc rząd nie wynosi `2`.

### Przykład w Pythonie

Prosty przykład sprawdzający zależność dwóch wierszy w macierzy `2 × 2`:

```python
A = [
    [1, 2],
    [2, 4]
]

if A[0][0] != 0:
    wspolczynnik = A[1][0] / A[0][0]

    zalezne = True

    for j in range(len(A[0])):
        if A[1][j] != wspolczynnik * A[0][j]:
            zalezne = False

    if zalezne:
        print("Wiersze są liniowo zależne")
    else:
        print("Wiersze nie są liniowo zależne")
else:
    print("Nie sprawdzam tym sposobem, bo pierwszy element jest równy 0")
```

---

## 5. Twierdzenie Kroneckera-Capellego

Twierdzenie Kroneckera-Capellego pozwala określić liczbę rozwiązań układu równań liniowych na podstawie rzędów macierzy.

### 5.1. Układ oznaczony

Jeżeli:

$$  
rank(A) = rank(A_b) = n  
$$

to układ ma dokładnie jedno rozwiązanie.

Taki układ nazywa się **oznaczony**.

### 5.2. Układ nieoznaczony

Jeżeli:

$$  
rank(A) = rank(A_b) < n  
$$

to układ ma nieskończenie wiele rozwiązań.

Taki układ nazywa się **nieoznaczony**.

### 5.3. Układ sprzeczny

Jeżeli:

$$  
rank(A) < rank(A_b)  
$$

to układ nie ma rozwiązań.

Taki układ nazywa się **sprzeczny**.

### Przykład w Pythonie

```python
rank_A = 2
rank_Ab = 2
n = 2

if rank_A == rank_Ab and rank_A == n:
    print("Układ oznaczony — dokładnie jedno rozwiązanie")
elif rank_A == rank_Ab and rank_A < n:
    print("Układ nieoznaczony — nieskończenie wiele rozwiązań")
elif rank_A < rank_Ab:
    print("Układ sprzeczny — brak rozwiązań")
```

---

## 6. Typy układów równań liniowych

### 6.1. Układ jednorodny

Jeżeli wszystkie wyrazy wolne są równe `0`, to układ nazywa się **jednorodnym**.

Taki układ ma zawsze rozwiązanie.

Czyli:

$$  
b =  
\begin{bmatrix}  
0 \  
0 \  
\vdots \  
0  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
b = [0, 0, 0]

czy_jednorodny = True

for i in range(len(b)):
    if b[i] != 0:
        czy_jednorodny = False

if czy_jednorodny:
    print("Układ jest jednorodny")
else:
    print("Układ nie jest jednorodny")
```

---

### 6.2. Układ kwadratowy

Jeżeli liczba wierszy jest równa liczbie kolumn w macierzy głównej, czyli:

$$  
m = n  
$$

to układ nazywa się **kwadratowym**.

### Przykład w Pythonie

```python
A = [
    [2, 1],
    [1, 3]
]

m = len(A)
n = len(A[0])

if m == n:
    print("Układ jest kwadratowy")
else:
    print("Układ nie jest kwadratowy")
```

---

## 7. Metody rozwiązywania układów równań liniowych

W wykładzie podano dwa główne typy metod:

1. metody bezpośrednie,
    
2. metody iteracyjne.
    

---

## 7.1. Metody bezpośrednie

Metody bezpośrednie dają dokładne rozwiązanie po skończonej liczbie przekształceń układu wejściowego, pomijając błędy zaokrągleń.

Cechy metod bezpośrednich:

- są efektywne dla układów o macierzach pełnych,
    
- mocno obciążają pamięć,
    
- ze względu na błędy zaokrągleń mogą być niestabilne.
    

Do metod bezpośrednich należą między innymi:

- użycie macierzy odwrotnej,
    
- wzory Cramera,
    
- układ równań z macierzą trójkątną,
    
- metoda eliminacji Gaussa,
    
- rozkłady trójkątne macierzy,
    
- metoda Gaussa-Jordana,
    
- metoda Doolittle’a,
    
- metoda Crouta,
    
- metoda Cholesky’ego.
    

### Przykład w Pythonie

```python
metody_bezposrednie = [
    "macierz odwrotna",
    "wzory Cramera",
    "macierz trójkątna",
    "eliminacja Gaussa",
    "rozkład LU",
    "Gauss-Jordan",
    "Doolittle",
    "Crout",
    "Cholesky"
]

for metoda in metody_bezposrednie:
    print(metoda)
```

---

## 7.2. Metody iteracyjne

Metody iteracyjne tworzą ciąg wektorów zbieżny do szukanego rozwiązania.

Cechy metod iteracyjnych:

- liczba kroków nie jest z góry znana,
    
- dobrze sprawdzają się dla macierzy rzadkich o dużych rozmiarach,
    
- obciążenie pamięci nie jest zbyt duże,
    
- mogą wystąpić problemy ze zbieżnością rozwiązania.
    

Do metod iteracyjnych należą między innymi:

- metoda Jacobiego,
    
- metoda Gaussa-Seidela,
    
- metoda Czebyszewa.
    

### Przykład w Pythonie

```python
metody_iteracyjne = [
    "Jacobi",
    "Gauss-Seidel",
    "Czebyszew"
]

for metoda in metody_iteracyjne:
    print(metoda)
```

---

## 8. Macierze pełne i rzadkie

W praktyce macierze współczynników dzielą się na dwie grupy.

---

## 8.1. Macierze pełne

Macierze pełne mają dużo elementów niezerowych.

W wykładzie podano, że nieduże macierze pełne mogą mieć stopień mniejszy np. od `30`.

### Przykład

$$  
A =  
\begin{bmatrix}  
1 & 2 & 3 \  
4 & 5 & 6 \  
7 & 8 & 9  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

liczba_niezerowych = 0

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] != 0:
            liczba_niezerowych = liczba_niezerowych + 1

print("Liczba elementów niezerowych:", liczba_niezerowych)
```

---

## 8.2. Macierze rzadkie

Macierze rzadkie mają mało elementów niezerowych.

W wykładzie podano, że takie macierze często są bardzo duże, np. stopnia `100` lub większego, a elementy niezerowe mogą leżeć blisko głównej diagonali.

### Przykład

$$  
A =  
\begin{bmatrix}  
4 & 1 & 0 & 0 \  
1 & 4 & 1 & 0 \  
0 & 1 & 4 & 1 \  
0 & 0 & 1 & 4  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [4, 1, 0, 0],
    [1, 4, 1, 0],
    [0, 1, 4, 1],
    [0, 0, 1, 4]
]

liczba_zer = 0
liczba_niezerowych = 0

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == 0:
            liczba_zer = liczba_zer + 1
        else:
            liczba_niezerowych = liczba_niezerowych + 1

print("Zera:", liczba_zer)
print("Elementy niezerowe:", liczba_niezerowych)
```

---

# 9. Rozwiązywanie układu za pomocą macierzy odwrotnej

Dla macierzy odwrotnej zachodzi:

$$  
AA^{-1} = A^{-1}A = I  
$$

Układ:

$$  
Ax = b  
$$

można rozwiązać, jeśli znamy macierz odwrotną:

$$  
A^{-1}Ax = A^{-1}b  
$$

czyli:

$$  
Ix = A^{-1}b  
$$

ostatecznie:

$$  
x = A^{-1}b  
$$

### Przykład

Dla:

$$  
A^{-1} =  
\begin{bmatrix}  
3 & -1 \  
-5 & 2  
\end{bmatrix}  
$$

oraz:

$$  
b =  
\begin{bmatrix}  
5 \  
7  
\end{bmatrix}  
$$

liczymy:

$$  
x = A^{-1}b  
$$

### Przykład w Pythonie

```python
A_inv = [
    [3, -1],
    [-5, 2]
]

b = [5, 7]

x = []

for i in range(len(A_inv)):
    suma = 0

    for j in range(len(A_inv[0])):
        suma = suma + A_inv[i][j] * b[j]

    x.append(suma)

print(x)
```

Wynik:

```text
[8, -11]
```

---

# 10. Wzory Cramera

Wzory Cramera są metodą bezpośrednią rozwiązywania układów równań liniowych.

Jeżeli:

$$  
\det(A) \neq 0  
$$

to:

$$  
x_k = \frac{\det(A_k)}{\det(A)}  
$$

dla:

$$  
k = 1,2,\dots,n  
$$

gdzie `A_k` jest macierzą powstałą przez zastąpienie `k`-tej kolumny macierzy `A` wektorem wyrazów wolnych `b`.

### Przykład dla układu 2 × 2

Układ:

$$  
2x_1 + x_2 = 5  
$$

$$  
x_1 + 3x_2 = 7  
$$

Macierz główna:

$$  
A =  
\begin{bmatrix}  
2 & 1 \  
1 & 3  
\end{bmatrix}  
$$

Wektor wyrazów wolnych:

$$  
b =  
\begin{bmatrix}  
5 \  
7  
\end{bmatrix}  
$$

Macierz `A_1`:

$$  
A_1 =  
\begin{bmatrix}  
5 & 1 \  
7 & 3  
\end{bmatrix}  
$$

Macierz `A_2`:

$$  
A_2 =  
\begin{bmatrix}  
2 & 5 \  
1 & 7  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


A = [
    [2, 1],
    [1, 3]
]

b = [5, 7]

A1 = [
    [b[0], A[0][1]],
    [b[1], A[1][1]]
]

A2 = [
    [A[0][0], b[0]],
    [A[1][0], b[1]]
]

det_A = det2(A)
det_A1 = det2(A1)
det_A2 = det2(A2)

if det_A != 0:
    x1 = det_A1 / det_A
    x2 = det_A2 / det_A

    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("Nie można użyć wzorów Cramera, bo det(A) = 0")
```

Wynik:

```text
x1 = 1.6
x2 = 1.8
```

---

## 11. Wzory Cramera — przykład 3 × 3

Dla układu:

$$  
a_{1,1}x_1 + a_{1,2}x_2 + a_{1,3}x_3 = b_1  
$$

$$  
a_{2,1}x_1 + a_{2,2}x_2 + a_{2,3}x_3 = b_2  
$$

$$  
a_{3,1}x_1 + a_{3,2}x_2 + a_{3,3}x_3 = b_3  
$$

obliczamy:

$$  
\det(A) =  
\det  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & a_{1,3} \  
a_{2,1} & a_{2,2} & a_{2,3} \  
a_{3,1} & a_{3,2} & a_{3,3}  
\end{bmatrix}  
$$

Następnie:

# $$  
x_1 =  
\frac{1}{\det(A)}  
\det  
\begin{bmatrix}  
b_1 & a_{1,2} & a_{1,3} \  
b_2 & a_{2,2} & a_{2,3} \  
b_3 & a_{3,2} & a_{3,3}  
\end{bmatrix}

\frac{\det(A_1)}{\det(A)}  
$$

# $$  
x_2 =  
\frac{1}{\det(A)}  
\det  
\begin{bmatrix}  
a_{1,1} & b_1 & a_{1,3} \  
a_{2,1} & b_2 & a_{2,3} \  
a_{3,1} & b_3 & a_{3,3}  
\end{bmatrix}

\frac{\det(A_2)}{\det(A)}  
$$

# $$  
x_3 =  
\frac{1}{\det(A)}  
\det  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & b_1 \  
a_{2,1} & a_{2,2} & b_2 \  
a_{3,1} & a_{3,2} & b_3  
\end{bmatrix}

\frac{\det(A_3)}{\det(A)}  
$$

### Przykład w Pythonie

```python
def det3(A):
    wynik = (
        A[0][0] * A[1][1] * A[2][2]
        + A[0][1] * A[1][2] * A[2][0]
        + A[0][2] * A[1][0] * A[2][1]
        - A[0][2] * A[1][1] * A[2][0]
        - A[0][1] * A[1][0] * A[2][2]
        - A[0][0] * A[1][2] * A[2][1]
    )

    return wynik


A = [
    [1, 1, 1],
    [2, 1, 3],
    [1, -1, 1]
]

b = [6, 13, 2]

A1 = [
    [b[0], A[0][1], A[0][2]],
    [b[1], A[1][1], A[1][2]],
    [b[2], A[2][1], A[2][2]]
]

A2 = [
    [A[0][0], b[0], A[0][2]],
    [A[1][0], b[1], A[1][2]],
    [A[2][0], b[2], A[2][2]]
]

A3 = [
    [A[0][0], A[0][1], b[0]],
    [A[1][0], A[1][1], b[1]],
    [A[2][0], A[2][1], b[2]]
]

det_A = det3(A)

if det_A != 0:
    x1 = det3(A1) / det_A
    x2 = det3(A2) / det_A
    x3 = det3(A3) / det_A

    print("x1 =", x1)
    print("x2 =", x2)
    print("x3 =", x3)
else:
    print("Nie można użyć wzorów Cramera")
```

---

# 12. Układ z macierzą trójkątną górną

Jeżeli macierz układu równań liniowych jest macierzą trójkątną, to układ rozwiązuje się szczególnie łatwo.

Dla macierzy trójkątnej górnej układ ma postać:

$$  
a_{1,1}x_1 + a_{1,2}x_2 + \dots + a_{1,n}x_n = b_1  
$$

$$  
a_{2,2}x_2 + \dots + a_{2,n}x_n = b_2  
$$

$$  
\dots  
$$

$$  
a_{n,n}x_n = b_n  
$$

Aby istniało jednoznaczne rozwiązanie, wszystkie elementy na głównej przekątnej muszą być różne od zera.

Rozwiązanie zaczynamy od ostatniej niewiadomej:

$$  
x_n = \frac{b_n}{a_{n,n}}  
$$

Następnie:

$$  
x_i =  
\frac{  
b_i - \sum_{k=i+1}^{n} a_{i,k}x_k  
}  
{a_{i,i}}  
$$

dla:

$$  
i = n-1, n-2, \dots, 1  
$$

Metoda ta nazywa się **podstawianiem w tył**.

### Przykład

Układ:

$$  
2x_1 + x_2 - x_3 = 1  
$$

$$  
3x_2 + 2x_3 = 12  
$$

$$  
4x_3 = 8  
$$

Z ostatniego równania:

$$  
x_3 = 2  
$$

### Przykład w Pythonie

```python
U = [
    [2.0, 1.0, -1.0],
    [0.0, 3.0, 2.0],
    [0.0, 0.0, 4.0]
]

b = [1.0, 12.0, 8.0]

n = len(U)
x = [0.0, 0.0, 0.0]

for i in range(n - 1, -1, -1):
    suma = 0

    for k in range(i + 1, n):
        suma = suma + U[i][k] * x[k]

    x[i] = (b[i] - suma) / U[i][i]

print(x)
```

---

# 13. Układ z macierzą trójkątną dolną

Dla macierzy trójkątnej dolnej wykonuje się **podstawianie w przód**.

Najpierw liczymy:

$$  
x_1 = \frac{b_1}{a_{1,1}}  
$$

Następnie:

$$  
x_i =  
\frac{  
b_i - \sum_{k=1}^{i-1} a_{i,k}x_k  
}  
{a_{i,i}}  
$$

dla:

$$  
i = 2,3,\dots,n  
$$

### Przykład

Układ:

$$  
2x_1 = 4  
$$

$$  
3x_1 + x_2 = 7  
$$

$$  
x_1 - x_2 + 2x_3 = 3  
$$

### Przykład w Pythonie

```python
L = [
    [2.0, 0.0, 0.0],
    [3.0, 1.0, 0.0],
    [1.0, -1.0, 2.0]
]

b = [4.0, 7.0, 3.0]

n = len(L)
x = [0.0, 0.0, 0.0]

for i in range(n):
    suma = 0

    for k in range(0, i):
        suma = suma + L[i][k] * x[k]

    x[i] = (b[i] - suma) / L[i][i]

print(x)
```

---

# 14. Eliminacja Gaussa

Eliminacja Gaussa polega na sprowadzeniu układu równań do postaci trójkątnej, a następnie rozwiązaniu go przez podstawianie wstecz.

Dla układu `3 × 3`:

$$  
a_{1,1}x_1 + a_{1,2}x_2 + a_{1,3}x_3 = b_1  
$$

$$  
a_{2,1}x_1 + a_{2,2}x_2 + a_{2,3}x_3 = b_2  
$$

$$  
a_{3,1}x_1 + a_{3,2}x_2 + a_{3,3}x_3 = b_3  
$$

celem jest wyzerowanie elementów pod główną przekątną.

### Idea kroku eliminacji

W każdym kroku odejmujemy od jednego wiersza odpowiednią wielokrotność innego wiersza.

Dla pierwszej kolumny:

$$  
R_i := R_i - mR_1  
$$

gdzie:

$$  
m = \frac{a_{i,1}}{a_{1,1}}  
$$

### Przykład w Pythonie

```python
A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]

b = [8.0, -11.0, -3.0]

n = len(A)

# Eliminacja Gaussa
for k in range(n - 1):
    for i in range(k + 1, n):
        m = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] = A[i][j] - m * A[k][j]

        b[i] = b[i] - m * b[k]

print("Macierz po eliminacji:")
print(A)

print("Wektor b po eliminacji:")
print(b)
```

---

## 15. Wzory ogólne w eliminacji Gaussa

Współczynniki macierzy i wyrazy wolne w każdym kroku eliminacji można obliczać ze wzorów:

## $$  
a_{i,j}^{(k)} =  
a_{i,j}^{(k-1)}

\frac{  
a_{i,k}^{(k-1)}a_{k,j}^{(k-1)}  
}  
{  
a_{k,k}^{(k-1)}  
}  
$$

oraz:

## $$  
b_i^{(k)} =  
b_i^{(k-1)}

\frac{  
a_{i,k}^{(k-1)}b_k^{(k-1)}  
}  
{  
a_{k,k}^{(k-1)}  
}  
$$

dla:

$$  
i,j = k+1,k+2,\dots,n  
$$

Po otrzymaniu układu trójkątnego rozwiązujemy go przez podstawianie wstecz:

## $$  
x_i =  
\frac{  
b_i^{(i-1)}

\sum_{j=i+1}^{n} a_{i,j}^{(i-1)}x_j  
}  
{  
a_{i,i}^{(i-1)}  
}  
$$

dla:

$$  
i = n,n-1,\dots,1  
$$

### Przykład w Pythonie

```python
def eliminacja_gaussa(A, b):
    n = len(A)

    for k in range(n - 1):
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]

            for j in range(k, n):
                A[i][j] = A[i][j] - m * A[k][j]

            b[i] = b[i] - m * b[k]

    x = [0.0 for i in range(n)]

    for i in range(n - 1, -1, -1):
        suma = 0

        for j in range(i + 1, n):
            suma = suma + A[i][j] * x[j]

        x[i] = (b[i] - suma) / A[i][i]

    return x


A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]

b = [8.0, -11.0, -3.0]

x = eliminacja_gaussa(A, b)

print(x)
```

---

# 16. Wybór elementu podstawowego

Eliminacja Gaussa w podstawowej formie nie jest niezawodna.

Jeżeli element podstawowy, czyli pivot, jest równy zero, algorytm wymagałby dzielenia przez zero.

Element podstawowy to element macierzy, za pomocą którego dokonujemy eliminacji zmiennej z dalszych równań.

Jeżeli:

$$  
a_{k,k}^{(k)} = 0  
$$

należy zamienić wiersze, aby uzyskać niezerowy pivot.

W praktyce często wybiera się wiersz, w którym element w danej kolumnie ma największą wartość bezwzględną.

### Przykład

Macierz rozszerzona:

$$  
\begin{bmatrix}  
0 & 2 & 2 & | & 1 \  
3 & 3 & 0 & | & 3 \  
1 & 0 & 1 & | & 2  
\end{bmatrix}  
$$

Tu pierwszy pivot byłby równy:

$$  
a_{1,1} = 0  
$$

więc trzeba zamienić wiersze.

### Przykład w Pythonie

```python
Ab = [
    [0.0, 2.0, 2.0, 1.0],
    [3.0, 3.0, 0.0, 3.0],
    [1.0, 0.0, 1.0, 2.0]
]

k = 0
p = k
najwiekszy = abs(Ab[k][k])

for i in range(k + 1, len(Ab)):
    if abs(Ab[i][k]) > najwiekszy:
        najwiekszy = abs(Ab[i][k])
        p = i

Ab[k], Ab[p] = Ab[p], Ab[k]

print(Ab)
```

Wynik:

```text
[[3.0, 3.0, 0.0, 3.0], [0.0, 2.0, 2.0, 1.0], [1.0, 0.0, 1.0, 2.0]]
```

---

# 17. Częściowy wybór elementu głównego

Częściowy wybór elementu głównego polega na tym, że w `i`-tym kroku eliminacji Gaussa patrzymy na elementy w `i`-tej kolumnie i wybieramy wiersz z największą wartością bezwzględną.

Po zamianie wierszy można wykonać kolejny krok eliminacji.

W wykładzie po zamianie wierszy otrzymano macierz:

$$  
\begin{bmatrix}  
3 & 3 & 0 & | & 3 \  
0 & 2 & 2 & | & 1 \  
0 & -1 & 1 & | & 1  
\end{bmatrix}  
$$

Po kolejnym kroku:

$$  
\begin{bmatrix}  
3 & 3 & 0 & | & 3 \  
0 & 2 & 2 & | & 1 \  
0 & 0 & 2 & | & \frac{3}{2}  
\end{bmatrix}  
$$

Końcowe rozwiązanie:

$$  
x_3 = \frac{3}{4}  
$$

$$  
x_2 = -\frac{1}{4}  
$$

$$  
x_1 = \frac{5}{4}  
$$

### Przykład w Pythonie

```python
A = [
    [0.0, 2.0, 2.0],
    [3.0, 3.0, 0.0],
    [1.0, 0.0, 1.0]
]

b = [1.0, 3.0, 2.0]

n = len(A)

for k in range(n - 1):
    p = k
    najwiekszy = abs(A[k][k])

    for i in range(k + 1, n):
        if abs(A[i][k]) > najwiekszy:
            najwiekszy = abs(A[i][k])
            p = i

    if p != k:
        A[k], A[p] = A[p], A[k]
        b[k], b[p] = b[p], b[k]

    for i in range(k + 1, n):
        m = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] = A[i][j] - m * A[k][j]

        b[i] = b[i] - m * b[k]

x = [0.0, 0.0, 0.0]

for i in range(n - 1, -1, -1):
    suma = 0

    for j in range(i + 1, n):
        suma = suma + A[i][j] * x[j]

    x[i] = (b[i] - suma) / A[i][i]

print(x)
```

Wynik:

```text
[1.25, -0.25, 0.75]
```

---

# 18. Pełny wybór elementu głównego

Pełny wybór elementu głównego polega na wyszukaniu największego co do modułu współczynnika nie tylko w kolumnie pod napotkanym zerem, ale w całej podmacierzy „w dół i w prawo”.

Może to poprawić dokładność, ale jest bardziej czasochłonne.

### Przykład w Pythonie

```python
A = [
    [0.0, 2.0, 2.0],
    [3.0, 3.0, 0.0],
    [1.0, 0.0, 1.0]
]

k = 0

najwiekszy = abs(A[k][k])
wiersz_pivota = k
kolumna_pivota = k

for i in range(k, len(A)):
    for j in range(k, len(A[0])):
        if abs(A[i][j]) > najwiekszy:
            najwiekszy = abs(A[i][j])
            wiersz_pivota = i
            kolumna_pivota = j

print("Największy element:", najwiekszy)
print("Wiersz:", wiersz_pivota)
print("Kolumna:", kolumna_pivota)
```

---

# 19. Rozkład LU

Jeżeli macierz `A` można przedstawić jako iloczyn macierzy trójkątnej dolnej `L` i trójkątnej górnej `U`, to:

$$  
A = LU  
$$

Jeżeli macierz `A` jest nieosobliwa, to:

$$  
A^{-1} = (LU)^{-1} = U^{-1}L^{-1}  
$$

Rozwiązanie układu:

$$  
Ax = b  
$$

można sprowadzić do dwóch układów trójkątnych:

$$  
Ly = b  
$$

oraz:

$$  
Ux = y  
$$

Najpierw rozwiązujemy `Ly = b` przez podstawianie w przód, a potem `Ux = y` przez podstawianie wstecz.

### Przykład w Pythonie

```python
L = [
    [1.0, 0.0, 0.0],
    [2.0, 1.0, 0.0],
    [1.0, -1.0, 1.0]
]

U = [
    [2.0, 1.0, -1.0],
    [0.0, 3.0, 2.0],
    [0.0, 0.0, 4.0]
]

b = [1.0, 12.0, 8.0]

n = len(L)

# Rozwiązujemy Ly = b
y = [0.0, 0.0, 0.0]

for i in range(n):
    suma = 0

    for k in range(0, i):
        suma = suma + L[i][k] * y[k]

    y[i] = (b[i] - suma) / L[i][i]

# Rozwiązujemy Ux = y
x = [0.0, 0.0, 0.0]

for i in range(n - 1, -1, -1):
    suma = 0

    for k in range(i + 1, n):
        suma = suma + U[i][k] * x[k]

    x[i] = (y[i] - suma) / U[i][i]

print("y =", y)
print("x =", x)
```

---

## 20. Eliminacja Gaussa a rozkład LU

Jednym ze sposobów uzyskania rozkładu LU jest eliminacja Gaussa.

W wyniku eliminacji Gaussa otrzymujemy macierz górnotrójkątną `U`.

Macierz dolnotrójkątną `L` wyznacza się tak, że współczynniki użyte do eliminacji wpisuje się w odpowiednie miejsca macierzy `L`.

Macierz `L` ma na diagonali wartości `1`.

### Przykład

Jeżeli w eliminacji używamy mnożnika:

$$  
m = \frac{a_{i,k}}{a_{k,k}}  
$$

to ten mnożnik trafia do macierzy `L`.

### Przykład w Pythonie

```python
A = [
    [2.0, 1.0],
    [4.0, 3.0]
]

n = len(A)

L = [
    [1.0, 0.0],
    [0.0, 1.0]
]

U = [
    [A[0][0], A[0][1]],
    [A[1][0], A[1][1]]
]

for k in range(n - 1):
    for i in range(k + 1, n):
        m = U[i][k] / U[k][k]

        L[i][k] = m

        for j in range(k, n):
            U[i][j] = U[i][j] - m * U[k][j]

print("L =", L)
print("U =", U)
```

---

## 21. Macierz permutacji

Jeżeli eliminacja Gaussa wymaga zamiany wierszy, to zamiast rozkładu:

$$  
A = LU  
$$

otrzymujemy:

$$  
PA = LU  
$$

gdzie `P` jest macierzą permutacji.

Przykład z wykładu:

# $$  
PA =  
\begin{bmatrix}  
0 & 0 & 1 \  
1 & 0 & 0 \  
0 & 1 & 0  
\end{bmatrix}  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & a_{1,3} \  
a_{2,1} & a_{2,2} & a_{2,3} \  
a_{3,1} & a_{3,2} & a_{3,3}  
\end{bmatrix}

\begin{bmatrix}  
a_{3,1} & a_{3,2} & a_{3,3} \  
a_{1,1} & a_{1,2} & a_{1,3} \  
a_{2,1} & a_{2,2} & a_{2,3}  
\end{bmatrix}  
$$

Macierz permutacji ma własność:

$$  
P^T P = I  
$$

stąd:

$$  
P^T = P^{-1}  
$$

oraz:

$$  
A = P^T LU  
$$

### Przykład w Pythonie

```python
P = [
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
]

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

PA = []

for i in range(len(P)):
    wiersz = []

    for j in range(len(A[0])):
        suma = 0

        for k in range(len(A)):
            suma = suma + P[i][k] * A[k][j]

        wiersz.append(suma)

    PA.append(wiersz)

print(PA)
```

Wynik:

```text
[[7, 8, 9], [1, 2, 3], [4, 5, 6]]
```

---

# 22. Metoda Doolittle’a

W metodzie Doolittle’a szukamy rozkładu:

$$  
A = LU  
$$

przy czym macierz `L` ma na diagonali same jedynki.

Dla macierzy `3 × 3`:

# $$  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & a_{1,3} \  
a_{2,1} & a_{2,2} & a_{2,3} \  
a_{3,1} & a_{3,2} & a_{3,3}  
\end{bmatrix}

\begin{bmatrix}  
1 & 0 & 0 \  
l_{2,1} & 1 & 0 \  
l_{3,1} & l_{3,2} & 1  
\end{bmatrix}  
\begin{bmatrix}  
u_{1,1} & u_{1,2} & u_{1,3} \  
0 & u_{2,2} & u_{2,3} \  
0 & 0 & u_{3,3}  
\end{bmatrix}  
$$

Wzory ogólne z wykładu:

## $$  
u_{i,j} =  
a_{i,j}

\sum_{k=1}^{i-1} l_{i,k}u_{k,j}  
$$

dla:

$$  
j = i,i+1,\dots,n  
$$

oraz:

## $$  
l_{j,i} =  
\frac{  
a_{j,i}

\sum_{k=1}^{i-1} l_{j,k}u_{k,i}  
}  
{u_{i,i}}  
$$

dla:

$$  
j = i+1,i+2,\dots,n  
$$

Metoda Doolittle’a staje się niezawodna dopiero w połączeniu z wyborem elementu podstawowego.

### Przykład w Pythonie

```python
A = [
    [2.0, 1.0, 1.0],
    [4.0, -6.0, 0.0],
    [-2.0, 7.0, 2.0]
]

n = len(A)

L = []
U = []

for i in range(n):
    wiersz_L = []
    wiersz_U = []

    for j in range(n):
        if i == j:
            wiersz_L.append(1.0)
        else:
            wiersz_L.append(0.0)

        wiersz_U.append(0.0)

    L.append(wiersz_L)
    U.append(wiersz_U)

for i in range(n):
    # Liczymy wiersz U
    for j in range(i, n):
        suma = 0

        for k in range(i):
            suma = suma + L[i][k] * U[k][j]

        U[i][j] = A[i][j] - suma

    # Liczymy kolumnę L
    for j in range(i + 1, n):
        suma = 0

        for k in range(i):
            suma = suma + L[j][k] * U[k][i]

        L[j][i] = (A[j][i] - suma) / U[i][i]

print("L =", L)
print("U =", U)
```

---

# 23. Metoda Crouta

W metodzie Crouta przyjmuje się, że macierz `U` ma na głównej przekątnej same jedynki.

Czyli dla macierzy `3 × 3`:

# $$  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & a_{1,3} \  
a_{2,1} & a_{2,2} & a_{2,3} \  
a_{3,1} & a_{3,2} & a_{3,3}  
\end{bmatrix}

\begin{bmatrix}  
l_{1,1} & 0 & 0 \  
l_{2,1} & l_{2,2} & 0 \  
l_{3,1} & l_{3,2} & l_{3,3}  
\end{bmatrix}  
\begin{bmatrix}  
1 & u_{1,2} & u_{1,3} \  
0 & 1 & u_{2,3} \  
0 & 0 & 1  
\end{bmatrix}  
$$

### Przykład w Pythonie

```python
A = [
    [2.0, 1.0, 1.0],
    [4.0, -6.0, 0.0],
    [-2.0, 7.0, 2.0]
]

n = len(A)

L = []
U = []

for i in range(n):
    wiersz_L = []
    wiersz_U = []

    for j in range(n):
        wiersz_L.append(0.0)

        if i == j:
            wiersz_U.append(1.0)
        else:
            wiersz_U.append(0.0)

    L.append(wiersz_L)
    U.append(wiersz_U)

for j in range(n):
    for i in range(j, n):
        suma = 0

        for k in range(j):
            suma = suma + L[i][k] * U[k][j]

        L[i][j] = A[i][j] - suma

    for i in range(j + 1, n):
        suma = 0

        for k in range(j):
            suma = suma + L[j][k] * U[k][i]

        U[j][i] = (A[j][i] - suma) / L[j][j]

print("L =", L)
print("U =", U)
```

---

# 24. Rozkład Cholesky’ego

Rozkład Cholesky’ego, nazywany też rozkładem Banachiewicza, stosuje się dla macierzy symetrycznych i dodatnio określonych.

Macierz musi spełniać warunek symetrii:

$$  
a_{i,j} = a_{j,i}  
$$

oraz warunek dodatniej określoności:

$$  
x^T Ax > 0  
$$

dla każdego `x`.

Wtedy można zapisać:

$$  
A = LL^T  
$$

gdzie `L` jest macierzą trójkątną dolną.

Wzory z wykładu:

## $$  
l_{i,i} =  
\sqrt{  
a_{i,i}

\sum_{k=1}^{i-1} l_{i,k}^2  
}  
$$

oraz:

## $$  
l_{j,i} =  
\frac{1}{l_{i,i}}  
\left(  
a_{j,i}

\sum_{k=1}^{i-1} l_{j,k}l_{i,k}  
\right)  
$$

dla:

$$  
j = i+1,i+2,\dots,n  
$$

Wykład podaje, że ilość operacji potrzebna do znalezienia rozkładu Cholesky’ego jest o połowę mniejsza w porównaniu z LU. Metoda jest też stabilna numerycznie i nie wymaga wyboru elementu podstawowego.

### Przykład w Pythonie

```python
import math

A = [
    [4.0, 2.0],
    [2.0, 3.0]
]

n = len(A)

L = []

for i in range(n):
    wiersz = []

    for j in range(n):
        wiersz.append(0.0)

    L.append(wiersz)

for i in range(n):
    suma = 0

    for k in range(i):
        suma = suma + L[i][k] ** 2

    L[i][i] = math.sqrt(A[i][i] - suma)

    for j in range(i + 1, n):
        suma = 0

        for k in range(i):
            suma = suma + L[j][k] * L[i][k]

        L[j][i] = (A[j][i] - suma) / L[i][i]

print(L)
```

---

# 25. Najważniejsze rzeczy do zapamiętania na kolosa

## 25.1. Zapis układu

Układ równań liniowych zapisujemy jako:

$$  
Ax = b  
$$

### Python

```python
A = [
    [2, 1],
    [1, 3]
]

b = [5, 7]

print(A)
print(b)
```

---

## 25.2. Macierz rozszerzona

Macierz rozszerzona to macierz główna z dołączonym wektorem wyrazów wolnych:

$$  
A_b =  
\begin{bmatrix}  
a_{1,1} & a_{1,2} & b_1 \  
a_{2,1} & a_{2,2} & b_2  
\end{bmatrix}  
$$

### Python

```python
A = [
    [2, 1],
    [1, 3]
]

b = [5, 7]

Ab = []

for i in range(len(A)):
    wiersz = []

    for j in range(len(A[0])):
        wiersz.append(A[i][j])

    wiersz.append(b[i])
    Ab.append(wiersz)

print(Ab)
```

---

## 25.3. Twierdzenie Kroneckera-Capellego

Jeżeli:

$$  
rank(A) = rank(A_b) = n  
$$

układ ma dokładnie jedno rozwiązanie.

Jeżeli:

$$  
rank(A) = rank(A_b) < n  
$$

układ ma nieskończenie wiele rozwiązań.

Jeżeli:

$$  
rank(A) < rank(A_b)  
$$

układ nie ma rozwiązań.

---

## 25.4. Wzory Cramera

Dla:

$$  
\det(A) \neq 0  
$$

można liczyć:

$$  
x_k = \frac{\det(A_k)}{\det(A)}  
$$

---

## 25.5. Podstawianie wstecz

Dla macierzy trójkątnej górnej:

$$  
x_i =  
\frac{  
b_i - \sum_{k=i+1}^{n} a_{i,k}x_k  
}  
{a_{i,i}}  
$$

---

## 25.6. Podstawianie w przód

Dla macierzy trójkątnej dolnej:

$$  
x_i =  
\frac{  
b_i - \sum_{k=1}^{i-1} a_{i,k}x_k  
}  
{a_{i,i}}  
$$

---

## 25.7. Eliminacja Gaussa

Eliminacja Gaussa sprowadza układ do postaci trójkątnej, a potem stosuje się podstawianie wstecz.

---

## 25.8. Pivot

Pivot to element podstawowy, przez który dzielimy podczas eliminacji.

Jeżeli pivot jest równy zero albo bardzo mały, należy zamienić wiersze.

---

## 25.9. Rozkład LU

Jeżeli:

$$  
A = LU  
$$

to rozwiązujemy dwa układy:

$$  
Ly = b  
$$

oraz:

$$  
Ux = y  
$$

---

## 25.10. Rozkład Cholesky’ego

Jeżeli macierz jest symetryczna i dodatnio określona, można zastosować rozkład:

$$  
A = LL^T  
$$

---

# 26. Krótkie podsumowanie

Wykład 3 dotyczył układów równań liniowych i bezpośrednich metod ich rozwiązywania.

Najważniejsze wnioski:

1. Układ równań liniowych można zapisać jako `Ax = b`.
    
2. Macierz rozszerzona powstaje przez dołączenie wektora `b` do macierzy `A`.
    
3. Twierdzenie Kroneckera-Capellego mówi, ile rozwiązań ma układ.
    
4. Metody bezpośrednie dają wynik po skończonej liczbie działań, ale mogą być wrażliwe na błędy zaokrągleń.
    
5. Wzory Cramera można stosować, gdy `det(A) ≠ 0`.
    
6. Układy z macierzami trójkątnymi rozwiązuje się przez podstawianie w przód albo wstecz.
    
7. Eliminacja Gaussa sprowadza układ do postaci trójkątnej.
    
8. Wybór elementu podstawowego poprawia niezawodność i dokładność obliczeń.
    
9. Rozkład LU sprowadza rozwiązanie układu do dwóch układów trójkątnych.
    
10. Rozkład Cholesky’ego jest używany dla macierzy symetrycznych i dodatnio określonych.