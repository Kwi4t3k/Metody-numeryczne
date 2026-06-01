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

### dlaczego odpowiedź może być błędna przy bezpośrednim porównaniu liczb zmiennoprzecinkowych

Komputery przechowują liczby zmiennoprzecinkowe w formacie binarnym (standard IEEE 754).

Niektóre liczby dziesiętne, takie jak:

- 0.1
    
- 0.2
    
- 0.3
    

**nie mają dokładnej reprezentacji w systemie binarnym**, podobnie jak 1/3 nie ma skończonego zapisu w systemie dziesiętnym.

W efekcie:

- 0.1 jest zapisywane jako liczba bardzo bliska 0.1
    
- 0.2 również
    
- ich suma daje 0.30000000000000004 zamiast dokładnie 0.3
    

To jest **błąd reprezentacji (rounding error)**.

#### Dlaczego bezpośrednie porównanie jest błędne?

Porównanie:

`suma == 0.3`

sprawdza **dokładną równość bitową**, a nie matematyczną równość w sensie „wystarczająco blisko”.

Z powodu minimalnych błędów zaokrągleń wynik może się różnić o bardzo małą wartość (np. 5e-17), więc porównanie zwróci `False`.

#### Poprawny sposób porównywania

Zamiast `==` należy używać porównania z tolerancją:

`import math  math.isclose(suma, 0.3)`

lub dla NumPy:

`np.isclose(suma32, np.float32(0.3))`

Można też ręcznie sprawdzić:

`abs(suma - 0.3) < 1e-9`

#### Wniosek

Suma dwóch liczb zmiennoprzecinkowych **nie zawsze** jest dokładnie równa wartości matematycznej.  
Bezpośrednie porównanie (`==`) może dawać błędne wyniki.  
Należy stosować porównania z tolerancją (`isclose`).

---

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

#### Matematycznie

Mamy:

a = 10000000000000000  
b = 0.000000000000001

czyli:

a = 10^16  
b = 10^-15

Matematycznie:

(10^16 + 10^-15) - 10^16 = 10^-15

Powinniśmy dostać:

0.000000000000001

#### Co dzieje się w praktyce?

Wynik będzie:

0.0

#### Dlaczego?

##### 1. Ograniczona precyzja `float64`

Liczby zmiennoprzecinkowe typu `float` w Pythonie mają:

- 64 bity
    
- około 15–16 cyfr znaczących
    

Liczba:

10000000000000000

ma już **16 cyfr znaczących**.

To oznacza, że:

- cała dostępna precyzja jest zużyta na zapis tej dużej liczby,
    
- nie ma już miejsca na zapis bardzo małej zmiany rzędu `10^-15`.
    

##### 2. Co dzieje się przy dodawaniu?

Komputer próbuje policzyć:

10000000000000000 + 0.000000000000001

Ale różnica rzędów wielkości wynosi:

10^16 vs 10^-15

To różnica **31 rzędów wielkości**.

Mała liczba jest tak niewyobrażalnie mała względem dużej, że:

> jej wpływ mieści się poza zakresem precyzji mantysy

W efekcie:

a + b  ≈  a

czyli w pamięci:

10000000000000000 + 0.000000000000001  
= 10000000000000000

##### 3. Odejmowanie

Skoro w pamięci mamy:

(a + b) = a

to:

(a + b) - a = 0

#### Co to pokazuje?

- Bardzo małe liczby mogą całkowicie „zniknąć” przy dodawaniu do bardzo dużych.
    
- Operacje na liczbach zmiennoprzecinkowych nie są dokładne przy dużych różnicach skali.
    
- To przykład **utraty precyzji** wynikającej z ograniczonej liczby cyfr znaczących.
    

#### Kluczowa intuicja!

To tak, jakbyś próbował dodać:

10 000 000 000 000 000,00  
+ 0,000000000000001

Przy dokładności do grosza ta zmiana po prostu nie istnieje.

---

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

- `float32` ma mniejszą precyzję - szybciej pojawia się błąd.
    
- `float64` jest dokładniejszy, ale też nie przechowuje 0.1 idealnie.
    
- 20 miejsc po przecinku pokazuje rzeczywistą reprezentację w pamięci.

---

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

>Wynik nie jest równy dokładnie 1 z powodu błędu reprezentacji binarnej liczb 0.3 i 0.1 w standardzie IEEE 754.

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

#### Dlaczego wyniki różnią się od teoretycznej różnicy?

Dzieje się tak z powodu **błędów reprezentacji liczb zmiennoprzecinkowych w systemie binarnym (IEEE 754)**.

##### Liczby nie są przechowywane dokładnie

Liczby:

1.0000001  
1.0000002

nie mają idealnej reprezentacji binarnej. W pamięci są zapisane jako **najbliższe możliwe przybliżenia**.

Czyli komputer faktycznie odejmuje:

(1.0000001 + mały_błąd1) - (1.0000000 + mały_błąd2)

##### Odejmowanie liczb bliskich sobie

Tutaj odejmujemy liczby prawie równe:

1.0000001 - 1.0000000

To powoduje zjawisko zwane:

##### utratą cyfr znaczących (catastrophic cancellation)

Podczas odejmowania:

- duże wspólne cyfry się „kasują”,
    
- pozostaje bardzo mała różnica,
    
- a względny wpływ błędu zaokrąglenia rośnie.
    

Dlatego wyniki:

1.0000000005838672e-07  
9.999999983634211e-08

różnią się minimalnie od siebie i od idealnego `1e-7`.

#### Podsumowanie
To są liczby bardzo bliskie `1e-7`, więc obliczenia są poprawne - różnice wynikają z reprezentacji zmiennoprzecinkowej.

Wyniki różnią się od teoretycznej wartości, ponieważ liczby zmiennoprzecinkowe nie są przechowywane dokładnie w systemie binarnym. Podczas odejmowania liczb bardzo bliskich sobie dochodzi do utraty cyfr znaczących, co powoduje, że niewielkie błędy reprezentacji stają się widoczne w wyniku.

---

## Zadanie 6
Podziel liczbę 1,0 przez 0,0 i liczbę 0,0 przez 0,0. Sprawdź, co zwrócą te operacje.

```python
wynik1 = 1.0 / 0.0  
wynik2 = 0.0 / 0.0  
  
print("wynik dzielenia pierwszego: ", wynik1)  
print("wynik dzielenia drugiego: ", wynik2)
```

```
Traceback (most recent call last):
  File "zad6.py", line 1, in <module>
    wynik1 = 1.0 / 0.0
             ~~~~^~~~~
ZeroDivisionError: float division by zero
-------------------------------------------
Traceback (most recent call last):
  File "zad6.py", line 2, in <module>
    wynik2 = 0.0 / 0.0
             ~~~~^~~~~
ZeroDivisionError: float division by zero
```

Mimo że liczby zmiennoprzecinkowe są zgodne ze standardem IEEE 754, Python **celowo zgłasza wyjątek**, aby zapobiec dalszym obliczeniom na niepoprawnych wartościach.

W Pythonie dzielenie przez zero dla liczb zmiennoprzecinkowych powoduje zgłoszenie wyjątku `ZeroDivisionError`. Jednak zgodnie ze standardem IEEE 754 operacja 1.0 / 0.0 powinna zwrócić nieskończoność (∞), a 0.0 / 0.0 wartość NaN (Not a Number). W bibliotekach takich jak NumPy zachowanie jest zgodne z IEEE 754 i zamiast wyjątku zwracane są wartości `inf` oraz `nan`.

#### Co mówi standard IEEE 754?

W czystej arytmetyce IEEE 754 (np. w NumPy):

|Operacja|Wynik|
|---|---|
|`1.0 / 0.0`|`+∞` (infinity)|
|`-1.0 / 0.0`|`-∞`|
|`0.0 / 0.0`|`NaN` (Not a Number)|

#### Jak to sprawdzić w NumPy?

```python
import numpy as np  
  
print(np.float64(1.0) / np.float64(0.0))  
print(np.float64(0.0) / np.float64(0.0))
```

Wtedy otrzymasz:

```
inf  
nan
```

(plus ostrzeżenie RuntimeWarning zamiast wyjątku)

#### Różnica

- 🔹 Python (czysty `float`) → zgłasza `ZeroDivisionError`
    
- 🔹 NumPy → zwraca `inf` lub `nan` zgodnie z IEEE 754

---

## Zadanie 7
Oblicz maszynowy epsilon dla typów float i double i porównaj wyniki. Wyjaśnij, czym jest maszynowy epsilon i jak wpływa na dokładność obliczeń komputerowych.

#### Maszynowy epsilon - definicja

Maszynowy epsilon ($\varepsilon_{mach}$) to najmniejsza dodatnia liczba $\varepsilon$, taka że:

$$
1 + \varepsilon > 1
$$

w arytmetyce zmiennoprzecinkowej danego typu.

Oznacza to najmniejszą wartość, którą komputer jest w stanie „zauważyć” przy dodaniu do 1.  
Wyznacza on granicę precyzji reprezentacji liczb w komputerze.

#### Obliczenie maszynowego epsilon w Pythonie

Maszynowy epsilon można wyznaczyć algorytmicznie, zmniejszając wartość $\varepsilon$ tak długo, aż suma $1 + \varepsilon$ przestanie być większa od 1.

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

print("Epsilon float32:", eps32)
print("Epsilon float64:", eps64)
````

```
Epsilon float32: 1.1920929e-07
Epsilon float64: 2.220446049250313e-16
```

|Typ|$\varepsilon_{mach}$|
|---|---|
|float32|≈ 1.19 · 10⁻⁷|
|float64|≈ 2.22 · 10⁻¹⁶|

Porównując wartości:

$$  
\frac{1.19 \cdot 10^{-7}}{2.22 \cdot 10^{-16}} \approx 10^9  
$$

Oznacza to, że typ **float64 jest około miliard razy dokładniejszy niż float32**.

#### Wpływ maszynowego epsilon na dokładność obliczeń

##### 1. Ogranicza liczbę cyfr znaczących

- float32 → około 7 cyfr znaczących
    
- float64 → około 15–16 cyfr znaczących
    

##### 2. Określa maksymalny względny błąd pojedynczej operacji

Każda operacja arytmetyczna wprowadza błąd rzędu $\varepsilon_{mach}$.

##### 3. Wpływa na stabilność obliczeń

- Przy odejmowaniu liczb bardzo bliskich sobie może dojść do utraty cyfr znaczących.
    
- Przy dużej liczbie operacji błędy mogą się kumulować.
    

##### 4️. Wyznacza granicę rozróżnialności liczb

Jeśli dodamy do 1 liczbę mniejszą niż $\varepsilon_{mach}$, wynik nadal będzie równy 1, ponieważ zmiana jest poniżej granicy precyzji.

#### Wniosek

Maszynowy epsilon:

- dla **float32** wynosi około **1.19 · 10⁻⁷**
    
- dla **float64** wynosi około **2.22 · 10⁻¹⁶**
    

Im mniejszy epsilon, tym większa dokładność obliczeń komputerowych.  
Dlatego typ double (float64) zapewnia znacznie większą precyzję niż float (float32).

---

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

#### Dlaczego występuje różnica?

##### 1. 0.0001 nie ma dokładnej reprezentacji binarnej

Liczba `0.0001` nie jest zapisywana idealnie w systemie binarnym — jest przechowywana jako przybliżenie.

##### 2️. Akumulacja błędu

W pętli wykonujemy milion operacji dodawania:

suma = suma + przybliżona_wartość

Każde dodanie wprowadza bardzo mały błąd zaokrąglenia.  
Po 1 000 000 iteracjach te małe błędy się sumują.

To zjawisko nazywamy:

> **akumulacją błędu numerycznego**

##### 3️. Dlaczego mnożenie daje dokładniejszy wynik?

Mnożenie wykonuje:

n * wartosc

czyli jedną operację zamiast miliona, więc błąd pojawia się tylko raz, a nie milion razy.

#### Wniosek

- Sumowanie wielu małych liczb może prowadzić do akumulacji błędów.
    
- Wynik obliczony w pętli może różnić się od wyniku mnożenia.
    
- To pokazuje, że operacje zmiennoprzecinkowe nie są dokładne matematycznie.
    
- Im więcej operacji, tym większe ryzyko narastania błędu.

---

## Zadanie 9
Oblicz sumę odwrotności liczb od 1 do 1.000.000 w kolejności rosnącej i malejącej. Porównaj wyniki.

```python
n = 1_000_000

# 1️⃣ Sumowanie w kolejności rosnącej (od 1 do 1_000_000)
suma_rosnaco = 0.0
for i in range(1, n + 1):
    suma_rosnaco += 1.0 / i

# 2️⃣ Sumowanie w kolejności malejącej (od 1_000_000 do 1)
suma_malejaco = 0.0
for i in range(n, 0, -1):
    suma_malejaco += 1.0 / i

# Różnica
roznica = suma_rosnaco - suma_malejaco

print("Suma rosnąco:", suma_rosnaco)
print("Suma malejąco:", suma_malejaco)
print("Różnica:", roznica)
````

Matematycznie obie sumy powinny być identyczne:

$$  
\sum_{i=1}^{1,000,000} \frac{1}{i}  
$$

Jest to tzw. **milionowy wyraz szeregu harmonicznego**.

W praktyce otrzymujemy:

```
Suma rosnąco: 14.392726722864989
Suma malejąco: 14.392726722865772
Różnica: -7.833733661755105e-13
```

#### Dlaczego wyniki się różnią?

##### 1️. Ograniczona precyzja liczb zmiennoprzecinkowych

Liczby typu `float` mają ograniczoną liczbę cyfr znaczących (około 15–16).

##### 2️. Akumulacja błędu zaokrągleń

Każde dodawanie wprowadza bardzo mały błąd.  
Ponieważ wykonujemy **milion operacji**, błędy się kumulują.

##### 3. Znaczenie kolejności dodawania

To kluczowe.

#### 🔹 Sumowanie rosnąco (1 → 1 000 000)

Na początku dodajemy duże liczby (1, 1/2, 1/3...).  
Na końcu bardzo małe liczby (np. 1/1 000 000).

Małe składniki dodawane do dużej sumy mogą zostać częściowo „zgubione” z powodu ograniczonej precyzji.

#### 🔹 Sumowanie malejąco (1 000 000 → 1)

Najpierw dodajemy bardzo małe liczby.  
Suma jest jeszcze mała, więc precyzja względna jest lepsza.

Dopiero później dodawane są większe składniki.

➡ Ta metoda daje zwykle **dokładniejszy wynik**.

#### Wniosek

- Matematycznie kolejność sumowania nie ma znaczenia.
    
- W arytmetyce zmiennoprzecinkowej ma znaczenie.
    
- Sumowanie od najmniejszych do największych wartości jest numerycznie stabilniejsze.
    
- Różnice wynikają z ograniczonej precyzji i akumulacji błędów zaokrągleń.
    

---

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


#### Łatwo zauważyć, że algebraicznie:

$$
g(x) = f(x)
$$

ponieważ:

$$
\sqrt{x^2+1} - 1
=
\frac{(\sqrt{x^2+1}-1)(\sqrt{x^2+1}+1)}{\sqrt{x^2+1}+1}
=
\frac{x^2}{\sqrt{x^2+1}+1}
$$



#### Obliczenia w Pythonie

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
````

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

#### Co się stanie?

Dla większych wartości x obie funkcje dadzą niemal identyczne wyniki.

Jednak gdy x staje się bardzo małe (np. 8⁻⁸, 8⁻⁹, 8⁻¹⁰):

- wartości f(x) zaczynają tracić dokładność,
    
- g(x) pozostaje stabilne numerycznie.
    

#### Dlaczego?

Dla bardzo małych x:

$$  
\sqrt{x^2+1} \approx 1  
$$

W funkcji:

$$  
f(x) = \sqrt{x^2+1} - 1  
$$

odejmujemy dwie prawie równe liczby:

$$  
1.000000000000... - 1  
$$

Powoduje to zjawisko:

> **katastrofalnej utraty cyfr znaczących (catastrophic cancellation)**

W wyniku tracimy znaczną część dokładności.

Natomiast funkcja:

$$  
g(x) = \frac{x^2}{\sqrt{x^2+1}+1}  
$$

nie zawiera odejmowania prawie równych liczb, więc jest znacznie stabilniejsza numerycznie.

#### Wniosek

- Algebraicznie: ( f(x) = g(x) )
    
- Numerycznie: dla małych x funkcja g(x) daje dokładniejsze wyniki.
    
- Powód: w f(x) występuje utrata cyfr znaczących.
    
- Jest to klasyczny przykład niestabilności numerycznej.
    

Dla bardzo małych x funkcja g(x) powinna być używana zamiast f(x).

---

# Lab 2
# Zadanie 1

Napisz funkcję, która wygeneruje tablicę liczb zmiennoprzecinkowych pojedynczej precyzji reprezentujących elementy ciągu postaci:

$$
S_n = \sum_{k=0}^{n-1} a_k = \sum_{k=0}^{n-1} \frac{1}{(k \bmod m + 1)(k \bmod m + 2)},
$$

gdzie $n$ i $m$ są potęgami liczby $2$ oraz $n > m$.

## Jak rozumieć to zadanie?

Nie liczymy tu jeszcze całej sumy $S_n$, tylko najpierw generujemy **same elementy ciągu**:

$$
a_k = \frac{1}{(k \bmod m + 1)(k \bmod m + 2)}
$$

Czyli dla każdego $k$:
1. liczysz resztę z dzielenia $k \bmod m$,
2. dodajesz 1 i 2,
3. mnożysz te dwie liczby,
4. bierzesz odwrotność.

Ponieważ zadanie mówi o **pojedynczej precyzji**, każdy element zapisujemy jako `float32`.

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz pustą tablicę.

### Krok 2

Dla każdego $k$ od `0` do `n-1` liczysz wartość:

$$
a_k = \frac{1}{(k \bmod m + 1)(k \bmod m + 2)}
$$

### Krok 3

Zapisujesz wynik jako `np.float32`, czyli liczbę pojedynczej precyzji.

### Krok 4

Dodajesz element do tablicy.

## Kod

```python
import numpy as np  # importujemy bibliotekę numpy i nadajemy jej skrót np

def generuj_tablice(n, m):  # funkcja generuje tablicę n elementów według podanego wzoru
    tablica = []  # tworzymy pustą listę, do której będziemy dodawać kolejne elementy ciągu

    for k in range(n):  # pętla wykonuje się n razy, dla k od 0 do n-1
        licznik = 1  # ustawiamy licznik ułamka na 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)  # liczymy mianownik według wzoru z użyciem reszty z dzielenia k przez m

        element = licznik / mianownik  # obliczamy wartość elementu ciągu jako licznik podzielony przez mianownik

        tablica.append(np.float32(element))  # dodajemy element do tablicy jako liczbę typu float32

    return tablica  # zwracamy gotową tablicę z elementami ciągu

n = 64  # liczba elementów, które chcemy wygenerować
m = 16  # wartość używana w działaniu modulo, czyli okres powtarzania mianownika

tablica = generuj_tablice(n, m)  # wywołujemy funkcję i zapisujemy wynik do zmiennej tablica

print("Elementy ciągu:")  # wypisujemy napis informacyjny
for i, wartosc in enumerate(tablica):  # przechodzimy po elementach tablicy razem z ich indeksami
    print("a_", i, "=", wartosc)  # wypisujemy indeks elementu oraz jego wartość
```

## Co otrzymujemy?

Otrzymujemy tablicę elementów ciągu $(a_0, a_1, a_2, \dots, a_{n-1})$, zapisanych w pojedynczej precyzji.

---

# Zadanie 2

Napisz funkcję sumującą elementy tablicy z zadania 1. Sprawdź dokładność otrzymanej sumy.

## Jak rozumieć to zadanie?

Tutaj liczymy już zwykłą sumę wszystkich elementów tablicy:

$$
S_n = a_0 + a_1 + a_2 + \dots + a_{n-1}
$$

Jest to najprostszy sposób sumowania:

* zaczynasz od zera,
* dodajesz kolejne elementy jeden po drugim.

## Jak rozumieć schemat implementacji?

### Krok 1

Generujesz tablicę elementów.

### Krok 2

Tworzysz zmienną `suma` równą `0.0` w typie `float32`.

### Krok 3

W pętli dodajesz do niej kolejne elementy tablicy.

### Krok 4

Na końcu zwracasz wynik.

## Kod

```python
import numpy as np  # importujemy bibliotekę numpy i nadajemy jej skrót np

def generuj_tablice(n, m):  # funkcja generuje tablicę n elementów według podanego wzoru
    tablica = []  # tworzymy pustą listę, do której będziemy dodawać elementy

    for k in range(n):  # pętla wykonuje się n razy, dla k od 0 do n-1
        licznik = 1  # ustawiamy licznik ułamka na 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)  # liczymy mianownik według wzoru z użyciem reszty z dzielenia k przez m

        a = licznik / mianownik  # obliczamy wartość elementu ciągu
        tablica.append(np.float32(a))  # dodajemy element do tablicy jako liczbę typu float32

    return tablica  # zwracamy gotową tablicę


def sumuj_tablice(tablica):  # funkcja sumuje elementy tablicy
    suma = np.float32(0.0)  # tworzymy zmienną suma typu float32 i ustawiamy ją na 0.0

    for element in tablica:  # przechodzimy po każdym elemencie tablicy
        suma = np.float32(suma + element)  # dodajemy element do sumy i zapisujemy wynik jako float32

    return suma  # zwracamy obliczoną sumę


n = 64  # liczba elementów tablicy
m = 16  # wartość używana w modulo, czyli okres powtarzania wartości

tablica = generuj_tablice(n, m)  # generujemy tablicę elementów i zapisujemy ją do zmiennej tablica

suma = sumuj_tablice(tablica)  # obliczamy sumę elementów tablicy

print("Elementy tablicy:")  # wypisujemy napis informacyjny
for i, wartosc in enumerate(tablica):  # przechodzimy po elementach tablicy razem z ich indeksami
    print("a_", i, "=", wartosc)  # wypisujemy indeks elementu i jego wartość

print("\nSuma elementów:", suma)  # wypisujemy sumę elementów tablicy
```

## Jak sprawdzić dokładność?

Dokładną wartość sumy można porównać z:

$$
\frac{n}{m+1}
$$

W tym zadaniu:

$$
\frac{64}{17}
$$

To jest wartość odniesienia, z którą porównujemy wynik obliczony numerycznie.

---

# Zadanie 3

Napisz funkcję sumującą elementy tablicy z zadania 1 z wykorzystaniem algorytmu Gilla–Møllera. Sprawdź dokładność otrzymanej sumy.

## Co to jest algorytm Gilla–Møllera?

To metoda dokładniejszego sumowania niż zwykłe dodawanie.

W zwykłym sumowaniu część informacji może się gubić przez zaokrąglenia.
Algorytm Gilla–Møllera próbuje zachować tę „zgubioną” część w dodatkowej zmiennej, czyli poprawce.

## Jak rozumieć schemat implementacji?

### Krok 1

Zaczynasz od:

* `suma = 0`
* `poprawka = 0`

### Krok 2

Dla każdego elementu liczysz:

$$
t = suma + element
$$

### Krok 3

Obliczasz, jaka część została utracona podczas dodawania, i dopisujesz ją do poprawki.

### Krok 4

Na końcu zwracasz:

$$
suma + poprawka
$$

---

## Kod

```python
import numpy as np  # importujemy bibliotekę numpy i nadajemy jej skrót np

def generuj_tablice(n, m):  # funkcja generuje tablicę n elementów według podanego wzoru
    tablica = []  # tworzymy pustą listę, do której będą dodawane elementy

    for k in range(n):  # pętla wykonuje się n razy, dla k od 0 do n-1
        licznik = 1  # ustawiamy licznik ułamka na 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)  # obliczamy mianownik zależny od reszty z dzielenia k przez m

        a = licznik / mianownik  # obliczamy wartość elementu ciągu
        tablica.append(np.float32(a))  # dodajemy element do tablicy jako liczbę typu float32

    return tablica  # zwracamy gotową tablicę


def sumuj_tablice(tablica):  # funkcja sumuje elementy tablicy metodą z poprawką
    suma = np.float32(0.0)  # tworzymy zmienną suma typu float32 i ustawiamy ją na 0
    poprawka = np.float32(0.0)  # tworzymy zmienną poprawka, która będzie przechowywać utracone części wyniku

    for element in tablica:  # przechodzimy po każdym elemencie tablicy
        t = np.float32(suma + element)  # dodajemy aktualny element do sumy i zapisujemy wynik jako float32
        poprawka = np.float32(poprawka + (element - (t-suma)))  # obliczamy część elementu utraconą przez zaokrąglenie i dodajemy ją do poprawki
        suma = t  # aktualizujemy sumę

    return np.float32(suma + poprawka)  # zwracamy sumę powiększoną o poprawkę


n = 64  # liczba elementów tablicy
m = 16  # wartość używana w modulo, czyli okres powtarzania mianownika

tablica = generuj_tablice(n, m)  # generujemy tablicę elementów

suma = sumuj_tablice(tablica)  # sumujemy elementy tablicy metodą z poprawką

print("Suma:", suma)  # wypisujemy obliczoną sumę
```

## Co daje ta metoda?

Wynik zwykle jest dokładniejszy niż przy zwykłym sumowaniu, ponieważ zmniejsza wpływ błędów zaokrągleń.

---

# Zadanie 4

Napisz funkcję sumującą elementy tablicy z zadania 1 z wykorzystaniem algorytmu Kahana. Sprawdź dokładność otrzymanej sumy. Porównaj wyniki wszystkich omówionych metod sumowania.

## Co to jest algorytm Kahana?

Algorytm Kahana to inna metoda dokładniejszego sumowania.

Tak samo jak w metodzie Gilla–Møllera, chodzi o to, żeby kontrolować błąd zaokrąglenia.
Tutaj używa się zmiennej `c`, która przechowuje utraconą część sumy.

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz:

* `suma = 0`
* `c = 0`

### Krok 2

Dla każdego elementu liczysz:

$$
y = element - c
$$

czyli najpierw korygujesz element o wcześniej utracony błąd.

### Krok 3

Dodajesz poprawioną wartość do sumy:

$$
t = suma + y
$$

### Krok 4

Wyznaczasz nowy błąd:

$$
c = (t - suma) - y
$$

### Krok 5

Ustawiasz nową sumę.

## Kod

```python
import numpy as np  # importujemy bibliotekę numpy, żeby używać typu np.float32

def generuj_tablice(n, m):  # funkcja generuje tablicę n elementów według danego wzoru
    tablica = []  # tworzymy pustą listę na elementy ciągu

    for k in range(n):  # przechodzimy po kolejnych indeksach od 0 do n-1
        licznik = 1  # licznik ułamka jest równy 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)  # obliczamy mianownik na podstawie reszty z dzielenia k przez m

        a = licznik / mianownik  # obliczamy wartość elementu ciągu
        tablica.append(np.float32(a))  # dodajemy element do tablicy jako liczbę typu float32

    return tablica  # zwracamy wygenerowaną tablicę


def sumuj_tablice(tablica):  # funkcja wykonuje zwykłe, klasyczne sumowanie elementów tablicy
    suma = np.float32(0.0)  # ustawiamy początkową sumę na 0.0 jako float32

    for element in tablica:  # przechodzimy po każdym elemencie tablicy
        suma = np.float32(suma + element)  # dodajemy element do sumy i zapisujemy wynik jako float32

    return suma  # zwracamy obliczoną sumę


def sumuj_tablice_Møller(tablica):  # funkcja sumuje elementy metodą Møllera, czyli z poprawką błędu
    suma = np.float32(0.0)  # ustawiamy początkową sumę na 0.0 jako float32
    poprawka = np.float32(0.0)  # zmienna poprawka przechowuje utracone części wyniku

    for element in tablica:  # przechodzimy po każdym elemencie tablicy
        t = np.float32(suma + element)  # obliczamy tymczasową nową sumę
        poprawka = np.float32(poprawka + (element - (t-suma)))  # dodajemy do poprawki część utraconą przez zaokrąglenie
        suma = t  # aktualizujemy sumę

    return np.float32(suma + poprawka)  # zwracamy sumę powiększoną o poprawkę


def sumuj_tablice_Kahan(tablica):  # funkcja sumuje elementy metodą Kahana, czyli z kompensacją błędu
    suma = np.float32(0.0)  # ustawiamy początkową sumę na 0.0 jako float32
    c = np.float32(0.0)  # zmienna c przechowuje błąd kompensacji

    for element in tablica:  # przechodzimy po każdym elemencie tablicy
        y = np.float32(element - c)  # odejmujemy wcześniejszy błąd kompensacji od aktualnego elementu
        t = np.float32(suma + y)  # dodajemy skorygowany element do sumy
        c = np.float32((t-suma) - y)  # obliczamy nowy błąd zaokrąglenia
        suma = t  # aktualizujemy sumę

    return np.float32(suma)  # zwracamy obliczoną sumę


n = 64  # liczba elementów tablicy
m = 16  # wartość używana w modulo, czyli okres powtarzania elementów

tablica = generuj_tablice(n, m)  # generujemy tablicę elementów

suma = sumuj_tablice(tablica)  # liczymy sumę zwykłą metodą
suma_m = sumuj_tablice_Møller(tablica)  # liczymy sumę metodą Møllera
suma_k = sumuj_tablice_Kahan(tablica)  # liczymy sumę metodą Kahana

print("Suma zwykła:", suma)  # wypisujemy wynik zwykłego sumowania
print("Suma Møller:", suma_m)  # wypisujemy wynik sumowania metodą Møllera
print("Suma Kahan:", suma_k)  # wypisujemy wynik sumowania metodą Kahana

print("Sprawdznie dokładności:", n/(m+1))  # wypisujemy wartość dokładną, z którą można porównać wyniki
```

## Jak porównać wyniki?

Porównujesz:

* zwykłą sumę,
* sumę metodą Gilla–Møllera,
* sumę metodą Kahana,

z wartością teoretyczną:

$$
\frac{n}{m+1}
$$

Im bliżej tej wartości, tym metoda jest dokładniejsza.

## Wniosek do zadania 4

Zwykle:

* zwykłe sumowanie daje największy błąd,
* metoda Gilla–Møllera daje dokładniejszy wynik,
* metoda Kahana także poprawia dokładność i często daje najlepszy wynik.

---

# Zadanie 5

Przeprowadź analogiczne działania dla danych w podwójnej precyzji.

## Co się zmienia?

W poprzednich zadaniach używaliśmy liczb pojedynczej precyzji (`float32`).

Teraz robimy to samo, ale dla liczb podwójnej precyzji, czyli `float` / `float64`.

Podwójna precyzja daje większą dokładność, bo liczba jest przechowywana na większej liczbie bitów.

## Jak rozumieć schemat implementacji?

Wszystko działa tak samo jak wcześniej:

* generujesz elementy ciągu,
* sumujesz je trzema metodami,
* porównujesz wyniki.

Różnica polega tylko na tym, że zamiast `np.float32` używasz zwykłego `float`.

## Kod

```python
def generuj_tablice(n, m):  # funkcja generuje tablicę n elementów według danego wzoru
    tablica = []  # tworzymy pustą listę, do której będą dodawane elementy

    for k in range(n):  # pętla wykonuje się n razy, dla k od 0 do n-1
        licznik = 1  # ustawiamy licznik ułamka na 1
        mianownik = ((k % m) + 1) * ((k % m) + 2)  # obliczamy mianownik z użyciem reszty z dzielenia k przez m

        a = licznik / mianownik  # obliczamy wartość elementu ciągu
        tablica.append(float(a))  # dodajemy element do tablicy jako typ float

    return tablica  # zwracamy gotową tablicę


def sumuj_tablice(tablica):  # funkcja sumuje elementy tablicy zwykłą metodą
    suma = float(0.0)  # ustawiamy początkową sumę na 0.0 jako float

    for element in tablica:  # przechodzimy po każdym elemencie tablicy
        suma = float(suma + element)  # dodajemy aktualny element do sumy i zapisujemy wynik jako float

    return suma  # zwracamy obliczoną sumę


def sumuj_tablice_Møller(tablica):  # funkcja sumuje elementy tablicy metodą Møllera
    suma = float(0.0)  # ustawiamy początkową sumę na 0.0 jako float
    poprawka = float(0.0)  # tworzymy zmienną poprawka, która przechowuje utracone części sumy

    for element in tablica:  # przechodzimy po każdym elemencie tablicy
        t = float(suma + element)  # obliczamy tymczasową nową sumę
        poprawka = float(poprawka + (element - (t-suma)))  # dodajemy do poprawki część utraconą przez zaokrąglenie
        suma = t  # aktualizujemy sumę

    return float(suma + poprawka)  # zwracamy sumę powiększoną o poprawkę


def sumuj_tablice_Kahan(tablica):  # funkcja sumuje elementy tablicy metodą Kahana
    suma = float(0.0)  # ustawiamy początkową sumę na 0.0 jako float
    c = float(0.0)  # tworzymy zmienną c, która przechowuje błąd kompensacji

    for element in tablica:  # przechodzimy po każdym elemencie tablicy
        y = float(element - c)  # odejmujemy wcześniejszy błąd kompensacji od aktualnego elementu
        t = float(suma + y)  # dodajemy skorygowany element do sumy
        c = float((t-suma) - y)  # obliczamy nowy błąd zaokrąglenia
        suma = t  # aktualizujemy sumę

    return float(suma)  # zwracamy obliczoną sumę


n = 64  # liczba elementów tablicy
m = 16  # wartość używana w operacji modulo, czyli okres powtarzania mianownika

tablica = generuj_tablice(n, m)  # generujemy tablicę elementów

suma = sumuj_tablice(tablica)  # liczymy sumę zwykłą metodą
suma_m = sumuj_tablice_Møller(tablica)  # liczymy sumę metodą Møllera
suma_k = sumuj_tablice_Kahan(tablica)  # liczymy sumę metodą Kahana

print("Suma zwykła:", suma)  # wypisujemy wynik zwykłego sumowania
print("Suma Møller:", suma_m)  # wypisujemy wynik sumowania metodą Møllera
print("Suma Kahan:", suma_k)  # wypisujemy wynik sumowania metodą Kahana

print("Sprawdznie dokładności:", n/(m+1))  # wypisujemy wartość dokładną, z którą porównujemy wyniki
```

## Jak porównać wyniki z poprzednimi zadaniami?

Porównujesz wyniki z pojedynczej i podwójnej precyzji.

Zwykle:

* w podwójnej precyzji błędy są mniejsze,
* wszystkie metody dają wyniki bliższe wartości teoretycznej,
* metoda zwykła też działa lepiej niż w `float32`, ale nadal może być słabsza od Kahana i Gilla–Møllera.

# Wniosek końcowy

W laboratorium porównano różne sposoby sumowania elementów ciągu liczb zmiennoprzecinkowych.

* Zwykłe sumowanie jest najprostsze, ale najbardziej narażone na błędy zaokrągleń.
* Algorytm Gilla–Møllera poprawia dokładność przez przechowywanie poprawki błędu.
* Algorytm Kahana również kompensuje błąd i zwykle daje bardzo dokładne wyniki.
* W podwójnej precyzji wszystkie obliczenia są dokładniejsze niż w pojedynczej precyzji.

Otrzymane wyniki potwierdzają, że sposób sumowania i rodzaj precyzji mają istotny wpływ na dokładność obliczeń numerycznych.

---

# Lab 3

**Zadanie 1.** Napisz program, który obliczy normę: euklidesową, Manhattan, maximum dla $n$-wymiarowego wektora.

```python
import math  # importujemy moduł math, ponieważ używamy funkcji math.sqrt()

def normy_wektora(wektor):  # funkcja liczy trzy normy wektora: euklidesową, Manhattan i maksimum

    # norma euklidesowa  # norma euklidesowa to pierwiastek z sumy kwadratów elementów wektora
    suma_kwadratow = 0  # tworzymy zmienną, w której będziemy przechowywać sumę kwadratów
    for x in wektor:  # przechodzimy po każdym elemencie wektora
        suma_kwadratow += x**2  # dodajemy kwadrat aktualnego elementu do sumy
    norma_euklidesowa = math.sqrt(suma_kwadratow)  # obliczamy pierwiastek z sumy kwadratów

    # norma Manhattan  # norma Manhattan to suma wartości bezwzględnych elementów wektora
    norma_manhattan = 0  # tworzymy zmienną, w której będziemy przechowywać sumę wartości bezwzględnych
    for x in wektor:  # przechodzimy po każdym elemencie wektora
        norma_manhattan += abs(x)  # dodajemy wartość bezwzględną aktualnego elementu

    # norma maximum  # norma maksimum to największa wartość bezwzględna elementu wektora
    # norma_max = max(abs(x) for x in wektor)  # krótsza wersja z użyciem funkcji max(), ale tutaj jej nie używamy
    norma_max = 0  # tworzymy zmienną przechowującą największą znalezioną wartość bezwzględną

    for x in wektor:  # przechodzimy po każdym elemencie wektora
        wartosc_bezwzgledna = abs(x)  # liczymy wartość bezwzględną aktualnego elementu

        if wartosc_bezwzgledna > norma_max:  # sprawdzamy, czy aktualna wartość bezwzględna jest większa od dotychczasowego maksimum
            norma_max = wartosc_bezwzgledna  # jeśli tak, aktualizujemy maksimum

    return norma_euklidesowa, norma_manhattan, norma_max  # zwracamy trzy obliczone normy

wektor = [3, 4, 5]  # tworzymy przykładowy wektor

euklidesowa, manhattan, maksimum = normy_wektora(wektor)  # wywołujemy funkcję i zapisujemy trzy wyniki do osobnych zmiennych

print("Norma euklidesowa:", euklidesowa)  # wypisujemy normę euklidesową
print("Norma Manhattan:", manhattan)  # wypisujemy normę Manhattan
print("Norma maximum:", maksimum)  # wypisujemy normę maksimum
```
![Normy wektorowe](zdjecia/normy_wektorowe.png)
## 1. Norma euklidesowa
### Wzór

$$
\|x\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2}
$$

### Jak to czytać po ludzku?

- bierzesz wszystkie liczby z wektora,
- każdą podnosisz do kwadratu,
- wszystko dodajesz,
- z wyniku wyciągasz pierwiastek.

### Przykład

Dla:

$$
x = (2, -1, 4)
$$

liczymy:

$$
\|x\|_2 = \sqrt{2^2 + (-1)^2 + 4^2}
$$

czyli:

$$
\sqrt{4 + 1 + 16} = \sqrt{21}
$$

To jest zwykła „szkolna długość” wektora.

---

## 2. Norma Manhattan
### Wzór

$$
\|x\|_1 = \sum_{i=1}^{n} |x_i|
$$

### Jak to czytać po ludzku?

- bierzesz wszystkie liczby z wektora,
- zamieniasz je na dodatnie (wartość bezwzględna),
- dodajesz je wszystkie.

### Przykład

Dla:

$$
x = (2, -1, 4)
$$

liczymy:

$$
\|x\|_1 = |2| + |-1| + |4|
$$

czyli:

$$
2 + 1 + 4 = 7
$$

To się nazywa Manhattan, bo przypomina chodzenie po ulicach miasta: tylko poziomo i pionowo, bez skrótów na ukos.

---

## 3. Norma maksimum
### Wzór

$$
\|x\|_{\infty} = \max_{1 \le i \le n} |x_i|
$$

### Jak to czytać po ludzku?

- bierzesz wszystkie liczby z wektora,
- robisz z nich wartości dodatnie,
- wybierasz największą.

### Przykład

Dla:

$$
x = (2, -1, 4)
$$

liczymy:

$$
|2| = 2,\quad |-1| = 1,\quad |4| = 4
$$

największa z nich to:

$$
4
$$

więc:

$$
\|x\|_{\infty} = 4
$$

---

**Zadanie 2.** Napisz program, który będzie wyliczał odległość pomiędzy dwoma punktami przestrzeni dwuwymiarowej w metrykach: euklidesowej, Manhattan, rzece i kolejowej.


```python
import math  # importujemy moduł math, ponieważ używamy pierwiastka math.sqrt() i potęgowania math.pow()

def odleglosci(P, Q):  # funkcja liczy różne odległości między punktami P i Q
    p1, p2 = P  # rozpakowujemy współrzędne punktu P, czyli P = (p1, p2)
    q1, q2 = Q  # rozpakowujemy współrzędne punktu Q, czyli Q = (q1, q2)

    # metryka euklidesowa  # zwykła odległość między punktami w linii prostej
    euklidesowa = math.sqrt(math.pow((q1 - p1), 2) + math.pow((q2 - p2), 2))  # liczymy pierwiastek z sumy kwadratów różnic współrzędnych

    #matryka Manhattan  # odległość liczona jak poruszanie się po kratce, czyli poziomo i pionowo
    manhattan = abs(p1 - q1) + abs(p2 - q2)  # dodajemy wartości bezwzględne różnic współrzędnych

    #metryka rzeka  # odległość w metryce rzeka
    if p1 == q1:  # sprawdzamy, czy punkty leżą na tej samej pionowej prostej
        rzeka = abs(p2 - q2)  # jeśli tak, odległość to tylko różnica drugich współrzędnych
    else:  # jeśli punkty nie leżą na tej samej pionowej prostej
        rzeka = abs(p1 - q1) + abs(p2) + abs(q2)  # liczymy drogę przez rzekę, czyli dojście do osi, przejście wzdłuż osi i odejście od osi

    # metryka kolejowa  # odległość w metryce kolejowej, gdzie centrum jest punktem (0, 0)
    det = p1 * q2 - p2 * q1  # liczymy wyznacznik, który sprawdza, czy punkty i początek układu są współliniowe
    if det == 0:  # jeśli wyznacznik jest równy 0, punkty leżą na jednej prostej przechodzącej przez początek układu
        kolejowa = math.sqrt(math.pow((q1 - p1), 2) + math.pow((q2 - p2), 2))  # wtedy odległość kolejowa jest taka sama jak euklidesowa między P i Q
    else:  # jeśli punkty nie leżą na jednej prostej z początkiem układu
        kolejowa = math.sqrt(math.pow((0 - p1), 2) + math.pow((0 - p2), 2)) + math.sqrt(math.pow((0 - q1), 2) + math.pow((0 - q2), 2))  # liczymy drogę z P do centrum i z centrum do Q

    return euklidesowa, manhattan, rzeka, kolejowa  # zwracamy wszystkie obliczone odległości

punktP = (2, 3)  # tworzymy punkt P o współrzędnych (2, 3)
punktQ = (5, 7)  # tworzymy punkt Q o współrzędnych (5, 7)

euklidesowa, manhattan, rzeka, kolejowa = odleglosci(punktP, punktQ)  # wywołujemy funkcję i zapisujemy wyniki do osobnych zmiennych

print("Norma euklidesowa:", euklidesowa)  # wypisujemy odległość euklidesową
print("Norma Manhattan:", manhattan)  # wypisujemy odległość Manhattan
print("Norma rzeka:", rzeka)  # wypisujemy odległość w metryce rzeka
print("Norma kolejowa/centrum:", kolejowa)  # wypisujemy odległość w metryce kolejowej
```

![Odległości w R2(metryki)](zdjecia/odleglosci_w_R2.png)

Dla punktów:

$$
p = (x_1, x_2)
$$

oraz

$$
q = (y_1, y_2)
$$

chcemy policzyć odległość między nimi na kilka różnych sposobów.

## 1. Metryka euklidesowa
### Wzór

$$
d_2(p, q) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}
$$

### Jak to czytać po ludzku?

- bierzesz różnicę pierwszych współrzędnych,
- bierzesz różnicę drugich współrzędnych,
- obie różnice podnosisz do kwadratu,
- dodajesz je,
- z wyniku wyciągasz pierwiastek.

To jest zwykła „szkolna” odległość między dwoma punktami.

### Przykład

Dla:

$$
p = (2, 3), \quad q = (5, 7)
$$

liczymy:

$$
d_2(p, q) = \sqrt{(2 - 5)^2 + (3 - 7)^2}
$$

czyli:

$$
\sqrt{(-3)^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

---
## 2. Metryka Manhattan
### Wzór

$$
d_1(p, q) = |x_1 - y_1| + |x_2 - y_2|
$$

### Jak to czytać po ludzku?

- bierzesz różnicę pierwszych współrzędnych,
- bierzesz różnicę drugich współrzędnych,
- zamieniasz je na wartości dodatnie,
- dodajesz je.

Ta metryka przypomina poruszanie się po ulicach miasta: tylko poziomo i pionowo, bez skrótów na ukos.

### Przykład

Dla:

$$
p = (2, 3), \quad q = (5, 7)
$$

liczymy:

$$
d_1(p, q) = |2 - 5| + |3 - 7|
$$

czyli:

$$
3 + 4 = 7
$$

---

## 3. Metryka rzeki

Na slajdzie jest napisane, że rzeka to oś $Ox$.

To znaczy, że można poruszać się wzdłuż osi poziomej, a żeby przejść między punktami o różnych pierwszych współrzędnych, trzeba „zejść do rzeki”, przejść nią i potem „wejść” do drugiego punktu.

### Wzór

$$
d_R(p, q) =
\begin{cases}
|x_2 - y_2|, & x_1 = y_1 \\
|x_1 - y_1| + |x_2| + |y_2|, & x_1 \ne y_1
\end{cases}
$$

### Jak to czytać po ludzku?

#### Przypadek 1: gdy $x_1 = y_1$

Jeśli punkty mają tę samą pierwszą współrzędną, to leżą „nad tym samym miejscem” na osi poziomej.

Wtedy wystarczy policzyć tylko różnicę drugich współrzędnych:

$$
|x_2 - y_2|
$$

#### Przypadek 2: gdy $x_1 \ne y_1$

Wtedy:
- schodzisz z punktu $p$ do osi $Ox$,
- idziesz w poziomie do miejsca pod punktem $q$,
- wchodzisz do punktu $q$.

Dlatego liczymy:

$$
|x_1 - y_1| + |x_2| + |y_2|
$$

### Przykład

Dla:

$$
p = (2, 3), \quad q = (5, 7)
$$

mamy:

$$
x_1 \ne y_1
$$

więc używamy drugiego wzoru:

$$
d_R(p, q) = |2 - 5| + |3| + |7|
$$

czyli:

$$
3 + 3 + 7 = 13
$$

## Notatka z talicy

$$
\operatorname{euclid}(P,D)+\operatorname{euclid}(D,C)+\operatorname{euclid}(C,D)
$$

![wykres rzeka](zdjecia/wykres_rzeka.png)

---

## 4. Metryka kolejowa / centrum

Tutaj idea jest taka, że jeśli trzeba, jedziemy przez punkt centralny:

$$
(0, 0)
$$

### Wzór

$$
d_C(p, q) =
\begin{cases}
\|p - q\|_2, & p \text{ i } q \text{ leżą na jednej prostej przechodzącej przez } (0,0) \\
\|p\|_2 + \|q\|_2, & \text{w przeciwnym razie}
\end{cases}
$$

### Jak to czytać po ludzku?

#### Przypadek 1: punkty leżą na jednej prostej przechodzącej przez $(0,0)$

Wtedy można przejechać bezpośrednio między nimi.

Liczymy zwykłą odległość euklidesową:

$$
\|p - q\|_2
$$

czyli po prostu:

$$
\sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}
$$

#### Przypadek 2: punkty nie leżą na jednej takiej prostej

Wtedy:
- jedziesz z punktu $p$ do centrum $(0,0)$,
- potem z centrum do punktu $q$.

Czyli liczysz:

$$
\|p\|_2 + \|q\|_2
$$

To znaczy:
- długość odcinka od $(0,0)$ do $p$,
- plus długość odcinka od $(0,0)$ do $q$.

### Przykład

Dla:

$$
p = (2, 3), \quad q = (5, 7)
$$

sprawdzamy, czy punkty leżą na jednej prostej przechodzącej przez $(0,0)$.

Jeśli nie, to liczymy:

$$
d_C(p, q) = \|p\|_2 + \|q\|_2
$$

czyli:

$$
\sqrt{2^2 + 3^2} + \sqrt{5^2 + 7^2}
$$

czyli:

$$
\sqrt{13} + \sqrt{74}
$$

w przybliżeniu:

$$
3.6055 + 8.6023 = 12.2078
$$

## Notatka z tablicy

$$
\operatorname{euclid}(P,Q) = \sqrt{(q_1 - p_1)^2 + (q_2 - p_2)^2}
$$

Dla punktów:

$$
P = (p_1, p_2)
$$

$$
Q = (q_1, q_2)
$$

punkty $P$, $Q$, $O$ są współliniowe wtedy i tylko wtedy, gdy:

$$
\det
\begin{bmatrix}
p_1 & p_2 \\
q_1 & q_2
\end{bmatrix}
= p_1 q_2 - p_2 q_1 = 0
$$

Jeśli:

$$
\det = 0
$$

to:

$$
\operatorname{odległość}_{kolejowa}(P,Q) = \operatorname{euclid}(P,Q)
$$

w przeciwnym razie:

$$
\operatorname{odległość}_{kolejowa}(P,Q) = \operatorname{euclid}(P,O) + \operatorname{euclid}(Q,O)
$$

![Wykres odległości](zdjecia/wykres_odleglosci.png)

---

**Zadanie 3.** Napisz program, który obliczy normę: Frobeniusa, Manhattan, maximum dla $n \times m$-wymiarowej macierzy.

```python
import math  # importujemy moduł math, ponieważ używamy math.pow() i math.sqrt()

def normy_macierzy(macierz):  # funkcja liczy trzy normy macierzy: Frobeniusa, Manhattan i maksimum
    wiersze = len(macierz)  # zapisujemy liczbę wierszy macierzy
    kolumny = len(macierz[0])  # zapisujemy liczbę kolumn macierzy, czyli długość pierwszego wiersza

    # norma Frobeniusa  # pierwiastek z sumy kwadratów wszystkich elementów macierzy
    suma_kwadratow = 0  # tworzymy zmienną, w której będziemy przechowywać sumę kwadratów elementów
    for i in range(wiersze):  # przechodzimy po indeksach wierszy
        for j in range(kolumny):  # przechodzimy po indeksach kolumn
            suma_kwadratow += math.pow(macierz[i][j], 2)  # dodajemy kwadrat aktualnego elementu macierzy
    Frobeniusa = math.sqrt(suma_kwadratow)  # obliczamy pierwiastek z sumy kwadratów

    # norma Manhattan  # suma wartości bezwzględnych wszystkich elementów macierzy
    suma_modulow = 0  # tworzymy zmienną, w której będziemy przechowywać sumę modułów
    for i in range(wiersze):  # przechodzimy po indeksach wierszy
        for j in range(kolumny):  # przechodzimy po indeksach kolumn
            suma_modulow += abs(macierz[i][j])  # dodajemy wartość bezwzględną aktualnego elementu
    Manhattan = suma_modulow  # zapisujemy sumę modułów jako normę Manhattan

    # norma maksimum  # największa wartość bezwzględna spośród elementów macierzy
    maksimum = 0  # tworzymy zmienną przechowującą największą znalezioną wartość bezwzględną
    for i in range(wiersze):  # przechodzimy po indeksach wierszy
        for j in range(kolumny):  # przechodzimy po indeksach kolumn
            if abs(macierz[i][j]) > maksimum:  # sprawdzamy, czy aktualny moduł elementu jest większy niż dotychczasowe maksimum
                maksimum = abs(macierz[i][j])  # jeśli tak, aktualizujemy maksimum

    return Frobeniusa, Manhattan, maksimum  # zwracamy trzy obliczone normy

macierz = [  # tworzymy przykładową macierz
    [1, -2, 3],  # pierwszy wiersz macierzy
    [4, 5, -6]  # drugi wiersz macierzy
]  # koniec definicji macierzy

Frobeniusa, Manhattan, maksimum = normy_macierzy(macierz)  # wywołujemy funkcję i zapisujemy wyniki do osobnych zmiennych

print("Norma Frobeniusa:", Frobeniusa)  # wypisujemy normę Frobeniusa
print("Norma Manhattan:", Manhattan)  # wypisujemy normę Manhattan
print("Norma maksimum:", maksimum)  # wypisujemy normę maksimum
```

![normy macierzy](zdjecia/normy_macierzy.png)

Dla macierzy:

$$
A = [a_{ij}] \in \mathbb{R}^{n \times m}
$$

czyli macierzy o `n` wierszach i `m` kolumnach, można zdefiniować kilka norm.

---

## 1. Norma Frobeniusa
### Wzór

$$
\|A\|_F = \sqrt{\sum_{i=1}^{n}\sum_{j=1}^{m} a_{ij}^2}
$$

### Jak to czytać po ludzku?

- bierzesz wszystkie elementy macierzy,
- każdy podnosisz do kwadratu,
- dodajesz wszystkie te kwadraty,
- z otrzymanej sumy wyciągasz pierwiastek.

To jest odpowiednik normy euklidesowej dla macierzy.

### Przykład

Dla macierzy:

$$
A =
\begin{bmatrix}
1 & -2 & 3 \\
4 & 5 & -6
\end{bmatrix}
$$

liczymy:

$$
\|A\|_F = \sqrt{1^2 + (-2)^2 + 3^2 + 4^2 + 5^2 + (-6)^2}
$$

czyli:

$$
\sqrt{1 + 4 + 9 + 16 + 25 + 36} = \sqrt{91}
$$

---

## 2. Norma Manhattan
### Wzór

$$
\|A\|_{1,\text{sum}} = \sum_{i=1}^{n}\sum_{j=1}^{m} |a_{ij}|
$$

### Jak to czytać po ludzku?

- bierzesz wszystkie elementy macierzy,
- zamieniasz je na wartości dodatnie (wartości bezwzględne),
- dodajesz wszystkie te wartości.

To jest po prostu suma modułów wszystkich elementów macierzy.

### Przykład

Dla macierzy:

$$
A =
\begin{bmatrix}
1 & -2 & 3 \\
4 & 5 & -6
\end{bmatrix}
$$

liczymy:

$$
\|A\|_{1,\text{sum}} = |1| + |-2| + |3| + |4| + |5| + |-6|
$$

czyli:

$$
1 + 2 + 3 + 4 + 5 + 6 = 21
$$

---

## 3. Norma maksimum
### Wzór

$$
\|A\|_{\max} = \max_{1 \le i \le n,\; 1 \le j \le m} |a_{ij}|
$$

### Jak to czytać po ludzku?

- bierzesz wszystkie elementy macierzy,
- zamieniasz je na wartości dodatnie,
- wybierasz największą z nich.

To jest największy moduł spośród wszystkich elementów macierzy.

### Przykład

Dla macierzy:

$$
A =
\begin{bmatrix}
1 & -2 & 3 \\
4 & 5 & -6
\end{bmatrix}
$$

liczymy moduły elementów:

$$
|1| = 1,\quad |-2| = 2,\quad |3| = 3,\quad |4| = 4,\quad |5| = 5,\quad |-6| = 6
$$

największa z tych wartości to:

$$
6
$$

więc:

$$
\|A\|_{\max} = 6
$$

---

# Co oznaczają symbole?

## \(a_{ij}\)

To element macierzy znajdujący się:
- w `i`-tym wierszu,
- w `j`-tej kolumnie.

Na przykład w macierzy

$$
\begin{bmatrix}
1 & -2 & 3 \\
4 & 5 & -6
\end{bmatrix}
$$

- \(a_{11} = 1\)
- \(a_{12} = -2\)
- \(a_{23} = -6\)

---

## \(\sum \sum\)

Podwójna suma znaczy:
- przejdź po wszystkich wierszach,
- w każdym wierszu przejdź po wszystkich kolumnach,
- dodaj wszystkie elementy.

---

**Zadanie 4.** Napisz program, który wykona mnożenie dwóch macierzy. Kiedy działanie takie nie może zostać przeprowadzone? Sprawdź czy mnożenie macierzy jest przemienne lub łączne?

```python
def mnozenie_macierzy(macierz1, macierz2):  # funkcja mnoży dwie macierze
    ilosc_wierszy_macierz1 = len(macierz1)  # zapisujemy liczbę wierszy pierwszej macierzy
    ilosc_wierszy_macierz2 = len(macierz2)  # zapisujemy liczbę wierszy drugiej macierzy
    ilosc_kolumn_macierz1 = len(macierz1[0])  # zapisujemy liczbę kolumn pierwszej macierzy
    ilosc_kolumn_macierz2 = len(macierz2[0])  # zapisujemy liczbę kolumn drugiej macierzy

    if ilosc_kolumn_macierz1 != ilosc_wierszy_macierz2:  # sprawdzamy, czy liczba kolumn pierwszej macierzy jest równa liczbie wierszy drugiej macierzy
        raise ValueError("Nie da się pomnożyć tych macierzy")  # jeśli warunek nie jest spełniony, zgłaszamy błąd
    
    wynik = []  # tworzymy pustą listę na macierz wynikową
    for i in range(ilosc_wierszy_macierz1):  # przechodzimy po wierszach pierwszej macierzy
        wiersz = []  # tworzymy pusty wiersz wyniku
        for j in range(ilosc_kolumn_macierz2):  # przechodzimy po kolumnach drugiej macierzy
            suma = 0  # zerujemy sumę dla jednego elementu macierzy wynikowej
            for k in range(ilosc_kolumn_macierz1):  # przechodzimy po elementach wiersza pierwszej macierzy i kolumny drugiej macierzy
                suma += macierz1[i][k] * macierz2[k][j]  # mnożymy odpowiednie elementy i dodajemy je do sumy
            wiersz.append(suma)  # dodajemy obliczony element do aktualnego wiersza
        wynik.append(wiersz)  # dodajemy gotowy wiersz do macierzy wynikowej

    return wynik  # zwracamy macierz wynikową

macierz1 = [  # tworzymy pierwszą macierz
    [1, 2],  # pierwszy wiersz pierwszej macierzy
    [3, 4]  # drugi wiersz pierwszej macierzy
]  # koniec pierwszej macierzy

macierz2 = [  # tworzymy drugą macierz
    [5, 6],  # pierwszy wiersz drugiej macierzy
    [7, 8]  # drugi wiersz drugiej macierzy
]  # koniec drugiej macierzy

wynik = mnozenie_macierzy(macierz1, macierz2)  # wywołujemy funkcję mnożenia i zapisujemy wynik

print("Wynik mnożenia:")  # wypisujemy tekst informacyjny
for wiersz in wynik:  # przechodzimy po kolejnych wierszach wyniku
    print(wiersz)  # wypisujemy aktualny wiersz
```

# Mnożenie macierzy – notatka

## 1. Kiedy można mnożyć macierze?

Jeśli:

$$
A \in \mathbb{R}^{m_1 \times n_1}
\quad \text{oraz} \quad
B \in \mathbb{R}^{m_2 \times n_2}
$$

to iloczyn:

$$
AB
$$

istnieje **wtedy i tylko wtedy**, gdy:

$$
n_1 = m_2
$$

Czyli:

- liczba **kolumn** pierwszej macierzy
- musi być równa liczbie **wierszy** drugiej macierzy.

## 2. Jaki rozmiar ma wynik?

Jeśli mnożenie jest możliwe, to:

$$
AB \in \mathbb{R}^{m_1 \times n_2}
$$

czyli wynik ma:

- tyle wierszy, ile ma macierz **A**
- tyle kolumn, ile ma macierz **B**

## 3. Jak wygląda wzór na mnożenie macierzy?

Niech:

$$
A =
\begin{bmatrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m,1} & a_{m,2} & \cdots & a_{m,n}
\end{bmatrix}
$$

oraz

$$
B =
\begin{bmatrix}
b_{1,1} & b_{1,2} & \cdots & b_{1,k} \\
b_{2,1} & b_{2,2} & \cdots & b_{2,k} \\
\vdots & \vdots & \ddots & \vdots \\
b_{n,1} & b_{n,2} & \cdots & b_{n,k}
\end{bmatrix}
$$

Wtedy:

$$
C = AB
$$

jest macierzą postaci:

$$
C =
\begin{bmatrix}
c_{1,1} & c_{1,2} & \cdots & c_{1,k} \\
c_{2,1} & c_{2,2} & \cdots & c_{2,k} \\
\vdots & \vdots & \ddots & \vdots \\
c_{m,1} & c_{m,2} & \cdots & c_{m,k}
\end{bmatrix}
$$

a każdy element macierzy wynikowej liczymy ze wzoru:

$$
c_{i,j} = \sum_{l=1}^{n} a_{i,l} b_{l,j}
$$

dla:

$$
i = 1,2,\dots,m
\quad \text{oraz} \quad
j = 1,2,\dots,k
$$

## 4. Jak to czytać po ludzku?

Żeby policzyć element:

$$
c_{i,j}
$$

trzeba:

- wziąć **i-ty wiersz** z macierzy **A**
- i **j-tą kolumnę** z macierzy **B**
- pomnożyć odpowiadające sobie elementy
- dodać wszystkie wyniki

## 5. Przykład obliczania jednego elementu

Jeśli:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\quad \text{oraz} \quad
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
$$

to element:

$$
c_{1,1}
$$

liczymy tak:

- pierwszy wiersz z \(A\): \((1,2)\)
- pierwsza kolumna z \(B\): \((5,7)\)

więc:

$$
c_{1,1} = 1 \cdot 5 + 2 \cdot 7 = 5 + 14 = 19
$$

element:

$$
c_{1,2}
$$

- pierwszy wiersz z \(A\): \((1,2)\)
- druga kolumna z \(B\): \((6,8)\)

więc:

$$
c_{1,2} = 1 \cdot 6 + 2 \cdot 8 = 6 + 16 = 22
$$

element:

$$
c_{2,1}
$$

- drugi wiersz z \(A\): \((3,4)\)
- pierwsza kolumna z \(B\): \((5,7)\)

więc:

$$
c_{2,1} = 3 \cdot 5 + 4 \cdot 7 = 15 + 28 = 43
$$

element:

$$
c_{2,2}
$$

- drugi wiersz z \(A\): \((3,4)\)
- druga kolumna z \(B\): \((6,8)\)

więc:

$$
c_{2,2} = 3 \cdot 6 + 4 \cdot 8 = 18 + 32 = 50
$$

Czyli:

$$
AB =
\begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}
$$

## 6. Własności mnożenia macierzy

### Mnożenie macierzy nie jest przemienne

W ogólności:

$$
AB \ne BA
$$

To znaczy, że zmiana kolejności macierzy zwykle daje inny wynik.

### Mnożenie macierzy jest łączne

$$
(AB)C = A(BC)
$$

o ile wymiary macierzy pozwalają wykonać oba mnożenia.

### Mnożenie macierzy jest rozłączne względem dodawania

$$
A(B + C) = AB + AC
$$

oraz

$$
(A + B)C = AC + BC
$$

### Macierz jednostkowa jest elementem neutralnym

Jeśli \(I\) to macierz jednostkowa, to:

$$
AI = A
\quad \text{oraz} \quad
IA = A
$$

## 7. Przykład pokazujący, że \(AB \ne BA\)

Weźmy:

$$
A =
\begin{bmatrix}
1 & 2 \\
0 & 1
\end{bmatrix}
\quad , \quad
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

Zatem:

$$
AB \ne BA
$$

## 8. Łączność mnożenia

Dla macierzy o pasujących wymiarach zawsze zachodzi:

$$
(AB)C = A(BC)
$$

czyli wynik nie zależy od tego, które mnożenie wykonamy najpierw.

## 9. Koszt obliczeń

Jeśli:

$$
A \in \mathbb{R}^{m_1 \times n_1}
\quad \text{oraz} \quad
B \in \mathbb{R}^{n_1 \times n_2}
$$

to koszt obliczenia iloczynu \(AB\) wynosi:

$$
\Theta(m_1 \cdot n_1 \cdot n_2)
$$

czyli liczba działań rośnie w przybliżeniu jak:

- liczba wierszy pierwszej macierzy
- razy liczba wspólnego wymiaru
- razy liczba kolumn drugiej macierzy

## 10. Najkrócej

### Kiedy można mnożyć?
Gdy liczba kolumn pierwszej macierzy jest równa liczbie wierszy drugiej.

### Jaki rozmiar ma wynik?
Tyle wierszy co pierwsza macierz i tyle kolumn co druga.

### Jak liczymy element wyniku?
Wiersz z pierwszej macierzy razy kolumna z drugiej.

### Czy mnożenie jest przemienne?
Nie.

### Czy mnożenie jest łączne?
Tak.

---

**Zadanie 5*.** Zaprojektuj i utwórz klasę dla macierzy umożliwiającą tworzenie, wypisywanie i wykonywanie działań: mnożenie przez stałą, dodawanie, mnożenie.

```python
# definicja klasy Macierz
class Macierz:
    # funkcja uruchamiana przy tworzeniu nowego obiektu klasy
    def __init__(self, dane):
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

# wypisanie napisu informacyjnego
print("Macierz A:")

# wypisanie macierzy A
A.wypisz()

# wypisanie napisu informacyjnego
print("Macierz B:")

# wypisanie macierzy B
B.wypisz()

# wypisanie napisu informacyjnego
print("A + B:")

# dodanie macierzy A i B, a potem wypisanie wyniku
A.dodawanie(B).wypisz()

# wypisanie napisu informacyjnego
print("A * 2:")

# pomnożenie macierzy A przez 2, a potem wypisanie wyniku
A.mnozenie_przez_stala(2).wypisz()

# wypisanie napisu informacyjnego
print("A * B:")

# pomnożenie macierzy A i B, a potem wypisanie wyniku
A.mnozenie(B).wypisz()
```

## 1. Czym jest macierz?

Macierz to prostokątna tablica liczb ułożonych w wierszach i kolumnach.

Przykład:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

Ta macierz ma:
- 2 wiersze,
- 2 kolumny.

Elementy macierzy oznaczamy zwykle jako:

$$
a_{ij}
$$

gdzie:
- \(i\) oznacza numer wiersza,
- \(j\) oznacza numer kolumny.

Na przykład w macierzy:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

mamy:
- \(a_{11} = 1\)
- \(a_{12} = 2\)
- \(a_{21} = 3\)
- \(a_{22} = 4\)

---

## 2. Mnożenie macierzy przez stałą

Jeśli mamy macierz:

$$
A =
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
$$

i liczbę \(c\), to mnożenie macierzy przez stałą polega na pomnożeniu **każdego elementu macierzy** przez tę liczbę.

Wzór:

$$
cA =
\begin{bmatrix}
c a_{11} & c a_{12} \\
c a_{21} & c a_{22}
\end{bmatrix}
$$

### Przykład

Dla:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

mnożenie przez \(2\) daje:

$$
2A =
\begin{bmatrix}
2 \cdot 1 & 2 \cdot 2 \\
2 \cdot 3 & 2 \cdot 4
\end{bmatrix}
=
\begin{bmatrix}
2 & 4 \\
6 & 8
\end{bmatrix}
$$

### Jak to rozumieć?

Każdy element macierzy zmienia się proporcjonalnie do tej stałej.

---

## 3. Dodawanie macierzy

Dwie macierze można dodać tylko wtedy, gdy mają **te same wymiary**, czyli tyle samo wierszy i tyle samo kolumn.

Jeśli:

$$
A =
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
\quad \text{oraz} \quad
B =
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{bmatrix}
$$

to:

$$
A + B =
\begin{bmatrix}
a_{11}+b_{11} & a_{12}+b_{12} \\
a_{21}+b_{21} & a_{22}+b_{22}
\end{bmatrix}
$$

Czyli dodajemy do siebie elementy leżące w tych samych miejscach.

### Przykład

Niech:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\quad \text{oraz} \quad
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
$$

Wtedy:

$$
A + B =
\begin{bmatrix}
1+5 & 2+6 \\
3+7 & 4+8
\end{bmatrix}
=
\begin{bmatrix}
6 & 8 \\
10 & 12
\end{bmatrix}
$$

### Kiedy nie można dodawać?

Nie można dodać macierzy o różnych wymiarach, na przykład:
- \(2 \times 2\) i \(2 \times 3\),
- \(3 \times 2\) i \(2 \times 2\).

---

## 4. Mnożenie macierzy

Mnożenie macierzy jest trudniejsze niż dodawanie.

Jeśli:

$$
A \in \mathbb{R}^{m \times n}
\quad \text{oraz} \quad
B \in \mathbb{R}^{n \times k}
$$

to iloczyn:

$$
AB
$$

istnieje i ma wymiary:

$$
m \times k
$$

### Warunek mnożenia

Macierze można pomnożyć tylko wtedy, gdy:

- liczba kolumn pierwszej macierzy
- jest równa liczbie wierszy drugiej macierzy.

---

## 5. Jak liczy się elementy iloczynu?

Jeśli:

$$
C = AB
$$

to każdy element macierzy wynikowej obliczamy ze wzoru:

$$
c_{ij} = \sum_{l=1}^{n} a_{il} b_{lj}
$$

To znaczy:

- bierzemy \(i\)-ty wiersz macierzy \(A\),
- bierzemy \(j\)-tą kolumnę macierzy \(B\),
- mnożymy odpowiadające sobie elementy,
- dodajemy wyniki.

---

## 6. Przykład mnożenia macierzy

Niech:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\quad \text{oraz} \quad
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
$$

Szukamy:

$$
AB
$$

### Element \(c_{11}\)

Pierwszy wiersz macierzy \(A\):

$$
(1,2)
$$

Pierwsza kolumna macierzy \(B\):

$$
\begin{bmatrix}
5 \\
7
\end{bmatrix}
$$

Liczymy:

$$
c_{11} = 1 \cdot 5 + 2 \cdot 7 = 5 + 14 = 19
$$

### Element \(c_{12}\)

Pierwszy wiersz macierzy \(A\):

$$
(1,2)
$$

Druga kolumna macierzy \(B\):

$$
\begin{bmatrix}
6 \\
8
\end{bmatrix}
$$

Liczymy:

$$
c_{12} = 1 \cdot 6 + 2 \cdot 8 = 6 + 16 = 22
$$

### Element \(c_{21}\)

Drugi wiersz macierzy \(A\):

$$
(3,4)
$$

Pierwsza kolumna macierzy \(B\):

$$
\begin{bmatrix}
5 \\
7
\end{bmatrix}
$$

Liczymy:

$$
c_{21} = 3 \cdot 5 + 4 \cdot 7 = 15 + 28 = 43
$$

### Element \(c_{22}\)

Drugi wiersz macierzy \(A\):

$$
(3,4)
$$

Druga kolumna macierzy \(B\):

$$
\begin{bmatrix}
6 \\
8
\end{bmatrix}
$$

Liczymy:

$$
c_{22} = 3 \cdot 6 + 4 \cdot 8 = 18 + 32 = 50
$$

Zatem:

$$
AB =
\begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}
$$

---

## 7. Ważne własności działań na macierzach

### Dodawanie macierzy
Dodawanie macierzy jest:
- **przemienne**:

$$
A + B = B + A
$$

- **łączne**:

$$
(A + B) + C = A + (B + C)
$$

---

### Mnożenie przez stałą
Jeśli \(c\) jest liczbą, to:

$$
c(A+B)=cA+cB
$$

oraz:

$$
(c+d)A = cA + dA
$$

---

### Mnożenie macierzy
Mnożenie macierzy:
- **nie jest przemienne**:

$$
AB \ne BA
$$

- jest **łączne**:

$$
(AB)C = A(BC)
$$

- jest **rozdzielne względem dodawania**:

$$
A(B+C)=AB+AC
$$

oraz

$$
(A+B)C=AC+BC
$$

---

## 8. Podsumowanie

W tym zadaniu klasa macierzy ma odwzorowywać podstawowe działania matematyczne:

### Mnożenie przez stałą
Każdy element macierzy mnożymy przez daną liczbę.

### Dodawanie
Dodajemy do siebie elementy stojące na tych samych pozycjach.
Można to zrobić tylko dla macierzy o tych samych wymiarach.

### Mnożenie
Aby pomnożyć dwie macierze:
- liczba kolumn pierwszej musi być równa liczbie wierszy drugiej,
- każdy element wyniku oblicza się jako sumę iloczynów elementów odpowiedniego wiersza i kolumny.

---

## 9. Najkrócej

- **mnożenie przez stałą** – każdy element razy liczba,
- **dodawanie** – element do elementu,
- **mnożenie macierzy** – wiersz razy kolumna.

---

# Lab 4

# Zadanie 1

Napisz funkcję zwracającą wyznacznik macierzy kwadratowej dowolnego rozmiaru.

## Jak rozumieć to zadanie?

Wyznacznik można policzyć tylko dla **macierzy kwadratowej**, czyli takiej, która ma tyle samo wierszy co kolumn.

Dla małych macierzy są proste wzory:

### Dla macierzy $1 \times 1$

$$
\det(A) = a_{11}
$$

### Dla macierzy $2 \times 2$

$$
\det(A) =
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix}
= ad - bc
$$

### Dla większych macierzy

Stosujemy **rozwinięcie Laplace’a** względem pierwszego wiersza:

$$
\det(A)=\sum_{j=1}^{n}(-1)^{1+j}a_{1j}M_{1j}
$$

gdzie $M_{1j}$ to minor, czyli wyznacznik macierzy powstałej po skreśleniu pierwszego wiersza i $j$-tej kolumny.

## Jak rozumieć schemat implementacji?

### Krok 1

Sprawdzasz, czy macierz jest kwadratowa.

### Krok 2

Jeśli macierz ma rozmiar $1 \times 1$, zwracasz jedyny element.

### Krok 3

Jeśli macierz ma rozmiar $2 \times 2$, liczysz wyznacznik ze wzoru:

$$
ad - bc
$$

### Krok 4

Dla większych macierzy:
- tworzysz minory,
- liczysz ich wyznaczniki rekurencyjnie,
- sumujesz wszystko ze znakami $+$ i $-$.

## Kod

```python
import math  # importujemy moduł math, ponieważ później używamy funkcji math.pow()

def minor(macierz, usun_wiersz, usun_kolumne):  # funkcja tworzy minor, czyli macierz po usunięciu jednego wiersza i jednej kolumny
    wynik = []  # tworzymy pustą listę, do której będą dodawane wiersze nowej macierzy

    for i in range(len(macierz)):  # przechodzimy po wszystkich wierszach macierzy
        if i == usun_wiersz:  # sprawdzamy, czy aktualny wiersz jest tym, który trzeba usunąć
            continue  # pomijamy ten wiersz i przechodzimy do następnego

        nowy_wiersz = []  # tworzymy pusty wiersz dla nowej macierzy
        for j in range(len(macierz[i])):  # przechodzimy po wszystkich kolumnach w aktualnym wierszu
            if j == usun_kolumne:  # sprawdzamy, czy aktualna kolumna jest tą, którą trzeba usunąć
                continue  # pomijamy ten element i przechodzimy do następnej kolumny
            nowy_wiersz.append(macierz[i][j])  # dodajemy element do nowego wiersza, jeśli nie leży w usuwanej kolumnie

        wynik.append(nowy_wiersz)  # dodajemy gotowy wiersz do macierzy wynikowej

    return wynik  # zwracamy macierz po usunięciu wskazanego wiersza i kolumny

def wyznacznik_macierzy(macierz):  # funkcja liczy wyznacznik macierzy
    n = len(macierz)  # zapisujemy liczbę wierszy macierzy
    
    for wiersz in macierz:  # przechodzimy po każdym wierszu macierzy
        if len(wiersz) != n:  # sprawdzamy, czy liczba kolumn jest równa liczbie wierszy
            raise ValueError("Nie da się policzyc wyznacznika macierzy, która nie jest kwadratowa")  # zgłaszamy błąd, jeśli macierz nie jest kwadratowa
        
    if n == 1:  # sprawdzamy przypadek macierzy 1 × 1
        return macierz[0][0]  # wyznacznik macierzy 1 × 1 to jej jedyny element
    
    if n == 2:  # sprawdzamy przypadek macierzy 2 × 2
        return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]  # liczymy wyznacznik ze wzoru ad - bc
    
    det = 0  # ustawiamy początkową wartość wyznacznika na 0
    for j in range(n):  # przechodzimy po kolejnych elementach pierwszego wiersza
        podmacierz = minor(macierz, 0, j)  # tworzymy minor przez usunięcie pierwszego wiersza i kolumny j
        det += math.pow((-1), 0+j) * macierz[0][j] * wyznacznik_macierzy(podmacierz)  # dodajemy kolejny składnik rozwinięcia Laplace'a

    return det  # zwracamy obliczony wyznacznik

macierz = [  # tworzymy macierz, dla której będzie liczony wyznacznik
    [2, 4, 6],  # pierwszy wiersz macierzy
    [0, 2, -1],  # drugi wiersz macierzy
    [-3, 3, 3]  # trzeci wiersz macierzy
]  # koniec definicji macierzy

print("Wyznacznik macierzy: ", wyznacznik_macierzy(macierz))  # wypisujemy wynik działania funkcji wyznacznik_macierzy
```

## Wynik

Dla macierzy

$$
A=
\begin{bmatrix}
2 & 4 & 6 \\
0 & 2 & -1 \\
-3 & 3 & 3
\end{bmatrix}
$$

otrzymujemy:

$$
\det(A)=66
$$

---

# Zadanie 2

Napisz funkcję zwracającą transpozycję macierzy dowolnego rozmiaru.

## Co to jest transpozycja?

Transpozycja macierzy polega na zamianie:

* wierszy na kolumny,
* kolumn na wiersze.

Jeśli:

$$
A=
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

to:

$$
A^T=
\begin{bmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix}
$$

## Jak rozumieć schemat implementacji?

### Krok 1

Sprawdzasz liczbę wierszy i kolumn.

### Krok 2

Tworzysz nową macierz wynikową.

### Krok 3

Dla każdej kolumny starej macierzy tworzysz nowy wiersz.

Czyli element:

$$
a_{ij}
$$

staje się elementem:

$$
a_{ji}
$$

## Kod

```python
def transpozycja(macierz):  # funkcja wykonuje transpozycję macierzy, czyli zamienia wiersze na kolumny
    liczba_wierszy = len(macierz)  # zapisujemy liczbę wierszy macierzy
    liczba_kolumn = len(macierz[0])  # zapisujemy liczbę kolumn macierzy, czyli długość pierwszego wiersza

    wynik = []  # tworzymy pustą listę, do której będziemy dodawać wiersze macierzy po transpozycji

    for j in range(liczba_kolumn):  # przechodzimy po kolumnach starej macierzy
        nowy_wiersz = []  # tworzymy nowy wiersz macierzy wynikowej
        for i in range(liczba_wierszy):  # przechodzimy po wierszach starej macierzy
            nowy_wiersz.append(macierz[i][j])  # dodajemy element z kolumny starej macierzy do nowego wiersza
        wynik.append(nowy_wiersz)  # dodajemy gotowy nowy wiersz do macierzy wynikowej

    return wynik  # zwracamy macierz po transpozycji


macierz = [  # tworzymy macierz, którą będziemy transponować
    [2, 4, 6],  # pierwszy wiersz macierzy
    [0, 2, -1],  # drugi wiersz macierzy
    [-3, 3, 3]  # trzeci wiersz macierzy
]  # koniec definicji macierzy

print("Przed transpozycją macierzy:")  # wypisujemy informację, że poniżej będzie macierz przed transpozycją
for wiersz in macierz:  # przechodzimy po kolejnych wierszach macierzy
    print(wiersz)  # wypisujemy aktualny wiersz macierzy

wynik = transpozycja(macierz)  # wywołujemy funkcję transpozycja i zapisujemy wynik do zmiennej wynik

print("Po transpozycji macierzy:")  # wypisujemy informację, że poniżej będzie macierz po transpozycji
for wiersz in wynik:  # przechodzimy po kolejnych wierszach macierzy po transpozycji
    print(wiersz)  # wypisujemy aktualny wiersz macierzy wynikowej
```

## Wynik

Dla macierzy:

$$
\begin{bmatrix}
2 & 4 & 6 \\
0 & 2 & -1 \\
-3 & 3 & 3
\end{bmatrix}
$$

transpozycja ma postać:

$$
\begin{bmatrix}
2 & 0 & -3 \\
4 & 2 & 3 \\
6 & -1 & 3
\end{bmatrix}
$$

---

# Zadanie 3

Napisz funkcję znajdującą macierz odwrotną do macierzy kwadratowej dowolnego rozmiaru za pomocą:

* a) rozwinięcia Laplace’a
* b) metody Gaussa-Jordana

## Zadanie 3a — macierz odwrotna metodą Laplace’a

## Idea metody

Jeśli macierz $A$ ma wyznacznik różny od zera, to macierz odwrotna istnieje i można ją policzyć ze wzoru:

$$
A^{-1} = \frac{1}{\det(A)} \cdot Adj
$$

gdzie:

* $det(A)$ to wyznacznik,
* $Adj$ to macierz dołączona, czyli transpozycja macierzy dopełnień algebraicznych.

## Jak rozumieć schemat implementacji?

### Krok 1

Liczysz wyznacznik macierzy.

### Krok 2

Jeśli wyznacznik jest równy 0, macierz nie ma odwrotności.

### Krok 3

Dla każdego elementu liczysz minor i dopełnienie algebraiczne:

$$
C_{ij} = (-1)^{i+j} \det(M_{ij})
$$

### Krok 4

Tworzysz macierz dopełnień algebraicznych.

### Krok 5

Robisz jej transpozycję, czyli macierz dołączoną.

### Krok 6

Dzielisz każdy element przez wyznacznik.

## Kod

```python
import math  # importujemy moduł math, ponieważ używamy funkcji math.pow()

def minor(macierz, usun_wiersz, usun_kolumne):  # funkcja tworzy minor, czyli macierz po usunięciu wskazanego wiersza i kolumny
    wynik = []  # tworzymy pustą listę na macierz wynikową

    for i in range(len(macierz)):  # przechodzimy po indeksach wszystkich wierszy macierzy
        if i == usun_wiersz:  # sprawdzamy, czy aktualny wiersz jest tym, który ma zostać usunięty
            continue  # pomijamy ten wiersz

        nowy_wiersz = []  # tworzymy pusty wiersz do nowej macierzy
        for j in range(len(macierz[i])):  # przechodzimy po indeksach wszystkich kolumn w aktualnym wierszu
            if j == usun_kolumne:  # sprawdzamy, czy aktualna kolumna jest tą, która ma zostać usunięta
                continue  # pomijamy ten element
            nowy_wiersz.append(macierz[i][j])  # dodajemy element do nowego wiersza, jeśli nie jest w usuwanej kolumnie

        wynik.append(nowy_wiersz)  # dodajemy nowy wiersz do macierzy wynikowej

    return wynik  # zwracamy minor macierzy

def wyznacznik_macierzy(macierz):  # funkcja liczy wyznacznik macierzy
    n = len(macierz)  # zapisujemy liczbę wierszy macierzy
    
    for wiersz in macierz:  # przechodzimy po każdym wierszu macierzy
        if len(wiersz) != n:  # sprawdzamy, czy liczba kolumn jest równa liczbie wierszy
            raise ValueError("Nie da się policzyc wyznacznika macierzy, która nie jest kwadratowa")  # zgłaszamy błąd, jeśli macierz nie jest kwadratowa
        
    if n == 1:  # sprawdzamy przypadek macierzy 1 × 1
        return macierz[0][0]  # wyznacznik macierzy 1 × 1 to jej jedyny element
    
    if n == 2:  # sprawdzamy przypadek macierzy 2 × 2
        return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]  # liczymy wyznacznik ze wzoru ad - bc
    
    det = 0  # ustawiamy początkową wartość wyznacznika na 0
    for j in range(n):  # przechodzimy po elementach pierwszego wiersza
        podmacierz = minor(macierz, 0, j)  # tworzymy minor przez usunięcie pierwszego wiersza i kolumny j
        det += math.pow((-1), 0+j) * macierz[0][j] * wyznacznik_macierzy(podmacierz)  # dodajemy składnik rozwinięcia Laplace'a

    return det  # zwracamy obliczony wyznacznik

def transpozycja(macierz):  # funkcja wykonuje transpozycję macierzy
    liczba_wierszy = len(macierz)  # zapisujemy liczbę wierszy macierzy
    liczba_kolumn = len(macierz[0])  # zapisujemy liczbę kolumn macierzy

    wynik = []  # tworzymy pustą macierz wynikową

    for j in range(liczba_kolumn):  # przechodzimy po kolumnach starej macierzy
        nowy_wiersz = []  # tworzymy nowy wiersz macierzy po transpozycji
        for i in range(liczba_wierszy):  # przechodzimy po wierszach starej macierzy
            nowy_wiersz.append(macierz[i][j])  # dodajemy element z kolumny starej macierzy do wiersza nowej macierzy
        wynik.append(nowy_wiersz)  # dodajemy gotowy wiersz do macierzy wynikowej

    return wynik  # zwracamy macierz po transpozycji

def zeros(n,m):  # funkcja tworzy macierz zerową o wymiarach n × m
    macierz = []  # tworzymy pustą listę na macierz

    for i in range(n):  # przechodzimy po liczbie wierszy
        wiersz = []  # tworzymy pusty wiersz
        for j in range(m):  # przechodzimy po liczbie kolumn
            wiersz.append(0)  # dodajemy zero do aktualnego wiersza
        macierz.append(wiersz)  # dodajemy gotowy wiersz do macierzy

    return macierz  # zwracamy macierz zerową

def macierz_odwrotna_Laplace(macierz): # punkt a  # funkcja liczy macierz odwrotną metodą dopełnień algebraicznych
    n = len(macierz)  # zapisujemy rozmiar macierzy
    d = wyznacznik_macierzy(macierz)  # liczymy wyznacznik macierzy

    if d == 0:  # sprawdzamy, czy wyznacznik jest równy zero
        raise ValueError("Macierz jest osobliwa, nie ma odwrotności")  # jeśli wyznacznik jest zerowy, macierz nie ma odwrotności
    
    C = zeros(n, n)  # tworzymy macierz dopełnień algebraicznych wypełnioną zerami

    for i in range(n):  # przechodzimy po wierszach macierzy
        for j in range(n):  # przechodzimy po kolumnach macierzy
            M = minor(macierz, i, j)  # tworzymy minor przez usunięcie wiersza i oraz kolumny j
            C[i][j] = math.pow(-1, i+j) * wyznacznik_macierzy(M)  # liczymy dopełnienie algebraiczne elementu a_ij

    Adj = transpozycja(C)  # tworzymy macierz dołączoną, czyli transponujemy macierz dopełnień algebraicznych
    
    wynik = zeros(n, n)  # tworzymy pustą macierz wynikową wypełnioną zerami
    for i in range(n):  # przechodzimy po wierszach macierzy wynikowej
        for j in range(n):  # przechodzimy po kolumnach macierzy wynikowej
            wynik[i][j] = Adj[i][j] / d  # dzielimy każdy element macierzy dołączonej przez wyznacznik macierzy

    return wynik  # zwracamy macierz odwrotną

macierz = [  # tworzymy macierz, dla której będziemy liczyć macierz odwrotną
    [2, 4, 6],  # pierwszy wiersz macierzy
    [0, 2, -1],  # drugi wiersz macierzy
    [-3, 3, 3]  # trzeci wiersz macierzy
]  # koniec definicji macierzy

wynik_Laplace = macierz_odwrotna_Laplace(macierz)  # liczymy macierz odwrotną metodą Laplace'a i zapisujemy wynik

print("Macierz odwrotna Laplace:")  # wypisujemy opis wyniku
for wiersz in wynik_Laplace:  # przechodzimy po kolejnych wierszach macierzy odwrotnej
    print(wiersz)  # wypisujemy aktualny wiersz macierzy odwrotnej
```

## Wynik

Dla macierzy:

$$
A=
\begin{bmatrix}
2 & 4 & 6 \\
0 & 2 & -1 \\
-3 & 3 & 3
\end{bmatrix}
$$

otrzymujemy macierz odwrotną:

$$
A^{-1}=
\begin{bmatrix}
0.13636363636363635 & 0.09090909090909091 & -0.24242424242424243 \\
0.045454545454545456 & 0.36363636363636365 & 0.030303030303030304 \\
0.09090909090909091 & -0.2727272727272727 & 0.06060606060606061
\end{bmatrix}
$$

## Zadanie 3b — macierz odwrotna metodą Gaussa-Jordana

## Idea metody

Tworzy się macierz rozszerzoną:

$$
[A \mid I]
$$

a następnie wykonuje się operacje na wierszach tak, aby lewa część stała się macierzą jednostkową:

$$
[I \mid A^{-1}]
$$

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz macierz rozszerzoną:

* po lewej masz macierz $A$,
* po prawej macierz jednostkową $I$.

### Krok 2

Dla każdej kolumny ustawiasz jedynkę na przekątnej.

### Krok 3

Wyzerowujesz pozostałe elementy w tej kolumnie.

### Krok 4

Po zakończeniu prawa część jest macierzą odwrotną.

## Kod

```python
import math  # importujemy moduł math, chociaż w tym kodzie nie jest bezpośrednio używany

def macierz_odwrotna_Gaussa_Jordana(macierz): # punkt b  # funkcja liczy macierz odwrotną metodą Gaussa-Jordana
    n = len(macierz)  # zapisujemy liczbę wierszy macierzy

    for wiersz in macierz:  # przechodzimy po każdym wierszu macierzy
        if len(wiersz) != n:  # sprawdzamy, czy liczba kolumn jest równa liczbie wierszy
            raise ValueError("Macierz musi być kwadratowa")  # zgłaszamy błąd, jeśli macierz nie jest kwadratowa

    # macierz rozszerzona [A | I]  # będziemy tworzyć macierz złożoną z macierzy A oraz macierzy jednostkowej
    rozszerzona_macierz = []  # tworzymy pustą listę na macierz rozszerzoną

    for i in range(n):  # przechodzimy po kolejnych wierszach macierzy
        wiersz = []  # tworzymy pusty wiersz macierzy rozszerzonej

        # lewa strona: macierz A  # najpierw wpisujemy elementy oryginalnej macierzy
        for j in range(n):  # przechodzimy po kolumnach macierzy A
            wiersz.append(macierz[i][j])  # dodajemy element z macierzy A do aktualnego wiersza
            # wiersz.append(float(macierz[i][j]))  # alternatywnie można byłoby od razu zamienić elementy na liczby zmiennoprzecinkowe
        
        # prawa strona: macierz jednostkowa I  # potem dopisujemy macierz jednostkową po prawej stronie
        for j in range(n):  # przechodzimy po kolumnach macierzy jednostkowej
            if i == j:  # sprawdzamy, czy element leży na przekątnej głównej
                wiersz.append(1)  # jeśli tak, wpisujemy 1
            else:  # jeśli element nie leży na przekątnej głównej
                wiersz.append(0)  # wpisujemy 0

        rozszerzona_macierz.append(wiersz)  # dodajemy gotowy wiersz do macierzy rozszerzonej

    # algorytm Gaussa-Jordana  # zaczynamy przekształcanie macierzy rozszerzonej
    for i in range(n):  # przechodzimy po kolejnych kolumnach głównych
        # jeśli na przekątnej jest 0, zamień wiersze  # element główny nie może być zerem
        if rozszerzona_macierz[i][i] == 0:  # sprawdzamy, czy element główny jest równy zero
            znaleziono = False  # zakładamy, że jeszcze nie znaleziono wiersza do zamiany
            for k in range(i+1, n):  # szukamy niżej wiersza, który ma niezerowy element w tej samej kolumnie
                if rozszerzona_macierz[k][i] != 0:  # sprawdzamy, czy dany wiersz ma niezerowy element
                    rozszerzona_macierz[i], rozszerzona_macierz[k] = rozszerzona_macierz[k], rozszerzona_macierz[i]  # zamieniamy aktualny wiersz z wybranym wierszem
                    znaleziono = True  # zapisujemy, że udało się znaleźć wiersz do zamiany
                    break  # kończymy szukanie, bo zamiana została wykonana
            if not znaleziono:  # sprawdzamy, czy nie udało się znaleźć odpowiedniego wiersza
                raise ValueError("Macierz nie ma odwrotności")  # jeśli nie ma wiersza do zamiany, macierz nie ma odwrotności
            
        # dzielenie całego wiersza przez element główny  # normalizujemy wiersz, żeby na przekątnej otrzymać 1
        element_glowny = rozszerzona_macierz[i][i]  # zapisujemy element główny z przekątnej
        for j in range(2 * n):  # przechodzimy po wszystkich kolumnach macierzy rozszerzonej
            rozszerzona_macierz[i][j] = rozszerzona_macierz[i][j] / element_glowny  # dzielimy każdy element wiersza przez element główny

        # zerowanie pozostałych elementów w tej kolumnie  # robimy zera nad i pod elementem głównym
        for k in range(n):  # przechodzimy po wszystkich wierszach
            if k != i:  # pomijamy aktualny wiersz główny
                wspolczynnik = rozszerzona_macierz[k][i]  # zapisujemy liczbę, którą trzeba wyzerować
                for j in range(2 * n):  # przechodzimy po wszystkich kolumnach macierzy rozszerzonej
                    rozszerzona_macierz[k][j] = rozszerzona_macierz[k][j] - wspolczynnik * rozszerzona_macierz[i][j]  # odejmujemy odpowiednią wielokrotność wiersza głównego

    odwrotna = []  # tworzymy pustą listę na macierz odwrotną
    for i in range(n):  # przechodzimy po wierszach macierzy rozszerzonej
        wiersz = []  # tworzymy pusty wiersz macierzy odwrotnej
        for j in range(n, 2 * n):  # przechodzimy tylko po prawej części macierzy rozszerzonej
            wiersz.append(rozszerzona_macierz[i][j])  # dodajemy element z prawej strony, czyli z macierzy odwrotnej
        odwrotna.append(wiersz)  # dodajemy gotowy wiersz do macierzy odwrotnej

    return odwrotna  # zwracamy obliczoną macierz odwrotną

macierz = [  # tworzymy macierz, dla której będziemy liczyć macierz odwrotną
    [2, 4, 6],  # pierwszy wiersz macierzy
    [0, 2, -1],  # drugi wiersz macierzy
    [-3, 3, 3]  # trzeci wiersz macierzy
]  # koniec definicji macierzy

wynik_Gauss_Jordan = macierz_odwrotna_Gaussa_Jordana(macierz)  # wywołujemy funkcję i zapisujemy wynik

print("Macierz odwrotna Gauss Jordan:")  # wypisujemy opis wyniku
for wiersz in wynik_Gauss_Jordan:  # przechodzimy po kolejnych wierszach macierzy odwrotnej
    print(wiersz)  # wypisujemy aktualny wiersz macierzy odwrotnej
```

## Wynik
Otrzymujemy macierz odwrotną:

$$
A^{-1}=
\begin{bmatrix}
0.13636363636363635 & 0.09090909090909083 & -0.24242424242424243 \\
0.045454545454545456 & 0.36363636363636365 & 0.030303030303030304 \\
0.09090909090909091 & -0.2727272727272727 & 0.06060606060606061
\end{bmatrix}
$$

## Porównanie wyników obu metod

Obie metody dają tę samą macierz odwrotną.
Mogą pojawić się bardzo małe różnice w zapisie dziesiętnym, ale wynik matematycznie jest ten sam.

---

# Zadanie 4

Napisz funkcję, która wykona mnożenie dwóch macierzy.

## Kiedy można mnożyć macierze?

Macierze można mnożyć tylko wtedy, gdy:

* liczba kolumn pierwszej macierzy
* jest równa liczbie wierszy drugiej macierzy.

Jeśli:

$$
A \in \mathbb{R}^{m \times n}, \qquad B \in \mathbb{R}^{n \times k}
$$

to wynik ma rozmiar:

$$
AB \in \mathbb{R}^{m \times k}
$$

## Jak rozumieć schemat implementacji?

### Krok 1

Sprawdzasz zgodność wymiarów.

### Krok 2

Dla każdego elementu wyniku liczysz sumę iloczynów elementów odpowiedniego wiersza i kolumny.

Czyli:

$$
c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}
$$

## Kod

```python
def mnozenie_macierzy(macierz1, macierz2):  # funkcja mnoży dwie macierze
    ilosc_wierszy_macierz1 = len(macierz1)  # zapisujemy liczbę wierszy pierwszej macierzy
    ilosc_wierszy_macierz2 = len(macierz2)  # zapisujemy liczbę wierszy drugiej macierzy
    ilosc_kolumn_macierz1 = len(macierz1[0])  # zapisujemy liczbę kolumn pierwszej macierzy
    ilosc_kolumn_macierz2 = len(macierz2[0])  # zapisujemy liczbę kolumn drugiej macierzy

    if ilosc_kolumn_macierz1 != ilosc_wierszy_macierz2:  # sprawdzamy, czy można pomnożyć macierze
        raise ValueError("Nie da się pomnożyć tych macierzy")  # zgłaszamy błąd, jeśli liczba kolumn pierwszej macierzy nie jest równa liczbie wierszy drugiej macierzy
    
    wynik = []  # tworzymy pustą listę na macierz wynikową
    for i in range(ilosc_wierszy_macierz1):  # przechodzimy po wierszach pierwszej macierzy
        wiersz = []  # tworzymy pusty wiersz macierzy wynikowej
        for j in range(ilosc_kolumn_macierz2):  # przechodzimy po kolumnach drugiej macierzy
            suma = 0  # ustawiamy początkową sumę na 0
            for k in range(ilosc_kolumn_macierz1):  # przechodzimy po elementach, które trzeba przez siebie pomnożyć i dodać
                suma += macierz1[i][k] * macierz2[k][j]  # dodajemy iloczyn odpowiednich elementów do sumy
            wiersz.append(suma)  # dodajemy obliczony element do wiersza macierzy wynikowej
        wynik.append(wiersz)  # dodajemy gotowy wiersz do macierzy wynikowej

    return wynik  # zwracamy wynik mnożenia macierzy

macierz1 = [  # tworzymy pierwszą macierz
    [1, 2],  # pierwszy wiersz pierwszej macierzy
    [3, 4]  # drugi wiersz pierwszej macierzy
]  # koniec definicji pierwszej macierzy

macierz2 = [  # tworzymy drugą macierz
    [5, 6],  # pierwszy wiersz drugiej macierzy
    [7, 8]  # drugi wiersz drugiej macierzy
]  # koniec definicji drugiej macierzy

wynik = mnozenie_macierzy(macierz1, macierz2)  # wywołujemy funkcję mnożenia macierzy i zapisujemy wynik

print("Wynik mnożenia:")  # wypisujemy opis wyniku
for wiersz in wynik:  # przechodzimy po kolejnych wierszach macierzy wynikowej
    print(wiersz)  # wypisujemy aktualny wiersz macierzy wynikowej
```

---

## Wynik

Dla:

$$
A=
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
$$

otrzymujemy:

$$
AB=
\begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}
$$

---

# Zadanie 5

Korzystając z rozwiązań poprzednich zadań wykonaj następujące mnożenia macierzowe: $A \cdot A^{-1}$ oraz $A^{-1} \cdot A$ i porównaj ich wyniki.

## Idea zadania

Jeśli macierz (A) jest odwracalna, to powinno zachodzić:

$$
A \cdot A^{-1} = I
$$

oraz

$$
A^{-1} \cdot A = I
$$

gdzie $I$ to macierz jednostkowa.

Czyli zadanie polega na sprawdzeniu, czy wyznaczona wcześniej macierz odwrotna rzeczywiście jest poprawna.

## Jak rozumieć schemat implementacji?

### Krok 1

Liczysz macierz odwrotną.

### Krok 2

Mnożysz:

* $A \cdot A^{-1}$
* $A^{-1} \cdot A$

### Krok 3

Porównujesz wyniki z macierzą jednostkową.

Jeśli pojawiają się małe liczby typu:

$$
2.220446049250313 \cdot 10^{-16}
$$

to traktuje się je jako 0, ponieważ są to błędy zaokrągleń.

## Kod

```python
def macierz_odwrotna_Gaussa_Jordana(macierz): # punkt b  # funkcja liczy macierz odwrotną metodą Gaussa-Jordana
    n = len(macierz)  # zapisujemy liczbę wierszy macierzy

    for wiersz in macierz:  # przechodzimy po każdym wierszu macierzy
        if len(wiersz) != n:  # sprawdzamy, czy liczba kolumn jest równa liczbie wierszy
            raise ValueError("Macierz musi być kwadratowa")  # zgłaszamy błąd, jeśli macierz nie jest kwadratowa

    # macierz rozszerzona [A | I]  # tworzymy macierz rozszerzoną, czyli po lewej A, a po prawej macierz jednostkową
    rozszerzona_macierz = []  # tworzymy pustą listę na macierz rozszerzoną

    for i in range(n):  # przechodzimy po kolejnych wierszach macierzy
        wiersz = []  # tworzymy pusty wiersz macierzy rozszerzonej

        # lewa strona: macierz A  # najpierw do wiersza wpisujemy elementy macierzy A
        for j in range(n):  # przechodzimy po kolumnach macierzy A
            wiersz.append(macierz[i][j])  # dodajemy element z macierzy A do aktualnego wiersza
            # wiersz.append(float(macierz[i][j]))  # alternatywna wersja, gdybyśmy chcieli od razu zamienić liczby na float
        
        # prawa strona: macierz jednostkowa I  # po prawej stronie dopisujemy macierz jednostkową
        for j in range(n):  # przechodzimy po kolumnach macierzy jednostkowej
            if i == j:  # sprawdzamy, czy element znajduje się na przekątnej głównej
                wiersz.append(1)  # na przekątnej głównej wpisujemy 1
            else:  # jeśli element nie jest na przekątnej głównej
                wiersz.append(0)  # poza przekątną wpisujemy 0

        rozszerzona_macierz.append(wiersz)  # dodajemy gotowy wiersz do macierzy rozszerzonej

    # algorytm Gaussa-Jordana  # zaczynamy przekształcanie macierzy rozszerzonej
    for i in range(n):  # przechodzimy po kolejnych elementach głównych na przekątnej
        # jeśli na przekątnej jest 0, zamień wiersze  # element główny nie może być zerem
        if rozszerzona_macierz[i][i] == 0:  # sprawdzamy, czy element główny jest równy 0
            znaleziono = False  # zakładamy, że jeszcze nie znaleziono wiersza do zamiany
            for k in range(i+1, n):  # szukamy niżej wiersza z niezerowym elementem w tej samej kolumnie
                if rozszerzona_macierz[k][i] != 0:  # sprawdzamy, czy w tym wierszu element w kolumnie i nie jest zerem
                    rozszerzona_macierz[i], rozszerzona_macierz[k] = rozszerzona_macierz[k], rozszerzona_macierz[i]  # zamieniamy miejscami dwa wiersze
                    znaleziono = True  # zapisujemy, że znaleziono odpowiedni wiersz
                    break  # przerywamy pętlę, bo zamiana została wykonana
            if not znaleziono:  # sprawdzamy, czy nie udało się znaleźć wiersza do zamiany
                raise ValueError("Macierz nie ma odwrotności")  # jeśli nie ma takiego wiersza, macierz nie ma odwrotności
            
        # dzielenie całego wiersza przez element główny  # normalizujemy wiersz, żeby element główny stał się równy 1
        element_glowny = rozszerzona_macierz[i][i]  # zapisujemy aktualny element główny
        for j in range(2 * n):  # przechodzimy po wszystkich kolumnach macierzy rozszerzonej
            rozszerzona_macierz[i][j] = rozszerzona_macierz[i][j] / element_glowny  # dzielimy każdy element wiersza przez element główny

        # zerowanie pozostałych elementów w tej kolumnie  # zerujemy elementy nad i pod elementem głównym
        for k in range(n):  # przechodzimy po wszystkich wierszach
            if k != i:  # nie zmieniamy aktualnego wiersza głównego
                wspolczynnik = rozszerzona_macierz[k][i]  # zapisujemy współczynnik potrzebny do wyzerowania elementu
                for j in range(2 * n):  # przechodzimy po wszystkich kolumnach macierzy rozszerzonej
                    rozszerzona_macierz[k][j] = rozszerzona_macierz[k][j] - wspolczynnik * rozszerzona_macierz[i][j]  # odejmujemy odpowiednią wielokrotność wiersza głównego

    odwrotna = []  # tworzymy pustą listę na macierz odwrotną
    for i in range(n):  # przechodzimy po wierszach macierzy rozszerzonej
        wiersz = []  # tworzymy pusty wiersz macierzy odwrotnej
        for j in range(n, 2 * n):  # przechodzimy po prawej części macierzy rozszerzonej
            wiersz.append(rozszerzona_macierz[i][j])  # dodajemy element z prawej strony, czyli element macierzy odwrotnej
        odwrotna.append(wiersz)  # dodajemy gotowy wiersz do macierzy odwrotnej

    return odwrotna  # zwracamy macierz odwrotną


def mnozenie_macierzy(macierz1, macierz2):  # funkcja mnoży dwie macierze
    ilosc_wierszy_macierz1 = len(macierz1)  # zapisujemy liczbę wierszy pierwszej macierzy
    ilosc_wierszy_macierz2 = len(macierz2)  # zapisujemy liczbę wierszy drugiej macierzy
    ilosc_kolumn_macierz1 = len(macierz1[0])  # zapisujemy liczbę kolumn pierwszej macierzy
    ilosc_kolumn_macierz2 = len(macierz2[0])  # zapisujemy liczbę kolumn drugiej macierzy

    if ilosc_kolumn_macierz1 != ilosc_wierszy_macierz2:  # sprawdzamy warunek mnożenia macierzy
        raise ValueError("Nie da się pomnożyć tych macierzy")  # zgłaszamy błąd, jeśli liczba kolumn pierwszej macierzy nie jest równa liczbie wierszy drugiej macierzy
    
    wynik = []  # tworzymy pustą listę na macierz wynikową
    for i in range(ilosc_wierszy_macierz1):  # przechodzimy po wierszach pierwszej macierzy
        wiersz = []  # tworzymy pusty wiersz macierzy wynikowej
        for j in range(ilosc_kolumn_macierz2):  # przechodzimy po kolumnach drugiej macierzy
            suma = 0  # ustawiamy początkową sumę na 0
            for k in range(ilosc_kolumn_macierz1):  # przechodzimy po elementach potrzebnych do obliczenia jednego elementu wyniku
                suma += macierz1[i][k] * macierz2[k][j]  # mnożymy odpowiednie elementy i dodajemy je do sumy
            wiersz.append(suma)  # dodajemy obliczony element do aktualnego wiersza
        wynik.append(wiersz)  # dodajemy gotowy wiersz do macierzy wynikowej

    return wynik  # zwracamy wynik mnożenia macierzy


macierz = [  # tworzymy macierz A
    [2, 4, 6],  # pierwszy wiersz macierzy
    [0, 2, -1],  # drugi wiersz macierzy
    [-3, 3, 3]  # trzeci wiersz macierzy
]  # koniec definicji macierzy

macierz_odwrotna = macierz_odwrotna_Gaussa_Jordana(macierz)  # liczymy macierz odwrotną do macierzy A

wynik1 = mnozenie_macierzy(macierz, macierz_odwrotna)  # mnożymy A przez A^-1
wynik2 = mnozenie_macierzy(macierz_odwrotna, macierz)  # mnożymy A^-1 przez A

print("Wynik mnożenia A * A^-1:")  # wypisujemy opis pierwszego wyniku
for wiersz in wynik1:  # przechodzimy po wierszach wyniku A * A^-1
    print(wiersz)  # wypisujemy aktualny wiersz wyniku

print("Wynik mnożenia A^-1 * A:")  # wypisujemy opis drugiego wyniku
for wiersz in wynik2:  # przechodzimy po wierszach wyniku A^-1 * A
    print(wiersz)  # wypisujemy aktualny wiersz wyniku
```

## Wynik

Oba iloczyny powinny być bardzo bliskie macierzy jednostkowej:

$$
I=
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

W praktyce może się pojawić na przykład:

$$
2.220446049250313e-16
$$

zamiast dokładnego zera. To jest normalne i wynika z ograniczonej dokładności obliczeń zmiennoprzecinkowych.

# Wniosek

Wszystkie zadania zostały wykonane poprawnie.

* W zadaniu 1 obliczono wyznacznik macierzy metodą rozwinięcia Laplace’a.
* W zadaniu 2 obliczono transpozycję macierzy.
* W zadaniu 3 wyznaczono macierz odwrotną dwiema metodami: Laplace’a oraz Gaussa-Jordana.
* W zadaniu 4 wykonano mnożenie dwóch macierzy.
* W zadaniu 5 sprawdzono poprawność macierzy odwrotnej przez obliczenie iloczynów $A \cdot A^{-1}$ oraz $A^{-1} \cdot A$.

Otrzymane wyniki są zgodne z teorią, a ewentualne bardzo małe różnice wynikają z błędów zaokrągleń numerycznych.

---

# Lab 5

# Zadanie 1

Korzystając z funkcji napisanych na poprzednich zajęciach rozwiąż układy równań liniowych.

## Zadanie 1a

![alt text](zdjecia/1a.png)

## Jak to rozwiązać metodą z poprzednich zajęć?

Skoro masz już funkcję liczącą macierz odwrotną, to korzystasz ze wzoru:

$x = A^{-1}b$

Czyli:

1. liczysz macierz odwrotną $A^{-1}$,
2. mnożysz ją przez wektor $b$,
3. dostajesz rozwiązanie.

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz macierz `A` i wektor `b`.

### Krok 2

Zamieniasz `b` na macierz kolumnową:

$
b =
\begin{bmatrix}
-9 \\
61 \\
-9
\end{bmatrix}
$

bo funkcja mnożenia działa na macierzach.

### Krok 3

Liczysz:

$
A^{-1} \cdot b
$

### Krok 4

Otrzymujesz wynik w postaci macierzy kolumnowej, więc zamieniasz go na zwykły wektor.

## Kod

```python
import time

def zmierz_czas(funkcja, A, b): 
    start = time.perf_counter()
    wynik = funkcja(A, b)
    koniec = time.perf_counter()
    return wynik, koniec - start

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

    for i in range(n):
        if rozszerzona_macierz[i][i] == 0:
            znaleziono = False
            for k in range(i+1, n):
                if rozszerzona_macierz[k][i] != 0:
                    rozszerzona_macierz[i], rozszerzona_macierz[k] = rozszerzona_macierz[k], rozszerzona_macierz[i]
                    znaleziono = True
                    break
            if not znaleziono:
                raise ValueError("Macierz nie ma odwrotności")
            
        element_glowny = rozszerzona_macierz[i][i]
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

def rozwiarz_uklad_rownan(macierz_A, wektor_b):
    b_macierz = [[b] for b in wektor_b]

    A_odwrotna = macierz_odwrotna_Gaussa_Jordana(macierz_A)

    wynik = mnozenie_macierzy(A_odwrotna, b_macierz)

    return wynik

A = [
    [1, 2, 1],
    [3, -7, 2],
    [2, 4, 5]
]

b = [-9, 61, -9]

wynik, czas = zmierz_czas(rozwiarz_uklad_rownan, A, b)

print("Rozwiązanie układu równań a):")
print("x =", wynik[0][0])
print("y =", wynik[1][0])
print("z =", wynik[2][0])
print("Czas: ", czas)
```

## Wynik

$
x = 2.0,\qquad y = -7.0,\qquad z = 3.0
$

$
czas = 1.4600111171603203e-05 = 1.4600111171603203 * 10^{-5} = 0.0000146 s = 14.6 mikrosekundy
$

---

## Zadanie 1b

![alt text](zdjecia/1b.png)

Rozwiązać układ:

$
Ax = b
$

gdzie:

* $(A \in \mathbb{R}^{n \times n})$,
* $(b \in \mathbb{R}^{n \times 1})$,
* $(n \in \{8, 10\})$,

a macierz ma postać trójdiagonalną:

* na przekątnej są (11),
* nad i pod przekątną są (-5),
* reszta elementów to (0).

Wektor:

$
b =
\begin{bmatrix}
11 \\
0 \\
0 \\
\vdots \\
0
\end{bmatrix}
$

## Jak rozumieć tę macierz?

Dla (n=8) macierz wygląda tak:

$
A =
\begin{bmatrix}
11 & -5 & 0 & 0 & 0 & 0 & 0 & 0 \\
-5 & 11 & -5 & 0 & 0 & 0 & 0 & 0 \\
0 & -5 & 11 & -5 & 0 & 0 & 0 & 0 \\
0 & 0 & -5 & 11 & -5 & 0 & 0 & 0 \\
0 & 0 & 0 & -5 & 11 & -5 & 0 & 0 \\
0 & 0 & 0 & 0 & -5 & 11 & -5 & 0 \\
0 & 0 & 0 & 0 & 0 & -5 & 11 & -5 \\
0 & 0 & 0 & 0 & 0 & 0 & -5 & 11
\end{bmatrix}
$

To znaczy:

* główna przekątna ma same `11`,
* sąsiednie przekątne mają `-5`.

## Jak zrobić implementację?

Najpierw trzeba umieć wygenerować taką macierz automatycznie.

## Kod tworzący macierz i wektor

```python
def zeros(n,m):
    macierz = []

    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0)
        macierz.append(wiersz)

    return macierz

def tworzenie_macierzy(n):
    A = zeros(n, n)
    b = [11] + [0] * (n - 1)

    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 11
            elif abs(i - j) == 1:
                A[i][j] = -5
    
    return A, b
```

## Jak rozumieć schemat implementacji?

### Krok 1

Tworzysz pustą macierz `n x n`.

### Krok 2

Jeśli jesteś na przekątnej (`i == j`), wpisujesz `11`.

### Krok 3

Jeśli jesteś tuż obok przekątnej (`abs(i-j) == 1`), wpisujesz `-5`.

### Krok 4

Wektor `b` ma `11` na pierwszej pozycji i same zera dalej.

## Rozwiązanie

Potem rozwiązujesz dokładnie tak samo jak w 1a:

$
x = A^{-1}*b
$

## Kod

```python
n_8_A, n_8_b = tworzenie_macierzy(8)
n_10_A, n_10_b = tworzenie_macierzy(10)

wynik, czas = zmierz_czas(rozwiarz_uklad_rownan, n_8_A, n_8_b)
print("Rozwiązanie układu równań b) n=8:")
for i in range(len(wynik)):
    print(wynik[i])
print("Czas: ", czas)

wynik, czas = zmierz_czas(rozwiarz_uklad_rownan, n_10_A, n_10_b)
print("Rozwiązanie układu równań b) n=10:")
for i in range(len(wynik)):
    print(wynik[i])
print("Czas: ", czas)
```

## Wynik

$
\begin{array}{}
Rozwiązanie \space układu \space równań \space b) \space n=8: \\
[1.4111459559532078] \\
[0.9045211030970575] \\
[0.5788004708603187] \\
[0.36883993279564314] \\
[0.23264738129009646] \\
[0.1429843060425689] \\
[0.0819180920035551] \\
[0.037235496365252314] \\
Czas:  6.560003384947777e-05 \\
Rozwiązanie \space układu \space równań \space b) \space n=10: \\
[1.4117167939551722] \\
[0.905776946701379] \\
[0.5809924887878618] \\
[0.3724065286319164] \\
[0.23830187420235457] \\
[0.15185759461326348] \\
[0.09578483394682505] \\
[0.05886904006975162] \\
[0.03372705420662853] \\
[0.015330479184831151] \\
Czas:  0.00011690007522702217
\end{array}
$

---

## Zadanie 1c

Rozwiązać układ równań, którego współczynniki tworzą macierz gęstą $(10 \times 10)$.

## Co to znaczy macierz gęsta?

Macierz gęsta to taka, w której dużo elementów jest różnych od zera.

To przeciwieństwo macierzy rzadkiej lub trójdiagonalnej.

## Jak to zrobić sensownie?

Najlepiej zbudować macierz, dla której znasz rozwiązanie.
Wtedy łatwo sprawdzić, czy program działa dobrze.

### Pomysł

1. wybierasz macierz gęstą (A),
2. wybierasz znany wektor (x),
3. liczysz:

$
b = Ax
$

4. potem rozwiązujesz układ (Ax = b),
5. i sprawdzasz, czy odzyskałaś swoje (x).

## Kod

```python
def tworzenie_macierzy_gestej(n, m):
    A = zeros(n, m)

    for i in range(n):
        for j in range(m):
            if i == j:
                A[i][j] = 20.0
            else:
                A[i][j] = float(i + j + 1)

    x_prawdziwe = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

    x_macierz = [[x] for x in x_prawdziwe]
    b_macierz = mnozenie_macierzy(A, x_macierz)

    b = []
    for i in range(len(b_macierz)):
        b.append(b_macierz[i][0])

    return A, b, x_prawdziwe

macierz, wektor, x = tworzenie_macierzy_gestej(10, 10)

wynik, czas = zmierz_czas(rozwiarz_uklad_rownan, macierz, wektor)

print("Rozwiązanie układu równań c):")
for i in range(len(wynik)):
    print(wynik[i])
print("Czas: ", czas)
```

## Jak rozumieć ten schemat?

Nie zgadujesz `b`.
Tworzysz takie `b`, żeby mieć pewność, że rozwiązanie jest znane.

To bardzo wygodne przy testowaniu metod numerycznych.

## Wynik

$
\begin{array}{}
[1.0] \\
[1.9999999999999716] \\
[3.0] \\
[4.0] \\
[5.000000000000057] \\
[5.999999999999972]\\
[7.0]\\
[8.000000000000028]\\
[8.999999999999972]\\
[10.0]\\
Czas:  9.989994578063488e-05
\end{array}
$

> Otrzymane rozwiązanie jest bardzo bliskie wektorowi x = [1,2,3,4,5,6,7,8,9,10], co potwierdza poprawność działania programu. Niewielkie różnice wynikają z błędów zaokrągleń.

---

# Zadanie 2

Napisz funkcję znajdującą rozkład macierzy na iloczyn macierzy trójkątnych

$
A = LU
$

Powyższą funkcję wykorzystaj w celu znalezienia rozwiązania układu równań
liniowych. Przetestuj działanie dla przykładów z zadania 1. Zmierz czas potrzebny na
znalezienie każdego z rozwiązań. Porównaj otrzymane wyniki.

## Co to jest rozkład LU?

Macierz (A) rozkłada się na:

* (L) — macierz dolnotrójkątną,
* (U) — macierz górnotrójkątną.

Czyli:

$
A = LU
$

## Po co to robić?

Bo zamiast rozwiązywać od razu:

$
Ax = b
$

rozbijasz to na dwa prostsze układy:

$
Ly = b
$

a potem:

$
Ux = y
$

## Jak rozumieć schemat implementacji?

### Etap 1 — wyznaczenie `L` i `U`

Budujesz dwie macierze:

* `L` ma jedynki na przekątnej,
* `U` powstaje z odpowiednich wzorów.

### Etap 2 — podstawianie w przód

Rozwiązujesz $Ly=b$.

Ponieważ `L` jest dolnotrójkątna, liczysz:

* najpierw $y_1$,
* potem $y_2$,
* itd.

### Etap 3 — podstawianie w tył

Rozwiązujesz $Ux=y$.

Ponieważ `U` jest górnotrójkątna, liczysz:

* najpierw ostatnią niewiadomą,
* potem poprzednią,
* itd.

## Kod

```python
import time

def zmierz_czas(funkcja, A, b):
    start = time.perf_counter()
    wynik = funkcja(A, b)
    koniec = time.perf_counter()
    return wynik, koniec - start

def zeros(n, m):
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0.0)
        macierz.append(wiersz)
    return macierz


def rozklad_LU_Doolittle(A):
    n = len(A)

    for wiersz in A:
        if len(wiersz) != n:
            raise ValueError("Macierz musi być kwadratowa")

    L = zeros(n, n)
    U = zeros(n, n)

    # na przekątnej L są jedynki
    for i in range(n):
        L[i][i] = 1.0

    for i in range(n):
        # liczenie elementów U
        for j in range(i, n):
            suma = 0.0
            for k in range(i):
                suma += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - suma

        # liczenie elementów L
        for j in range(i + 1, n):
            suma = 0.0
            for k in range(i):
                suma += L[j][k] * U[k][i]

            if U[i][i] == 0:
                raise ValueError("Nie można wykonać rozkładu LU metodą Doolittle’a")

            L[j][i] = (A[j][i] - suma) / U[i][i]

    return L, U
```

## Rozwiązywanie układu przez LU

```python
def podstawianie_w_przod(L, b):
    n = len(L)
    y = [0.0] * n

    for i in range(n):
        suma = 0.0
        for j in range(i):
            suma += L[i][j] * y[j]
        y[i] = b[i] - suma

    return y


def podstawianie_w_tyl(U, y):
    n = len(U)
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += U[i][j] * x[j]

        if U[i][i] == 0:
            raise ValueError("Dzielenie przez zero w podstawianiu w tył")

        x[i] = (y[i] - suma) / U[i][i]

    return x


def rozwiaz_uklad_Doolittle(A, b):
    L, U = rozklad_LU_Doolittle(A)
    y = podstawianie_w_przod(L, b)
    x = podstawianie_w_tyl(U, y)
    return x
```

### punkt a

```python
A = [
    [1.0, 2.0, 1.0],
    [3.0, -7.0, 2.0],
    [2.0, 4.0, 5.0]
]

b = [-9.0, 61.0, -9.0]

wynik, czas = zmierz_czas(rozwiaz_uklad_Doolittle, A, b)

print("Rozwiązanie metodą Doolittle’a dla a):")
for i in range(len(wynik)):
    print("x" + str(i + 1) + " =", wynik[i])
print("Czas: ", czas)
```

### punkt b

```python
def wypisz_wektor(wektor):
    for i in range(len(wektor)):
        print("x" + str(i + 1) + " =", wektor[i])

def tworzenie_macierzy_b(n):
    A = zeros(n, n)
    b = [11.0] + [0.0] * (n - 1)

    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 11.0
            elif abs(i - j) == 1:
                A[i][j] = -5.0
            else:
                A[i][j] = 0.0

    return A, b

#punkt b, n = 8

A8, b8 = tworzenie_macierzy_b(8)

wynik8, czas8 = zmierz_czas(rozwiaz_uklad_Doolittle, A8, b8)

print("\nRozwiązanie metodą Doolittle’a dla b), n=8:")
wypisz_wektor(wynik8)
print("Czas:", czas8, "s")

#punkt b, n = 10

A10, b10 = tworzenie_macierzy_b(10)

wynik10, czas10 = zmierz_czas(rozwiaz_uklad_Doolittle, A10, b10)

print("\nRozwiązanie metodą Doolittle’a dla b), n=10:")
wypisz_wektor(wynik10)
print("Czas:", czas10, "s")
```

### punkt c

```python
def wektor_na_macierz_kolumnowa(wektor):
    wynik = []
    for x in wektor:
        wynik.append([float(x)])
    return wynik


def macierz_kolumnowa_na_wektor(macierz):
    wynik = []
    for i in range(len(macierz)):
        wynik.append(macierz[i][0])
    return wynik

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
            suma = 0.0
            for k in range(ilosc_kolumn_macierz1):
                suma += macierz1[i][k] * macierz2[k][j]
            wiersz.append(suma)
        wynik.append(wiersz)

    return wynik

def tworzenie_macierzy_gestej(n, m):
    A = zeros(n, m)

    for i in range(n):
        for j in range(m):
            if i == j:
                A[i][j] = 20.0
            else:
                A[i][j] = float(i + j + 1)

    x_prawdziwe = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

    x_macierz = wektor_na_macierz_kolumnowa(x_prawdziwe)
    b_macierz = mnozenie_macierzy(A, x_macierz)
    b = macierz_kolumnowa_na_wektor(b_macierz)

    return A, b, x_prawdziwe

Ag, bg, x_prawdziwe = tworzenie_macierzy_gestej(10, 10)

wynikg, czasg = zmierz_czas(rozwiaz_uklad_Doolittle, Ag, bg)

print("\nRozwiązanie metodą Doolittle’a dla c):")
wypisz_wektor(wynikg)
print("Czas:", czasg, "s")
print("Oczekiwane rozwiązanie:", x_prawdziwe)
```

## Wyniki

```
Rozwiązanie metodą Doolittle’a dla a):
x1 = 2.0
x2 = -7.0
x3 = 3.0
Czas:  1.3699987903237343e-05

Rozwiązanie metodą Doolittle’a dla b), n=8:
x1 = 1.411145955953208
x2 = 0.9045211030970576
x3 = 0.5788004708603186
x4 = 0.36883993279564314
x5 = 0.23264738129009638
x6 = 0.14298430604256884
x7 = 0.08191809200355507
x8 = 0.03723549636525231
Czas: 2.500019036233425e-05 s

Rozwiązanie metodą Doolittle’a dla b), n=10:
x1 = 1.4117167939551722
x2 = 0.9057769467013792
x3 = 0.5809924887878617
x4 = 0.3724065286319165
x5 = 0.23830187420235452
x6 = 0.1518575946132634
x7 = 0.09578483394682502
x8 = 0.05886904006975161
x9 = 0.033727054206628526
x10 = 0.015330479184831148
Czas: 3.5800039768218994e-05 s

Rozwiązanie metodą Doolittle’a dla c):
x1 = 1.0000000000000455
x2 = 2.000000000000047
x3 = 3.0000000000000417
x4 = 4.0000000000000435
x5 = 5.000000000000042
x6 = 6.000000000000046
x7 = 7.000000000000037
x8 = 8.00000000000005
x9 = 8.999999999999991
x10 = 9.999999999999762
Czas: 3.4300144761800766e-05 s
Oczekiwane rozwiązanie: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
Oczekiwane rozwiązanie: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
Oczekiwane rozwiązanie: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
Oczekiwane rozwiązanie: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
Oczekiwane rozwiązanie: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
Oczekiwane rozwiązanie: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
```

---

# Zadanie 3

Napisz funkcję znajdującą rozkład Choleskiego dla macierzy:

* kwadratowej,
* symetrycznej,
* dodatnio określonej.

Powyższą funkcję wykorzystaj w celu znalezienia rozwiązania układu równań liniowych. Przetestuj działanie dla przykładu b) z zadania 1.
Zmierz czas potrzebny na znalezienie każdego z rozwiązań. Porównaj otrzymane wyniki.

## Co to jest rozkład Choleskiego?

Dla odpowiedniej macierzy:

$
A = LL^T
$

gdzie:

* $L$ jest macierzą dolnotrójkątną,
* $L^T$ jest jej transpozycją.

## Kiedy można go używać?

Tylko gdy macierz jest:

* symetryczna,
* dodatnio określona.

Macierz z zadania 1b spełnia ten warunek.

## Jak rozumieć schemat implementacji?

### Krok 1

Liczysz kolejne elementy macierzy `L`.

### Krok 2

Na przekątnej liczysz pierwiastek z odpowiedniej wartości.

### Krok 3

Poza przekątną liczysz elementy ze wzoru zależnego od już policzonych elementów.

### Krok 4

Rozwiązujesz:
$
Ly=b
$

a potem:
$
L^Tx=y
$

## Kod

```python
import time

def zeros(n, m):
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0.0)
        macierz.append(wiersz)
    return macierz


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


def podstawianie_w_przod(L, b):
    n = len(L)
    y = [0.0] * n

    for i in range(n):
        suma = 0.0
        for j in range(i):
            suma += L[i][j] * y[j]
        y[i] = (b[i] - suma) / L[i][i]

    return y


def podstawianie_w_tyl(U, y):
    n = len(U)
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += U[i][j] * x[j]
        x[i] = (y[i] - suma) / U[i][i]

    return x


def rozklad_Choleskiego(A):
    n = len(A)

    for wiersz in A:
        if len(wiersz) != n:
            raise ValueError("Macierz musi być kwadratowa")

    L = zeros(n, n)

    for i in range(n):
        for j in range(i + 1):
            suma = 0.0
            for k in range(j):
                suma += L[i][k] * L[j][k]

            if i == j:
                wartosc = A[i][i] - suma
                if wartosc <= 0:
                    raise ValueError("Macierz nie jest dodatnio określona")
                L[i][j] = wartosc ** 0.5
            else:
                L[i][j] = (A[i][j] - suma) / L[j][j]

    return L


def rozwiaz_uklad_Choleski(A, b):
    L = rozklad_Choleskiego(A)
    Lt = transpozycja(L)

    y = podstawianie_w_przod(L, b)
    x = podstawianie_w_tyl(Lt, y)

    return x


def wypisz_wektor(wektor):
    for i in range(len(wektor)):
        print("x" + str(i + 1) + " =", wektor[i])


def tworzenie_macierzy_b(n):
    A = zeros(n, n)
    b = [11.0] + [0.0] * (n - 1)

    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 11.0
            elif abs(i - j) == 1:
                A[i][j] = -5.0
            else:
                A[i][j] = 0.0

    return A, b


def zmierz_czas(funkcja, A, b):
    start = time.perf_counter()
    wynik = funkcja(A, b)
    koniec = time.perf_counter()
    return wynik, koniec - start


# przykład b) z zadania 1, n = 8
A8, b8 = tworzenie_macierzy_b(8)
wynik8, czas8 = zmierz_czas(rozwiaz_uklad_Choleski, A8, b8)

print("Rozwiązanie metodą Cholesky’ego dla n = 8:")
wypisz_wektor(wynik8)
print("Czas:", czas8)


# przykład b) z zadania 1, n = 10
A10, b10 = tworzenie_macierzy_b(10)
wynik10, czas10 = zmierz_czas(rozwiaz_uklad_Choleski, A10, b10)

print("\nRozwiązanie metodą Cholesky’ego dla n = 10:")
wypisz_wektor(wynik10)
print("Czas:", czas10)
```

## Wyniki

```
Rozwiązanie metodą Cholesky’ego dla n = 8:
x1 = 1.4111459559532078
x2 = 0.9045211030970575
x3 = 0.5788004708603184
x4 = 0.36883993279564303
x5 = 0.2326473812900963
x6 = 0.1429843060425688
x7 = 0.08191809200355503
x8 = 0.03723549636525228
Czas: 2.5999965146183968e-05

Rozwiązanie metodą Cholesky’ego dla n = 10:
x1 = 1.4117167939551722
x2 = 0.905776946701379
x3 = 0.5809924887878615
x4 = 0.37240652863191626
x5 = 0.23830187420235438
x6 = 0.15185759461326334
x7 = 0.09578483394682495
x8 = 0.05886904006975156
x9 = 0.0337270542066285
x10 = 0.015330479184831134
Czas: 2.8199981898069382e-05
```

---

# Zadanie 4

Napisz funkcję rozwiązującą układy równań za pomocą eliminacji Gaussa. Przetestuj działanie dla przykładów z zadania 1. Zmierz czas potrzebny na znalezienie każdego z rozwiązań. Porównaj otrzymane wyniki.

## Na czym polega eliminacja Gaussa?

Macierz sprowadzasz do postaci trójkątnej górnej przez zerowanie elementów pod przekątną.

Potem rozwiązujesz układ podstawianiem w tył.

## Jak rozumieć schemat implementacji?

### Etap 1 — eliminacja w przód

Dla każdej kolumny:

* wybierasz wiersz główny,
* zerujesz elementy pod nim.

### Etap 2 — podstawianie w tył

Gdy macierz jest już górnotrójkątna, liczysz niewiadome od końca.

## Funkcja do Gaussa

```python
def rozwiaz_uklad_Gaussa(A, b):
    n = len(A)

    # kopia macierzy i wektora
    M = kopiuj_macierz(A)
    bb = []
    for x in b:
        bb.append(float(x))

    # eliminacja w przód
    for i in range(n):
        # jeśli pivot jest zerem, trzeba zamienić wiersze
        if M[i][i] == 0:
            znaleziono = False
            for k in range(i + 1, n):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    bb[i], bb[k] = bb[k], bb[i]
                    znaleziono = True
                    break
            if not znaleziono:
                raise ValueError("Układ nie ma jednoznacznego rozwiązania")

        # zerowanie elementów poniżej przekątnej
        for k in range(i + 1, n):
            wspolczynnik = M[k][i] / M[i][i]

            for j in range(i, n):
                M[k][j] = M[k][j] - wspolczynnik * M[i][j]

            bb[k] = bb[k] - wspolczynnik * bb[i]

    # podstawianie w tył
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += M[i][j] * x[j]

        x[i] = (bb[i] - suma) / M[i][i]

    return x
```

## Kod

```python
import time

def zeros(n, m):
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0.0)
        macierz.append(wiersz)
    return macierz


def kopiuj_macierz(macierz):
    wynik = []
    for wiersz in macierz:
        nowy_wiersz = []
        for element in wiersz:
            nowy_wiersz.append(float(element))
        wynik.append(nowy_wiersz)
    return wynik


def wypisz_wektor(wektor):
    for i in range(len(wektor)):
        print("x" + str(i + 1) + " =", wektor[i])


def rozwiaz_uklad_Gaussa(A, b):
    n = len(A)

    # kopia macierzy i wektora
    M = kopiuj_macierz(A)
    bb = []
    for x in b:
        bb.append(float(x))

    # eliminacja w przód
    for i in range(n):
        # jeśli pivot jest zerem, trzeba zamienić wiersze
        if M[i][i] == 0:
            znaleziono = False
            for k in range(i + 1, n):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    bb[i], bb[k] = bb[k], bb[i]
                    znaleziono = True
                    break
            if not znaleziono:
                raise ValueError("Układ nie ma jednoznacznego rozwiązania")

        # zerowanie elementów poniżej przekątnej
        for k in range(i + 1, n):
            wspolczynnik = M[k][i] / M[i][i]

            for j in range(i, n):
                M[k][j] = M[k][j] - wspolczynnik * M[i][j]

            bb[k] = bb[k] - wspolczynnik * bb[i]

    # podstawianie w tył
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += M[i][j] * x[j]

        x[i] = (bb[i] - suma) / M[i][i]

    return x

#a)

A1 = [
    [1.0, 2.0, 1.0],
    [3.0, -7.0, 2.0],
    [2.0, 4.0, 5.0]
]

b1 = [-9.0, 61.0, -9.0]

#b)

def tworzenie_macierzy_b(n):
    A = zeros(n, n)
    b = [11.0] + [0.0] * (n - 1)

    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 11.0
            elif abs(i - j) == 1:
                A[i][j] = -5.0
            else:
                A[i][j] = 0.0

    return A, b

#c)

def mnozenie_macierzy(macierz1, macierz2):
    liczba_wierszy_1 = len(macierz1)
    liczba_wierszy_2 = len(macierz2)
    liczba_kolumn_1 = len(macierz1[0])
    liczba_kolumn_2 = len(macierz2[0])

    if liczba_kolumn_1 != liczba_wierszy_2:
        raise ValueError("Nie da się pomnożyć tych macierzy")

    wynik = []
    for i in range(liczba_wierszy_1):
        wiersz = []
        for j in range(liczba_kolumn_2):
            suma = 0.0
            for k in range(liczba_kolumn_1):
                suma += macierz1[i][k] * macierz2[k][j]
            wiersz.append(suma)
        wynik.append(wiersz)

    return wynik


def wektor_na_macierz_kolumnowa(wektor):
    wynik = []
    for x in wektor:
        wynik.append([float(x)])
    return wynik


def macierz_kolumnowa_na_wektor(macierz):
    wynik = []
    for i in range(len(macierz)):
        wynik.append(macierz[i][0])
    return wynik


def tworzenie_macierzy_gestej_10():
    A = zeros(10, 10)

    for i in range(10):
        for j in range(10):
            if i == j:
                A[i][j] = 20.0
            else:
                A[i][j] = float(i + j + 1)

    x_prawdziwe = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

    x_kolumna = wektor_na_macierz_kolumnowa(x_prawdziwe)
    b_kolumna = mnozenie_macierzy(A, x_kolumna)
    b = macierz_kolumnowa_na_wektor(b_kolumna)

    return A, b, x_prawdziwe

#czasy

def zmierz_czas(funkcja, A, b):
    start = time.perf_counter()
    wynik = funkcja(A, b)
    koniec = time.perf_counter()
    return wynik, koniec - start

print("========== ZADANIE 4 – eliminacja Gaussa ==========")

# przykład a)
A1 = [
    [1.0, 2.0, 1.0],
    [3.0, -7.0, 2.0],
    [2.0, 4.0, 5.0]
]
b1 = [-9.0, 61.0, -9.0]

wynik_Gauss_1, czas_Gauss_1 = zmierz_czas(rozwiaz_uklad_Gaussa, A1, b1)
print("Gauss, przykład a):")
wypisz_wektor(wynik_Gauss_1)
print("Czas:", czas_Gauss_1)

# przykład b), n = 8
A8, b8 = tworzenie_macierzy_b(8)
wynik_Gauss_8, czas_Gauss_8 = zmierz_czas(rozwiaz_uklad_Gaussa, A8, b8)
print("\nGauss, przykład b), n=8:")
wypisz_wektor(wynik_Gauss_8)
print("Czas:", czas_Gauss_8)

# przykład b), n = 10
A10, b10 = tworzenie_macierzy_b(10)
wynik_Gauss_10, czas_Gauss_10 = zmierz_czas(rozwiaz_uklad_Gaussa, A10, b10)
print("\nGauss, przykład b), n=10:")
wypisz_wektor(wynik_Gauss_10)
print("Czas:", czas_Gauss_10)

# przykład c)
A_gesta, b_gesta, x_prawdziwe = tworzenie_macierzy_gestej_10()
wynik_Gauss_gesta, czas_Gauss_gesta = zmierz_czas(rozwiaz_uklad_Gaussa, A_gesta, b_gesta)
print("\nGauss, przykład c):")
wypisz_wektor(wynik_Gauss_gesta)
print("Czas:", czas_Gauss_gesta)
print("Oczekiwane rozwiązanie:", x_prawdziwe)
```

## Wyniki

```
========== ZADANIE 4 – eliminacja Gaussa ==========
Gauss, przykład a):
x1 = 2.0
x2 = -7.0
x3 = 3.0
Czas: 1.2800097465515137e-05

Gauss, przykład b), n=8:
x1 = 1.411145955953208
x2 = 0.9045211030970576
x3 = 0.5788004708603186
x4 = 0.36883993279564314
x5 = 0.23264738129009638
x6 = 0.14298430604256884
x7 = 0.08191809200355507
x8 = 0.03723549636525231
Czas: 1.8999911844730377e-05

Gauss, przykład b), n=10:
x1 = 1.4117167939551722
x2 = 0.9057769467013792
x3 = 0.5809924887878617
x4 = 0.3724065286319165
x5 = 0.23830187420235452
x6 = 0.1518575946132634
x7 = 0.09578483394682502
x8 = 0.05886904006975161
x9 = 0.033727054206628526
x10 = 0.015330479184831148
Czas: 3.0899886041879654e-05

Gauss, przykład c):
x1 = 1.0000000000000058
x2 = 2.000000000000004
x3 = 2.9999999999999996
x4 = 4.000000000000014
x5 = 5.000000000000001
x6 = 5.999999999999999
x7 = 7.000000000000005
x8 = 7.999999999999986
x9 = 9.000000000000007
x10 = 9.999999999999988
Czas: 2.7399975806474686e-05
Oczekiwane rozwiązanie: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
```

---

# Mierzenie czasu

W każdym zadaniu masz porównać czasy.

## Jak rozumieć schemat?

1. zapisujesz czas startu,
2. uruchamiasz metodę,
3. zapisujesz czas końca,
4. odejmujesz.

## Kod

```python
import time

def zmierz_czas(funkcja, A, b):
    start = time.perf_counter()
    wynik = funkcja(A, b)
    koniec = time.perf_counter()
    return wynik, koniec - start
```

---

# Krótki wniosek do wszystkich zadań

Możesz napisać tak:

```markdown
## Wnioski

Wszystkie zastosowane metody prowadzą do tego samego rozwiązania układów równań liniowych, jednak różnią się kosztami obliczeniowymi i warunkami stosowalności.

- Metoda oparta na macierzy odwrotnej jest poprawna, ale najmniej opłacalna obliczeniowo.
- Rozkład LU upraszcza rozwiązanie układu do dwóch prostszych układów trójkątnych.
- Rozkład Choleskiego jest bardzo efektywny, ale można go stosować tylko do macierzy symetrycznych i dodatnio określonych.
- Eliminacja Gaussa jest metodą uniwersalną i jedną z podstawowych metod rozwiązywania układów liniowych.
- Porównanie czasów wykonania pokazuje, które metody są bardziej praktyczne dla większych macierzy.
```

---

# Lab 6

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

![alt text](obrazy/1.png)

## Warunki zatrzymania

### a) Liczba iteracji

Program kończy działanie po zadanej liczbie kroków.

### b) Iloraz normy różnicy kolejnych przybliżeń i normy bieżącego przybliżenia

Sprawdzasz, czy:

$$
\frac{\|x^{(k)} - x^{(k-1)}\|}{\|x^{(k)}\|} \le \varepsilon
$$

W programie używana jest norma maksimum.  
Jeżeli warunek jest spełniony, uznajesz, że kolejne przybliżenia zmieniają się już bardzo nieznacznie.

### c) Błąd uzyskanego przybliżenia

Jeżeli znasz dokładne rozwiązanie $x^*$, możesz sprawdzać:

$$
\|x^{(k)} - x^*\| < \varepsilon
$$

## Kod

```python
def norma_max(wektor):  # funkcja oblicza normę maksimum wektora
    maksimum = abs(wektor[0])  # jako początkowe maksimum przyjmujemy moduł pierwszego elementu
    for i in range(1, len(wektor)):  # przechodzimy po kolejnych elementach wektora
        if abs(wektor[i]) > maksimum:  # sprawdzamy, czy moduł bieżącego elementu jest większy od dotychczasowego maksimum
            maksimum = abs(wektor[i])  # jeśli tak, aktualizujemy maksimum
    return maksimum  # zwracamy największy moduł elementu wektora


def odejmij_wektory(wektor1, wektor2):  # funkcja odejmuje od siebie dwa wektory o tej samej długości
    wynik = []  # tworzymy pustą listę na wynik odejmowania
    for i in range(len(wektor1)):  # przechodzimy po wszystkich indeksach wektora
        wynik.append(wektor1[i] - wektor2[i])  # dodajemy do wyniku różnicę odpowiednich elementów
    return wynik  # zwracamy wektor różnicy


def wypisz_wektor(wektor, nazwa="x"):  # funkcja wypisuje kolejne współrzędne wektora
    for i in range(len(wektor)):  # przechodzimy po wszystkich elementach wektora
        print(f"{nazwa}{i+1} = {wektor[i]}")  # wypisujemy element w formacie x1, x2, x3 itd.


def jacobi(A, b, x0, max_iter=100, epsilon=1e-3, warunek_stopu="iteracje", rozwiazanie_dokladne=None):  # funkcja realizuje metodę Jacobiego
    n = len(A)  # zapisujemy liczbę równań i niewiadomych
    x_stare = x0[:]  # kopiujemy przybliżenie początkowe do wektora poprzedniej iteracji

    for i in range(n):  # sprawdzamy wszystkie elementy na przekątnej macierzy
        if A[i][i] == 0:  # jeśli na przekątnej pojawi się zero
            raise ValueError("Na przekątnej macierzy nie może być zera")  # przerywamy działanie programu z komunikatem o błędzie

    for krok in range(1, max_iter + 1):  # wykonujemy kolejne iteracje od 1 do maksymalnej liczby iteracji
        x_nowe = [0.0] * n  # tworzymy nowy wektor przybliżenia wypełniony zerami

        for i in range(n):  # przechodzimy po wszystkich równaniach
            suma = 0.0  # zerujemy sumę składników spoza przekątnej dla i-tego równania
            for j in range(n):  # przechodzimy po wszystkich kolumnach macierzy
                if j != i:  # pomijamy element z przekątnej
                    suma += A[i][j] * x_stare[j]  # dodajemy iloczyn współczynnika macierzy i starego przybliżenia

            x_nowe[i] = (b[i] - suma) / A[i][i]  # liczymy nową wartość i-tej niewiadomej ze wzoru Jacobiego

        if warunek_stopu == "iteracje":  # sprawdzamy, czy wybrano warunek stopu oparty na liczbie iteracji
            if krok == max_iter:  # jeśli osiągnięto zadaną liczbę iteracji
                return x_nowe, krok  # zwracamy aktualne przybliżenie i liczbę wykonanych iteracji

        elif warunek_stopu == "roznica":  # sprawdzamy, czy wybrano warunek stopu ze slajdu
            roznica = odejmij_wektory(x_nowe, x_stare)  # obliczamy różnicę kolejnych przybliżeń
            norma_roznicy = norma_max(roznica)  # liczymy normę maksimum tej różnicy
            norma_biezaca = norma_max(x_nowe)  # liczymy normę maksimum bieżącego przybliżenia

            if norma_biezaca == 0:  # sprawdzamy przypadek szczególny, gdy norma bieżącego wektora jest równa zero
                if norma_roznicy <= epsilon:  # jeśli sama norma różnicy spełnia warunek
                    return x_nowe, krok  # zwracamy wynik i numer iteracji
            else:  # w zwykłym przypadku, gdy norma bieżącego przybliżenia nie jest zerowa
                if (norma_roznicy / norma_biezaca) <= epsilon:  # sprawdzamy warunek stopu w postaci ilorazu norm
                    return x_nowe, krok  # zwracamy wynik i numer iteracji

        elif warunek_stopu == "blad":  # sprawdzamy, czy wybrano warunek stopu oparty na błędzie względem rozwiązania dokładnego
            if rozwiazanie_dokladne is None:  # jeśli nie podano rozwiązania dokładnego
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")  # zgłaszamy błąd
            blad = odejmij_wektory(x_nowe, rozwiazanie_dokladne)  # obliczamy różnicę między przybliżeniem a rozwiązaniem dokładnym
            if norma_max(blad) < epsilon:  # sprawdzamy, czy norma maksimum błędu jest mniejsza od epsilon
                return x_nowe, krok  # zwracamy wynik i numer iteracji

        x_stare = x_nowe[:]  # po zakończeniu iteracji przepisujemy nowe przybliżenie jako stare

    return x_stare, max_iter  # jeśli nie spełniono warunku stopu wcześniej, zwracamy ostatnie przybliżenie i maksymalną liczbę iteracji


print("--------------------ZADANIE 1--------------------")  # wypisujemy nagłówek zadania

A = [  # definiujemy macierz współczynników układu ze slajdów
    [4.0, -2.0, 0.0, 0.0],  # pierwszy wiersz macierzy A
    [-2.0, 5.0, -1.0, 0.0],  # drugi wiersz macierzy A
    [0.0, -1.0, 4.0, 2.0],  # trzeci wiersz macierzy A
    [0.0, 0.0, 2.0, 3.0]  # czwarty wiersz macierzy A
]

b = [0.0, 2.0, 3.0, -2.0]  # definiujemy wektor prawej strony układu
x0 = [0.0, 0.0, 0.0, 0.0]  # definiujemy przybliżenie początkowe
x_dokladne = [0.5, 1.0, 2.0, -2.0]  # zapisujemy rozwiązanie dokładne dla tego przykładu

print("\nDane:")  # wypisujemy napis informujący o danych wejściowych
print("Macierz A:")  # wypisujemy nagłówek dla macierzy A
for wiersz in A:  # przechodzimy po wszystkich wierszach macierzy
    print(wiersz)  # wypisujemy każdy wiersz macierzy

print("\nWektor b:")  # wypisujemy nagłówek dla wektora b
print(b)  # wypisujemy wektor prawej strony

print("\nPrzybliżenie początkowe x^(0):")  # wypisujemy nagłówek dla przybliżenia początkowego
print(x0)  # wypisujemy wektor początkowy

print("\nDokładne rozwiązanie:")  # wypisujemy nagłówek dla rozwiązania dokładnego
print(x_dokladne)  # wypisujemy rozwiązanie dokładne

print("\n-------------------- a) LICZBA ITERACJI --------------------")  # wypisujemy nagłówek dla punktu a
wynik_a, iteracje_a = jacobi(  # wywołujemy metodę Jacobiego dla warunku stopu opartego na liczbie iteracji
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=10,  # ustawiamy liczbę iteracji na 10
    warunek_stopu="iteracje"  # wybieramy warunek stopu oparty na liczbie iteracji
)

print("\nWynik końcowy po zadanej liczbie iteracji:")  # wypisujemy opis wyniku z punktu a
wypisz_wektor(wynik_a)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_a)  # wypisujemy liczbę wykonanych iteracji

blad_a = odejmij_wektory(wynik_a, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu a
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_a))  # wypisujemy normę maksimum błędu

print("\n-------------------- b) WARUNEK ZE SLAJDU --------------------")  # wypisujemy nagłówek dla punktu b
wynik_b, iteracje_b = jacobi(  # wywołujemy metodę Jacobiego dla warunku stopu ze slajdu
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=100,  # ustawiamy maksymalną liczbę iteracji na 100
    epsilon=1e-3,  # ustawiamy dokładność zgodną ze slajdem
    warunek_stopu="roznica"  # wybieramy warunek stopu oparty na ilorazie norm
)

print("\nWynik końcowy:")  # wypisujemy opis wyniku z punktu b
wypisz_wektor(wynik_b)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_b)  # wypisujemy liczbę wykonanych iteracji

blad_b = odejmij_wektory(wynik_b, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu b
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_b))  # wypisujemy normę maksimum błędu

print("\n-------------------- c) BŁĄD UZYSKANEGO PRZYBLIŻENIA --------------------")  # wypisujemy nagłówek dla punktu c
wynik_c, iteracje_c = jacobi(  # wywołujemy metodę Jacobiego dla warunku stopu opartego na błędzie
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=100,  # ustawiamy maksymalną liczbę iteracji na 100
    epsilon=1e-3,  # ustawiamy dokładność na 10 do potęgi minus 3
    warunek_stopu="blad",  # wybieramy warunek stopu oparty na błędzie względem rozwiązania dokładnego
    rozwiazanie_dokladne=x_dokladne  # przekazujemy rozwiązanie dokładne potrzebne do obliczenia błędu
)

print("\nWynik końcowy:")  # wypisujemy opis wyniku z punktu c
wypisz_wektor(wynik_c)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_c)  # wypisujemy liczbę wykonanych iteracji

blad_c = odejmij_wektory(wynik_c, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu c
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_c))  # wypisujemy normę maksimum błędu
```

---

# Zadanie 2

**Napisz program implementujący metodę Gaussa-Seidla iteracyjnego rozwiązywania układów równań liniowych z analogicznymi warunkami zatrzymania jak w zadaniu 1.**

## Co to jest metoda Gaussa-Seidla?

Metoda Gaussa-Seidla jest podobna do metody Jacobiego, ale ma ważną różnicę:

podczas liczenia nowego przybliżenia wykorzystuje od razu te wartości, które zostały już policzone w bieżącej iteracji.

Każdą niewiadomą w iteracji $k$ obliczamy ze wzoru:

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
- iloraz normy różnicy kolejnych przybliżeń i normy bieżącego przybliżenia,
- błąd przybliżenia.

## Warunek stosowalności

Aby metoda mogła być wykonywana, na przekątnej macierzy nie może być zera, czyli:

$$
a_{ii} \ne 0 \quad \text{dla wszystkich } i=1,2,\dots,n
$$

## Warunki zatrzymania

### a) Liczba iteracji

Program kończy działanie po zadanej liczbie kroków.

### b) Iloraz normy różnicy kolejnych przybliżeń i normy bieżącego przybliżenia

Zgodnie ze slajdami sprawdzamy warunek:

$$
\frac{\|x^{(k)} - x^{(k-1)}\|}{\|x^{(k)}\|} \le \varepsilon
$$

W programie używana jest norma maksimum.

### c) Błąd uzyskanego przybliżenia

Jeżeli znamy rozwiązanie dokładne $x^*$, możemy sprawdzać:

$$
\|x^{(k)} - x^*\| < \varepsilon
$$

## Przykład użyty w programie

W programie wykorzystano ten sam układ równań co na slajdach:

$$
\begin{cases}
4x_1 - 2x_2 = 0 \\
-2x_1 + 5x_2 - x_3 = 2 \\
-x_2 + 4x_3 + 2x_4 = 3 \\
2x_3 + 3x_4 = -2
\end{cases}
$$

z przybliżeniem początkowym:

$$
x^{(0)} = (0,0,0,0)^T
$$

oraz rozwiązaniem dokładnym:

$$
x^* = (0.5,1,2,-2)^T
$$

Dla warunku ze slajdów przyjęto:

$$
\varepsilon = 10^{-3}
$$

## Kod

```python
def norma_max(wektor):  # definiujemy funkcję obliczającą normę maksimum wektora
    maksimum = abs(wektor[0])  # jako początkowe maksimum przyjmujemy moduł pierwszego elementu
    for i in range(1, len(wektor)):  # przechodzimy po kolejnych elementach wektora
        if abs(wektor[i]) > maksimum:  # sprawdzamy, czy moduł bieżącego elementu jest większy od obecnego maksimum
            maksimum = abs(wektor[i])  # jeśli tak, aktualizujemy wartość maksimum
    return maksimum  # zwracamy największy moduł elementu wektora


def odejmij_wektory(wektor1, wektor2):  # definiujemy funkcję odejmującą od siebie dwa wektory
    wynik = []  # tworzymy pustą listę na wynik odejmowania
    for i in range(len(wektor1)):  # przechodzimy po wszystkich indeksach wektora
        wynik.append(wektor1[i] - wektor2[i])  # dodajemy do wyniku różnicę odpowiednich elementów
    return wynik  # zwracamy obliczony wektor różnicy


def wypisz_wektor(wektor, nazwa="x"):  # definiujemy funkcję do ładnego wypisywania wektora
    for i in range(len(wektor)):  # przechodzimy po wszystkich elementach wektora
        print(f"{nazwa}{i+1} = {wektor[i]}")  # wypisujemy elementy jako x1, x2, x3 itd.


def gauss_seidel(A, b, x0, max_iter=100, epsilon=1e-3, warunek_stopu="iteracje", rozwiazanie_dokladne=None):  # definiujemy funkcję realizującą metodę Gaussa-Seidla
    n = len(A)  # zapisujemy liczbę równań i niewiadomych
    x = x0[:]  # kopiujemy przybliżenie początkowe do wektora roboczego

    for i in range(n):  # przechodzimy po wszystkich elementach przekątnej macierzy
        if A[i][i] == 0:  # sprawdzamy, czy na przekątnej nie ma zera
            raise ValueError("Na przekątnej macierzy nie może być zera")  # jeśli jest zero, zgłaszamy błąd

    for krok in range(1, max_iter + 1):  # wykonujemy kolejne iteracje od 1 do max_iter
        x_stare = x[:]  # zapisujemy kopię poprzedniego przybliżenia

        for i in range(n):  # przechodzimy po wszystkich niewiadomych
            suma1 = 0.0  # zerujemy sumę składników liczonych z nowych wartości
            for j in range(i):  # przechodzimy po indeksach wcześniejszych niż i
                suma1 += A[i][j] * x[j]  # dodajemy składniki z już zaktualizowanych wartości bieżącej iteracji

            suma2 = 0.0  # zerujemy sumę składników liczonych ze starych wartości
            for j in range(i + 1, n):  # przechodzimy po indeksach późniejszych niż i
                suma2 += A[i][j] * x_stare[j]  # dodajemy składniki z poprzedniej iteracji

            x[i] = (b[i] - suma1 - suma2) / A[i][i]  # obliczamy nową wartość x_i zgodnie ze wzorem Gaussa-Seidla

        if warunek_stopu == "iteracje":  # sprawdzamy, czy wybrano warunek stopu oparty na liczbie iteracji
            if krok == max_iter:  # jeśli osiągnięto zadaną liczbę iteracji
                return x, krok  # zwracamy aktualny wynik i liczbę iteracji

        elif warunek_stopu == "roznica":  # sprawdzamy, czy wybrano warunek stopu ze slajdów
            roznica = odejmij_wektory(x, x_stare)  # obliczamy różnicę między nowym i poprzednim przybliżeniem
            norma_roznicy = norma_max(roznica)  # obliczamy normę maksimum tej różnicy
            norma_biezaca = norma_max(x)  # obliczamy normę maksimum bieżącego przybliżenia

            if norma_biezaca == 0:  # sprawdzamy przypadek szczególny, gdy norma bieżącego przybliżenia wynosi zero
                if norma_roznicy <= epsilon:  # jeśli sama norma różnicy spełnia warunek stopu
                    return x, krok  # zwracamy wynik i liczbę iteracji
            else:  # wykonujemy standardowe sprawdzenie warunku stopu
                if (norma_roznicy / norma_biezaca) <= epsilon:  # sprawdzamy iloraz norm zgodnie ze slajdami
                    return x, krok  # zwracamy wynik i liczbę iteracji

        elif warunek_stopu == "blad":  # sprawdzamy, czy wybrano warunek stopu oparty na błędzie względem rozwiązania dokładnego
            if rozwiazanie_dokladne is None:  # jeśli nie podano rozwiązania dokładnego
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")  # zgłaszamy błąd
            blad = odejmij_wektory(x, rozwiazanie_dokladne)  # obliczamy wektor błędu względem rozwiązania dokładnego
            if norma_max(blad) < epsilon:  # sprawdzamy, czy norma maksimum błędu jest mniejsza od epsilon
                return x, krok  # zwracamy wynik i liczbę iteracji

        else:  # obsługujemy przypadek niepoprawnej nazwy warunku stopu
            raise ValueError("Niepoprawny warunek stopu")  # zgłaszamy błąd dla nieznanego warunku stopu

    return x, max_iter  # jeśli warunek stopu nie został spełniony wcześniej, zwracamy ostatni wynik i maksymalną liczbę iteracji


A = [  # definiujemy macierz współczynników układu ze slajdów
    [4.0, -2.0, 0.0, 0.0],  # pierwszy wiersz macierzy A
    [-2.0, 5.0, -1.0, 0.0],  # drugi wiersz macierzy A
    [0.0, -1.0, 4.0, 2.0],  # trzeci wiersz macierzy A
    [0.0, 0.0, 2.0, 3.0]  # czwarty wiersz macierzy A
]

b = [0.0, 2.0, 3.0, -2.0]  # definiujemy wektor prawej strony układu
x0 = [0.0, 0.0, 0.0, 0.0]  # definiujemy przybliżenie początkowe x^(0)
x_dokladne = [0.5, 1.0, 2.0, -2.0]  # definiujemy rozwiązanie dokładne tego układu

print("\nDane:")  # wypisujemy nagłówek danych wejściowych
print("Macierz A:")  # wypisujemy napis informujący o macierzy A
for wiersz in A:  # przechodzimy po wszystkich wierszach macierzy
    print(wiersz)  # wypisujemy każdy wiersz macierzy

print("\nWektor b:")  # wypisujemy napis informujący o wektorze b
print(b)  # wypisujemy wektor prawej strony

print("\nPrzybliżenie początkowe x^(0):")  # wypisujemy napis informujący o przybliżeniu początkowym
print(x0)  # wypisujemy wektor początkowy

print("\nDokładne rozwiązanie:")  # wypisujemy napis informujący o rozwiązaniu dokładnym
print(x_dokladne)  # wypisujemy rozwiązanie dokładne

print("\n-------------------- a) LICZBA ITERACJI --------------------")  # wypisujemy nagłówek punktu a
wynik_a, iteracje_a = gauss_seidel(  # wywołujemy metodę Gaussa-Seidla dla warunku stopu opartego na liczbie iteracji
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=10,  # ustawiamy liczbę iteracji na 10
    warunek_stopu="iteracje"  # wybieramy warunek stopu oparty na liczbie iteracji
)

print("\nWynik końcowy po zadanej liczbie iteracji:")  # wypisujemy opis wyniku dla punktu a
wypisz_wektor(wynik_a)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_a)  # wypisujemy liczbę wykonanych iteracji

blad_a = odejmij_wektory(wynik_a, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu a
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_a))  # wypisujemy normę maksimum błędu

print("\n-------------------- b) WARUNEK ZE SLAJDU --------------------")  # wypisujemy nagłówek punktu b
wynik_b, iteracje_b = gauss_seidel(  # wywołujemy metodę Gaussa-Seidla dla warunku stopu zgodnego ze slajdami
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=100,  # ustawiamy maksymalną liczbę iteracji na 100
    epsilon=1e-3,  # ustawiamy epsilon zgodnie ze slajdami
    warunek_stopu="roznica"  # wybieramy warunek stopu oparty na ilorazie norm
)

print("\nWynik końcowy:")  # wypisujemy opis wyniku dla punktu b
wypisz_wektor(wynik_b)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_b)  # wypisujemy liczbę wykonanych iteracji

blad_b = odejmij_wektory(wynik_b, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu b
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_b))  # wypisujemy normę maksimum błędu

print("\n-------------------- c) BŁĄD UZYSKANEGO PRZYBLIŻENIA --------------------")  # wypisujemy nagłówek punktu c
wynik_c, iteracje_c = gauss_seidel(  # wywołujemy metodę Gaussa-Seidla dla warunku stopu opartego na błędzie dokładnym
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=100,  # ustawiamy maksymalną liczbę iteracji na 100
    epsilon=1e-3,  # ustawiamy epsilon na 10 do potęgi minus 3
    warunek_stopu="blad",  # wybieramy warunek stopu oparty na błędzie względem rozwiązania dokładnego
    rozwiazanie_dokladne=x_dokladne  # przekazujemy rozwiązanie dokładne potrzebne do obliczenia błędu
)

print("\nWynik końcowy:")  # wypisujemy opis wyniku dla punktu c
wypisz_wektor(wynik_c)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_c)  # wypisujemy liczbę wykonanych iteracji

blad_c = odejmij_wektory(wynik_c, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu c
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_c))  # wypisujemy normę maksimum błędu
```

### Jeśli trzeba **wyświetlić wszystkie iteracje** to zmienić fragment:

```python
x[i] = (b[i] - suma1 - suma2) / A[i][i]

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x, krok

        elif warunek_stopu == "roznica":
            roznica = odejmij_wektory(x, x_stare)
            norma_roznicy = norma_max(roznica)
            norma_biezaca = norma_max(x)
```

na:

```python
 x[i] = (b[i] - suma1 - suma2) / A[i][i]

        roznica = odejmij_wektory(x, x_stare)
        norma_roznicy = norma_max(roznica)

        print(f"\nIteracja {krok}:")
        wypisz_wektor(x)
        print("Norma maksimum różnicy:", norma_roznicy)

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x, krok

        elif warunek_stopu == "roznica":
            norma_biezaca = norma_max(x)

            if norma_biezaca == 0:
                if norma_roznicy <= epsilon:
```

---

# Zadanie 3

**Sprawdź zbieżność układu pod kątem metod z zadania 1 oraz 2.**

Układ do testowania:

$$
\begin{cases}
4x_1 - 2x_2 = 0, \\
-2x_1 + 5x_2 - x_3 = 2, \\
-x_2 + 4x_3 + 2x_4 = 3, \\
2x_3 + 3x_4 = -2.
\end{cases}
$$

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

## Co sprawdzamy w tym zadaniu?

W zadaniu 1 używaliśmy **metody Jacobiego**, a w zadaniu 2 **metody Gaussa-Seidla**.
Teraz nie liczymy kolejnych iteracji, tylko sprawdzamy, **czy te metody powinny być zbieżne** dla danego układu.

Na slajdach pojawia się ogólna postać metody iteracyjnej:

$$
x^{(k)} = W x^{(k-1)} + Z
$$

Najważniejsze pytanie brzmi:

> czy kolejne iteracje prowadzą do rozwiązania?

Według slajdów zależy to od macierzy iteracji (W).
W praktyce używamy warunku:

$$
||W|| < 1
$$

W tej notatce korzystamy z **normy wierszowej**:

$$
\|W\|_{\infty} = \max_i \sum_{j=1}^{n} |w_{ij}|
$$

Jeżeli:

$$
||W||_\infty < 1
$$

to metoda powinna być zbieżna.

## 1. Metoda Jacobiego

Dla metody Jacobiego macierz iteracji wyznaczamy dokładnie z wzoru ze slajdu:

$$
W_{ij} =
\begin{cases}
0 & \text{gdy } i=j, \\
-\dfrac{a_{ij}}{a_{ii}} & \text{gdy } i \ne j
\end{cases}
$$

Dla naszego układu otrzymujemy:

$$
W_J =
\begin{bmatrix}
0 & \frac12 & 0 & 0 \\
\frac25 & 0 & \frac15 & 0 \\
0 & \frac14 & 0 & -\frac12 \\
0 & 0 & -\frac23 & 0
\end{bmatrix}
$$

Teraz liczymy normę wierszową:

* wiersz 1:
  $$
  0 + \frac12 + 0 + 0 = \frac12
  $$

* wiersz 2:
  $$
  \frac25 + 0 + \frac15 + 0 = \frac35
  $$

* wiersz 3:
  $$
  0 + \frac14 + 0 + \frac12 = \frac34
  $$

* wiersz 4:
  $$
  0 + 0 + \frac23 + 0 = \frac23
  $$

Zatem:

$$
|W_J|_\infty =
\max\left(
\frac12,\frac35,\frac34,\frac23
\right)
=
\frac34
= 0.75
$$

Ponieważ:

$$
||W_J||_\infty < 1
$$

to **metoda Jacobiego jest zbieżna**.

## 2. Metoda Gaussa-Seidla

Dla metody Gaussa-Seidla na slajdach mamy wzór:

$$
(L + D)x^{(k)} = -Ux^{(k-1)} + b
$$

gdzie:

* $L$ — macierz trójkątna dolna,
* $D$ — macierz diagonalna,
* $U$ — macierz trójkątna górna.

Po przekształceniu dostajemy:

$$
x^{(k)} = -(L + D)^{-1}U,x^{(k-1)} + (L + D)^{-1}b
$$

Stąd macierz iteracji dla Gaussa-Seidla ma postać:

$$
W_{GS} = -(L + D)^{-1}U
$$

To jest ważna różnica względem Jacobiego:

* dla Jacobiego mamy prosty wzór element po elemencie,
* dla Gaussa-Seidla trzeba skorzystać z rozkładu macierzy $A$ na części $L$, $D$, $U$.

Dla naszego układu otrzymujemy:

$$
W_{GS} =
\begin{bmatrix}
0 & \frac12 & 0 & 0 \\
0 & \frac15 & \frac15 & 0 \\
0 & \frac1{20} & \frac1{20} & -\frac12 \\
0 & -\frac1{30} & -\frac1{30} & \frac13
\end{bmatrix}
$$

Liczymy normę wierszową:

* wiersz 1:
  $$
  0 + \frac12 + 0 + 0 = \frac12
  $$

* wiersz 2:
  $$
  0 + \frac15 + \frac15 + 0 = \frac25
  $$

* wiersz 3:
  $$
  0 + \frac1{20} + \frac1{20} + \frac12 = \frac35
  $$

* wiersz 4:
  $$
  0 + \frac1{30} + \frac1{30} + \frac13 = \frac25
  $$

Zatem:

$$
|W_{GS}|_\infty =
\max\left(
\frac12,\frac25,\frac35,\frac25
\right)
=
\frac35
= 0.6
$$

Ponieważ:

$$
|W_{GS}|_\infty < 1
$$

to **metoda Gaussa-Seidla jest zbieżna**.

---

## Porównanie obu metod

Otrzymaliśmy:

$$
|W_J|_\infty = 0.75
$$

oraz

$$
|W_{GS}|_\infty = 0.6
$$

Obie metody są zbieżne, ale ponieważ:

$$
0.6 < 0.75
$$

to metoda Gaussa-Seidla powinna zbiegać szybciej niż metoda Jacobiego.
Zgadza się to z wcześniejszymi obserwacjami z zadań 1 i 2.

## Kod

```python
print("--------------------ZADANIE 3--------------------")  # wypisujemy nagłówek zadania 3

def zeros(n, m):  # definiujemy funkcję tworzącą macierz n x m wypełnioną zerami
    macierz = []  # tworzymy pustą listę na całą macierz
    for i in range(n):  # wykonujemy pętlę po wszystkich wierszach
        wiersz = []  # tworzymy pustą listę na jeden wiersz
        for j in range(m):  # wykonujemy pętlę po wszystkich kolumnach
            wiersz.append(0.0)  # dodajemy do wiersza element 0.0
        macierz.append(wiersz)  # dodajemy gotowy wiersz do macierzy
    return macierz  # zwracamy utworzoną macierz zerową

def wypisz_macierz(macierz):  # definiujemy funkcję do wypisywania macierzy
    for wiersz in macierz:  # przechodzimy po wszystkich wierszach macierzy
        print(wiersz)  # wypisujemy bieżący wiersz

def norma_wierszowa_macierzy(macierz):  # definiujemy funkcję liczącą normę wierszową macierzy
    maksimum = 0.0  # ustawiamy początkowe maksimum na 0
    for i in range(len(macierz)):  # przechodzimy po wszystkich wierszach macierzy
        suma = 0.0  # zerujemy sumę modułów elementów w bieżącym wierszu
        for j in range(len(macierz[i])):  # przechodzimy po wszystkich elementach bieżącego wiersza
            suma += abs(macierz[i][j])  # dodajemy moduł bieżącego elementu do sumy
        if suma > maksimum:  # sprawdzamy, czy suma z tego wiersza jest większa od dotychczasowego maksimum
            maksimum = suma  # aktualizujemy maksimum
    return maksimum  # zwracamy największą sumę modułów z wierszy

def macierz_iteracji_jacobiego(A):  # definiujemy funkcję wyznaczającą macierz iteracji metody Jacobiego
    n = len(A)  # zapisujemy rozmiar macierzy A
    W = zeros(n, n)  # tworzymy pustą macierz iteracji W o rozmiarze n x n

    for i in range(n):  # przechodzimy po wszystkich wierszach macierzy
        for j in range(n):  # przechodzimy po wszystkich kolumnach macierzy
            if i == j:  # sprawdzamy, czy jesteśmy na przekątnej
                W[i][j] = 0.0  # na przekątnej wpisujemy 0 zgodnie ze wzorem dla Jacobiego
            else:  # w przeciwnym wypadku jesteśmy poza przekątną
                W[i][j] = -A[i][j] / A[i][i]  # wpisujemy wartość -a_ij / a_ii zgodnie ze wzorem ze slajdu

    return W  # zwracamy macierz iteracji Jacobiego

def rozwiaz_uklad_dolnotrojkatny(LD, b):  # definiujemy funkcję rozwiązującą układ dolnotrójkątny LDx=b
    n = len(LD)  # zapisujemy rozmiar macierzy
    x = [0.0] * n  # tworzymy wektor rozwiązania wypełniony zerami

    for i in range(n):  # przechodzimy po kolejnych równaniach od góry do dołu
        suma = 0.0  # zerujemy sumę znanych składników
        for j in range(i):  # przechodzimy po wcześniej obliczonych elementach rozwiązania
            suma += LD[i][j] * x[j]  # dodajemy składniki z już wyznaczonych wartości
        x[i] = (b[i] - suma) / LD[i][i]  # obliczamy bieżący element rozwiązania przez podstawianie w przód

    return x  # zwracamy wyznaczony wektor rozwiązania

def macierz_iteracji_gaussa_seidla(A):  # definiujemy funkcję wyznaczającą macierz iteracji metody Gaussa-Seidla
    n = len(A)  # zapisujemy rozmiar macierzy A

    LD = zeros(n, n)  # tworzymy pustą macierz dla części L + D
    U = zeros(n, n)  # tworzymy pustą macierz dla części U

    for i in range(n):  # przechodzimy po wszystkich wierszach macierzy A
        for j in range(n):  # przechodzimy po wszystkich kolumnach macierzy A
            if j <= i:  # sprawdzamy, czy element należy do dolnej części wraz z przekątną
                LD[i][j] = A[i][j]  # przepisujemy element do macierzy LD
            else:  # w przeciwnym wypadku element należy do części górnej
                U[i][j] = A[i][j]  # przepisujemy element do macierzy U

    W = zeros(n, n)  # tworzymy pustą macierz iteracji Gaussa-Seidla

    for kolumna in range(n):  # przechodzimy po kolejnych kolumnach macierzy W
        prawa_strona = []  # tworzymy pustą listę na prawą stronę układu pomocniczego
        for i in range(n):  # przechodzimy po wszystkich wierszach
            prawa_strona.append(-U[i][kolumna])  # budujemy prawą stronę jako przeciwną kolumnę macierzy U

        rozwiazanie = rozwiaz_uklad_dolnotrojkatny(LD, prawa_strona)  # rozwiązujemy układ (L+D)x = -u_k dla bieżącej kolumny

        for i in range(n):  # przechodzimy po wszystkich wierszach rozwiązania
            W[i][kolumna] = rozwiazanie[i]  # wpisujemy obliczoną kolumnę do macierzy iteracji W

    return W  # zwracamy macierz iteracji Gaussa-Seidla

A = [  # definiujemy macierz współczynników układu
    [4.0, -2.0, 0.0, 0.0],  # pierwszy wiersz macierzy A
    [-2.0, 5.0, -1.0, 0.0],  # drugi wiersz macierzy A
    [0.0, -1.0, 4.0, 2.0],  # trzeci wiersz macierzy A
    [0.0, 0.0, 2.0, 3.0]  # czwarty wiersz macierzy A
]

print("\nMacierz A:")  # wypisujemy nagłówek dla macierzy A
wypisz_macierz(A)  # wypisujemy macierz A

print("\n-------------------- METODA JACOBIEGO --------------------")  # wypisujemy nagłówek sekcji dla metody Jacobiego
WJ = macierz_iteracji_jacobiego(A)  # wyznaczamy macierz iteracji Jacobiego
print("Macierz iteracyjna W_J:")  # wypisujemy nagłówek dla macierzy W_J
wypisz_macierz(WJ)  # wypisujemy macierz iteracji Jacobiego

norma_WJ = norma_wierszowa_macierzy(WJ)  # obliczamy normę wierszową macierzy iteracji Jacobiego
print("Norma wierszowa ||W_J|| =", norma_WJ)  # wypisujemy wartość normy macierzy W_J

if norma_WJ < 1:  # sprawdzamy warunek zbieżności dla Jacobiego
    print("Metoda Jacobiego jest zbieżna, ponieważ ||W_J|| < 1.")  # wypisujemy pozytywny wniosek
else:  # w przeciwnym przypadku
    print("Metoda Jacobiego może nie być zbieżna, ponieważ ||W_J|| >= 1.")  # wypisujemy negatywny wniosek

print("\n-------------------- METODA GAUSSA-SEIDLA --------------------")  # wypisujemy nagłówek sekcji dla metody Gaussa-Seidla
WGS = macierz_iteracji_gaussa_seidla(A)  # wyznaczamy macierz iteracji Gaussa-Seidla
print("Macierz iteracyjna W_GS:")  # wypisujemy nagłówek dla macierzy W_GS
wypisz_macierz(WGS)  # wypisujemy macierz iteracji Gaussa-Seidla

norma_WGS = norma_wierszowa_macierzy(WGS)  # obliczamy normę wierszową macierzy iteracji Gaussa-Seidla
print("Norma wierszowa ||W_GS|| =", norma_WGS)  # wypisujemy wartość normy macierzy W_GS

if norma_WGS < 1:  # sprawdzamy warunek zbieżności dla Gaussa-Seidla
    print("Metoda Gaussa-Seidla jest zbieżna, ponieważ ||W_GS|| < 1.")  # wypisujemy pozytywny wniosek
else:  # w przeciwnym przypadku
    print("Metoda Gaussa-Seidla może nie być zbieżna, ponieważ ||W_GS|| >= 1.")  # wypisujemy negatywny wniosek

print("\n-------------------- WNIOSEK KOŃCOWY --------------------")  # wypisujemy nagłówek końcowego wniosku
print("Zbieżność metod z zadania 1 i 2 badamy przez normę macierzy iteracji.")  # wypisujemy ogólną informację o sposobie badania zbieżności
print("Dla Jacobiego sprawdzamy macierz W_J.")  # wypisujemy informację dotyczącą metody Jacobiego
print("Dla Gaussa-Seidla sprawdzamy macierz W_GS.")  # wypisujemy informację dotyczącą metody Gaussa-Seidla
print("Jeżeli ||W|| < 1, to metoda jest zbieżna.")  # wypisujemy końcowe kryterium zbieżności
```

---

## Wnioski

W zadaniu 3 zbieżność badamy zgodnie ze slajdami przez macierz iteracji (W) i warunek:

$$
|W| < 1
$$

Dla badanego układu:

* dla metody Jacobiego:
  $$
  |W_J|_\infty = 0.75 < 1
  $$

* dla metody Gaussa-Seidla:
  $$
  |W_{GS}|_\infty = 0.6 < 1
  $$

Oznacza to, że:

* metoda Jacobiego jest zbieżna,
* metoda Gaussa-Seidla jest zbieżna,
* metoda Gaussa-Seidla powinna zbiegać szybciej niż metoda Jacobiego.

---

# Lab 6

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

![alt text](obrazy/1.png)

## Warunki zatrzymania

### a) Liczba iteracji

Program kończy działanie po zadanej liczbie kroków.

### b) Iloraz normy różnicy kolejnych przybliżeń i normy bieżącego przybliżenia

Sprawdzasz, czy:

$$
\frac{\|x^{(k)} - x^{(k-1)}\|}{\|x^{(k)}\|} \le \varepsilon
$$

W programie używana jest norma maksimum.  
Jeżeli warunek jest spełniony, uznajesz, że kolejne przybliżenia zmieniają się już bardzo nieznacznie.

### c) Błąd uzyskanego przybliżenia

Jeżeli znasz dokładne rozwiązanie $x^*$, możesz sprawdzać:

$$
\|x^{(k)} - x^*\| < \varepsilon
$$

## Kod

```python
def norma_max(wektor):  # funkcja oblicza normę maksimum wektora
    maksimum = abs(wektor[0])  # jako początkowe maksimum przyjmujemy moduł pierwszego elementu
    for i in range(1, len(wektor)):  # przechodzimy po kolejnych elementach wektora
        if abs(wektor[i]) > maksimum:  # sprawdzamy, czy moduł bieżącego elementu jest większy od dotychczasowego maksimum
            maksimum = abs(wektor[i])  # jeśli tak, aktualizujemy maksimum
    return maksimum  # zwracamy największy moduł elementu wektora


def odejmij_wektory(wektor1, wektor2):  # funkcja odejmuje od siebie dwa wektory o tej samej długości
    wynik = []  # tworzymy pustą listę na wynik odejmowania
    for i in range(len(wektor1)):  # przechodzimy po wszystkich indeksach wektora
        wynik.append(wektor1[i] - wektor2[i])  # dodajemy do wyniku różnicę odpowiednich elementów
    return wynik  # zwracamy wektor różnicy


def wypisz_wektor(wektor, nazwa="x"):  # funkcja wypisuje kolejne współrzędne wektora
    for i in range(len(wektor)):  # przechodzimy po wszystkich elementach wektora
        print(f"{nazwa}{i+1} = {wektor[i]}")  # wypisujemy element w formacie x1, x2, x3 itd.


def jacobi(A, b, x0, max_iter=100, epsilon=1e-3, warunek_stopu="iteracje", rozwiazanie_dokladne=None):  # funkcja realizuje metodę Jacobiego
    n = len(A)  # zapisujemy liczbę równań i niewiadomych
    x_stare = x0[:]  # kopiujemy przybliżenie początkowe do wektora poprzedniej iteracji

    for i in range(n):  # sprawdzamy wszystkie elementy na przekątnej macierzy
        if A[i][i] == 0:  # jeśli na przekątnej pojawi się zero
            raise ValueError("Na przekątnej macierzy nie może być zera")  # przerywamy działanie programu z komunikatem o błędzie

    for krok in range(1, max_iter + 1):  # wykonujemy kolejne iteracje od 1 do maksymalnej liczby iteracji
        x_nowe = [0.0] * n  # tworzymy nowy wektor przybliżenia wypełniony zerami

        for i in range(n):  # przechodzimy po wszystkich równaniach
            suma = 0.0  # zerujemy sumę składników spoza przekątnej dla i-tego równania
            for j in range(n):  # przechodzimy po wszystkich kolumnach macierzy
                if j != i:  # pomijamy element z przekątnej
                    suma += A[i][j] * x_stare[j]  # dodajemy iloczyn współczynnika macierzy i starego przybliżenia

            x_nowe[i] = (b[i] - suma) / A[i][i]  # liczymy nową wartość i-tej niewiadomej ze wzoru Jacobiego

        if warunek_stopu == "iteracje":  # sprawdzamy, czy wybrano warunek stopu oparty na liczbie iteracji
            if krok == max_iter:  # jeśli osiągnięto zadaną liczbę iteracji
                return x_nowe, krok  # zwracamy aktualne przybliżenie i liczbę wykonanych iteracji

        elif warunek_stopu == "roznica":  # sprawdzamy, czy wybrano warunek stopu ze slajdu
            roznica = odejmij_wektory(x_nowe, x_stare)  # obliczamy różnicę kolejnych przybliżeń
            norma_roznicy = norma_max(roznica)  # liczymy normę maksimum tej różnicy
            norma_biezaca = norma_max(x_nowe)  # liczymy normę maksimum bieżącego przybliżenia

            if norma_biezaca == 0:  # sprawdzamy przypadek szczególny, gdy norma bieżącego wektora jest równa zero
                if norma_roznicy <= epsilon:  # jeśli sama norma różnicy spełnia warunek
                    return x_nowe, krok  # zwracamy wynik i numer iteracji
            else:  # w zwykłym przypadku, gdy norma bieżącego przybliżenia nie jest zerowa
                if (norma_roznicy / norma_biezaca) <= epsilon:  # sprawdzamy warunek stopu w postaci ilorazu norm
                    return x_nowe, krok  # zwracamy wynik i numer iteracji

        elif warunek_stopu == "blad":  # sprawdzamy, czy wybrano warunek stopu oparty na błędzie względem rozwiązania dokładnego
            if rozwiazanie_dokladne is None:  # jeśli nie podano rozwiązania dokładnego
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")  # zgłaszamy błąd
            blad = odejmij_wektory(x_nowe, rozwiazanie_dokladne)  # obliczamy różnicę między przybliżeniem a rozwiązaniem dokładnym
            if norma_max(blad) < epsilon:  # sprawdzamy, czy norma maksimum błędu jest mniejsza od epsilon
                return x_nowe, krok  # zwracamy wynik i numer iteracji

        x_stare = x_nowe[:]  # po zakończeniu iteracji przepisujemy nowe przybliżenie jako stare

    return x_stare, max_iter  # jeśli nie spełniono warunku stopu wcześniej, zwracamy ostatnie przybliżenie i maksymalną liczbę iteracji


print("--------------------ZADANIE 1--------------------")  # wypisujemy nagłówek zadania

A = [  # definiujemy macierz współczynników układu ze slajdów
    [4.0, -2.0, 0.0, 0.0],  # pierwszy wiersz macierzy A
    [-2.0, 5.0, -1.0, 0.0],  # drugi wiersz macierzy A
    [0.0, -1.0, 4.0, 2.0],  # trzeci wiersz macierzy A
    [0.0, 0.0, 2.0, 3.0]  # czwarty wiersz macierzy A
]

b = [0.0, 2.0, 3.0, -2.0]  # definiujemy wektor prawej strony układu
x0 = [0.0, 0.0, 0.0, 0.0]  # definiujemy przybliżenie początkowe
x_dokladne = [0.5, 1.0, 2.0, -2.0]  # zapisujemy rozwiązanie dokładne dla tego przykładu

print("\nDane:")  # wypisujemy napis informujący o danych wejściowych
print("Macierz A:")  # wypisujemy nagłówek dla macierzy A
for wiersz in A:  # przechodzimy po wszystkich wierszach macierzy
    print(wiersz)  # wypisujemy każdy wiersz macierzy

print("\nWektor b:")  # wypisujemy nagłówek dla wektora b
print(b)  # wypisujemy wektor prawej strony

print("\nPrzybliżenie początkowe x^(0):")  # wypisujemy nagłówek dla przybliżenia początkowego
print(x0)  # wypisujemy wektor początkowy

print("\nDokładne rozwiązanie:")  # wypisujemy nagłówek dla rozwiązania dokładnego
print(x_dokladne)  # wypisujemy rozwiązanie dokładne

print("\n-------------------- a) LICZBA ITERACJI --------------------")  # wypisujemy nagłówek dla punktu a
wynik_a, iteracje_a = jacobi(  # wywołujemy metodę Jacobiego dla warunku stopu opartego na liczbie iteracji
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=10,  # ustawiamy liczbę iteracji na 10
    warunek_stopu="iteracje"  # wybieramy warunek stopu oparty na liczbie iteracji
)

print("\nWynik końcowy po zadanej liczbie iteracji:")  # wypisujemy opis wyniku z punktu a
wypisz_wektor(wynik_a)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_a)  # wypisujemy liczbę wykonanych iteracji

blad_a = odejmij_wektory(wynik_a, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu a
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_a))  # wypisujemy normę maksimum błędu

print("\n-------------------- b) WARUNEK ZE SLAJDU --------------------")  # wypisujemy nagłówek dla punktu b
wynik_b, iteracje_b = jacobi(  # wywołujemy metodę Jacobiego dla warunku stopu ze slajdu
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=100,  # ustawiamy maksymalną liczbę iteracji na 100
    epsilon=1e-3,  # ustawiamy dokładność zgodną ze slajdem
    warunek_stopu="roznica"  # wybieramy warunek stopu oparty na ilorazie norm
)

print("\nWynik końcowy:")  # wypisujemy opis wyniku z punktu b
wypisz_wektor(wynik_b)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_b)  # wypisujemy liczbę wykonanych iteracji

blad_b = odejmij_wektory(wynik_b, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu b
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_b))  # wypisujemy normę maksimum błędu

print("\n-------------------- c) BŁĄD UZYSKANEGO PRZYBLIŻENIA --------------------")  # wypisujemy nagłówek dla punktu c
wynik_c, iteracje_c = jacobi(  # wywołujemy metodę Jacobiego dla warunku stopu opartego na błędzie
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=100,  # ustawiamy maksymalną liczbę iteracji na 100
    epsilon=1e-3,  # ustawiamy dokładność na 10 do potęgi minus 3
    warunek_stopu="blad",  # wybieramy warunek stopu oparty na błędzie względem rozwiązania dokładnego
    rozwiazanie_dokladne=x_dokladne  # przekazujemy rozwiązanie dokładne potrzebne do obliczenia błędu
)

print("\nWynik końcowy:")  # wypisujemy opis wyniku z punktu c
wypisz_wektor(wynik_c)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_c)  # wypisujemy liczbę wykonanych iteracji

blad_c = odejmij_wektory(wynik_c, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu c
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_c))  # wypisujemy normę maksimum błędu
```

---

# Zadanie 2

**Napisz program implementujący metodę Gaussa-Seidla iteracyjnego rozwiązywania układów równań liniowych z analogicznymi warunkami zatrzymania jak w zadaniu 1.**

## Co to jest metoda Gaussa-Seidla?

Metoda Gaussa-Seidla jest podobna do metody Jacobiego, ale ma ważną różnicę:

podczas liczenia nowego przybliżenia wykorzystuje od razu te wartości, które zostały już policzone w bieżącej iteracji.

Każdą niewiadomą w iteracji $k$ obliczamy ze wzoru:

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
- iloraz normy różnicy kolejnych przybliżeń i normy bieżącego przybliżenia,
- błąd przybliżenia.

## Warunek stosowalności

Aby metoda mogła być wykonywana, na przekątnej macierzy nie może być zera, czyli:

$$
a_{ii} \ne 0 \quad \text{dla wszystkich } i=1,2,\dots,n
$$

## Warunki zatrzymania

### a) Liczba iteracji

Program kończy działanie po zadanej liczbie kroków.

### b) Iloraz normy różnicy kolejnych przybliżeń i normy bieżącego przybliżenia

Zgodnie ze slajdami sprawdzamy warunek:

$$
\frac{\|x^{(k)} - x^{(k-1)}\|}{\|x^{(k)}\|} \le \varepsilon
$$

W programie używana jest norma maksimum.

### c) Błąd uzyskanego przybliżenia

Jeżeli znamy rozwiązanie dokładne $x^*$, możemy sprawdzać:

$$
\|x^{(k)} - x^*\| < \varepsilon
$$

## Przykład użyty w programie

W programie wykorzystano ten sam układ równań co na slajdach:

$$
\begin{cases}
4x_1 - 2x_2 = 0 \\
-2x_1 + 5x_2 - x_3 = 2 \\
-x_2 + 4x_3 + 2x_4 = 3 \\
2x_3 + 3x_4 = -2
\end{cases}
$$

z przybliżeniem początkowym:

$$
x^{(0)} = (0,0,0,0)^T
$$

oraz rozwiązaniem dokładnym:

$$
x^* = (0.5,1,2,-2)^T
$$

Dla warunku ze slajdów przyjęto:

$$
\varepsilon = 10^{-3}
$$

## Kod

```python
def norma_max(wektor):  # definiujemy funkcję obliczającą normę maksimum wektora
    maksimum = abs(wektor[0])  # jako początkowe maksimum przyjmujemy moduł pierwszego elementu
    for i in range(1, len(wektor)):  # przechodzimy po kolejnych elementach wektora
        if abs(wektor[i]) > maksimum:  # sprawdzamy, czy moduł bieżącego elementu jest większy od obecnego maksimum
            maksimum = abs(wektor[i])  # jeśli tak, aktualizujemy wartość maksimum
    return maksimum  # zwracamy największy moduł elementu wektora


def odejmij_wektory(wektor1, wektor2):  # definiujemy funkcję odejmującą od siebie dwa wektory
    wynik = []  # tworzymy pustą listę na wynik odejmowania
    for i in range(len(wektor1)):  # przechodzimy po wszystkich indeksach wektora
        wynik.append(wektor1[i] - wektor2[i])  # dodajemy do wyniku różnicę odpowiednich elementów
    return wynik  # zwracamy obliczony wektor różnicy


def wypisz_wektor(wektor, nazwa="x"):  # definiujemy funkcję do ładnego wypisywania wektora
    for i in range(len(wektor)):  # przechodzimy po wszystkich elementach wektora
        print(f"{nazwa}{i+1} = {wektor[i]}")  # wypisujemy elementy jako x1, x2, x3 itd.


def gauss_seidel(A, b, x0, max_iter=100, epsilon=1e-3, warunek_stopu="iteracje", rozwiazanie_dokladne=None):  # definiujemy funkcję realizującą metodę Gaussa-Seidla
    n = len(A)  # zapisujemy liczbę równań i niewiadomych
    x = x0[:]  # kopiujemy przybliżenie początkowe do wektora roboczego

    for i in range(n):  # przechodzimy po wszystkich elementach przekątnej macierzy
        if A[i][i] == 0:  # sprawdzamy, czy na przekątnej nie ma zera
            raise ValueError("Na przekątnej macierzy nie może być zera")  # jeśli jest zero, zgłaszamy błąd

    for krok in range(1, max_iter + 1):  # wykonujemy kolejne iteracje od 1 do max_iter
        x_stare = x[:]  # zapisujemy kopię poprzedniego przybliżenia

        for i in range(n):  # przechodzimy po wszystkich niewiadomych
            suma1 = 0.0  # zerujemy sumę składników liczonych z nowych wartości
            for j in range(i):  # przechodzimy po indeksach wcześniejszych niż i
                suma1 += A[i][j] * x[j]  # dodajemy składniki z już zaktualizowanych wartości bieżącej iteracji

            suma2 = 0.0  # zerujemy sumę składników liczonych ze starych wartości
            for j in range(i + 1, n):  # przechodzimy po indeksach późniejszych niż i
                suma2 += A[i][j] * x_stare[j]  # dodajemy składniki z poprzedniej iteracji

            x[i] = (b[i] - suma1 - suma2) / A[i][i]  # obliczamy nową wartość x_i zgodnie ze wzorem Gaussa-Seidla

        if warunek_stopu == "iteracje":  # sprawdzamy, czy wybrano warunek stopu oparty na liczbie iteracji
            if krok == max_iter:  # jeśli osiągnięto zadaną liczbę iteracji
                return x, krok  # zwracamy aktualny wynik i liczbę iteracji

        elif warunek_stopu == "roznica":  # sprawdzamy, czy wybrano warunek stopu ze slajdów
            roznica = odejmij_wektory(x, x_stare)  # obliczamy różnicę między nowym i poprzednim przybliżeniem
            norma_roznicy = norma_max(roznica)  # obliczamy normę maksimum tej różnicy
            norma_biezaca = norma_max(x)  # obliczamy normę maksimum bieżącego przybliżenia

            if norma_biezaca == 0:  # sprawdzamy przypadek szczególny, gdy norma bieżącego przybliżenia wynosi zero
                if norma_roznicy <= epsilon:  # jeśli sama norma różnicy spełnia warunek stopu
                    return x, krok  # zwracamy wynik i liczbę iteracji
            else:  # wykonujemy standardowe sprawdzenie warunku stopu
                if (norma_roznicy / norma_biezaca) <= epsilon:  # sprawdzamy iloraz norm zgodnie ze slajdami
                    return x, krok  # zwracamy wynik i liczbę iteracji

        elif warunek_stopu == "blad":  # sprawdzamy, czy wybrano warunek stopu oparty na błędzie względem rozwiązania dokładnego
            if rozwiazanie_dokladne is None:  # jeśli nie podano rozwiązania dokładnego
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")  # zgłaszamy błąd
            blad = odejmij_wektory(x, rozwiazanie_dokladne)  # obliczamy wektor błędu względem rozwiązania dokładnego
            if norma_max(blad) < epsilon:  # sprawdzamy, czy norma maksimum błędu jest mniejsza od epsilon
                return x, krok  # zwracamy wynik i liczbę iteracji

        else:  # obsługujemy przypadek niepoprawnej nazwy warunku stopu
            raise ValueError("Niepoprawny warunek stopu")  # zgłaszamy błąd dla nieznanego warunku stopu

    return x, max_iter  # jeśli warunek stopu nie został spełniony wcześniej, zwracamy ostatni wynik i maksymalną liczbę iteracji


A = [  # definiujemy macierz współczynników układu ze slajdów
    [4.0, -2.0, 0.0, 0.0],  # pierwszy wiersz macierzy A
    [-2.0, 5.0, -1.0, 0.0],  # drugi wiersz macierzy A
    [0.0, -1.0, 4.0, 2.0],  # trzeci wiersz macierzy A
    [0.0, 0.0, 2.0, 3.0]  # czwarty wiersz macierzy A
]

b = [0.0, 2.0, 3.0, -2.0]  # definiujemy wektor prawej strony układu
x0 = [0.0, 0.0, 0.0, 0.0]  # definiujemy przybliżenie początkowe x^(0)
x_dokladne = [0.5, 1.0, 2.0, -2.0]  # definiujemy rozwiązanie dokładne tego układu

print("\nDane:")  # wypisujemy nagłówek danych wejściowych
print("Macierz A:")  # wypisujemy napis informujący o macierzy A
for wiersz in A:  # przechodzimy po wszystkich wierszach macierzy
    print(wiersz)  # wypisujemy każdy wiersz macierzy

print("\nWektor b:")  # wypisujemy napis informujący o wektorze b
print(b)  # wypisujemy wektor prawej strony

print("\nPrzybliżenie początkowe x^(0):")  # wypisujemy napis informujący o przybliżeniu początkowym
print(x0)  # wypisujemy wektor początkowy

print("\nDokładne rozwiązanie:")  # wypisujemy napis informujący o rozwiązaniu dokładnym
print(x_dokladne)  # wypisujemy rozwiązanie dokładne

print("\n-------------------- a) LICZBA ITERACJI --------------------")  # wypisujemy nagłówek punktu a
wynik_a, iteracje_a = gauss_seidel(  # wywołujemy metodę Gaussa-Seidla dla warunku stopu opartego na liczbie iteracji
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=10,  # ustawiamy liczbę iteracji na 10
    warunek_stopu="iteracje"  # wybieramy warunek stopu oparty na liczbie iteracji
)

print("\nWynik końcowy po zadanej liczbie iteracji:")  # wypisujemy opis wyniku dla punktu a
wypisz_wektor(wynik_a)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_a)  # wypisujemy liczbę wykonanych iteracji

blad_a = odejmij_wektory(wynik_a, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu a
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_a))  # wypisujemy normę maksimum błędu

print("\n-------------------- b) WARUNEK ZE SLAJDU --------------------")  # wypisujemy nagłówek punktu b
wynik_b, iteracje_b = gauss_seidel(  # wywołujemy metodę Gaussa-Seidla dla warunku stopu zgodnego ze slajdami
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=100,  # ustawiamy maksymalną liczbę iteracji na 100
    epsilon=1e-3,  # ustawiamy epsilon zgodnie ze slajdami
    warunek_stopu="roznica"  # wybieramy warunek stopu oparty na ilorazie norm
)

print("\nWynik końcowy:")  # wypisujemy opis wyniku dla punktu b
wypisz_wektor(wynik_b)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_b)  # wypisujemy liczbę wykonanych iteracji

blad_b = odejmij_wektory(wynik_b, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu b
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_b))  # wypisujemy normę maksimum błędu

print("\n-------------------- c) BŁĄD UZYSKANEGO PRZYBLIŻENIA --------------------")  # wypisujemy nagłówek punktu c
wynik_c, iteracje_c = gauss_seidel(  # wywołujemy metodę Gaussa-Seidla dla warunku stopu opartego na błędzie dokładnym
    A, b, x0,  # przekazujemy macierz A, wektor b i przybliżenie początkowe
    max_iter=100,  # ustawiamy maksymalną liczbę iteracji na 100
    epsilon=1e-3,  # ustawiamy epsilon na 10 do potęgi minus 3
    warunek_stopu="blad",  # wybieramy warunek stopu oparty na błędzie względem rozwiązania dokładnego
    rozwiazanie_dokladne=x_dokladne  # przekazujemy rozwiązanie dokładne potrzebne do obliczenia błędu
)

print("\nWynik końcowy:")  # wypisujemy opis wyniku dla punktu c
wypisz_wektor(wynik_c)  # wypisujemy końcowy wektor przybliżenia
print("Liczba iteracji:", iteracje_c)  # wypisujemy liczbę wykonanych iteracji

blad_c = odejmij_wektory(wynik_c, x_dokladne)  # obliczamy błąd względem rozwiązania dokładnego dla punktu c
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_c))  # wypisujemy normę maksimum błędu
```

### Jeśli trzeba **wyświetlić wszystkie iteracje** to zmienić fragment:

```python
x[i] = (b[i] - suma1 - suma2) / A[i][i]

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x, krok

        elif warunek_stopu == "roznica":
            roznica = odejmij_wektory(x, x_stare)
            norma_roznicy = norma_max(roznica)
            norma_biezaca = norma_max(x)
```

na:

```python
 x[i] = (b[i] - suma1 - suma2) / A[i][i]

        roznica = odejmij_wektory(x, x_stare)
        norma_roznicy = norma_max(roznica)

        print(f"\nIteracja {krok}:")
        wypisz_wektor(x)
        print("Norma maksimum różnicy:", norma_roznicy)

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x, krok

        elif warunek_stopu == "roznica":
            norma_biezaca = norma_max(x)

            if norma_biezaca == 0:
                if norma_roznicy <= epsilon:
```

---

# Zadanie 3

**Sprawdź zbieżność układu pod kątem metod z zadania 1 oraz 2.**

Układ do testowania:

$$
\begin{cases}
4x_1 - 2x_2 = 0, \\
-2x_1 + 5x_2 - x_3 = 2, \\
-x_2 + 4x_3 + 2x_4 = 3, \\
2x_3 + 3x_4 = -2.
\end{cases}
$$

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

## Co sprawdzamy w tym zadaniu?

W zadaniu 1 używaliśmy **metody Jacobiego**, a w zadaniu 2 **metody Gaussa-Seidla**.
Teraz nie liczymy kolejnych iteracji, tylko sprawdzamy, **czy te metody powinny być zbieżne** dla danego układu.

Na slajdach pojawia się ogólna postać metody iteracyjnej:

$$
x^{(k)} = W x^{(k-1)} + Z
$$

Najważniejsze pytanie brzmi:

> czy kolejne iteracje prowadzą do rozwiązania?

Według slajdów zależy to od macierzy iteracji (W).
W praktyce używamy warunku:

$$
||W|| < 1
$$

W tej notatce korzystamy z **normy wierszowej**:

$$
\|W\|_{\infty} = \max_i \sum_{j=1}^{n} |w_{ij}|
$$

Jeżeli:

$$
||W||_\infty < 1
$$

to metoda powinna być zbieżna.

## 1. Metoda Jacobiego

Dla metody Jacobiego macierz iteracji wyznaczamy dokładnie z wzoru ze slajdu:

$$
W_{ij} =
\begin{cases}
0 & \text{gdy } i=j, \\
-\dfrac{a_{ij}}{a_{ii}} & \text{gdy } i \ne j
\end{cases}
$$

Dla naszego układu otrzymujemy:

$$
W_J =
\begin{bmatrix}
0 & \frac12 & 0 & 0 \\
\frac25 & 0 & \frac15 & 0 \\
0 & \frac14 & 0 & -\frac12 \\
0 & 0 & -\frac23 & 0
\end{bmatrix}
$$

Teraz liczymy normę wierszową:

* wiersz 1:
  $$
  0 + \frac12 + 0 + 0 = \frac12
  $$

* wiersz 2:
  $$
  \frac25 + 0 + \frac15 + 0 = \frac35
  $$

* wiersz 3:
  $$
  0 + \frac14 + 0 + \frac12 = \frac34
  $$

* wiersz 4:
  $$
  0 + 0 + \frac23 + 0 = \frac23
  $$

Zatem:

$$
|W_J|_\infty =
\max\left(
\frac12,\frac35,\frac34,\frac23
\right)
=
\frac34
= 0.75
$$

Ponieważ:

$$
||W_J||_\infty < 1
$$

to **metoda Jacobiego jest zbieżna**.

## 2. Metoda Gaussa-Seidla

Dla metody Gaussa-Seidla na slajdach mamy wzór:

$$
(L + D)x^{(k)} = -Ux^{(k-1)} + b
$$

gdzie:

* $L$ — macierz trójkątna dolna,
* $D$ — macierz diagonalna,
* $U$ — macierz trójkątna górna.

Po przekształceniu dostajemy:

$$
x^{(k)} = -(L + D)^{-1}U,x^{(k-1)} + (L + D)^{-1}b
$$

Stąd macierz iteracji dla Gaussa-Seidla ma postać:

$$
W_{GS} = -(L + D)^{-1}U
$$

To jest ważna różnica względem Jacobiego:

* dla Jacobiego mamy prosty wzór element po elemencie,
* dla Gaussa-Seidla trzeba skorzystać z rozkładu macierzy $A$ na części $L$, $D$, $U$.

Dla naszego układu otrzymujemy:

$$
W_{GS} =
\begin{bmatrix}
0 & \frac12 & 0 & 0 \\
0 & \frac15 & \frac15 & 0 \\
0 & \frac1{20} & \frac1{20} & -\frac12 \\
0 & -\frac1{30} & -\frac1{30} & \frac13
\end{bmatrix}
$$

Liczymy normę wierszową:

* wiersz 1:
  $$
  0 + \frac12 + 0 + 0 = \frac12
  $$

* wiersz 2:
  $$
  0 + \frac15 + \frac15 + 0 = \frac25
  $$

* wiersz 3:
  $$
  0 + \frac1{20} + \frac1{20} + \frac12 = \frac35
  $$

* wiersz 4:
  $$
  0 + \frac1{30} + \frac1{30} + \frac13 = \frac25
  $$

Zatem:

$$
|W_{GS}|_\infty =
\max\left(
\frac12,\frac25,\frac35,\frac25
\right)
=
\frac35
= 0.6
$$

Ponieważ:

$$
|W_{GS}|_\infty < 1
$$

to **metoda Gaussa-Seidla jest zbieżna**.

---

## Porównanie obu metod

Otrzymaliśmy:

$$
|W_J|_\infty = 0.75
$$

oraz

$$
|W_{GS}|_\infty = 0.6
$$

Obie metody są zbieżne, ale ponieważ:

$$
0.6 < 0.75
$$

to metoda Gaussa-Seidla powinna zbiegać szybciej niż metoda Jacobiego.
Zgadza się to z wcześniejszymi obserwacjami z zadań 1 i 2.

## Kod

```python
print("--------------------ZADANIE 3--------------------")  # wypisujemy nagłówek zadania 3

def zeros(n, m):  # definiujemy funkcję tworzącą macierz n x m wypełnioną zerami
    macierz = []  # tworzymy pustą listę na całą macierz
    for i in range(n):  # wykonujemy pętlę po wszystkich wierszach
        wiersz = []  # tworzymy pustą listę na jeden wiersz
        for j in range(m):  # wykonujemy pętlę po wszystkich kolumnach
            wiersz.append(0.0)  # dodajemy do wiersza element 0.0
        macierz.append(wiersz)  # dodajemy gotowy wiersz do macierzy
    return macierz  # zwracamy utworzoną macierz zerową

def wypisz_macierz(macierz):  # definiujemy funkcję do wypisywania macierzy
    for wiersz in macierz:  # przechodzimy po wszystkich wierszach macierzy
        print(wiersz)  # wypisujemy bieżący wiersz

def norma_wierszowa_macierzy(macierz):  # definiujemy funkcję liczącą normę wierszową macierzy
    maksimum = 0.0  # ustawiamy początkowe maksimum na 0
    for i in range(len(macierz)):  # przechodzimy po wszystkich wierszach macierzy
        suma = 0.0  # zerujemy sumę modułów elementów w bieżącym wierszu
        for j in range(len(macierz[i])):  # przechodzimy po wszystkich elementach bieżącego wiersza
            suma += abs(macierz[i][j])  # dodajemy moduł bieżącego elementu do sumy
        if suma > maksimum:  # sprawdzamy, czy suma z tego wiersza jest większa od dotychczasowego maksimum
            maksimum = suma  # aktualizujemy maksimum
    return maksimum  # zwracamy największą sumę modułów z wierszy

def macierz_iteracji_jacobiego(A):  # definiujemy funkcję wyznaczającą macierz iteracji metody Jacobiego
    n = len(A)  # zapisujemy rozmiar macierzy A
    W = zeros(n, n)  # tworzymy pustą macierz iteracji W o rozmiarze n x n

    for i in range(n):  # przechodzimy po wszystkich wierszach macierzy
        for j in range(n):  # przechodzimy po wszystkich kolumnach macierzy
            if i == j:  # sprawdzamy, czy jesteśmy na przekątnej
                W[i][j] = 0.0  # na przekątnej wpisujemy 0 zgodnie ze wzorem dla Jacobiego
            else:  # w przeciwnym wypadku jesteśmy poza przekątną
                W[i][j] = -A[i][j] / A[i][i]  # wpisujemy wartość -a_ij / a_ii zgodnie ze wzorem ze slajdu

    return W  # zwracamy macierz iteracji Jacobiego

def rozwiaz_uklad_dolnotrojkatny(LD, b):  # definiujemy funkcję rozwiązującą układ dolnotrójkątny LDx=b
    n = len(LD)  # zapisujemy rozmiar macierzy
    x = [0.0] * n  # tworzymy wektor rozwiązania wypełniony zerami

    for i in range(n):  # przechodzimy po kolejnych równaniach od góry do dołu
        suma = 0.0  # zerujemy sumę znanych składników
        for j in range(i):  # przechodzimy po wcześniej obliczonych elementach rozwiązania
            suma += LD[i][j] * x[j]  # dodajemy składniki z już wyznaczonych wartości
        x[i] = (b[i] - suma) / LD[i][i]  # obliczamy bieżący element rozwiązania przez podstawianie w przód

    return x  # zwracamy wyznaczony wektor rozwiązania

def macierz_iteracji_gaussa_seidla(A):  # definiujemy funkcję wyznaczającą macierz iteracji metody Gaussa-Seidla
    n = len(A)  # zapisujemy rozmiar macierzy A

    LD = zeros(n, n)  # tworzymy pustą macierz dla części L + D
    U = zeros(n, n)  # tworzymy pustą macierz dla części U

    for i in range(n):  # przechodzimy po wszystkich wierszach macierzy A
        for j in range(n):  # przechodzimy po wszystkich kolumnach macierzy A
            if j <= i:  # sprawdzamy, czy element należy do dolnej części wraz z przekątną
                LD[i][j] = A[i][j]  # przepisujemy element do macierzy LD
            else:  # w przeciwnym wypadku element należy do części górnej
                U[i][j] = A[i][j]  # przepisujemy element do macierzy U

    W = zeros(n, n)  # tworzymy pustą macierz iteracji Gaussa-Seidla

    for kolumna in range(n):  # przechodzimy po kolejnych kolumnach macierzy W
        prawa_strona = []  # tworzymy pustą listę na prawą stronę układu pomocniczego
        for i in range(n):  # przechodzimy po wszystkich wierszach
            prawa_strona.append(-U[i][kolumna])  # budujemy prawą stronę jako przeciwną kolumnę macierzy U

        rozwiazanie = rozwiaz_uklad_dolnotrojkatny(LD, prawa_strona)  # rozwiązujemy układ (L+D)x = -u_k dla bieżącej kolumny

        for i in range(n):  # przechodzimy po wszystkich wierszach rozwiązania
            W[i][kolumna] = rozwiazanie[i]  # wpisujemy obliczoną kolumnę do macierzy iteracji W

    return W  # zwracamy macierz iteracji Gaussa-Seidla

A = [  # definiujemy macierz współczynników układu
    [4.0, -2.0, 0.0, 0.0],  # pierwszy wiersz macierzy A
    [-2.0, 5.0, -1.0, 0.0],  # drugi wiersz macierzy A
    [0.0, -1.0, 4.0, 2.0],  # trzeci wiersz macierzy A
    [0.0, 0.0, 2.0, 3.0]  # czwarty wiersz macierzy A
]

print("\nMacierz A:")  # wypisujemy nagłówek dla macierzy A
wypisz_macierz(A)  # wypisujemy macierz A

print("\n-------------------- METODA JACOBIEGO --------------------")  # wypisujemy nagłówek sekcji dla metody Jacobiego
WJ = macierz_iteracji_jacobiego(A)  # wyznaczamy macierz iteracji Jacobiego
print("Macierz iteracyjna W_J:")  # wypisujemy nagłówek dla macierzy W_J
wypisz_macierz(WJ)  # wypisujemy macierz iteracji Jacobiego

norma_WJ = norma_wierszowa_macierzy(WJ)  # obliczamy normę wierszową macierzy iteracji Jacobiego
print("Norma wierszowa ||W_J|| =", norma_WJ)  # wypisujemy wartość normy macierzy W_J

if norma_WJ < 1:  # sprawdzamy warunek zbieżności dla Jacobiego
    print("Metoda Jacobiego jest zbieżna, ponieważ ||W_J|| < 1.")  # wypisujemy pozytywny wniosek
else:  # w przeciwnym przypadku
    print("Metoda Jacobiego może nie być zbieżna, ponieważ ||W_J|| >= 1.")  # wypisujemy negatywny wniosek

print("\n-------------------- METODA GAUSSA-SEIDLA --------------------")  # wypisujemy nagłówek sekcji dla metody Gaussa-Seidla
WGS = macierz_iteracji_gaussa_seidla(A)  # wyznaczamy macierz iteracji Gaussa-Seidla
print("Macierz iteracyjna W_GS:")  # wypisujemy nagłówek dla macierzy W_GS
wypisz_macierz(WGS)  # wypisujemy macierz iteracji Gaussa-Seidla

norma_WGS = norma_wierszowa_macierzy(WGS)  # obliczamy normę wierszową macierzy iteracji Gaussa-Seidla
print("Norma wierszowa ||W_GS|| =", norma_WGS)  # wypisujemy wartość normy macierzy W_GS

if norma_WGS < 1:  # sprawdzamy warunek zbieżności dla Gaussa-Seidla
    print("Metoda Gaussa-Seidla jest zbieżna, ponieważ ||W_GS|| < 1.")  # wypisujemy pozytywny wniosek
else:  # w przeciwnym przypadku
    print("Metoda Gaussa-Seidla może nie być zbieżna, ponieważ ||W_GS|| >= 1.")  # wypisujemy negatywny wniosek

print("\n-------------------- WNIOSEK KOŃCOWY --------------------")  # wypisujemy nagłówek końcowego wniosku
print("Zbieżność metod z zadania 1 i 2 badamy przez normę macierzy iteracji.")  # wypisujemy ogólną informację o sposobie badania zbieżności
print("Dla Jacobiego sprawdzamy macierz W_J.")  # wypisujemy informację dotyczącą metody Jacobiego
print("Dla Gaussa-Seidla sprawdzamy macierz W_GS.")  # wypisujemy informację dotyczącą metody Gaussa-Seidla
print("Jeżeli ||W|| < 1, to metoda jest zbieżna.")  # wypisujemy końcowe kryterium zbieżności
```

---

## Wnioski

W zadaniu 3 zbieżność badamy zgodnie ze slajdami przez macierz iteracji (W) i warunek:

$$
|W| < 1
$$

Dla badanego układu:

* dla metody Jacobiego:
  $$
  |W_J|_\infty = 0.75 < 1
  $$

* dla metody Gaussa-Seidla:
  $$
  |W_{GS}|_\infty = 0.6 < 1
  $$

Oznacza to, że:

* metoda Jacobiego jest zbieżna,
* metoda Gaussa-Seidla jest zbieżna,
* metoda Gaussa-Seidla powinna zbiegać szybciej niż metoda Jacobiego.

---

# Lab 7

# Zadanie 1

**Napisz program implementujący metodę bisekcji. Program przetestuj dla
następujących funkcji:**

a)
$
f(x) = x^2 - 4, x \in <0; 2.2>
$

b)
$
f(x) = \sin x - \frac{1}{2}, x \in <0; 2.2>
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
    if f(b) * f(a) >= 0:  # sprawdzamy, czy na końcach przedziału nie ma takiego samego znaku
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

![alt text](zdjecia/1.png)

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

# Zadanie 2

**Napisz program implementujący metodę Newtona (czyli metodę stycznych). Program przetestuj dla funkcji z zadania 1.**

Rozważane funkcje:

a)
$$
f(x)=x^2-4,\quad x\in<0,2.2>
$$

b)
$$
f(x)=\sin x-\frac12,\quad x\in<0,2.2>
$$

![alt text](zdjecia/2.png)

## Co to jest metoda Newtona?

Metoda stycznych, nazywana też metodą Newtona, służy do przybliżonego wyznaczania miejsca zerowego funkcji $f(x)$, czyli rozwiązania równania:

$$
f(x)=0
$$

Metoda polega na konstruowaniu kolejnych punktów będących miejscami zerowymi stycznych do wykresu funkcji.

Na slajdach wzór iteracyjny zapisano jako:

$$
x_i=x_{i-1}-\frac{f(x_{i-1})}{f'(x_{i-1})},
\qquad i=2,3,4,\dots
$$

Oznacza to, że mając poprzednie przybliżenie $x_{i-1}$, obliczamy nowe przybliżenie $x_i$ korzystając z wartości funkcji i jej pochodnej w punkcie $x_{i-1}$.

## Jak rozumieć wzór metody Newtona?

W każdym kroku obliczamy poprawkę:

$$
h=\frac{f(x)}{f'(x)}
$$

a następnie nowe przybliżenie:

$$
x=x-h
$$

Jeżeli punkt $x$ jest blisko rzeczywistego pierwiastka, to metoda zwykle bardzo szybko poprawia wynik.

## Wybór przedziału startowego

Zgodnie z tablicą najpierw wybieramy przedział:

$$
[a,b]
$$

taki, że:

$$
f(a)\cdot f(b)<0
$$

To oznacza, że na końcach przedziału funkcja ma przeciwne znaki, więc w przedziale znajduje się miejsce zerowe.

## Wybór pierwszego przybliżenia

Na slajdach podano, że pierwsze przybliżenie $x_1$ często wybieramy z końców przedziału $[a,b]$. Kryterium wyboru zależy od znaku iloczynu:

$$
f'(x)\cdot f''(x)
$$

Dla $x\in[a,b]$:

- jeżeli
  $$
  f'(x)\cdot f''(x)<0
  $$
  to wybieramy:
  $$
  x_1=a
  $$

- jeżeli
  $$
  f'(x)\cdot f''(x)>0
  $$
  to wybieramy:
  $$
  x_1=b
  $$

Na tablicy do praktycznego sprawdzenia tego warunku przyjęto punkt:

$$
c=\frac{a+b}{2}
$$

i badano znak iloczynu:

$$
f'(c)\cdot f''(c)
$$

W programie zastosowano właśnie ten sposób.

## Kolejne iteracje

Po wybraniu punktu startowego obliczamy kolejne kroki metodą:

$$
h=\frac{f(x)}{f'(x)}
$$

$$
x=x-h
$$

Jest to ta sama metoda co wzór ze slajdów:

$$
x_i=x_{i-1}-\frac{f(x_{i-1})}{f'(x_{i-1})}
$$

tylko zapisana w wygodniejszej postaci programistycznej.

## Oszacowanie błędu

Na slajdach zapisano, że błąd przybliżenia można oszacować przez różnicę kolejnych przybliżeń:

$$
\Delta \approx |x_i-x_{i-1}|
$$

W programie ta różnica jest reprezentowana przez wartość:

$$
|h|
$$

ponieważ:

$$
x_i=x_{i-1}-h
$$

czyli:

$$
|x_i-x_{i-1}|=|h|
$$

## Warunek zakończenia obliczeń

Na slajdach podano warunek stopu:

$$
|x_i-x_{i-1}|<\varepsilon
$$

W programie sprawdzamy równoważnie:

$$
|h|<\varepsilon
$$

Obliczenia przerywamy również wtedy, gdy liczba iteracji przekroczy zadany limit.

## Potencjalne problemy

Na slajdach oraz tablicy zaznaczono, że problem pojawia się wtedy, gdy:

$$
f'(x)=0
$$

Wtedy nie można wykonać kroku Newtona, ponieważ wystąpiłoby dzielenie przez zero:

$$
\frac{f(x)}{f'(x)}
$$

Dlatego program sprawdza ten przypadek i zgłasza błąd.

Dodatkowo metoda może być rozbieżna, jeśli punkt startowy jest źle dobrany lub funkcja nie jest dostatecznie „gładka” w otoczeniu pierwiastka.

## Pochodne dla funkcji z zadania

### a) Funkcja
$$
f(x)=x^2-4
$$

Pochodna pierwsza:

$$
f'(x)=2x
$$

Pochodna druga:

$$
f''(x)=2
$$

### b) Funkcja
$$
f(x)=\sin x-\frac12
$$

Pochodna pierwsza:

$$
f'(x)=\cos x
$$

Pochodna druga:

$$
f''(x)=-\sin x
$$

## Kod

```python
import math  # importujemy moduł math, ponieważ będzie potrzebny do funkcji trygonometrycznych

def newton(f, a, b, df, ddf, max_iter=100, epsilon=1e-3):  # definiujemy funkcję realizującą metodę Newtona
    lista_iteracji = []  # tworzymy pustą listę, w której będziemy zapisywać kolejne iteracje

    if f(a) * f(b) >= 0:  # sprawdzamy warunek z tablicy, że na krańcach przedziału funkcja ma mieć przeciwne znaki
        raise ValueError("Na krańcach przedziału funkcja musi mieć przeciwne znaki.")  # jeśli warunek nie jest spełniony, zgłaszamy błąd
    
    c = (a+b) / 2.0  # obliczamy środek przedziału zgodnie z pomysłem z tablicy
    iloczyn_pochodnych = df(c) * ddf(c)  # obliczamy iloczyn pochodnej pierwszej i drugiej w punkcie c

    x = 0.0  # tworzymy zmienną na punkt startowy

    if iloczyn_pochodnych < 0:  # sprawdzamy pierwszy przypadek ze slajdu
        x = a  # jeśli iloczyn jest ujemny, wybieramy lewy koniec przedziału jako pierwsze przybliżenie
    elif iloczyn_pochodnych > 0:  # sprawdzamy drugi przypadek ze slajdu
        x = b  # jeśli iloczyn jest dodatni, wybieramy prawy koniec przedziału jako pierwsze przybliżenie
    else:  # obsługujemy przypadek, w którym iloczyn pochodnych jest równy zero
        raise ValueError("Nie można jednoznacznie wybrać punktu startowego, bo f'(c) * f''(c) = 0.")  # zgłaszamy błąd, bo reguła wyboru nie rozstrzyga

    punkt_startowy = x  # zapamiętujemy wybrany punkt startowy do późniejszego wypisania

    for i in range(1, max_iter+1):  # wykonujemy kolejne iteracje od 1 do ustalonego limitu
        fx = f(x)  # obliczamy wartość funkcji w aktualnym punkcie
        dfx = df(x)  # obliczamy wartość pochodnej pierwszej w aktualnym punkcie

        if dfx == 0:  # sprawdzamy przypadek problematyczny zaznaczony na tablicy i slajdach
            raise ValueError("Pochodna f'(x) = 0, metoda Newtona nie może wykonać kolejnego kroku.")  # jeśli pochodna jest zerowa, nie da się obliczyć następnego kroku
        
        h = fx / dfx  # obliczamy poprawkę h zgodnie ze wzorem z tablicy
        x_nowe = x - h  # obliczamy nowe przybliżenie według wzoru Newtona

        lista_iteracji.append([i, x, fx, dfx, h, x_nowe])  # zapisujemy bieżącą iterację do historii

        if abs(h) < epsilon:  # sprawdzamy warunek stopu zgodny ze slajdem |x_i - x_{i-1}| < epsilon
            return punkt_startowy, x_nowe, lista_iteracji  # jeśli poprawka jest wystarczająco mała, kończymy obliczenia i zwracamy wynik
        
        x = x_nowe  # aktualizujemy punkt, żeby przejść do następnej iteracji

    return punkt_startowy, x, lista_iteracji  # jeśli osiągnięto limit iteracji, zwracamy ostatnie przybliżenie i historię

def wypisz_historie(historia):  # definiujemy funkcję wypisującą zapisane iteracje
    print("i        x               f(x)            f'(x)            h               x_nowe")  # wypisujemy nagłówek tabeli
    for krok in historia:  # przechodzimy po wszystkich iteracjach zapisanych w historii
        print(  # wypisujemy jeden wiersz tabeli
            f"{krok[0]:<2} "  # wypisujemy numer iteracji
            f"{krok[1]:>14.10f} "  # wypisujemy aktualne przybliżenie x
            f"{krok[2]:>14.10f} "  # wypisujemy wartość funkcji f(x)
            f"{krok[3]:>14.10f} "  # wypisujemy wartość pochodnej f'(x)
            f"{krok[4]:>14.10f} "  # wypisujemy poprawkę h
            f"{krok[5]:>14.10f}"  # wypisujemy nowe przybliżenie x_nowe
        )  # kończymy wypisywanie jednego wiersza

def f1(x):  # definiujemy funkcję z punktu a)
    return x**2 - 4  # zwracamy wartość funkcji x^2 - 4

def df1(x):  # definiujemy pochodną pierwszą funkcji z punktu a)
    return 2*x  # zwracamy wartość pochodnej 2x

def ddf1(x):  # definiujemy pochodną drugą funkcji z punktu a)
    return 2  # zwracamy wartość pochodnej drugiej równej 2

def f2(x):  # definiujemy funkcję z punktu b)
    return math.sin(x) - 0.5  # zwracamy wartość funkcji sin(x) - 1/2

def df2(x):  # definiujemy pochodną pierwszą funkcji z punktu b)
    return math.cos(x)  # zwracamy wartość pochodnej cos(x)

def ddf2(x):  # definiujemy pochodną drugą funkcji z punktu b)
    return -math.sin(x)  # zwracamy wartość pochodnej drugiej -sin(x)

print("-------------------- ZADANIE 2 --------------------")  # wypisujemy nagłówek zadania

print("\n==================== FUNKCJA a) ====================")  # wypisujemy nagłówek dla funkcji a)
print("f(x) = x^2 - 4, przedział [0, 2.2]")  # wypisujemy opis funkcji a) i przedziału

punkt_startowy_a, wynik_a, historia_a = newton(f1, 0.0, 2.2, df1, ddf1, max_iter=100, epsilon=1e-3)  # uruchamiamy metodę Newtona dla funkcji a)
print("Punkt startowy x0 =", punkt_startowy_a)  # wypisujemy wybrany punkt startowy
wypisz_historie(historia_a)  # wypisujemy pełną historię iteracji
print("Przybliżony pierwiastek:", wynik_a)  # wypisujemy końcowe przybliżenie pierwiastka
print("f(x) =", f1(wynik_a))  # wypisujemy wartość funkcji w znalezionym punkcie
print("Liczba iteracji:", len(historia_a))  # wypisujemy liczbę wykonanych iteracji

print("\n==================== FUNKCJA b) ====================")  # wypisujemy nagłówek dla funkcji b)
print("f(x) = sin(x) - 1/2, przedział [0, 2.2]")  # wypisujemy opis funkcji b) i przedziału

punkt_startowy_b, wynik_b, historia_b = newton(f2, 0.0, 2.2, df2, ddf2, max_iter=100, epsilon=1e-3)  # uruchamiamy metodę Newtona dla funkcji b)
print("Punkt startowy x0 =", punkt_startowy_b)  # wypisujemy wybrany punkt startowy
wypisz_historie(historia_b)  # wypisujemy pełną historię iteracji
print("Przybliżony pierwiastek:", wynik_b)  # wypisujemy końcowe przybliżenie pierwiastka
print("f(x) =", f2(wynik_b))  # wypisujemy wartość funkcji w znalezionym punkcie
print("Liczba iteracji:", len(historia_b))  # wypisujemy liczbę wykonanych iteracji
```

---

## Wnioski

Metoda Newtona wykorzystuje styczne do wykresu funkcji do budowy kolejnych przybliżeń pierwiastka równania \(f(x)=0\). Jej wzór iteracyjny ma postać:

$$
x_i=x_{i-1}-\frac{f(x_{i-1})}{f'(x_{i-1})}
$$

W zadaniu punkt startowy wybierany jest na podstawie znaku iloczynu:

$$
f'(c)\cdot f''(c)
$$

gdzie:

$$
c=\frac{a+b}{2}
$$

Następnie w każdej iteracji obliczana jest poprawka:

$$
h=\frac{f(x)}{f'(x)}
$$

i nowe przybliżenie:

$$
x=x-h
$$

Warunek zakończenia obliczeń oparto na slajdzie:

$$
|x_i-x_{i-1}|<\varepsilon
$$

czyli w programie równoważnie:

$$
|h|<\varepsilon
$$

Dla funkcji:

$$
f(x)=x^2-4
$$

metoda prowadzi do pierwiastka bliskiego wartości:

$$
x=2
$$

Dla funkcji:

$$
f(x)=\sin x-\frac12
$$

metoda prowadzi do pierwiastka bliskiego wartości:

$$
x\approx 0.5236
$$

czyli:

$$
x=\frac{\pi}{6}
$$

Oznacza to, że program działa poprawnie i realizuje metodę Newtona zgodnie z algorytmem przedstawionym na tablicy oraz slajdach.

---

# Zadanie 3

**Napisz program implementujący metodę siecznych. Program przetestuj dla funkcji z zadania 1.**

Rozważane funkcje:

a)
$$
f(x)=x^2-4,\quad x\in<0,2.2>
$$

b)
$$
f(x)=\sin x-\frac12,\quad x\in<0,2.2>
$$

![alt text](zdjecia/3.jpg)

## Co to jest metoda siecznych?

Metoda siecznych służy do przybliżania miejsca zerowego równania:

$$
f(x)=0
$$

W metodzie tej zamiast stycznej, jak w metodzie Newtona, wykorzystuje się **sieczną** przechodzącą przez dwa kolejne punkty wykresu funkcji:

$$
(x_i,f(x_i)) \quad \text{oraz} \quad (x_{i-1},f(x_{i-1}))
$$

Punkt przecięcia tej siecznej z osią $x$ daje kolejne przybliżenie pierwiastka.

Na slajdach wzór metody zapisano jako:

$$
x_{i+1}=x_i-f(x_i)\cdot \frac{x_i-x_{i-1}}{f(x_i)-f(x_{i-1})},
\qquad i=2,3,4,\dots
$$

## Interpretacja wzoru

W każdym kroku korzystamy z dwóch ostatnich przybliżeń:
- $x_{i-1}$,
- $x_i$,

i na ich podstawie wyznaczamy nowe przybliżenie $x_{i+1}$.

Metoda nie wymaga liczenia pochodnej funkcji, co jest jej dużą zaletą.

## Wybór przedziału i punktów startowych

Na tablicy podano, że najpierw wybieramy przedział:

$$
[a,b]
$$

taki, że:

$$
f(a)\cdot f(b)<0
$$

Następnie wybieramy punkty startowe $x_0$ i $x_1$.

Do ich wyboru wykorzystujemy, podobnie jak w metodzie Newtona, znak iloczynu:

$$
f'(c)\cdot f''(c)
$$

gdzie:

$$
c=\frac{a+b}{2}
$$

Zgodnie z tablicą:

- jeżeli
  $$
  f'(c)\cdot f''(c)<0
  $$
  to przyjmujemy:
  $$
  x_0=a,\quad x_1=b
  $$

- jeżeli
  $$
  f'(c)\cdot f''(c)>0
  $$
  to przyjmujemy:
  $$
  x_0=b,\quad x_1=a
  $$

## Kolejne iteracje

Po wybraniu punktów startowych liczymy kolejne przybliżenia ze wzoru:

$$
x_{i+1}=x_i-f(x_i)\cdot \frac{x_i-x_{i-1}}{f(x_i)-f(x_{i-1})}
$$

Następnie przesuwamy punkty:
- stare $x_i$ staje się nowym $x_{i-1}$,
- nowe $x_{i+1}$ staje się nowym $x_i$.

## Oszacowanie błędu

Na slajdach błąd przybliżenia oszacowano wzorem:

$$
\Delta \approx |x_{i+1}-x_i|
$$

W programie właśnie ta różnica jest używana jako miara dokładności.

## Warunek stopu

Na tablicy zapisano, że obliczenia kończymy, gdy:

$$
|x_1-x_0|<\varepsilon
$$

W praktyce w kolejnych iteracjach sprawdzamy równoważnie:

$$
|x_{i+1}-x_i|<\varepsilon
$$

czyli różnicę między nowym a poprzednim przybliżeniem.

Drugim warunkiem zakończenia jest przekroczenie maksymalnej liczby iteracji.

## Potencjalne problemy

Na slajdach podano, że metoda siecznych:
- nie wymaga pochodnej do wyznaczania kolejnych przybliżeń,
- może nie być zbieżna dla niektórych wyborów punktów startowych,
- zwykle wymaga więcej iteracji niż metoda Newtona,
- nie pilnuje przedziału tak jak metoda bisekcji, więc może wyjść poza zadany przedział.

Dlatego dobór punktów startowych ma duże znaczenie.

W tym zadaniu punkty startowe są wybierane automatycznie na podstawie znaku iloczynu:

$$
f'(c)\cdot f''(c),
\qquad c=\frac{a+b}{2}
$$

Trzeba jednak pamiętać, że nawet jeśli początkowo wybieramy punkty z przedziału \([a,b]\), to kolejne przybliżenia metody siecznych nie muszą już pozostać w tym przedziale.

## Pochodne potrzebne do wyboru punktów startowych

Mimo że sama metoda siecznych nie używa pochodnych do liczenia kolejnych iteracji, w tym zadaniu są one potrzebne do wyboru punktów startowych zgodnie z tablicą.

### a) Funkcja
$$
f(x)=x^2-4
$$

Pochodna pierwsza:

$$
f'(x)=2x
$$

Pochodna druga:

$$
f''(x)=2
$$

### b) Funkcja
$$
f(x)=\sin x-\frac12
$$

Pochodna pierwsza:

$$
f'(x)=\cos x
$$

Pochodna druga:

$$
f''(x)=-\sin x
$$

## Kod

```python
import math  # importujemy moduł math, ponieważ będzie potrzebny do funkcji trygonometrycznych

def sieczne(f, a, b, df, ddf, max_iter=100, epsilon=1e-3):  # definiujemy funkcję realizującą metodę siecznych
    lista_iteracji = []  # tworzymy pustą listę, w której będziemy zapisywać kolejne iteracje metody

    if f(a) * f(b) >= 0:  # sprawdzamy, czy na krańcach przedziału funkcja ma przeciwne znaki
        raise ValueError("Na krańcach przedziału funkcja musi mieć przeciwne znaki.")  # jeśli nie, zgłaszamy błąd
    
    c = (a+b) / 2.0  # obliczamy środek przedziału [a,b]
    iloczyn_pochodnych = df(c) * ddf(c)  # obliczamy iloczyn pochodnej pierwszej i drugiej w punkcie c

    if iloczyn_pochodnych < 0:  # sprawdzamy pierwszy przypadek wyboru punktów startowych z tablicy
        x0 = a  # jeśli iloczyn jest ujemny, pierwszy punkt startowy ustawiamy jako a
        x1 = b  # jeśli iloczyn jest ujemny, drugi punkt startowy ustawiamy jako b
    elif iloczyn_pochodnych > 0:  # sprawdzamy drugi przypadek wyboru punktów startowych z tablicy
        x0 = b  # jeśli iloczyn jest dodatni, pierwszy punkt startowy ustawiamy jako b
        x1 = a  # jeśli iloczyn jest dodatni, drugi punkt startowy ustawiamy jako a
    else:  # obsługujemy przypadek, gdy iloczyn pochodnych jest równy zero
        raise ValueError("Nie można jednoznacznie wybrać punktu startowego, bo f'(c) * f''(c) = 0.")  # zgłaszamy błąd

    x0_startowy = x0  # zapamiętujemy początkową wartość x0 do późniejszego wypisania
    x1_startowy = x1  # zapamiętujemy początkową wartość x1 do późniejszego wypisania

    for i in range(1, max_iter+1):  # wykonujemy kolejne iteracje od 1 do maksymalnej liczby iteracji
        fx0 = f(x0)  # obliczamy wartość funkcji w punkcie x0
        fx1 = f(x1)  # obliczamy wartość funkcji w punkcie x1

        if fx1 - fx0 == 0:  # sprawdzamy, czy mianownik we wzorze metody siecznych nie jest równy zero
            raise ValueError("Mianownik jest równy zero, metoda siecznych nie może wykonać kolejnego kroku.")  # jeśli jest, zgłaszamy błąd
        
        x_nowe = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))  # obliczamy nowe przybliżenie według wzoru metody siecznych

        lista_iteracji.append([i, x0, x1, fx0, fx1, x_nowe])  # zapisujemy dane z bieżącej iteracji do listy historii

        if abs(x_nowe - x1) < epsilon:  # sprawdzamy warunek stopu oparty na różnicy kolejnych przybliżeń
            return x0_startowy, x1_startowy, x0, x1, lista_iteracji  # jeśli warunek jest spełniony, kończymy i zwracamy wyniki
        
        x0 = x1  # przesuwamy punkt x0, ustawiając go na poprzednie x1
        x1 = x_nowe  # przesuwamy punkt x1, ustawiając go na nowe przybliżenie

    return x0_startowy, x1_startowy, x0, x1, lista_iteracji  # jeśli osiągnięto limit iteracji, zwracamy ostatnie wyniki

def wypisz_historie(historia):  # definiujemy funkcję do wypisywania historii iteracji
    print("i        x0              x1              f(x0)           f(x1)           x_nowe")  # wypisujemy nagłówek tabeli
    for krok in historia:  # przechodzimy po wszystkich zapisanych iteracjach
        print(  # wypisujemy jeden wiersz tabeli
            f"{krok[0]:<2} "  # wypisujemy numer iteracji
            f"{krok[1]:>14.10f} "  # wypisujemy wartość x0
            f"{krok[2]:>14.10f} "  # wypisujemy wartość x1
            f"{krok[3]:>14.10f} "  # wypisujemy wartość f(x0)
            f"{krok[4]:>14.10f} "  # wypisujemy wartość f(x1)
            f"{krok[5]:>14.10f}"  # wypisujemy nowe przybliżenie x_nowe
        )  # kończymy wypisywanie pojedynczego wiersza

def f1(x):  # definiujemy pierwszą funkcję testową
    return x**2 - 4  # zwracamy wartość funkcji x^2 - 4

def df1(x):  # definiujemy pochodną pierwszą funkcji f1
    return 2*x  # zwracamy wartość pochodnej 2x

def ddf1(x):  # definiujemy pochodną drugą funkcji f1
    return 2  # zwracamy wartość pochodnej drugiej równej 2

def f2(x):  # definiujemy drugą funkcję testową
    return math.sin(x) - 0.5  # zwracamy wartość funkcji sin(x) - 1/2

def df2(x):  # definiujemy pochodną pierwszą funkcji f2
    return math.cos(x)  # zwracamy wartość pochodnej cos(x)

def ddf2(x):  # definiujemy pochodną drugą funkcji f2
    return -math.sin(x)  # zwracamy wartość pochodnej drugiej -sin(x)

print("-------------------- ZADANIE 3 --------------------")  # wypisujemy nagłówek zadania

print("\n==================== FUNKCJA a) ====================")  # wypisujemy nagłówek dla funkcji a)
print("f(x) = x^2 - 4, przedział [0, 2.2]")  # wypisujemy opis pierwszej funkcji i jej przedziału

x0a, x1a, wynik0_a, wynik1_a, historia_a = sieczne(f1, 0.0, 2.2, df1, ddf1, max_iter=100, epsilon=1e-3)  # uruchamiamy metodę siecznych dla funkcji a)
print("Punkty startowe: x0 =", x0a, ", x1 =", x1a)  # wypisujemy wybrane punkty startowe
wypisz_historie(historia_a)  # wypisujemy historię iteracji dla funkcji a)
print("Ostatnie przybliżenia:", wynik0_a, wynik1_a)  # wypisujemy dwa ostatnie przybliżenia
print("Przybliżony pierwiastek:", wynik1_a)  # wypisujemy końcowe przybliżenie miejsca zerowego
print("f(x) =", f1(wynik1_a))  # wypisujemy wartość funkcji w znalezionym punkcie
print("Liczba iteracji:", len(historia_a))  # wypisujemy liczbę wykonanych iteracji

print("\n==================== FUNKCJA b) ====================")  # wypisujemy nagłówek dla funkcji b)
print("f(x) = sin(x) - 1/2, przedział [0, 2.2]")  # wypisujemy opis drugiej funkcji i jej przedziału

x0b, x1b, wynik0_b, wynik1_b, historia_b = sieczne(f2, 0.0, 2.2, df2, ddf2, max_iter=100, epsilon=1e-3)  # uruchamiamy metodę siecznych dla funkcji b)
print("Punkty startowe: x0 =", x0b, ", x1 =", x1b)  # wypisujemy wybrane punkty startowe
wypisz_historie(historia_b)  # wypisujemy historię iteracji dla funkcji b)
print("Ostatnie przybliżenia:", wynik0_b, wynik1_b)  # wypisujemy dwa ostatnie przybliżenia
print("Przybliżony pierwiastek:", wynik1_b)  # wypisujemy końcowe przybliżenie miejsca zerowego
print("f(x) =", f2(wynik1_b))  # wypisujemy wartość funkcji w znalezionym punkcie
print("Liczba iteracji:", len(historia_b))  # wypisujemy liczbę wykonanych iteracji
```

## Wnioski

Metoda siecznych wykorzystuje dwa kolejne przybliżenia pierwiastka i na ich podstawie wyznacza następne przybliżenie, korzystając z równania siecznej przechodzącej przez punkty wykresu funkcji.

Jej wzór iteracyjny ma postać:

$$
x_{i+1}=x_i-f(x_i)\cdot \frac{x_i-x_{i-1}}{f(x_i)-f(x_{i-1})}
$$

W zadaniu punkty startowe dla funkcji a) dobrano zgodnie z tablicą, wykorzystując znak iloczynu:

$$
f'(c)\cdot f''(c)
$$

gdzie:

$$
c=\frac{a+b}{2}
$$

Błąd przybliżenia szacujemy wzorem ze slajdów:

$$
\Delta \approx |x_{i+1}-x_i|
$$

Dla funkcji:

$$
f(x)=x^2-4
$$

metoda prowadzi do pierwiastka bliskiego wartości:

$$
x=2
$$

Dla funkcji:

$$
f(x)=\sin x-\frac12
$$

metoda przy punktach startowych wybranych automatycznie z przedziału $[0,2.2]$ może wyjść poza ten przedział. W takim przypadku otrzymane przybliżenia mogą zbiegać do innego miejsca zerowego funkcji niż to, które leży w badanym przedziale.

Oznacza to, że metoda siecznych realizuje poprawnie wzór iteracyjny i może być zbieżna, ale nie zachowuje własności izolacji pierwiastka tak jak metoda bisekcji. Dlatego przy interpretacji wyników trzeba uwzględniać, że otrzymane przybliżenie nie musi należeć do początkowego przedziału $[a,b]$.

---

# Lab 8

# Zadanie 1

**Napisz program implementujący rozwinięcie funkcji eksponencjalnej w szereg Maclaurina. Porównaj wyniki oraz czas wykonania z funkcją biblioteczną.**

## Co to jest szereg Maclaurina dla funkcji eksponencjalnej?

Funkcja eksponencjalna ma rozwinięcie w szereg Maclaurina:

$$
e^x=\sum_{k=0}^{\infty}\frac{x^k}{k!}
$$

W praktyce w programie nie liczymy nieskończenie wielu składników, tylko bierzemy **sumę skończoną** do pewnego wybranego $n$:

$$
e^x \approx \sum_{k=0}^{n}\frac{x^k}{k!}
$$

Oznacza to, że przybliżamy wartość funkcji $e^x$ przez sumę:

$$
1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\dots+\frac{x^n}{n!}
$$

Im większa wartość $n$, tym zwykle dokładniejsze przybliżenie.

## Jak działa obliczanie kolejnych wyrazów?

Na slajdzie podano ważną wskazówkę, że nie warto w każdej iteracji osobno liczyć:
- potęgi $x^k$,
- silni $k!$.

Zamiast tego korzystamy z zależności:

$$
\frac{x^k}{k!}=\frac{x^{k-1}}{(k-1)!}\cdot\frac{x}{k}
$$

Dzięki temu każdy kolejny wyraz szeregu obliczamy z poprzedniego.

Jeżeli oznaczymy:

$$
\text{wyraz}_{k-1}=\frac{x^{k-1}}{(k-1)!}
$$

to następny wyraz jest równy:

$$
\text{wyraz}_k=\text{wyraz}_{k-1}\cdot\frac{x}{k}
$$

To właśnie realizuje program.

## Dlaczego to jest lepsze?

Takie podejście:
- jest szybsze,
- nie wymaga funkcji `pow()`,
- nie wymaga osobnego liczenia silni,
- jest zgodne z metodą pokazaną na slajdzie.

## Porównanie z funkcją biblioteczną

W zadaniu trzeba porównać wynik z funkcją biblioteczną.  
W Pythonie używamy do tego:

```python
math.exp(x)
```

Porównujemy:
- otrzymaną wartość,
- błąd bezwzględny,
- czas wykonania.

Błąd bezwzględny liczymy jako:

$$
|\,\text{wynik Maclaurina} - \text{wynik biblioteczny}\,|
$$

## Pomiar czasu

Czas wykonania mierzony jest za pomocą:

```python
time.perf_counter()
```

Aby pomiar był bardziej wiarygodny, obliczenia wykonywane są wiele razy, a następnie mierzony jest łączny czas.

## Kod

```python
import time, math  # importujemy moduły time i math, ponieważ będą potrzebne do pomiaru czasu oraz funkcji bibliotecznej exp

def exp_maclaurin(x, n):  # definiujemy funkcję obliczającą przybliżenie e^x za pomocą szeregu Maclaurina
    suma = 1.0  # ustawiamy początkową sumę równą 1, ponieważ pierwszy wyraz szeregu to x^0 / 0! = 1
    wyraz = 1.0  # ustawiamy pierwszy wyraz szeregu na 1, aby z niego wyznaczać kolejne składniki

    for k in range(1, n+1):  # przechodzimy po kolejnych wyrazach szeregu od 1 do n
        wyraz = wyraz * (x / k)  # obliczamy następny wyraz z poprzedniego według zależności x^k/k! = x^(k-1)/(k-1)! * x/k
        suma += wyraz  # dodajemy nowo obliczony wyraz do sumy

    return suma  # zwracamy końcową wartość przybliżenia szeregu

def porownaj_exp(x, n, liczba_powtorzen=100000):  # definiujemy funkcję porównującą wynik i czas działania z funkcją biblioteczną
    start = time.perf_counter()  # zapisujemy moment rozpoczęcia pomiaru czasu dla metody Maclaurina
    for _ in range(liczba_powtorzen):  # wykonujemy obliczenia wiele razy, aby pomiar czasu był bardziej wiarygodny
        wynik_maclaurin = exp_maclaurin(x, n)  # obliczamy wartość e^x za pomocą własnej funkcji
    czas_maclaurin = time.perf_counter() - start  # obliczamy czas wykonania metody Maclaurina

    start = time.perf_counter()  # zapisujemy moment rozpoczęcia pomiaru czasu dla funkcji bibliotecznej
    for _ in range(liczba_powtorzen):  # wykonujemy funkcję biblioteczną wiele razy
        wynik_biblioteczny = math.exp(x)  # obliczamy wartość e^x za pomocą funkcji bibliotecznej
    czas_biblioteczny = time.perf_counter() - start  # obliczamy czas wykonania funkcji bibliotecznej

    blad = abs(wynik_maclaurin - wynik_biblioteczny)  # liczymy błąd bezwzględny między obiema metodami

    print(f"x = {x}, n = {n}")  # wypisujemy aktualną wartość x oraz liczbę składników użytych w sumie
    print(f"Wynik Maclaurina:   {wynik_maclaurin}")  # wypisujemy wynik uzyskany z szeregu Maclaurina
    print(f"Wynik biblioteczny: {wynik_biblioteczny}")  # wypisujemy wynik uzyskany z funkcji bibliotecznej
    print(f"Błąd bezwzględny:   {blad}")  # wypisujemy obliczony błąd bezwzględny
    print(f"Czas Maclaurina:    {czas_maclaurin:.10f} s")  # wypisujemy czas wykonania metody Maclaurina
    print(f"Czas biblioteczny:  {czas_biblioteczny:.10f} s")  # wypisujemy czas wykonania funkcji bibliotecznej
    print("-" * 50)  # wypisujemy linię oddzielającą kolejne testy

print("-------------------- ZADANIE 1 --------------------")  # wypisujemy nagłówek zadania

porownaj_exp(1.0, 10)  # porównujemy obie metody dla x = 1.0 i n = 10
porownaj_exp(2.0, 15)  # porównujemy obie metody dla x = 2.0 i n = 15
porownaj_exp(-1.0, 15)  # porównujemy obie metody dla x = -1.0 i n = 15
porownaj_exp(5.0, 25)  # porównujemy obie metody dla x = 5.0 i n = 25
```

## Wnioski

Funkcję eksponencjalną można skutecznie aproksymować za pomocą skończonego szeregu Maclaurina:

$$
e^x \approx \sum_{k=0}^{n}\frac{x^k}{k!}
$$

W programie kolejne składniki szeregu obliczane są z poprzednich według zależności:

$$
\frac{x^k}{k!}=\frac{x^{k-1}}{(k-1)!}\cdot\frac{x}{k}
$$

Dzięki temu nie trzeba w każdej iteracji osobno liczyć potęg i silni, co przyspiesza obliczenia.

Porównanie z funkcją biblioteczną `math.exp(x)` pokazuje, że:
- wyniki szeregu Maclaurina są bardzo zbliżone do wartości dokładnych,
- błąd maleje wraz ze wzrostem liczby składników,
- funkcja biblioteczna zwykle działa szybciej, ponieważ jest zoptymalizowana.

Oznacza to, że program poprawnie realizuje rozwinięcie funkcji eksponencjalnej w szereg Maclaurina oraz umożliwia porównanie dokładności i czasu wykonania z funkcją biblioteczną.

## Finalnie masz policzyć dla wybranych wartości (x):

### 1. Przybliżenie funkcji $(e^x)$

czyli:

$
e^x \approx \sum_{k=0}^{n}\frac{x^k}{k!}
$

na przykład dla:

* $x=1$,
* $x=2$,
* $x=-1$,
* $x=5$,

i dla wybranego $n$, np. 10, 15, 25.

### 2. Wartość dokładniejszą z funkcji bibliotecznej

czyli:

$
\texttt{math.exp(x)}
$

### 3. Błąd bezwzględny

czyli różnicę między tym, co policzyła Twoja funkcja, a funkcją biblioteczną:

$
|,\text{wynik Maclaurina} - \text{wynik biblioteczny},|
$

### 4. Czas wykonania obu metod

czyli:

* czas obliczania Twojej funkcji `exp_maclaurin(x, n)`,
* czas obliczania `math.exp(x)`.

## Czyli w tabelce albo w wynikach końcowych masz mieć dla każdego testu:

* wartość $x$,
* liczbę wyrazów $n$,
* wynik z szeregu Maclaurina,
* wynik z funkcji bibliotecznej,
* błąd bezwzględny,
* czas Twojej metody,
* czas funkcji bibliotecznej.

## Najkrócej

Finalnie masz policzyć:

$
\sum_{k=0}^{n}\frac{x^k}{k!}
$

a potem porównać to z:

$
e^x
$

z biblioteki.

---

# Zadanie 2

**Napisz program implementujący rozwinięcie funkcji sinus w szereg Maclaurina. Porównaj wyniki oraz czas wykonania z funkcją biblioteczną.**

## Co mamy policzyć?

Chcemy obliczyć wartość funkcji:

$$
\sin x
$$

nie używając od razu funkcji bibliotecznej `math.sin(x)`, tylko korzystając ze **szeregu Maclaurina**.

Potem mamy porównać:
- wynik otrzymany z naszego programu,
- wynik z funkcji bibliotecznej,
- błąd,
- czas wykonania obu metod.

## Wzór ze slajdu

Na slajdzie funkcja sinus została zapisana tak:

$$
\sin x = \sum_{k=1}^{\infty} (-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}
$$

W praktyce, w programie, nie liczymy nieskończenie wielu składników, tylko bierzemy sumę skończoną do pewnego $n$:

$$
\sin x \approx \sum_{k=1}^{n} (-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}
$$

To oznacza, że liczymy kolejno:

$$
\sin x \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots
$$

## Dlaczego na innych materiałach może być inny wzór?

Czasem ten sam szereg zapisuje się w trochę inny sposób:

$$
\sin x = \sum_{k=0}^{\infty} (-1)^k \frac{x^{2k+1}}{(2k+1)!}
$$

To **nie jest inny szereg**, tylko ten sam zapisany z innym początkiem indeksowania.

### Związek między tymi zapisami

Jeżeli we wzorze ze slajdu mamy:

$$
\sum_{k=1}^{\infty} (-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}
$$

to po zmianie numeracji indeksu dostajemy:

$$
\sum_{k=0}^{\infty} (-1)^k \frac{x^{2k+1}}{(2k+1)!}
$$

Oba wzory opisują dokładnie to samo:

$$
x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots
$$

W tej notatce trzymamy się **wzoru ze slajdu**, czyli sumy od $k=1$ do $n$.

## Łopatologicznie: co robi program?

Program:
1. bierze liczbę $x$,
2. liczy przybliżenie $\sin x$ ze wzoru ze slajdu,
3. porównuje je z `math.sin(x)`,
4. liczy błąd bezwzględny,
5. mierzy czas działania obu metod.

## Jak liczone są kolejne składniki?

Pierwszy składnik szeregu to:

$$
x
$$

czyli dla \(k=1\):

$$
(-1)^{1-1}\frac{x^{2\cdot1-1}}{(2\cdot1-1)!}
=
\frac{x^1}{1!}=x
$$

Następny składnik to:

$$
\frac{x^3}{3!}
$$

kolejny:

$$
\frac{x^5}{5!}
$$

i tak dalej.

W programie nie liczymy za każdym razem wszystkiego od początku, tylko każdy następny składnik wyznaczamy z poprzedniego.

Jeżeli mamy już:

$$
\frac{x^{2k-3}}{(2k-3)!}
$$

to następny składnik bez znaku można policzyć jako:

$$
\frac{x^{2k-1}}{(2k-1)!}
=
\frac{x^{2k-3}}{(2k-3)!}\cdot \frac{x^2}{(2k-2)(2k-1)}
$$

To właśnie robi program.

## Po co jest redukcja argumentu modulo $2\pi$?

Na slajdzie była wskazówka:

$$
x \mapsto x \bmod 2\pi
$$

czyli zamieniamy $x$ na resztę z dzielenia przez $2\pi$.

Dlaczego?

Bo dla bardzo dużych wartości $x$ szereg Maclaurina może zbiegać wolniej.  
Sinus jest funkcją okresową, więc:

$$
\sin x = \sin(x \bmod 2\pi)
$$

Dzięki temu liczymy tę samą wartość, ale dla mniejszego argumentu.

## Co oznaczają zmienne w programie?

- `suma` — aktualna suma wszystkich składników szeregu,
- `wyraz` — aktualny składnik szeregu bez znaku,
- `znak` — pilnuje, czy mamy dodać, czy odjąć dany składnik,
- `n` — liczba składników zgodnie ze wzorem ze slajdu od $k=1$ do $k=n$.

To znaczy:
- pierwszy składnik $k=1$ jest dodany od razu jako `x`,
- pętla liczy składniki od $k=2$ do $k=n$.

Czyli program jest zgodny ze wzorem:

$$
\sum_{k=1}^{n} (-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}
$$

## Jak liczony jest błąd?

Błąd bezwzględny liczymy jako:

$$
\left| \text{wynik Maclaurina} - \text{wynik biblioteczny} \right|
$$

Im mniejszy błąd, tym lepsze przybliżenie.

## Jak liczony jest czas?

Czas działania mierzony jest funkcją:

```python
time.perf_counter()
```

Żeby pomiar był bardziej sensowny, każda metoda wykonywana jest bardzo wiele razy.

## Kod

```python
import math, time  # importujemy moduły math i time, ponieważ będą potrzebne do funkcji sin, liczby pi oraz pomiaru czasu

def sin_maclaurin(x, n):  # definiujemy funkcję obliczającą przybliżenie sin(x) za pomocą szeregu Maclaurina
    x = x % (2 * math.pi)  # redukujemy argument modulo 2pi, aby dla dużych x obliczenia były stabilniejsze i szybsze

    suma = x  # ustawiamy początkową sumę równą x, ponieważ pierwszy składnik szeregu dla k=1 to właśnie x
    wyraz = x  # ustawiamy pierwszy wyraz szeregu na x, aby z niego wyznaczać kolejne składniki
    znak = -1.0  # ustawiamy znak kolejnego składnika na minus, bo po x występuje -x^3/3!

    for k in range(2, n + 1):  # przechodzimy po kolejnych składnikach szeregu od k=2 do k=n
        wyraz = wyraz * x * x / ((2 * k - 2) * (2 * k - 1))  # obliczamy kolejny składnik bez znaku z poprzedniego składnika
        suma += znak * wyraz  # dodajemy lub odejmujemy aktualny składnik zgodnie z aktualnym znakiem
        znak = -znak  # zmieniamy znak na przeciwny, aby kolejne składniki miały znaki naprzemienne

    return suma  # zwracamy końcowe przybliżenie funkcji sinus

def porownaj_sin(x, n, liczba_powtorzen=100000):  # definiujemy funkcję porównującą wynik i czas działania z funkcją biblioteczną
    start = time.perf_counter()  # zapisujemy moment rozpoczęcia pomiaru czasu dla naszej metody
    for _ in range(liczba_powtorzen):  # wykonujemy obliczenia wiele razy, aby pomiar czasu był bardziej wiarygodny
        wynik_maclaurin = sin_maclaurin(x, n)  # obliczamy wartość sin(x) za pomocą własnej funkcji
    czas_maclaurin = time.perf_counter() - start  # obliczamy całkowity czas działania naszej metody

    start = time.perf_counter()  # zapisujemy moment rozpoczęcia pomiaru czasu dla funkcji bibliotecznej
    for _ in range(liczba_powtorzen):  # wykonujemy funkcję biblioteczną wiele razy
        wynik_biblioteczny = math.sin(x)  # obliczamy wartość sin(x) za pomocą funkcji bibliotecznej
    czas_biblioteczny = time.perf_counter() - start  # obliczamy całkowity czas działania funkcji bibliotecznej

    blad = abs(wynik_maclaurin - wynik_biblioteczny)  # liczymy błąd bezwzględny między obiema metodami

    print(f"x = {x}, n = {n}")  # wypisujemy aktualną wartość x oraz liczbę składników użytych w szeregu
    print(f"Wynik Maclaurina:   {wynik_maclaurin}")  # wypisujemy wynik uzyskany z szeregu Maclaurina
    print(f"Wynik biblioteczny: {wynik_biblioteczny}")  # wypisujemy wynik uzyskany z funkcji bibliotecznej
    print(f"Błąd bezwzględny:   {blad}")  # wypisujemy błąd bezwzględny
    print(f"Czas Maclaurina:    {czas_maclaurin:.10f} s")  # wypisujemy czas działania naszej metody
    print(f"Czas biblioteczny:  {czas_biblioteczny:.10f} s")  # wypisujemy czas działania funkcji bibliotecznej
    print("-" * 50)  # wypisujemy linię oddzielającą kolejne testy


print("-------------------- ZADANIE 2 --------------------")  # wypisujemy nagłówek zadania

porownaj_sin(0.5, 10)  # porównujemy obie metody dla x = 0.5 i n = 10
porownaj_sin(1.0, 10)  # porównujemy obie metody dla x = 1.0 i n = 10
porownaj_sin(math.pi / 2, 12)  # porównujemy obie metody dla x = pi/2 i n = 12
porownaj_sin(10.0, 15)  # porównujemy obie metody dla x = 10.0 i n = 15
```

## Wnioski

Funkcję sinus można aproksymować za pomocą szeregu Maclaurina:

$$
\sin x \approx \sum_{k=1}^{n} (-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}
$$

Program liczy kolejne składniki szeregu rekurencyjnie, dzięki czemu nie trzeba osobno wyznaczać każdej potęgi i każdej silni.

Dodatkowo dla dużych wartości argumentu zastosowano redukcję:

$$
x \mapsto x \bmod 2\pi
$$

co poprawia praktyczne działanie programu.

Porównanie z funkcją biblioteczną `math.sin(x)` pokazuje, że:
- wyniki uzyskane z szeregu Maclaurina są bardzo zbliżone do wartości bibliotecznych,
- błąd maleje przy większej liczbie składników,
- funkcja biblioteczna zwykle działa szybciej, ponieważ jest gotową, zoptymalizowaną implementacją.

Oznacza to, że program poprawnie realizuje aproksymację funkcji sinus za pomocą szeregu Maclaurina i poprawnie porównuje ją z funkcją biblioteczną.

---

# Zadanie 3

**Napisz funkcję wyznaczającą współczynniki wielomianu interpolacyjnego Newtona dla stablicowanych wartości pewnej funkcji.**

## O co chodzi w tym zadaniu?

Mamy dane punkty, czyli wartości funkcji w wybranych miejscach:

$$
(x_0,f(x_0)),\ (x_1,f(x_1)),\ (x_2,f(x_2)),\dots
$$

Chcemy na ich podstawie zbudować **wielomian interpolacyjny Newtona**, czyli taki wielomian, który przechodzi dokładnie przez te punkty.

Nie liczymy jeszcze wartości wielomianu dla dowolnego $x$.  
W tym zadaniu mamy policzyć tylko jego **współczynniki**.

## Postać wielomianu Newtona

Wielomian interpolacyjny Newtona ma postać:

$$
P(x)=a_0+a_1(x-x_0)+a_2(x-x_0)(x-x_1)+a_3(x-x_0)(x-x_1)(x-x_2)+\dots
$$

Czyli:
- $a_0$ to pierwszy współczynnik,
- $a_1$ to drugi współczynnik,
- $a_2$ to trzeci współczynnik,
- itd.

W tym zadaniu mamy właśnie znaleźć liczby:

$$
a_0,\ a_1,\ a_2,\ a_3,\dots
$$

## Skąd biorą się współczynniki?

Współczynniki liczymy za pomocą **ilorazów różnicowych**.

Na slajdzie jest zapisane:

$$
a_k=f[x_0,x_1,\dots,x_k]
$$

To znaczy:
- $a_0=f[x_0]=f(x_0)$
- $a_1=f[x_0,x_1]$
- $a_2=f[x_0,x_1,x_2]$
- $a_3=f[x_0,x_1,x_2,x_3]$

## Łopatologicznie: jak to liczymy?

### Krok 1 — pierwszy współczynnik

Pierwszy współczynnik jest najprostszy:

$$
a_0=f(x_0)
$$

Czyli po prostu bierzemy pierwszą wartość funkcji.

### Krok 2 — ilorazy pierwszego rzędu

Liczymy:

$$
f[x_0,x_1]=\frac{f(x_1)-f(x_0)}{x_1-x_0}
$$

$$
f[x_1,x_2]=\frac{f(x_2)-f(x_1)}{x_2-x_1}
$$

$$
f[x_2,x_3]=\frac{f(x_3)-f(x_2)}{x_3-x_2}
$$

Pierwszy z nich daje nam:

$$
a_1=f[x_0,x_1]
$$

### Krok 3 — ilorazy drugiego rzędu

Teraz używamy wyników z poprzedniego kroku:

$$
f[x_0,x_1,x_2]=\frac{f[x_1,x_2]-f[x_0,x_1]}{x_2-x_0}
$$

$$
f[x_1,x_2,x_3]=\frac{f[x_2,x_3]-f[x_1,x_2]}{x_3-x_1}
$$

Pierwszy z nich daje:

$$
a_2=f[x_0,x_1,x_2]
$$

### Krok 4 — iloraz trzeciego rzędu

Na końcu liczymy:

$$
f[x_0,x_1,x_2,x_3]
=
\frac{f[x_1,x_2,x_3]-f[x_0,x_1,x_2]}{x_3-x_0}
$$

i to jest:

$$
a_3=f[x_0,x_1,x_2,x_3]
$$

## Dlaczego w programie wystarcza jedna tablica?

Na slajdzie jest wskazówka:

- użyj jednej tablicy do przechowywania współczynników,
- algorytm działa **od końca**.

To oznacza, że nie musimy tworzyć osobnej dużej tabeli ilorazów różnicowych.  
Możemy wziąć listę wartości `y` i stopniowo ją nadpisywać.

Na początku:

```python
a = y.copy()
```

czyli w tablicy `a` mamy:

$$
[f(x_0),\ f(x_1),\ f(x_2),\ f(x_3)]
$$

Potem:
- po pierwszym przebiegu część z tych wartości zamienia się w ilorazy pierwszego rzędu,
- po drugim przebiegu pojawiają się ilorazy drugiego rzędu,
- po trzecim przebiegu pojawia się iloraz trzeciego rzędu.

Na końcu w tablicy `a` dostajemy gotowe współczynniki:

$$
[a_0,\ a_1,\ a_2,\ a_3]
$$

## Dlaczego liczymy „od końca”?

Na slajdzie jest wzór:

$$
a_i=\frac{a_i-a_{i-1}}{x_i-x_{i-j}}
$$

Jeśli liczylibyśmy od początku, to zniszczylibyśmy wartości, które są jeszcze potrzebne.

Dlatego pętla wewnętrzna idzie od końca:

```python
for i in range(n - 1, j - 1, -1):
```

Dzięki temu:
- najpierw używamy starych wartości,
- dopiero potem je nadpisujemy.

## Co oznaczają dane w programie?

Mamy:

```python
x = [0.0, 1.0, 2.0, 3.0]
y = [1.0, 2.0, 0.0, 5.0]
```

To oznacza, że znamy punkty:

$$
(0,1),\ (1,2),\ (2,0),\ (3,5)
$$

Szukamy współczynników wielomianu Newtona przechodzącego przez te cztery punkty.

## Jakie powinny wyjść współczynniki?

Dla tych danych otrzymujemy:

$$
a_0=1
$$

$$
a_1=1
$$

$$
a_2=-1.5
$$

$$
a_3=\frac{5}{3}\approx 1.6666666667
$$

Czyli wielomian Newtona ma postać:

$$
P(x)=1+1(x-0)-1.5(x-0)(x-1)+\frac{5}{3}(x-0)(x-1)(x-2)
$$

## Złożoność obliczeniowa

Na slajdzie jest podane:

$$
O(n^2)
$$

To znaczy, że liczba operacji rośnie w przybliżeniu jak kwadrat liczby punktów.

## Kod

```python
def wspolczynniki_newtona(x, y):  # definiujemy funkcję obliczającą współczynniki wielomianu Newtona
    n = len(x)  # zapisujemy liczbę węzłów interpolacji

    if len(y) != n:  # sprawdzamy, czy lista wartości y ma taką samą długość jak lista x
        raise ValueError("Listy x i y muszą mieć taką samą długość.")  # jeśli nie, zgłaszamy błąd

    a = y.copy()  # tworzymy kopię listy y, ponieważ w tej jednej tablicy będziemy nadpisywać kolejne ilorazy różnicowe

    for j in range(1, n):  # przechodzimy po kolejnych rzędach ilorazów różnicowych: 1, 2, 3, ...
        for i in range(n - 1, j - 1, -1):  # przechodzimy od końca, żeby nie nadpisać wartości potrzebnych jeszcze w danym kroku
            if x[i] == x[i - j]:  # sprawdzamy, czy nie pojawił się zerowy mianownik
                raise ValueError("Wartości x muszą być różne.")  # jeśli dwa węzły są takie same, zgłaszamy błąd
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])  # liczymy nowy iloraz różnicowy według wzoru ze slajdu

    return a  # zwracamy tablicę współczynników Newtona


print("-------------------- ZADANIE 3 --------------------")  # wypisujemy nagłówek zadania

x = [0.0, 1.0, 2.0, 3.0]  # definiujemy węzły interpolacji x0, x1, x2, x3
y = [1.0, 2.0, 0.0, 5.0]  # definiujemy odpowiadające im wartości funkcji f(x0), f(x1), f(x2), f(x3)

a = wspolczynniki_newtona(x, y)  # wywołujemy funkcję i obliczamy współczynniki wielomianu Newtona

print("Węzły x:", x)  # wypisujemy listę węzłów x
print("Wartości y:", y)  # wypisujemy listę wartości funkcji
print("Współczynniki wielomianu Newtona:")  # wypisujemy nagłówek dla współczynników
for i in range(len(a)):  # przechodzimy po wszystkich współczynnikach
    print(f"a{i} = {a[i]}")  # wypisujemy każdy współczynnik osobno jako a0, a1, a2, ...
```

## Wnioski

W zadaniu obliczamy współczynniki wielomianu interpolacyjnego Newtona na podstawie stablicowanych wartości funkcji.

Współczynniki te wyznaczamy metodą ilorazów różnicowych:

$$
a_k=f[x_0,x_1,\dots,x_k]
$$

Program działa zgodnie ze slajdem:
- używa jednej tablicy,
- nadpisuje wartości,
- liczy od końca,
- ma złożoność \(O(n^2)\).

Dla danych:

$$
(0,1),\ (1,2),\ (2,0),\ (3,5)
$$

otrzymujemy współczynniki:

$$
a_0=1,\quad a_1=1,\quad a_2=-1.5,\quad a_3=\frac53
$$

Oznacza to, że program poprawnie wyznacza współczynniki wielomianu Newtona.

---

# Zadanie 4

**Napisz funkcję umożliwiającą obliczanie wartości wielomianu interpolacyjnego Newtona. Zastosuj algorytm analogiczny do schematu Hornera.**

## O co chodzi w tym zadaniu?

W poprzednim zadaniu wyznaczyliśmy współczynniki wielomianu Newtona:

$$
a_0,\ a_1,\ a_2,\ a_3,\dots
$$

Teraz chcemy zrobić następny krok, czyli:

- wziąć te współczynniki,
- wybrać punkt $X$,
- policzyć wartość wielomianu interpolacyjnego Newtona w tym punkcie.

Czyli zamiast budować cały wielomian „na piechotę”, chcemy tylko obliczyć:

$$
P(X)
$$

---

## Postać wielomianu Newtona

Wielomian interpolacyjny Newtona ma postać:

$$
P(x)=a_0+a_1(x-x_0)+a_2(x-x_0)(x-x_1)+a_3(x-x_0)(x-x_1)(x-x_2)+\dots
$$

Dla większej liczby składników taki zapis robi się niewygodny do liczenia, bo:
- jest dużo nawiasów,
- trzeba mnożyć wiele razy te same wyrażenia,
- łatwo się pomylić.

Dlatego stosujemy **algorytm analogiczny do schematu Hornera**.

## Co pokazuje slajd?

Na slajdzie zapisano schemat Hornera dla postaci Newtona:

$$
P(x)=a_n+(x-x_{n-1})(a_{n-1}+(x-x_{n-2})(\dots))
$$

To znaczy, że nie liczymy wielomianu od początku, tylko **idziemy od końca**.

Na slajdzie jest też podany krok algorytmu:

$$
result = result \cdot (X - x_i) + a_i
$$

To jest najważniejszy wzór w tym zadaniu.

## Łopatologicznie: jak to działa?

Załóżmy, że mamy 4 współczynniki:

$$
a_0,\ a_1,\ a_2,\ a_3
$$

Wtedy zamiast liczyć:

$$
P(x)=a_0+a_1(x-x_0)+a_2(x-x_0)(x-x_1)+a_3(x-x_0)(x-x_1)(x-x_2)
$$

przepisujemy to w wygodniejszej postaci:

$$
P(x)=a_0+(x-x_0)\left(a_1+(x-x_1)\left(a_2+a_3(x-x_2)\right)\right)
$$

I teraz liczymy od środka:

### Krok 1
Zaczynamy od ostatniego współczynnika:

$$
P=a_3
$$

### Krok 2
Potem:

$$
P=P(x-x_2)+a_2
$$

### Krok 3
Potem:

$$
P=P(x-x_1)+a_1
$$

### Krok 4
Na końcu:

$$
P=P(x-x_0)+a_0
$$

I to już daje wartość wielomianu w punkcie $x$.

## Dlaczego to jest podobne do schematu Hornera?

W zwykłym schemacie Hornera też liczymy od końca i stopniowo składamy wielomian.

Tutaj robimy bardzo podobnie, tylko zamiast zwykłych potęg $x$, pojawiają się przesunięcia:

$$
(X-x_i)
$$

Dlatego na slajdzie jest napisane, że to jest **algorytm analogiczny do schematu Hornera**.

## Co robi funkcja `wartosc_wielomianu_newtona`?

Ta funkcja:
1. bierze węzły $x_0,x_1,\dots$,
2. bierze wcześniej policzone współczynniki $a_0,a_1,\dots$,
3. bierze punkt $X$,
4. oblicza wartość wielomianu $P(X)$.

## Po co w tym kodzie jest jeszcze funkcja `wspolczynniki_newtona`?

Bo żeby policzyć wartość wielomianu Newtona, musimy najpierw znać jego współczynniki.

Dlatego:
- funkcja `wspolczynniki_newtona(x, y)` bierze dane punktowe i wyznacza współczynniki,
- funkcja `wartosc_wielomianu_newtona(x_wezly, a, X)` używa tych współczynników do policzenia wartości wielomianu w punkcie $X$.

## Co oznaczają dane z programu?

Mamy:

$$
x=[0,1,2,3]
$$

oraz:

$$
y=[1,2,0,5]
$$

To oznacza, że znamy punkty:

$$
(0,1),\ (1,2),\ (2,0),\ (3,5)
$$

Na ich podstawie tworzymy wielomian interpolacyjny Newtona.

Potem wybieramy punkt:

$$
X=1.5
$$

i chcemy obliczyć:

$$
P(1.5)
$$

czyli wartość wielomianu w tym punkcie.

## Jakie współczynniki wychodzą dla tych danych?

Dla tych danych współczynniki Newtona są równe:

$$
a_0=1
$$

$$
a_1=1
$$

$$
a_2=-1.5
$$

$$
a_3=\frac{5}{3}\approx 1.6666666667
$$

## Jak wygląda liczenie wartości wielomianu dla $X=1.5$?

Zaczynamy od:

$$
P=a_3=\frac{5}{3}
$$

Potem:

$$
P=P(1.5-2)+a_2
$$

Potem:

$$
P=P(1.5-1)+a_1
$$

Potem:

$$
P=P(1.5-0)+a_0
$$

Po wykonaniu tych kroków dostajemy wartość wielomianu w punkcie $X=1.5$.

## Złożoność obliczeniowa

Na slajdzie jest podane:

$$
O(n)
$$

To znaczy, że po wyznaczeniu współczynników wartość wielomianu liczymy bardzo szybko - liczba operacji rośnie liniowo wraz z liczbą współczynników.

## Kod

```python
def wspolczynniki_newtona(x, y):  # definiujemy funkcję wyznaczającą współczynniki wielomianu Newtona
    n = len(x)  # zapisujemy liczbę węzłów interpolacji

    if len(y) != n:  # sprawdzamy, czy liczba wartości y jest taka sama jak liczba węzłów x
        raise ValueError("Listy x i y muszą mieć taką samą długość.")  # jeśli długości się różnią, zgłaszamy błąd

    a = y.copy()  # tworzymy kopię listy y, ponieważ w tej tablicy będziemy nadpisywać kolejne ilorazy różnicowe

    for j in range(1, n):  # przechodzimy po kolejnych rzędach ilorazów różnicowych
        for i in range(n - 1, j - 1, -1):  # liczymy od końca, żeby nie nadpisać wartości potrzebnych jeszcze w tym samym kroku
            if x[i] == x[i - j]:  # sprawdzamy, czy nie pojawił się zerowy mianownik
                raise ValueError("Wartości x muszą być różne.")  # jeśli dwa węzły są takie same, zgłaszamy błąd
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])  # liczymy nowy iloraz różnicowy według wzoru Newtona

    return a  # zwracamy tablicę współczynników Newtona


def wartosc_wielomianu_newtona(x_wezly, a, X):  # definiujemy funkcję obliczającą wartość wielomianu Newtona w punkcie X
    n = len(a)  # zapisujemy liczbę współczynników wielomianu

    if len(x_wezly) != n:  # sprawdzamy, czy liczba węzłów x jest zgodna z liczbą współczynników
        raise ValueError("Liczba węzłów x i liczba współczynników musi być taka sama.")  # jeśli nie, zgłaszamy błąd

    wynik = a[n - 1]  # zaczynamy od ostatniego współczynnika, zgodnie ze schematem Hornera dla postaci Newtona

    for i in range(n - 2, -1, -1):  # przechodzimy od przedostatniego współczynnika do pierwszego
        wynik = wynik * (X - x_wezly[i]) + a[i]  # wykonujemy krok schematu: wynik = wynik * (X - x_i) + a_i

    return wynik  # zwracamy obliczoną wartość wielomianu w punkcie X

print("-------------------- ZADANIE 4 --------------------")  # wypisujemy nagłówek zadania

x = [0.0, 1.0, 2.0, 3.0]  # definiujemy węzły interpolacji
y = [1.0, 2.0, 0.0, 5.0]  # definiujemy wartości funkcji w tych węzłach

a = wspolczynniki_newtona(x, y)  # obliczamy współczynniki wielomianu Newtona na podstawie danych punktów

X = 1.5  # wybieramy punkt, w którym chcemy policzyć wartość wielomianu
wartosc = wartosc_wielomianu_newtona(x, a, X)  # obliczamy wartość wielomianu Newtona w punkcie X

print("Węzły x:", x)  # wypisujemy węzły interpolacji
print("Wartości y:", y)  # wypisujemy wartości funkcji
print("Współczynniki Newtona:", a)  # wypisujemy obliczone współczynniki wielomianu Newtona
print("Punkt X:", X)  # wypisujemy punkt, w którym liczymy wartość wielomianu
print("Wartość wielomianu w punkcie X:", wartosc)  # wypisujemy końcowy wynik obliczeń
```

## Wnioski

W zadaniu obliczamy wartość wielomianu interpolacyjnego Newtona w wybranym punkcie $X$.

Nie liczymy wielomianu bezpośrednio z pełnego wzoru, tylko stosujemy algorytm analogiczny do schematu Hornera:

$$
result = result\cdot (X-x_i)+a_i
$$

Obliczenia wykonujemy od końca, zaczynając od ostatniego współczynnika.

Dzięki temu:
- obliczenia są prostsze,
- nie trzeba ręcznie rozwijać wszystkich nawiasów,
- algorytm działa szybko, w czasie:

$$
O(n)
$$

Dla danych punktów:

$$
(0,1),\ (1,2),\ (2,0),\ (3,5)
$$

najpierw wyznaczamy współczynniki Newtona, a następnie obliczamy wartość wielomianu w punkcie:

$$
X=1.5
$$

Program poprawnie realizuje schemat Hornera dla postaci Newtona i poprawnie wyznacza wartość wielomianu interpolacyjnego.

---

# Zadanie 5*

**Rozwiązania dwóch poprzednich zadań wykorzystaj do narysowania wykresu wielomianu interpolacyjnego (zaznaczając również punktami zaobserwowane wartości funkcji).**

![alt text](wykres.png)

Do tego wykresu możesz wpisać takie wnioski:

* Wielomian interpolacyjny Newtona przechodzi dokładnie przez wszystkie zadane punkty wejściowe: ((0,1)), ((1,2)), ((2,0)), ((3,5)). To potwierdza poprawność interpolacji.
* Krzywa między punktami jest gładka, co pokazuje, że wielomian dobrze odtwarza przebieg funkcji zadanej w punktach tablicowych.
* W badanym przykładzie wielomian najpierw rośnie, następnie maleje do minimum w pobliżu punktu ((2,0)), a potem znowu rośnie.
* Wykres potwierdza, że funkcje z zadań 3 i 4 działają poprawnie, ponieważ współczynniki Newtona zostały dobrze wyznaczone, a wartości wielomianu poprawnie obliczone.
* Interpolacja Newtona pozwala nie tylko odtworzyć wartości w danych punktach, ale także oszacować wartości funkcji pomiędzy nimi.

## O co chodzi w tym zadaniu?

W zadaniu 3 wyznaczaliśmy **współczynniki wielomianu interpolacyjnego Newtona**.

W zadaniu 4 liczyliśmy **wartość tego wielomianu w wybranym punkcie $X$**.

W zadaniu 5 robimy kolejny krok:
- bierzemy wiele punktów z badanego przedziału,
- dla każdego z nich liczymy wartość wielomianu,
- na tej podstawie rysujemy wykres,
- dodatkowo zaznaczamy punkty wejściowe, z których wielomian został utworzony.

Czyli w praktyce:
- **punkty wejściowe** pokazują dane,
- **krzywa** pokazuje wielomian interpolacyjny Newtona.

## Co wykorzystujemy z poprzednich zadań?

### Z zadania 3
Bierzemy funkcję, która liczy współczynniki Newtona:

$$
a_0,\ a_1,\ a_2,\dots
$$

czyli funkcję:

```python
wspolczynniki_newtona(x, y)
```

### Z zadania 4
Bierzemy funkcję, która dla danego punktu $X$ liczy wartość wielomianu:

$$
P(X)
$$

czyli funkcję:

```python
wartosc_wielomianu_newtona(x_wezly, a, X)
```

## Co robimy nowego w zadaniu 5?

W zadaniu 4 liczyliśmy wartość wielomianu tylko dla jednego punktu, np.:

$$
X=1.5
$$

Tutaj chcemy narysować cały wykres, więc musimy policzyć wartości wielomianu **dla wielu punktów**.

Na przykład:
- $X_1$,
- $X_2\),
- $X_3$,
- $\dots$

Dla każdego z tych punktów liczymy:

$$
Y_i=P(X_i)
$$

Potem:
- wszystkie punkty $(X_i, Y_i)$ łączymy linią,
- a oryginalne punkty danych zaznaczamy osobno.

## Dlaczego wykres przechodzi przez punkty wejściowe?

Bo wielomian interpolacyjny Newtona jest zbudowany dokładnie tak, aby spełniać warunki:

$$
P(x_0)=y_0,\quad P(x_1)=y_1,\quad P(x_2)=y_2,\dots
$$

To oznacza, że wykres wielomianu musi przejść przez wszystkie zadane punkty.

Jeżeli tak się dzieje, to znaczy, że:
- współczynniki zostały policzone poprawnie,
- wartość wielomianu też jest liczona poprawnie.

## Jak wygląda algorytm zadania 5?

### Krok 1
Podajemy punkty wejściowe:

$$
(x_0,y_0),\ (x_1,y_1),\dots
$$

### Krok 2
Liczymy współczynniki Newtona:

$$
a_0,\ a_1,\ a_2,\dots
$$

### Krok 3
Wybieramy dużo punktów z przedziału od najmniejszego do największego $x$.

### Krok 4
Dla każdego punktu liczymy wartość wielomianu Newtona.

### Krok 5
Rysujemy:
- wykres wielomianu,
- punkty wejściowe.

## Dane użyte w programie

W programie przyjęto punkty:

$$
(0,1),\ (1,2),\ (2,0),\ (3,5)
$$

czyli:

```python
x = [0.0, 1.0, 2.0, 3.0]
y = [1.0, 2.0, 0.0, 5.0]
```

Na ich podstawie budowany jest wielomian interpolacyjny Newtona.

## Co powinno wyjść na wykresie?

Na wykresie powinno być widać:
- krzywą wielomianu interpolacyjnego,
- punkty wejściowe.

Krzywa powinna przechodzić dokładnie przez punkty:
- $(0,1)$,
- $(1,2)$,
- $(2,0)$,
- $(3,5)$.

Jeżeli tak jest, to wykres jest poprawny.

## Kod

```python
import matplotlib.pyplot as plt  # importujemy moduł matplotlib do rysowania wykresów

def wspolczynniki_newtona(x, y):  # definiujemy funkcję wyznaczającą współczynniki wielomianu Newtona
    n = len(x)  # zapisujemy liczbę węzłów interpolacji

    if len(y) != n:  # sprawdzamy, czy liczba wartości y jest taka sama jak liczba węzłów x
        raise ValueError("Listy x i y muszą mieć taką samą długość.")  # jeśli długości się różnią, zgłaszamy błąd

    a = y.copy()  # tworzymy kopię listy y, ponieważ w tej tablicy będziemy nadpisywać kolejne ilorazy różnicowe

    for j in range(1, n):  # przechodzimy po kolejnych rzędach ilorazów różnicowych
        for i in range(n - 1, j - 1, -1):  # liczymy od końca, żeby nie nadpisać wartości potrzebnych jeszcze w tym samym kroku
            if x[i] == x[i - j]:  # sprawdzamy, czy nie pojawił się zerowy mianownik
                raise ValueError("Wartości x muszą być różne.")  # jeśli dwa węzły są takie same, zgłaszamy błąd
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])  # liczymy nowy iloraz różnicowy według wzoru Newtona

    return a  # zwracamy tablicę współczynników Newtona


def wartosc_wielomianu_newtona(x_wezly, a, X):  # definiujemy funkcję liczącą wartość wielomianu Newtona w punkcie X
    n = len(a)  # zapisujemy liczbę współczynników

    if len(x_wezly) != n:  # sprawdzamy, czy liczba węzłów x jest zgodna z liczbą współczynników
        raise ValueError("Liczba węzłów x i liczba współczynników musi być taka sama.")  # jeśli nie, zgłaszamy błąd

    wynik = a[n - 1]  # zaczynamy od ostatniego współczynnika, zgodnie ze schematem Hornera dla postaci Newtona

    for i in range(n - 2, -1, -1):  # przechodzimy od przedostatniego współczynnika do pierwszego
        wynik = wynik * (X - x_wezly[i]) + a[i]  # wykonujemy krok schematu Hornera dla wielomianu Newtona

    return wynik  # zwracamy obliczoną wartość wielomianu


print("-------------------- ZADANIE 5 --------------------")  # wypisujemy nagłówek zadania

x = [0.0, 1.0, 2.0, 3.0]  # definiujemy węzły interpolacji
y = [1.0, 2.0, 0.0, 5.0]  # definiujemy wartości funkcji w tych punktach

a = wspolczynniki_newtona(x, y)  # obliczamy współczynniki wielomianu Newtona

x_min = min(x)  # wyznaczamy najmniejszą wartość x, od której zaczniemy rysowanie wykresu
x_max = max(x)  # wyznaczamy największą wartość x, na której skończymy rysowanie wykresu

x_wykres = []  # tworzymy pustą listę na punkty x użyte do rysowania wykresu
y_wykres = []  # tworzymy pustą listę na odpowiadające im wartości wielomianu

liczba_punktow = 200  # ustalamy, w ilu punktach chcemy policzyć wielomian, aby wykres był gładki

for i in range(liczba_punktow + 1):  # przechodzimy po wszystkich punktach, w których będziemy liczyć wielomian
    X = x_min + (x_max - x_min) * i / liczba_punktow  # wyznaczamy kolejny punkt X równomiernie rozmieszczony w badanym przedziale
    Y = wartosc_wielomianu_newtona(x, a, X)  # obliczamy wartość wielomianu Newtona w punkcie X
    x_wykres.append(X)  # dodajemy punkt X do listy punktów wykresu
    y_wykres.append(Y)  # dodajemy obliczoną wartość Y do listy wartości wykresu

plt.plot(x_wykres, y_wykres, label="Wielomian interpolacyjny Newtona")  # rysujemy krzywą wielomianu interpolacyjnego
plt.scatter(x, y, label="Punkty wejściowe")  # zaznaczamy na wykresie oryginalne punkty wejściowe

plt.title("Interpolacja Newtona")  # ustawiamy tytuł wykresu
plt.xlabel("x")  # ustawiamy podpis osi poziomej
plt.ylabel("y")  # ustawiamy podpis osi pionowej
plt.legend()  # wyświetlamy legendę
plt.grid(True)  # włączamy siatkę pomocniczą na wykresie
plt.show()  # wyświetlamy gotowy wykres
```

## Wnioski

W zadaniu 5 wykorzystano rozwiązania z zadań 3 i 4:
- z zadania 3 do wyznaczenia współczynników wielomianu Newtona,
- z zadania 4 do obliczania wartości wielomianu w wybranych punktach.

Następnie policzono wartości wielomianu w wielu punktach badanego przedziału i narysowano jego wykres.

Na wykresie zaznaczono:
- **punkty wejściowe**,
- **wielomian interpolacyjny Newtona**.

Otrzymany wykres jest poprawny, jeśli krzywa przechodzi dokładnie przez wszystkie zadane punkty.  
W tym zadaniu tak właśnie się dzieje, więc można stwierdzić, że:
- współczynniki Newtona zostały wyznaczone poprawnie,
- wartość wielomianu jest liczona poprawnie,
- wizualizacja została wykonana poprawnie.

---

# Lab 9

# Zadanie 1

**Napisz program implementujący aproksymację średniokwadratową liniową dla zbioru punktów**
$
\
\{(1.1, 2.1),\ (1.4, 2.3),\ (1.8, 2.9),\ (2.5, 3.2),\ (2.8, 3.6),\ (3.0, 4.2)\}.
\
$

## Na czym polega aproksymacja średniokwadratowa?

Aproksymacja średniokwadratowa, nazywana też **metodą najmniejszych kwadratów**, polega na znalezieniu takiej funkcji $F(x)$, która jak najlepiej przybliża dane punkty.

Dla zbioru punktów $(x_i,y_i)$, gdzie:

$$
y_i=f(x_i),
$$

szukamy funkcji $F(x)$, dla której wyrażenie:

$$
\|F-f\|_2=\sum_{i=1}^{n} w(x_i)(F(x_i)-y_i)^2
$$

osiąga minimum.

W slajdach przyjęto uproszczenie:

$
w(x)=1,
$

więc minimalizujemy po prostu sumę kwadratów odchyleń wartości aproksymacji od danych punktów.

## Aproksymacja liniowa

Najprostszym przypadkiem aproksymacji średniokwadratowej jest **aproksymacja liniowa**.

Szukamy prostej postaci:

$$
F(x)=ax+b
$$

takiej, aby minimalizować funkcję:

$$
h(a,b)=\sum_{i=1}^{n}(ax_i+b-y_i)^2.
$$

Oznacza to, że chcemy dobrać współczynniki $a$ i $b$ tak, aby suma kwadratów błędów była jak najmniejsza.

## Skąd biorą się wzory na $a$ i $b$?

Po obliczeniu pochodnych cząstkowych funkcji $h(a,b)$ i po przekształceniach dostajemy wzory:

$$
a=\frac{nA-BC}{nD-B^2},
\qquad
b=\frac{CD-AB}{nD-B^2},
$$

gdzie:

$$
A=\sum_{i=1}^{n} x_i y_i,
\qquad
B=\sum_{i=1}^{n} x_i,
\qquad
C=\sum_{i=1}^{n} y_i,
\qquad
D=\sum_{i=1}^{n} x_i^2.
$$

To właśnie te wielkości oblicza program.

## Dane z zadania

Mamy punkty:

$$
(1.1,2.1),\ (1.4,2.3),\ (1.8,2.9),\ (2.5,3.2),\ (2.8,3.6),\ (3.0,4.2)
$$

czyli:

- $x_1=1.1,\ y_1=2.1$
- $x_2=1.4,\ y_2=2.3$
- $x_3=1.8,\ y_3=2.9$
- $x_4=2.5,\ y_4=3.2$
- $x_5=2.8,\ y_5=3.6$
- $x_6=3.0,\ y_6=4.2$

Liczba punktów wynosi:

$$
n=6
$$

## Obliczenie sum pomocniczych

Liczymy zgodnie ze wzorami ze slajdu:

### Suma $A$

$$
A=\sum x_i y_i
$$

$$
A=1.1\cdot2.1+1.4\cdot2.3+1.8\cdot2.9+2.5\cdot3.2+2.8\cdot3.6+3.0\cdot4.2
$$

$$
A=2.31+3.22+5.22+8.00+10.08+12.60=41.43
$$

### Suma $B$

$$
B=\sum x_i
$$

$$
B=1.1+1.4+1.8+2.5+2.8+3.0=12.6
$$

### Suma $C$

$$
C=\sum y_i
$$

$$
C=2.1+2.3+2.9+3.2+3.6+4.2=18.3
$$

### Suma $D$

$$
D=\sum x_i^2
$$

$$
D=1.1^2+1.4^2+1.8^2+2.5^2+2.8^2+3.0^2
$$

$$
D=1.21+1.96+3.24+6.25+7.84+9.00=29.5
$$

## Obliczenie współczynników prostej

Podstawiamy do wzorów:

$$
a=\frac{nA-BC}{nD-B^2}
$$

$$
a=\frac{6\cdot41.43-12.6\cdot18.3}{6\cdot29.5-12.6^2}
$$

$$
a=\frac{248.58-230.58}{177-158.76}
$$

$$
a=\frac{18}{18.24}=0.9868421052631579
$$

Teraz współczynnik $b$:

$$
b=\frac{CD-AB}{nD-B^2}
$$

$$
b=\frac{18.3\cdot29.5-41.43\cdot12.6}{177-158.76}
$$

$$
b=\frac{539.85-522.018}{18.24}
$$

$$
b=\frac{17.832}{18.24}=0.9776315789473676
$$

## Otrzymana prosta aproksymacyjna

Zatem szukana prosta ma postać:

$$
F(x)=0.9868421052631579x+0.9776315789473676
$$

## Obliczenie sumy kwadratów błędów

Na końcu program liczy wartość funkcji błędu:

$$
h(a,b)=\sum_{i=1}^{n}(ax_i+b-y_i)^2
$$

Dla naszej prostej:

$$
h=\sum_{i=1}^{6}(0.9868421052631579x_i+0.9776315789473676-y_i)^2
$$

Program oblicza tę wartość automatycznie.  
Dla tych danych wychodzi:

$$
h \approx 0.17447368421052628
$$

## Kod

```python
print("-------------------- ZADANIE 1 --------------------")  # wypisujemy nagłówek zadania

punkty = [(1.1, 2.1), (1.4, 2.3), (1.8, 2.9), (2.5, 3.2),(2.8, 3.6), (3.0, 4.2)]  # zapisujemy punkty z zadania w postaci par (x, y)

n = len(punkty)  # obliczamy liczbę punktów, czyli n

A = 0.0  # tworzymy zmienną A na sumę iloczynów x_i * y_i
B = 0.0  # tworzymy zmienną B na sumę x_i
C = 0.0  # tworzymy zmienną C na sumę y_i
D = 0.0  # tworzymy zmienną D na sumę x_i^2

for x, y in punkty:  # przechodzimy po wszystkich punktach z listy
    B += x  # dodajemy bieżące x do sumy B = suma x_i
    C += y  # dodajemy bieżące y do sumy C = suma y_i
    D += x * x  # dodajemy kwadrat bieżącego x do sumy D = suma x_i^2
    A += x * y  # dodajemy iloczyn x * y do sumy A = suma x_i y_i

a = (n * A - B * C) / (n * D - B * B)  # obliczamy współczynnik a ze wzoru ze slajdu
b = (C * D - A * B) / (n * D - B * B)  # obliczamy współczynnik b ze wzoru ze slajdu

print("Współczynniki prostej aproksymacyjnej:")  # wypisujemy nagłówek dla współczynników
print("a =", a)  # wypisujemy obliczoną wartość współczynnika a
print("b =", b)  # wypisujemy obliczoną wartość współczynnika b

print("\nProsta aproksymacyjna:")  # wypisujemy nagłówek dla równania prostej
print(f"y = {a} * x + {b}")  # wypisujemy równanie wyznaczonej prostej aproksymacyjnej

h = 0.0  # tworzymy zmienną h na sumę kwadratów błędów, czyli wartość funkcji błędu
for x, y in punkty:  # ponownie przechodzimy po wszystkich punktach
    h += (a * x + b - y) ** 2  # dodajemy kwadrat różnicy między wartością z prostej a wartością rzeczywistą y

print("\nSuma kwadratów błędów:")  # wypisujemy nagłówek dla wartości błędu
print(h)  # wypisujemy końcową wartość funkcji błędu h(a,b)
```

## Wnioski

W zadaniu wyznaczono prostą aproksymacyjną metodą najmniejszych kwadratów dla punktów:

$
(1,1),\ (3,12),\ (5,25),\ (7,38).
$

Na podstawie wzorów ze slajdów obliczono:

$
a=6.2,\qquad b=-5.8.
$

Otrzymana prosta aproksymacyjna ma więc postać:

$
F(x)=6.2x-5.8.
$

Suma kwadratów błędów wynosi:

$
h=4.8.
$

Oznacza to, że prosta $F(x)=6.2x-5.8$ jest najlepszym liniowym przybliżeniem danych punktów w sensie metody najmniejszych kwadratów.

---

# Zadanie 2

**Napisz program implementujący aproksymację średniokwadratową wielomianem drugiego stopnia dla zbioru punktów**
$
\{(0,2),\ (0.5,2.48),\ (1,2.84),\ (1.5,3),\ (2,2.91)\}.
$

## Na czym polega aproksymacja wielomianowa?

W aproksymacji średniokwadratowej szukamy funkcji $F(x)$, która możliwie najlepiej przybliża dane punkty.

Przyjmujemy ogólną postać funkcji aproksymującej:

$$
F(x)=a_0\phi_0(x)+a_1\phi_1(x)+\dots+a_m\phi_m(x),
$$

gdzie dla uproszczenia:

$$
\phi_k(x)=x^k.
$$

Zadaniem jest minimalizacja funkcji błędu:

$$
h(a_0,a_1,\dots,a_m)=\sum_{i=1}^{n}\left(\sum_{j=0}^{m} a_j x_i^j-y_i\right)^2.
$$

## Układ równań ze slajdów

Ze slajdów wynika, że dla każdego:

$$
i=0,1,\dots,m
$$

otrzymujemy układ $m+1$ równań z $m+1$ niewiadomymi:

$$
\frac{\partial h}{\partial a_i}
=
2\sum_{i=1}^{n}
\left(
\sum_{j=0}^{m} a_j x_i^j-y_i
\right)x_i^i
=0.
$$

Jest to wzór ogólny dla aproksymacji wielomianowej.

## Zastosowanie do tego zadania

W tym zadaniu szukamy wielomianu drugiego stopnia, więc:

$$
m=2.
$$

Oznacza to, że funkcja aproksymująca ma postać:

$$
F(x)=a_0+a_1x+a_2x^2.
$$

W programie ten sam wielomian zapisujemy równoważnie jako:

$$
F(x)=ax^2+bx+c,
$$

gdzie:

- $a=a_2$
- $b=a_1$
- $c=a_0$

Po podstawieniu do wzoru ogólnego funkcja błędu przyjmuje postać:

$$
h(a_0,a_1,a_2)=\sum_{i=1}^{n}(a_0+a_1x_i+a_2x_i^2-y_i)^2.
$$

W zapisie używanym w programie jest to równoważnie:

$$
h(a,b,c)=\sum_{i=1}^{n}(ax_i^2+bx_i+c-y_i)^2.
$$

## Układ równań dla wielomianu drugiego stopnia

Dla wielomianu drugiego stopnia:

$$
F(x)=ax^2+bx+c
$$

ze slajdów otrzymujemy układ równań:

$$
a\sum_{i=1}^{n}x_i^4+b\sum_{i=1}^{n}x_i^3+c\sum_{i=1}^{n}x_i^2=\sum_{i=1}^{n}x_i^2y_i,
$$

$$
a\sum_{i=1}^{n}x_i^3+b\sum_{i=1}^{n}x_i^2+c\sum_{i=1}^{n}x_i=\sum_{i=1}^{n}x_iy_i,
$$

$$
a\sum_{i=1}^{n}x_i^2+b\sum_{i=1}^{n}x_i+nc=\sum_{i=1}^{n}y_i.
$$

Program właśnie buduje ten układ równań i rozwiązuje go metodą Gaussa.

## Dane z zadania

Mamy punkty:

$$
(0,2),\ (0.5,2.48),\ (1,2.84),\ (1.5,3),\ (2,2.91)
$$

czyli:

- $x_1=0,\ y_1=2$
- $x_2=0.5,\ y_2=2.48$
- $x_3=1,\ y_3=2.84$
- $x_4=1.5,\ y_4=3$
- $x_5=2,\ y_5=2.91$

Liczba punktów wynosi:

$$
n=5
$$

## Obliczenie sum pomocniczych

Liczymy sumy potrzebne do zbudowania układu równań.

### Suma $\sum x_i$

$$
\sum x_i=0+0.5+1+1.5+2=5
$$

### Suma $\sum x_i^2$

$$
\sum x_i^2=0^2+0.5^2+1^2+1.5^2+2^2
$$

$$
\sum x_i^2=0+0.25+1+2.25+4=7.5
$$

### Suma $\sum x_i^3$

$$
\sum x_i^3=0^3+0.5^3+1^3+1.5^3+2^3
$$

$$
\sum x_i^3=0+0.125+1+3.375+8=12.5
$$

### Suma $\sum x_i^4$

$$
\sum x_i^4=0^4+0.5^4+1^4+1.5^4+2^4
$$

$$
\sum x_i^4=0+0.0625+1+5.0625+16=22.125
$$

### Suma $\sum y_i$

$$
\sum y_i=2+2.48+2.84+3+2.91=13.23
$$

### Suma $\sum x_i y_i$

$$
\sum x_i y_i=0\cdot2+0.5\cdot2.48+1\cdot2.84+1.5\cdot3+2\cdot2.91
$$

$$
\sum x_i y_i=0+1.24+2.84+4.5+5.82=14.4
$$

### Suma $\sum x_i^2 y_i$

$$
\sum x_i^2 y_i=0^2\cdot2+0.5^2\cdot2.48+1^2\cdot2.84+1.5^2\cdot3+2^2\cdot2.91
$$

$$
\sum x_i^2 y_i=0+0.62+2.84+6.75+11.64=21.85
$$

## Budowa układu równań

Podstawiamy obliczone sumy do wzorów:

$$
22.125a+12.5b+7.5c=21.85
$$

$$
12.5a+7.5b+5c=14.4
$$

$$
7.5a+5b+5c=13.23
$$

W postaci macierzowej:

$$
\begin{bmatrix}
22.125 & 12.5 & 7.5 \\
12.5 & 7.5 & 5 \\
7.5 & 5 & 5
\end{bmatrix}
\cdot
\begin{bmatrix}
a \\
b \\
c
\end{bmatrix}
=
\begin{bmatrix}
21.85 \\
14.4 \\
13.23
\end{bmatrix}
$$

## Rozwiązanie układu

Po rozwiązaniu układu równań otrzymujemy:

$$
a=-\frac{67}{175}\approx -0.38285714285714284
$$

$$
b=\frac{2159}{1750}\approx 1.2337142857142858
$$

$$
c=\frac{6953}{3500}\approx 1.9865714285714287
$$

## Otrzymany wielomian aproksymacyjny

Zatem szukany wielomian ma postać:

$$
F(x)=-0.38285714285714284x^2+1.2337142857142858x+1.9865714285714287
$$

## Obliczenie sumy kwadratów błędów

Na końcu program liczy wartość funkcji błędu.

Zgodnie ze slajdami w postaci ogólnej:

$$
h(a_0,a_1,\dots,a_m)=\sum_{i=1}^{n}\left(\sum_{j=0}^{m} a_j x_i^j-y_i\right)^2.
$$

W tym zadaniu, dla wielomianu drugiego stopnia, mamy:

$$
h(a_0,a_1,a_2)=\sum_{i=1}^{n}(a_0+a_1x_i+a_2x_i^2-y_i)^2.
$$

W zapisie używanym w programie jest to równoważnie:

$$
h(a,b,c)=\sum_{i=1}^{n}(ax_i^2+bx_i+c-y_i)^2.
$$

Dla otrzymanego wielomianu:

$$
h=\sum_{i=1}^{5}\left(-0.38285714285714284x_i^2+1.2337142857142858x_i+1.9865714285714287-y_i\right)^2
$$

Program oblicza tę wartość automatycznie.  
Dla tych danych wychodzi:

$$
h \approx 0.00170285714285714
$$

czyli dokładnie:

$$
h=\frac{149}{87500}
$$

## Kod

```python
print("-------------------- ZADANIE 2 --------------------")  # wypisujemy nagłówek zadania

punkty = [(0.0, 2.0), (0.5, 2.48), (1.0, 2.84), (1.5, 3.0), (2.0, 2.91)]  # zapisujemy punkty z zadania jako pary (x, y)

def rozwiaz_uklad_gaussa(macierz, wyrazy_wolne):  # definiujemy funkcję rozwiązującą układ równań metodą Gaussa
    n = len(wyrazy_wolne)  # zapisujemy liczbę równań i niewiadomych

    for i in range(n):  # przechodzimy po kolejnych kolumnach i wierszach eliminacji
        if macierz[i][i] == 0:  # sprawdzamy, czy na przekątnej nie pojawiło się zero
            raise ValueError("Na przekątnej pojawiło się zero - nie można wykonać eliminacji Gaussa.")  # jeśli tak, zgłaszamy błąd

        for j in range(i + 1, n):  # przechodzimy po wierszach poniżej aktualnego wiersza
            wspolczynnik = macierz[j][i] / macierz[i][i]  # obliczamy współczynnik potrzebny do wyzerowania elementu pod przekątną

            for k in range(i, n):  # przechodzimy po elementach aktualnego wiersza od kolumny i do końca
                macierz[j][k] = macierz[j][k] - wspolczynnik * macierz[i][k]  # zerujemy elementy pod przekątną w macierzy

            wyrazy_wolne[j] = wyrazy_wolne[j] - wspolczynnik * wyrazy_wolne[i]  # wykonujemy tę samą operację na wektorze wyrazów wolnych

    rozwiazanie = [0.0] * n  # tworzymy listę na rozwiązanie układu

    for i in range(n - 1, -1, -1):  # wykonujemy podstawianie wsteczne od ostatniego równania do pierwszego
        suma = 0.0  # tworzymy zmienną na sumę znanych składników
        for j in range(i + 1, n):  # przechodzimy po współczynnikach przy już wyznaczonych niewiadomych
            suma += macierz[i][j] * rozwiazanie[j]  # dodajemy do sumy iloczyny współczynników i znanych rozwiązań

        rozwiazanie[i] = (wyrazy_wolne[i] - suma) / macierz[i][i]  # obliczamy bieżącą niewiadomą

    return rozwiazanie  # zwracamy listę rozwiązań układu

n = len(punkty)  # obliczamy liczbę punktów

suma_x = 0.0  # tworzymy zmienną na sumę x_i
suma_x2 = 0.0  # tworzymy zmienną na sumę x_i^2
suma_x3 = 0.0  # tworzymy zmienną na sumę x_i^3
suma_x4 = 0.0  # tworzymy zmienną na sumę x_i^4
suma_y = 0.0  # tworzymy zmienną na sumę y_i
suma_xy = 0.0  # tworzymy zmienną na sumę x_i y_i
suma_x2y = 0.0  # tworzymy zmienną na sumę x_i^2 y_i

for x, y in punkty:  # przechodzimy po wszystkich punktach z listy
    suma_x += x  # dodajemy bieżące x do sumy x_i
    suma_x2 += x ** 2  # dodajemy bieżące x^2 do sumy x_i^2
    suma_x3 += x ** 3  # dodajemy bieżące x^3 do sumy x_i^3
    suma_x4 += x ** 4  # dodajemy bieżące x^4 do sumy x_i^4
    suma_y += y  # dodajemy bieżące y do sumy y_i
    suma_xy += x * y  # dodajemy iloczyn x*y do sumy x_i y_i
    suma_x2y += x ** 2 * y  # dodajemy iloczyn x^2*y do sumy x_i^2 y_i

macierz_ukladu = [  # budujemy macierz układu równań zgodnie ze slajdami
    [suma_x4, suma_x3, suma_x2],  # pierwszy wiersz odpowiada równaniu z sumami x_i^4, x_i^3 i x_i^2
    [suma_x3, suma_x2, suma_x],  # drugi wiersz odpowiada równaniu z sumami x_i^3, x_i^2 i x_i
    [suma_x2, suma_x, n]  # trzeci wiersz odpowiada równaniu z sumami x_i^2, x_i i n
]

wyrazy_wolne = [suma_x2y, suma_xy, suma_y]  # budujemy wektor prawej strony układu równań

macierz_kopia = []  # tworzymy pustą listę na kopię macierzy układu
for wiersz in macierz_ukladu:  # przechodzimy po wszystkich wierszach macierzy układu
    macierz_kopia.append(wiersz.copy())  # dodajemy kopię wiersza, aby nie zmieniać oryginalnej macierzy

wyrazy_wolne_kopia = wyrazy_wolne.copy()  # tworzymy kopię wektora wyrazów wolnych, aby nie zmieniać oryginału

rozwiazanie = rozwiaz_uklad_gaussa(macierz_kopia, wyrazy_wolne_kopia)  # rozwiązujemy układ równań metodą Gaussa

a = rozwiazanie[0]  # pierwszy element rozwiązania to współczynnik a przy x^2
b = rozwiazanie[1]  # drugi element rozwiązania to współczynnik b przy x
c = rozwiazanie[2]  # trzeci element rozwiązania to współczynnik c wyrazu wolnego

print("Współczynniki wielomianu aproksymacyjnego:")  # wypisujemy nagłówek dla współczynników
print("a =", a)  # wypisujemy współczynnik a
print("b =", b)  # wypisujemy współczynnik b
print("c =", c)  # wypisujemy współczynnik c

print("\nWielomian aproksymacyjny:")  # wypisujemy nagłówek dla równania wielomianu
print(f"y = {a} * x^2 + {b} * x + {c}")  # wypisujemy równanie wielomianu aproksymacyjnego

h = 0.0  # tworzymy zmienną h na sumę kwadratów błędów
for x, y in punkty:  # przechodzimy po wszystkich punktach
    h += (a * x**2 + b * x + c - y) ** 2  # dodajemy kwadrat różnicy między wartością z wielomianu a wartością rzeczywistą

print("\nSuma kwadratów błędów:")  # wypisujemy nagłówek dla błędu
print(h)  # wypisujemy końcową wartość funkcji błędu
```

**Dodatkowa wersja z zamianą wierszy żeby się nie kończyło gdy znajdzie 0**

```python
punkty = [(0.0, 2.0), (0.5, 2.48), (1.0, 2.84), (1.5, 3.0), (2.0, 2.91)]  # lista punktów pomiarowych w postaci (x, y)


def rozwiaz_uklad_gaussa(macierz, wyrazy_wolne):  # funkcja rozwiązuje układ równań liniowych metodą Gaussa
    n = len(wyrazy_wolne)  # liczba niewiadomych, czyli długość wektora wyrazów wolnych

    # eliminacja Gaussa z zamianą wierszy
    for i in range(n):  # przechodzimy po kolejnych kolumnach i wierszach głównych

        # szukanie najlepszego wiersza, czyli największego elementu w kolumnie i
        max_wiersz = i  # zakładamy, że najlepszy wiersz to aktualny wiersz i

        for k in range(i + 1, n):  # sprawdzamy wiersze znajdujące się poniżej aktualnego
            if abs(macierz[k][i]) > abs(macierz[max_wiersz][i]):  # porównujemy wartości bezwzględne elementów w kolumnie i
                max_wiersz = k  # zapamiętujemy numer wiersza z większym elementem

        # jeśli największy element jest zerem, układ nie ma jednoznacznego rozwiązania
        if macierz[max_wiersz][i] == 0:  # sprawdzamy, czy element główny jest równy zero
            raise ValueError("Układ nie ma jednoznacznego rozwiązania.")  # przerywamy działanie, bo nie można dalej dzielić przez zero

        # zamiana wierszy, jeśli trzeba
        if max_wiersz != i:  # sprawdzamy, czy znaleziony najlepszy wiersz jest inny niż aktualny
            macierz[i], macierz[max_wiersz] = macierz[max_wiersz], macierz[i]  # zamieniamy miejscami wiersze macierzy
            wyrazy_wolne[i], wyrazy_wolne[max_wiersz] = wyrazy_wolne[max_wiersz], wyrazy_wolne[i]  # zamieniamy też odpowiednie wyrazy wolne

        # zerowanie elementów pod przekątną
        for j in range(i + 1, n):  # przechodzimy po wierszach poniżej aktualnego wiersza
            wspolczynnik = macierz[j][i] / macierz[i][i]  # obliczamy współczynnik potrzebny do wyzerowania elementu pod przekątną

            for k in range(i, n):  # przechodzimy po kolumnach od aktualnej do ostatniej
                macierz[j][k] = macierz[j][k] - wspolczynnik * macierz[i][k]  # odejmujemy odpowiednią wielokrotność wiersza głównego

            wyrazy_wolne[j] = wyrazy_wolne[j] - wspolczynnik * wyrazy_wolne[i]  # aktualizujemy wyraz wolny w tym samym wierszu

    # podstawianie wsteczne
    rozwiazanie = [0.0] * n  # tworzymy listę na rozwiązania, początkowo wypełnioną zerami

    for i in range(n - 1, -1, -1):  # przechodzimy od ostatniego równania do pierwszego
        suma = 0.0  # tworzymy zmienną pomocniczą na sumę znanych składników

        for j in range(i + 1, n):  # przechodzimy po niewiadomych, które są już obliczone
            suma += macierz[i][j] * rozwiazanie[j]  # dodajemy znany składnik równania do sumy

        rozwiazanie[i] = (wyrazy_wolne[i] - suma) / macierz[i][i]  # obliczamy aktualną niewiadomą

    return rozwiazanie  # zwracamy listę rozwiązań układu


print("-------------------- ZADANIE 2 --------------------")  # wypisujemy nagłówek zadania

n = len(punkty)  # zapisujemy liczbę punktów pomiarowych

suma_x = 0.0  # suma wartości x
suma_x2 = 0.0  # suma wartości x^2
suma_x3 = 0.0  # suma wartości x^3
suma_x4 = 0.0  # suma wartości x^4
suma_y = 0.0  # suma wartości y
suma_xy = 0.0  # suma wartości x*y
suma_x2y = 0.0  # suma wartości x^2*y

for x, y in punkty:  # przechodzimy po wszystkich punktach
    suma_x += x  # dodajemy aktualne x do sumy x
    suma_x2 += x ** 2  # dodajemy x^2 do sumy x^2
    suma_x3 += x ** 3  # dodajemy x^3 do sumy x^3
    suma_x4 += x ** 4  # dodajemy x^4 do sumy x^4
    suma_y += y  # dodajemy aktualne y do sumy y
    suma_xy += x * y  # dodajemy iloczyn x*y do sumy
    suma_x2y += x ** 2 * y  # dodajemy iloczyn x^2*y do sumy


macierz_ukladu = [  # tworzymy macierz układu równań normalnych
    [suma_x4, suma_x3, suma_x2],  # pierwszy wiersz macierzy układu
    [suma_x3, suma_x2, suma_x],  # drugi wiersz macierzy układu
    [suma_x2, suma_x, n]  # trzeci wiersz macierzy układu
]  # koniec definicji macierzy układu

wyrazy_wolne = [suma_x2y, suma_xy, suma_y]  # tworzymy wektor wyrazów wolnych układu równań normalnych


macierz_kopia = []  # tworzymy pustą listę na kopię macierzy układu

for wiersz in macierz_ukladu:  # przechodzimy po każdym wierszu macierzy układu
    macierz_kopia.append(wiersz.copy())  # dodajemy kopię wiersza, żeby nie zmieniać oryginalnej macierzy

wyrazy_wolne_kopia = wyrazy_wolne.copy()  # tworzymy kopię wektora wyrazów wolnych


rozwiazanie = rozwiaz_uklad_gaussa(macierz_kopia, wyrazy_wolne_kopia)  # rozwiązujemy układ równań normalnych

a = rozwiazanie[0]  # pierwszy współczynnik wielomianu, stojący przy x^2
b = rozwiazanie[1]  # drugi współczynnik wielomianu, stojący przy x
c = rozwiazanie[2]  # trzeci współczynnik wielomianu, wyraz wolny


print("Współczynniki wielomianu aproksymacyjnego:")  # wypisujemy opis współczynników
print("a =", a)  # wypisujemy współczynnik a
print("b =", b)  # wypisujemy współczynnik b
print("c =", c)  # wypisujemy współczynnik c

print("\nWielomian aproksymacyjny:")  # wypisujemy opis wielomianu
print(f"y = {a} * x^2 + {b} * x + {c}")  # wypisujemy wzór wielomianu aproksymacyjnego


h = 0.0  # tworzymy zmienną na sumę kwadratów błędów

for x, y in punkty:  # przechodzimy po wszystkich punktach
    h += (a * x**2 + b * x + c - y) ** 2  # dodajemy kwadrat różnicy między wartością wielomianu a wartością y

print("\nSuma kwadratów błędów:")  # wypisujemy opis sumy błędów
print(h)  # wypisujemy sumę kwadratów błędów
```

## Wnioski

W zadaniu wyznaczono wielomian aproksymacyjny drugiego stopnia metodą najmniejszych kwadratów dla punktów:

$$
(0,2),\ (0.5,2.48),\ (1,2.84),\ (1.5,3),\ (2,2.91).
$$

Na podstawie wzorów ze slajdów zbudowano układ równań:

$$
a\sum x_i^4+b\sum x_i^3+c\sum x_i^2=\sum x_i^2y_i,
$$

$$
a\sum x_i^3+b\sum x_i^2+c\sum x_i=\sum x_iy_i,
$$

$$
a\sum x_i^2+b\sum x_i+nc=\sum y_i,
$$

a następnie rozwiązano go metodą Gaussa.

Otrzymane współczynniki są równe:

$$
a=-\frac{67}{175},\qquad b=\frac{2159}{1750},\qquad c=\frac{6953}{3500},
$$

czyli w przybliżeniu:

$$
a\approx -0.38285714285714284,
$$

$$
b\approx 1.2337142857142858,
$$

$$
c\approx 1.9865714285714287.
$$

Zatem wielomian aproksymacyjny ma postać:

$$
F(x)=-0.38285714285714284x^2+1.2337142857142858x+1.9865714285714287.
$$

Suma kwadratów błędów wynosi:

$$
h \approx 0.00170285714285714.
$$

Oznacza to, że otrzymany wielomian bardzo dobrze przybliża dane punkty.

---
# Zadanie 3

**Napisz funkcję, która dla zadanego zbioru punktów oraz stopnia wielomianu optymalnego wyznaczy współczynniki wielomianu oraz błąd aproksymacji metodą najmniejszych kwadratów.**

## O co chodzi w tym zadaniu?

Zadanie 3 jest uogólnieniem zadań 1 i 2.

W zadaniu 1 szukaliśmy prostej:

$$
F(x)=ax+b
$$

czyli wielomianu stopnia 1.

W zadaniu 2 szukaliśmy wielomianu drugiego stopnia:

$$
F(x)=ax^2+bx+c
$$

W zadaniu 3 mamy napisać funkcję, która zrobi to samo, ale dla **dowolnego stopnia wielomianu** podanego przez użytkownika.

Czyli jeśli podamy:

- `stopien = 1`, funkcja wyznaczy prostą,
- `stopien = 2`, funkcja wyznaczy wielomian kwadratowy,
- `stopien = 3`, funkcja wyznaczy wielomian trzeciego stopnia,
- itd.

## Wzór ogólny ze slajdów

Na slajdach funkcja aproksymująca ma postać:

$$
F(x)=a_0\phi_0(x)+a_1\phi_1(x)+\dots+a_m\phi_m(x),
$$

gdzie dla uproszczenia przyjmujemy:

$$
\phi_k(x)=x^k.
$$

Wtedy funkcję aproksymującą można zapisać jako wielomian:

$$
F(x)=a_0+a_1x+a_2x^2+\dots+a_mx^m.
$$

Współczynniki:

$$
a_0,a_1,a_2,\dots,a_m
$$

są szukanymi współczynnikami wielomianu aproksymacyjnego.

## Funkcja błędu

Zgodnie ze slajdami minimalizujemy funkcję błędu:

$$
h(a_0,a_1,\dots,a_m)=\sum_{i=1}^{n}\left(\sum_{j=0}^{m}a_jx_i^j-y_i\right)^2.
$$

Oznacza to, że dla każdego punktu sprawdzamy różnicę między:

- wartością wielomianu w punkcie \(x_i\),
- wartością rzeczywistą \(y_i\),

a potem sumujemy kwadraty tych różnic.

## Układ równań normalnych

Ze slajdów wynika, że aby znaleźć najlepsze współczynniki, trzeba rozwiązać układ równań:

$$
\sum_{j=0}^{m}a_j\sum_{i=1}^{n}x_i^{j+k}
=
\sum_{i=1}^{n}x_i^k y_i,
$$

dla:

$$
k=0,1,\dots,m.
$$

To oznacza, że dla wielomianu stopnia \(m\) powstaje układ:

$$
m+1
$$

równań z:

$$
m+1
$$

niewiadomymi.

## Jak program buduje układ równań?

Program tworzy macierz układu:

$$
A
$$

oraz wektor wyrazów wolnych:

$$
B.
$$

Elementy macierzy są liczone ze wzoru:

$$
A_{k,j}=\sum_{i=1}^{n}x_i^{k+j}
$$

a elementy wektora prawej strony:

$$
B_k=\sum_{i=1}^{n}x_i^k y_i.
$$

Dzięki temu program sam tworzy układ równań dla dowolnego stopnia wielomianu.

## Dane użyte w przykładzie

W programie użyto punktów z zadania 2:

$$
(0,2),\ (0.5,2.48),\ (1,2.84),\ (1.5,3),\ (2,2.91)
$$

oraz stopnia:

$$
m=2.
$$

Czyli szukamy wielomianu:

$$
F(x)=a_0+a_1x+a_2x^2.
$$

Dla tego przykładu wynik powinien zgadzać się z zadaniem 2, tylko współczynniki są zapisane w innej kolejności.

W zadaniu 2 pisaliśmy:

$$
F(x)=ax^2+bx+c.
$$

W zadaniu 3 piszemy:

$$
F(x)=a_0+a_1x+a_2x^2.
$$

Zatem:

$$
a_0=c,\qquad a_1=b,\qquad a_2=a.
$$

## Wynik dla danych z programu

Dla danych:

$$
(0,2),\ (0.5,2.48),\ (1,2.84),\ (1.5,3),\ (2,2.91)
$$

oraz stopnia:

$$
m=2
$$

otrzymujemy:

$$
a_0\approx 1.9865714285714287
$$

$$
a_1\approx 1.2337142857142858
$$

$$
a_2\approx -0.38285714285714284
$$

czyli:

$$
F(x)=1.9865714285714287+1.2337142857142858x-0.38285714285714284x^2.
$$

Po uporządkowaniu według malejących potęg:

$$
F(x)=-0.38285714285714284x^2+1.2337142857142858x+1.9865714285714287.
$$

Suma kwadratów błędów wynosi:

$$
h\approx 0.00170285714285714.
$$

## Kod

```python
print("-------------------- ZADANIE 3 --------------------")  # wypisujemy nagłówek zadania

def rozwiaz_uklad_gaussa(macierz, wyrazy_wolne):  # definiujemy funkcję rozwiązującą układ równań metodą Gaussa
    n = len(wyrazy_wolne)  # zapisujemy liczbę równań i niewiadomych

    for i in range(n):  # przechodzimy po kolejnych kolumnach eliminacji
        if macierz[i][i] == 0:  # sprawdzamy, czy element główny na przekątnej nie jest zerem
            raise ValueError("Na przekątnej pojawiło się zero - nie można wykonać eliminacji Gaussa.")  # jeśli jest zero, zgłaszamy błąd

        for j in range(i + 1, n):  # przechodzimy po wierszach znajdujących się pod aktualnym wierszem
            wspolczynnik = macierz[j][i] / macierz[i][i]  # obliczamy współczynnik potrzebny do wyzerowania elementu pod przekątną

            for k in range(i, n):  # przechodzimy po elementach aktualnego wiersza od kolumny i do końca
                macierz[j][k] = macierz[j][k] - wspolczynnik * macierz[i][k]  # wykonujemy eliminację, czyli zerujemy element pod przekątną

            wyrazy_wolne[j] = wyrazy_wolne[j] - wspolczynnik * wyrazy_wolne[i]  # wykonujemy tę samą operację na wektorze wyrazów wolnych

    rozwiazanie = [0.0] * n  # tworzymy listę na rozwiązanie układu

    for i in range(n - 1, -1, -1):  # wykonujemy podstawianie wsteczne od ostatniego równania do pierwszego
        suma = 0.0  # tworzymy zmienną pomocniczą na sumę znanych składników
        for j in range(i + 1, n):  # przechodzimy po niewiadomych, które zostały już obliczone
            suma += macierz[i][j] * rozwiazanie[j]  # dodajemy iloczyny współczynników i znanych rozwiązań

        rozwiazanie[i] = (wyrazy_wolne[i] - suma) / macierz[i][i]  # obliczamy bieżącą niewiadomą

    return rozwiazanie  # zwracamy rozwiązanie układu


def aproksymacja_najmniejszych_kwadratow(punkty, stopien):  # definiujemy funkcję aproksymacji dla dowolnego stopnia wielomianu
    liczba_wspolczynnikow = stopien + 1  # obliczamy liczbę współczynników, bo dla stopnia m mamy m+1 współczynników

    macierz_ukladu = []  # tworzymy pustą macierz układu równań
    wyrazy_wolne = []  # tworzymy pusty wektor wyrazów wolnych

    for i in range(liczba_wspolczynnikow):  # tworzymy kolejne równania układu
        wiersz = []  # tworzymy pusty wiersz macierzy

        for j in range(liczba_wspolczynnikow):  # tworzymy kolejne elementy w danym wierszu macierzy
            suma = 0.0  # zerujemy sumę dla elementu macierzy

            for x, y in punkty:  # przechodzimy po wszystkich punktach
                suma += x ** (i + j)  # dodajemy składnik x_i^(i+j), zgodnie ze wzorem na macierz układu

            wiersz.append(suma)  # dodajemy obliczoną sumę do wiersza macierzy

        macierz_ukladu.append(wiersz)  # dodajemy gotowy wiersz do macierzy układu

        suma = 0.0  # zerujemy sumę dla wyrazu wolnego

        for x, y in punkty:  # przechodzimy po wszystkich punktach
            suma += (x ** i) * y  # dodajemy składnik x_i^i * y_i, zgodnie ze wzorem na prawą stronę układu

        wyrazy_wolne.append(suma)  # dodajemy obliczoną sumę do wektora wyrazów wolnych

    macierz_kopia = []  # tworzymy pustą listę na kopię macierzy
    for wiersz in macierz_ukladu:  # przechodzimy po wszystkich wierszach macierzy
        macierz_kopia.append(wiersz.copy())  # kopiujemy wiersz, aby metoda Gaussa nie zmieniła oryginalnej macierzy

    wyrazy_wolne_kopia = wyrazy_wolne.copy()  # kopiujemy wektor wyrazów wolnych, aby zachować oryginał

    wspolczynniki = rozwiaz_uklad_gaussa(macierz_kopia, wyrazy_wolne_kopia)  # rozwiązujemy układ równań i otrzymujemy współczynniki wielomianu

    h = 0.0  # tworzymy zmienną h na sumę kwadratów błędów

    for x, y in punkty:  # przechodzimy po wszystkich punktach
        y_aprox = 0.0  # tworzymy zmienną na wartość wielomianu w punkcie x

        for i in range(len(wspolczynniki)):  # przechodzimy po wszystkich współczynnikach wielomianu
            y_aprox += wspolczynniki[i] * (x ** i)  # dodajemy składnik a_i * x^i do wartości wielomianu

        h += (y_aprox - y) ** 2  # dodajemy kwadrat różnicy między wartością aproksymowaną a rzeczywistą

    return wspolczynniki, h  # zwracamy współczynniki wielomianu i sumę kwadratów błędów


punkty = [(0.0, 2.0), (0.5, 2.48), (1.0, 2.84), (1.5, 3.0), (2.0, 2.91)]  # zapisujemy dane punkty
stopien = 2  # ustawiamy stopień wielomianu aproksymacyjnego

wspolczynniki, h = aproksymacja_najmniejszych_kwadratow(punkty, stopien)  # wywołujemy funkcję aproksymacji

print("Współczynniki wielomianu aproksymacyjnego:")  # wypisujemy nagłówek dla współczynników
for i in range(len(wspolczynniki)):  # przechodzimy po wszystkich współczynnikach
    print(f"a{i} = {wspolczynniki[i]}")  # wypisujemy współczynnik a_i

print("\nWielomian aproksymacyjny:")  # wypisujemy nagłówek dla wielomianu
print("y =", end=" ")  # rozpoczynamy wypisywanie wzoru wielomianu

for i in range(len(wspolczynniki)):  # przechodzimy po wszystkich współczynnikach
    if i == 0:  # sprawdzamy, czy wypisujemy pierwszy składnik
        print(f"{wspolczynniki[i]}", end="")  # wypisujemy wyraz wolny bez znaku plus na początku
    else:  # jeśli to nie jest pierwszy składnik
        print(f" + {wspolczynniki[i]} * x^{i}", end="")  # wypisujemy kolejny składnik wielomianu

print("\n\nSuma kwadratów błędów:")  # wypisujemy nagłówek dla błędu
print(h)  # wypisujemy sumę kwadratów błędów
```

**Wersja z zamianą wierszy żeby nie wywaliło się jak znajdzie 0**

```python
def rozwiaz_uklad_gaussa(A, b):  # funkcja rozwiązuje układ równań liniowych Ax = b metodą Gaussa
    n = len(b)  # liczba niewiadomych, czyli długość wektora wyrazów wolnych

    for i in range(n):  # przechodzimy po kolejnych kolumnach i wierszach głównych

        max_wiersz = i  # zakładamy, że najlepszy wiersz to aktualny wiersz i

        for k in range(i + 1, n):  # sprawdzamy wiersze poniżej aktualnego wiersza
            if abs(A[k][i]) > abs(A[max_wiersz][i]):  # szukamy największej wartości bezwzględnej w kolumnie i
                max_wiersz = k  # zapamiętujemy numer wiersza z największym elementem

        if A[max_wiersz][i] == 0:  # jeśli największy element w kolumnie jest zerem
            raise ValueError("Układ nie ma jednoznacznego rozwiązania.")  # układ nie ma jednoznacznego rozwiązania

        if max_wiersz != i:  # sprawdzamy, czy trzeba zamienić wiersze
            A[i], A[max_wiersz] = A[max_wiersz], A[i]  # zamieniamy wiersze w macierzy A
            b[i], b[max_wiersz] = b[max_wiersz], b[i]  # zamieniamy odpowiadające im wyrazy wolne

        for j in range(i + 1, n):  # przechodzimy po wierszach poniżej aktualnego wiersza
            wspolczynnik = A[j][i] / A[i][i]  # obliczamy współczynnik potrzebny do wyzerowania elementu pod przekątną

            for k in range(i, n):  # przechodzimy po kolumnach od aktualnej do ostatniej
                A[j][k] = A[j][k] - wspolczynnik * A[i][k]  # odejmujemy odpowiednią wielokrotność wiersza głównego

            b[j] = b[j] - wspolczynnik * b[i]  # aktualizujemy wyraz wolny w tym samym wierszu

    x = [0.0] * n  # tworzymy listę na rozwiązanie układu, początkowo wypełnioną zerami

    for i in range(n - 1, -1, -1):  # wykonujemy podstawianie wsteczne od ostatniego równania do pierwszego
        suma = 0.0  # zmienna pomocnicza na sumę znanych składników

        for j in range(i + 1, n):  # przechodzimy po niewiadomych, które są już obliczone
            suma += A[i][j] * x[j]  # dodajemy znany składnik równania do sumy

        x[i] = (b[i] - suma) / A[i][i]  # obliczamy aktualną niewiadomą

    return x  # zwracamy rozwiązanie układu


def aproksymacja_najmniejszych_kwadratow(punkty, stopien):  # funkcja liczy aproksymację średniokwadratową wielomianem danego stopnia
    n = stopien + 1  # liczba współczynników wielomianu

    A = []  # tworzymy pustą macierz układu równań normalnych
    B = []  # tworzymy pusty wektor wyrazów wolnych

    for i in range(n):  # przechodzimy po kolejnych równaniach układu
        wiersz = []  # tworzymy pusty wiersz macierzy A

        for j in range(n):  # przechodzimy po kolejnych kolumnach macierzy A
            suma = 0.0  # tworzymy zmienną na sumę

            for x, y in punkty:  # przechodzimy po wszystkich punktach
                suma += x ** (i + j)  # dodajemy x podniesione do odpowiedniej potęgi

            wiersz.append(suma)  # dodajemy obliczoną sumę do wiersza macierzy

        A.append(wiersz)  # dodajemy gotowy wiersz do macierzy A

        suma = 0.0  # zerujemy sumę dla wyrazu wolnego

        for x, y in punkty:  # przechodzimy po wszystkich punktach
            suma += y * (x ** i)  # dodajemy składnik y razy x do odpowiedniej potęgi

        B.append(suma)  # dodajemy obliczony wyraz wolny do wektora B

    A_kopia = []  # tworzymy pustą listę na kopię macierzy A

    for wiersz in A:  # przechodzimy po wierszach macierzy A
        A_kopia.append(wiersz.copy())  # kopiujemy każdy wiersz, żeby nie zmieniać oryginalnej macierzy

    B_kopia = B.copy()  # tworzymy kopię wektora wyrazów wolnych

    wspolczynniki = rozwiaz_uklad_gaussa(A_kopia, B_kopia)  # rozwiązujemy układ równań i otrzymujemy współczynniki wielomianu

    h = 0.0  # zmienna na sumę kwadratów błędów

    for x, y in punkty:  # przechodzimy po wszystkich punktach
        y_aprox = 0.0  # zmienna na wartość wielomianu aproksymacyjnego w punkcie x

        for i in range(len(wspolczynniki)):  # przechodzimy po wszystkich współczynnikach wielomianu
            y_aprox += wspolczynniki[i] * (x ** i)  # dodajemy kolejny składnik wielomianu

        h += (y_aprox - y) ** 2  # dodajemy kwadrat błędu dla aktualnego punktu

    return wspolczynniki, h  # zwracamy współczynniki wielomianu i sumę kwadratów błędów


punkty = [(0.0, 2.0), (0.5, 2.48), (1.0, 2.84), (1.5, 3.0), (2.0, 2.91)]  # lista punktów pomiarowych

stopien = 2  # stopień wielomianu aproksymacyjnego

wspolczynniki, blad = aproksymacja_najmniejszych_kwadratow(punkty, stopien)  # wywołujemy funkcję aproksymacji

print("Współczynniki wielomianu:")  # wypisujemy opis wyniku

for i in range(len(wspolczynniki)):  # przechodzimy po kolejnych współczynnikach
    print(f"a{i} = {wspolczynniki[i]}")  # wypisujemy współczynnik ai

print("\nWielomian aproksymacyjny:")  # wypisujemy opis wielomianu
print(f"y = {wspolczynniki[0]} + {wspolczynniki[1]} * x + {wspolczynniki[2]} * x^2")  # wypisujemy wzór wielomianu

print("\nSuma kwadratów błędów:")  # wypisujemy opis błędu
print(blad)  # wypisujemy sumę kwadratów błędów
```

## Wnioski

W zadaniu 3 napisano funkcję, która uogólnia aproksymację średniokwadratową na dowolny stopień wielomianu.

Zamiast osobno tworzyć wzory dla prostej lub dla wielomianu drugiego stopnia, program automatycznie buduje układ równań normalnych na podstawie wzoru ze slajdów:

$$
\sum_{j=0}^{m}a_j\sum_{i=1}^{n}x_i^{j+k}
=
\sum_{i=1}^{n}x_i^k y_i.
$$

Następnie układ ten jest rozwiązywany metodą Gaussa.

Dla danych z zadania 2 oraz stopnia:

$$
m=2
$$

otrzymano współczynniki:

$$
a_0\approx 1.9865714285714287
$$

$$
a_1\approx 1.2337142857142858
$$

$$
a_2\approx -0.38285714285714284
$$

czyli wielomian:

$$
F(x)=1.9865714285714287+1.2337142857142858x-0.38285714285714284x^2.
$$

Suma kwadratów błędów wynosi:

$$
h\approx 0.00170285714285714.
$$

Wynik jest zgodny z zadaniem 2, ponieważ dla stopnia 2 funkcja ogólna tworzy ten sam wielomian aproksymacyjny.

---

Zadanie 4*. Rozwiązania dwóch pierwszych zadań przedstaw na wykresie, zaznaczając również zaobserwowane wartości funkcji.

![alt text](wykres1.png)

![alt text](wykres2.png)

```python
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
```

---

# Lab 10
