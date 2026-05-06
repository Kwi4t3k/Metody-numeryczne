# zad 1
import math

print("------------------------ZADANIE 1--------------------------")

def roznica_w_przod(f, x, h):
    return (f(x + h) - f(x)) / h

def blad_wzgledny(wartosc_dokladna, wartosc_przyblizona):
    if wartosc_dokladna != 0:
        return abs(wartosc_dokladna - wartosc_przyblizona) / abs(wartosc_dokladna)
    else:
        raise ValueError("Nie można policzyć błędu względnego, gdy wartość dokładna jest równa 0.")

def f1(x):
    return 2 * x**2 + 2

def df1(x):
    return 4 * x

def f2(x):
    return 2 * x**4 - x**2 + 3*x - 7

def df2(x):
    return 8 * x**3 - 2 * x + 3

def f3(x):
    return x**2 * math.exp(x)

def df3(x):
    return math.exp(x) * (x**2 + 2 * x)

def porownaj_pochodna(nazwa, f, df, x, h_lista):
    print("\n" + nazwa)
    print("x =", x)
    print("h              pochodna numeryczna        pochodna dokładna          błąd względny")

    for h in h_lista:
        pochodna_numeryczna = roznica_w_przod(f, x, h)
        pochodna_dokladna = df(x)
        blad = blad_wzgledny(pochodna_dokladna, pochodna_numeryczna)

        print(f"{h:<14} {pochodna_numeryczna:<25} {pochodna_dokladna:<25} {blad}")

x0 = 1.0

h_lista = [10**(-2), 10**(-4)]

porownaj_pochodna("a) f(x) = 2x^2 + 2", f1, df1, x0, h_lista)
porownaj_pochodna("b) f(x) = 2x^4 - x^2 + 3x - 7", f2, df2, x0, h_lista)
porownaj_pochodna("c) f(x) = x^2e^x", f3, df3, x0, h_lista)

# zad 2

print("------------------------ZADANIE 2--------------------------")

def roznica_wsteczna(f, x, h):
    return (f(x) - f(x - h)) / h
    
def roznica_centralna_dwupunktowa(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def blad_wzgledny(wartosc_dokladna, wartosc_przyblizona):
    if wartosc_dokladna != 0:
        return abs(wartosc_dokladna - wartosc_przyblizona) / abs(wartosc_dokladna)
    else:
        raise ValueError("Nie można policzyć błędu względnego, gdy wartość dokładna jest równa 0.")

def f1(x):
    return 2 * x**2 + 2

def df1(x):
    return 4 * x

def f2(x):
    return 2 * x**4 - x**2 + 3*x - 7

def df2(x):
    return 8 * x**3 - 2 * x + 3

def f3(x):
    return x**2 * math.exp(x)

def df3(x):
    return math.exp(x) * (x**2 + 2 * x)

def porownaj_metody(nazwa, f, df, x, h_lista):
    print("\n" + nazwa)
    print("x =", x)
    print("h              metoda          pochodna numeryczna        pochodna dokładna          błąd względny")

    for h in h_lista:
        pochodna_dokladna = df(x)

        pochodna_wsteczna = roznica_wsteczna(f, x, h)
        blad_wsteczny = blad_wzgledny(pochodna_dokladna, pochodna_wsteczna)

        print(f"{h:<14} {'wsteczna':<15} {pochodna_wsteczna:<25} {pochodna_dokladna:<25} {blad_wsteczny}")

        pochodna_centralna = roznica_centralna_dwupunktowa(f, x, h)
        blad_centralny = blad_wzgledny(pochodna_dokladna, pochodna_centralna)

        print(f"{h:<14} {'centralna':<15} {pochodna_centralna:<25} {pochodna_dokladna:<25} {blad_centralny}")

x0 = 1.0

h_lista = [10**(-2), 10**(-4)]

porownaj_metody("a) f(x) = 2x^2 + 2", f1, df1, x0, h_lista)
porownaj_metody("b) f(x) = 2x^4 - x^2 + 3x - 7", f2, df2, x0, h_lista)
porownaj_metody("c) f(x) = x^2e^x", f3, df3, x0, h_lista)

# zad 3

print("------------------------ZADANIE 3--------------------------")

def roznica_w_przod_trzypunktowa(f, x, h):
    return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)

def roznica_wsteczna_trzypunktowa(f, x, h):
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)
    
def roznica_centralna_czteropunktowa(f, x, h):
    return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h)

def blad_wzgledny(wartosc_dokladna, wartosc_przyblizona):
    if wartosc_dokladna != 0:
        return abs(wartosc_dokladna - wartosc_przyblizona) / abs(wartosc_dokladna)
    else:
        raise ValueError("Nie można policzyć błędu względnego, gdy wartość dokładna jest równa 0.")

def f1(x):
    return 2 * x**2 + 2

def df1(x):
    return 4 * x

def f2(x):
    return 2 * x**4 - x**2 + 3*x - 7

def df2(x):
    return 8 * x**3 - 2 * x + 3

def f3(x):
    return x**2 * math.exp(x)

def df3(x):
    return math.exp(x) * (x**2 + 2 * x)

def porownaj_metody(nazwa, f, df, x, h_lista):
    print("\n" + nazwa)
    print("x =", x)
    print("h              metoda                    pochodna numeryczna        pochodna dokładna          błąd względny")

    for h in h_lista:
        pochodna_dokladna = df(x)

        pochodna_przod = roznica_w_przod_trzypunktowa(f, x, h)
        blad_przod = blad_wzgledny(pochodna_dokladna, pochodna_przod)

        print(f"{h:<14} {'w przód 3-punktowa':<25} {pochodna_przod:<25} {pochodna_dokladna:<25} {blad_przod}")

        pochodna_wsteczna = roznica_wsteczna_trzypunktowa(f, x, h)
        blad_wsteczny = blad_wzgledny(pochodna_dokladna, pochodna_wsteczna)

        print(f"{h:<14} {'wsteczna 3-punktowa':<25} {pochodna_wsteczna:<25} {pochodna_dokladna:<25} {blad_wsteczny}")

        pochodna_centralna = roznica_centralna_czteropunktowa(f, x, h)
        blad_centralny = blad_wzgledny(pochodna_dokladna, pochodna_centralna)

        print(f"{h:<14} {'centralna 4-punktowa':<25} {pochodna_centralna:<25} {pochodna_dokladna:<25} {blad_centralny}")

x0 = 1.0

h_lista = [10**(-2), 10**(-4)]

porownaj_metody("a) f(x) = 2x^2 + 2", f1, df1, x0, h_lista)
porownaj_metody("b) f(x) = 2x^4 - x^2 + 3x - 7", f2, df2, x0, h_lista)
porownaj_metody("c) f(x) = x^2e^x", f3, df3, x0, h_lista)

# zad 4

print("-------------------- ZADANIE 4 --------------------")

def baza_lagrange(punkty, i, x):
    xi =  punkty[i][0]

    wynik = 1.0

    for j in range(len(punkty)):
        if j != i:
            xj = punkty[j][0]
            wynik *= (x - xj) / (xi - xj)

    return wynik

def wielomian_lagrange(punkty, x):
    suma = 0.0

    for i in range(len(punkty)):
        yi = punkty[i][1]
        suma += yi * baza_lagrange(punkty, i, x)

    return suma

def pochodna_lagrange_centralna(punkty, x, h):
    return (wielomian_lagrange(punkty, x + h) - wielomian_lagrange(punkty, x - h)) / (2 * h)

punkty = [(1, 4), (2, 10), (3, 20), (4, 34), (5, 52)]

X = 3.5
h = 10**(-4)

wynik = pochodna_lagrange_centralna(punkty, X, h)

print("Węzły interpolacji:")
print(punkty)

print("\nPunkt, w którym liczymy pochodną:")
print("x =", X)

print("\nKrok:")
print("h =", h)

print("\nPrzybliżona wartość pochodnej:")
print("f'(", X, ") =", wynik)