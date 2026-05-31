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