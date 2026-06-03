# Zad 1
# Metoda Crude Monte Carlo

import random
import math


print("-------------------- ZADANIE 1 --------------------")


def monte_carlo_1d(f, a, b, N):
    suma = 0.0

    for i in range(N):
        x = random.uniform(a, b)
        suma += f(x)

    return (b - a) * suma / N


def monte_carlo_2d(f, ax, bx, ay, by, N):
    suma = 0.0

    for i in range(N):
        x = random.uniform(ax, bx)
        y = random.uniform(ay, by)
        suma += f(x, y)

    pole_obszaru = (bx - ax) * (by - ay)

    return pole_obszaru / N * suma


def oszacuj_N_1d(f, a, b, dokladnosc=0.005, N_probne=10000):
    wartosci = []

    for i in range(N_probne):
        x = random.uniform(a, b)
        wartosci.append(f(x))

    srednia = sum(wartosci) / N_probne

    wariancja = 0.0
    for wartosc in wartosci:
        wariancja += (wartosc - srednia) ** 2

    wariancja = wariancja / (N_probne - 1)
    odchylenie = math.sqrt(wariancja)

    N = ((b - a) * odchylenie / dokladnosc) ** 2

    return math.ceil(N)


def oszacuj_N_2d(f, ax, bx, ay, by, dokladnosc=0.005, N_probne=10000):
    wartosci = []

    for i in range(N_probne):
        x = random.uniform(ax, bx)
        y = random.uniform(ay, by)
        wartosci.append(f(x, y))

    srednia = sum(wartosci) / N_probne

    wariancja = 0.0
    for wartosc in wartosci:
        wariancja += (wartosc - srednia) ** 2

    wariancja = wariancja / (N_probne - 1)
    odchylenie = math.sqrt(wariancja)

    pole_obszaru = (bx - ax) * (by - ay)

    N = (pole_obszaru * odchylenie / dokladnosc) ** 2

    return math.ceil(N)


def f1(x):
    return x ** 2


def f2(x):
    return 1 / x


def f3(x, y):
    return math.cos(x) + y + 1


N = 100000

wynik_a = monte_carlo_1d(f1, 0, 1, N)
dokladny_a = 1 / 3

wynik_b = monte_carlo_1d(f2, math.e, math.e ** 2, N)
dokladny_b = 1

wynik_c = monte_carlo_2d(f3, 0, 2, -math.pi, math.pi, N)
dokladny_c = 2 * math.pi * (math.sin(2) + 2)


print("\na) całka od 0 do 1 z x^2 dx")
print("Wynik Monte Carlo:", wynik_a)
print("Wartość dokładna:", dokladny_a)
print("Błąd bezwzględny:", abs(dokladny_a - wynik_a))

print("\nb) całka od e do e^2 z 1/x dx")
print("Wynik Monte Carlo:", wynik_b)
print("Wartość dokładna:", dokladny_b)
print("Błąd bezwzględny:", abs(dokladny_b - wynik_b))

print("\nc) całka podwójna po D = [0,2] x [-pi,pi]")
print("Wynik Monte Carlo:", wynik_c)
print("Wartość dokładna:", dokladny_c)
print("Błąd bezwzględny:", abs(dokladny_c - wynik_c))


print("\nOszacowanie liczby punktów dla dokładności do 2 cyfr po przecinku:")

N_a = oszacuj_N_1d(f1, 0, 1)
N_b = oszacuj_N_1d(f2, math.e, math.e ** 2)
N_c = oszacuj_N_2d(f3, 0, 2, -math.pi, math.pi)

print("a) potrzebne N ≈", N_a)
print("b) potrzebne N ≈", N_b)
print("c) potrzebne N ≈", N_c)

# Zad 2

import random
import math


print("-------------------- ZADANIE 2 --------------------")


def objetosc_kuli_jednostkowej(N):
    zaakceptowane = 0

    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)

        if x ** 2 + y ** 2 + z ** 2 <= 1:
            zaakceptowane += 1

    objetosc_szescianu = 2 ** 3

    return objetosc_szescianu * zaakceptowane / N


def objetosc_wspolna_szescianu_i_kuli(N):
    r = 2
    bok = 3

    polowa_boku = bok / 2

    zaakceptowane = 0

    for i in range(N):
        x = random.uniform(-polowa_boku, polowa_boku)
        y = random.uniform(-polowa_boku, polowa_boku)
        z = random.uniform(-polowa_boku, polowa_boku)

        if x ** 2 + y ** 2 + z ** 2 <= r ** 2:
            zaakceptowane += 1

    objetosc_szescianu = bok ** 3

    return objetosc_szescianu * zaakceptowane / N


N = 200000

wynik_kula = objetosc_kuli_jednostkowej(N)
dokladna_kula = 4 / 3 * math.pi

wynik_wspolna = objetosc_wspolna_szescianu_i_kuli(N)


print("\na) Objętość kuli jednostkowej")
print("Wynik Monte Carlo:", wynik_kula)
print("Wartość dokładna:", dokladna_kula)
print("Błąd bezwzględny:", abs(dokladna_kula - wynik_kula))

print("\nb) Objętość części wspólnej sześcianu i kuli")
print("Stosunek promienia kuli do boku sześcianu: 2:3")
print("Przyjmujemy r = 2 oraz bok = 3")
print("Wynik Monte Carlo:", wynik_wspolna)