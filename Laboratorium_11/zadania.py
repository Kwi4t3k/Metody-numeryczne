import math
# ==================== ZADANIE 1 ====================

def metoda_prostokatow(f, a, b, n):
    h = (b - a) / n

    suma = 0.0

    for i in range(n):
        x_srodek = a + (i + 0.5) * h
        suma += f(x_srodek)

    return h * suma


# ==================== ZADANIE 2 ====================

def metoda_trapezow(f, a, b, n):
    h = (b - a) / n

    suma = (f(a) + f(b)) / 2

    for i in range(1, n):
        x = a + i * h
        suma += f(x)

    return h * suma


# ==================== ZADANIE 3 ====================

def metoda_simpsona(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("W metodzie Simpsona liczba podprzedziałów n musi być parzysta.")

    h = (b - a) / n

    suma = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h

        if i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)

    return (h / 3) * suma


# ==================== ZADANIE 5 ====================

def blad_bezwzgledny(wartosc_dokladna, wartosc_przyblizona):
    return abs(wartosc_dokladna - wartosc_przyblizona)


def blad_wzgledny(wartosc_dokladna, wartosc_przyblizona):
    if wartosc_dokladna == 0:
        raise ValueError("Nie można policzyć błędu względnego, gdy wartość dokładna jest równa 0.")

    return abs(wartosc_dokladna - wartosc_przyblizona) / abs(wartosc_dokladna)


# ==================== FUNKCJE Z ZADANIA 4 ====================

def f1(x):
    return x**2


def f2(x):
    return math.cos(x)


def f3(x):
    return 1 / x


# ==================== TESTOWANIE METOD ====================

def testuj_calke(nazwa, f, a, b, wartosc_dokladna, n):
    print("\n" + nazwa)
    print("Przedział całkowania:", "[", a, ",", b, "]")
    print("Liczba podprzedziałów n =", n)
    print("Wartość dokładna =", wartosc_dokladna)

    wynik_prostokaty = metoda_prostokatow(f, a, b, n)
    wynik_trapezy = metoda_trapezow(f, a, b, n)
    wynik_simpson = metoda_simpsona(f, a, b, n)

    print("\nMetoda prostokątów:")
    print("Wynik =", wynik_prostokaty)
    print("Błąd bezwzględny =", blad_bezwzgledny(wartosc_dokladna, wynik_prostokaty))
    print("Błąd względny =", blad_wzgledny(wartosc_dokladna, wynik_prostokaty))

    print("\nMetoda trapezów:")
    print("Wynik =", wynik_trapezy)
    print("Błąd bezwzględny =", blad_bezwzgledny(wartosc_dokladna, wynik_trapezy))
    print("Błąd względny =", blad_wzgledny(wartosc_dokladna, wynik_trapezy))

    print("\nMetoda Simpsona:")
    print("Wynik =", wynik_simpson)
    print("Błąd bezwzględny =", blad_bezwzgledny(wartosc_dokladna, wynik_simpson))
    print("Błąd względny =", blad_wzgledny(wartosc_dokladna, wynik_simpson))


# ==================== ZADANIE 4 ====================

n = 100

testuj_calke(
    "a) całka od 0 do 1 z x^2 dx",
    f1,
    0,
    1,
    1 / 3,
    n
)

testuj_calke(
    "b) całka od 0 do pi/2 z cos(x) dx",
    f2,
    0,
    math.pi / 2,
    1,
    n
)

testuj_calke(
    "c) całka od e do e^2 z 1/x dx",
    f3,
    math.e,
    math.e**2,
    1,
    n
)