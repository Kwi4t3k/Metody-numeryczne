# zad 1 ------------------------------
def schemat_Hornera(wspolczynniki, z):
    p = wspolczynniki[0]

    for i in range(1, len(wspolczynniki)):
        # print(p) # kroki
        p = p * z + wspolczynniki[i]

    return p

# wspolczynniki = [3,2,-1,5]
# z = complex(2, 0)

# wynik = schemat_Hornera(wspolczynniki, z)
# print(wynik)

# zad 2 --------------------------

def schemat_Hornera_pochodne(wspolczynniki, z):
    p = wspolczynniki[0]
    dp = 0
    ddp = 0

    for i in range(1, len(wspolczynniki)):
        ddp = ddp * z + 2 * dp
        dp = dp * z + p
        p = p * z + wspolczynniki[i]

    return p, dp, ddp

# zad 3 --------------------------

import cmath

def metoda_laguerre_jeden_pierwiastek(wspolczynniki, z0, epsilon=1e-6, max_iteracji=100):
    z = complex(z0)
    n = len(wspolczynniki) - 1

    for k in range(max_iteracji):
        P, P_prim, P_2prim = schemat_Hornera_pochodne(wspolczynniki, z)

        if abs(P) < epsilon:
            return z
        
        G = P_prim / P
        H = G**2 - P_2prim / P

        pierwiastek = cmath.sqrt((n - 1) * (n * H - G**2))

        mianownik_plus = G + pierwiastek
        mianownik_minus = G - pierwiastek

        if abs(mianownik_plus) > abs(mianownik_minus):
            mianownik = mianownik_plus
        else:
            mianownik = mianownik_minus

        if abs(mianownik) == 0:
            z = z + complex(epsilon, epsilon)
            continue

        a = n / mianownik

        z_nowe = z - a

        if abs(a) < epsilon:
            return z_nowe
        
        z = z_nowe

    return z

# zad 4 --------------------------

def deflacja(wspolczynniki, pierwiastek):
    nowe_wspolczynniki = [complex(wspolczynniki[0])]

    for i in range(1, len(wspolczynniki) - 1):
        nowy = wspolczynniki[i] + pierwiastek * nowe_wspolczynniki[-1]
        nowe_wspolczynniki.append(nowy)

    reszta = wspolczynniki[-1] + pierwiastek * nowe_wspolczynniki[-1]

    return nowe_wspolczynniki, reszta

def pierwiastki_stopnia_drugiego(wspolczynniki):
    a = wspolczynniki[0]
    b = wspolczynniki[1]
    c = wspolczynniki[2]

    delta = b**2 - 4 * a * c

    z1 = (-b + cmath.sqrt(delta)) / (2 * a)
    z2 = (-b - cmath.sqrt(delta)) / (2 * a)

    return z1, z2

def metoda_laguerre_wszystkie_pierwiastki(wspolczynniki, z0=0, epsilon=1e-6):
    pierwotny_wielomian = wspolczynniki.copy()
    aktualny_wielomian = wspolczynniki.copy()
    pierwiastki = []

    while len(aktualny_wielomian) > 3:
        pierwiastek = metoda_laguerre_jeden_pierwiastek(aktualny_wielomian, z0, epsilon)

        pierwiastek = metoda_laguerre_jeden_pierwiastek(pierwotny_wielomian, pierwiastek, epsilon)

        pierwiastki.append(pierwiastek)

        aktualny_wielomian, reszta = deflacja(aktualny_wielomian, pierwiastek)

    z1, z2 = pierwiastki_stopnia_drugiego(aktualny_wielomian)

    pierwiastki.append(z1)
    pierwiastki.append(z2)

    return pierwiastki

# uładnienie wyniku
def ladnie(z, epsilon=1e-8):
    if abs(z.imag) < epsilon:
        return z.real

    if abs(z.real) < epsilon:
        return complex(0, z.imag)

    return z

# zad 5 --------------------------

def testuj_wielomian(nazwa, wspolczynniki):
    print("\n" + "=" * 60)
    print(nazwa)
    print("Współczynniki:", wspolczynniki)

    z = complex(2, 0)

    print("\nZadanie 1 - wartość wielomianu w punkcie z = 2:")
    print("P(2) =", ladnie(schemat_Hornera(wspolczynniki, z)))

    print("\nZadanie 2 - wartość P(2), P'(2), P''(2):")
    P, P_prim, P_2prim = schemat_Hornera_pochodne(wspolczynniki, z)

    print("P(2)   =", ladnie(P))
    print("P'(2)  =", ladnie(P_prim))
    print("P''(2) =", ladnie(P_2prim))

    print("\nZadanie 3 - jeden pierwiastek metodą Laguerre'a:")
    jeden_pierwiastek = metoda_laguerre_jeden_pierwiastek(wspolczynniki, z0=0)
    print("Jeden pierwiastek =", ladnie(jeden_pierwiastek))

    print("\nZadanie 4 - wszystkie pierwiastki metodą Laguerre'a:")
    pierwiastki = metoda_laguerre_wszystkie_pierwiastki(wspolczynniki, z0=0)

    for i in range(len(pierwiastki)):
        print(f"z{i + 1} =", ladnie(pierwiastki[i]))


# a) w(x) = x^3 - 6x^2 + 11x - 6
wielomian_A = [1, -6, 11, -6]

# b) w(x) = x^3 - 6x^2 + 11x - 1
wielomian_B = [1, -6, 11, -1]

# c) przykład ze strony 27 wykładu
wielomian_C = [
    39205740,
    -147747493,
    173235338,
    2869080,
    -158495872,
    118949888,
    -28016640
]

# d) przykład ze strony 27 wykładu + 1
wielomian_D = [
    39205740,
    -147747493,
    173235338,
    2869080,
    -158495872,
    118949888,
    -28016639
]


testuj_wielomian(
    "a) w(x) = x^3 - 6x^2 + 11x - 6",
    wielomian_A
)

testuj_wielomian(
    "b) w(x) = x^3 - 6x^2 + 11x - 1",
    wielomian_B
)

testuj_wielomian(
    "c) przykład ze strony 27 wykładu",
    wielomian_C
)

testuj_wielomian(
    "d) przykład ze strony 27 wykładu + 1",
    wielomian_D
)