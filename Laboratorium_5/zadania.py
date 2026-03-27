# #zad1

# import time

# def zmierz_czas(funkcja, A, b): #poprawić 
#     start = time.perf_counter()
#     wynik = funkcja(A, b)
#     koniec = time.perf_counter()
#     return wynik, koniec - start

# def macierz_odwrotna_Gaussa_Jordana(macierz):
#     n = len(macierz)

#     for wiersz in macierz:
#         if len(wiersz) != n:
#             raise ValueError("Macierz musi być kwadratowa")

#     rozszerzona_macierz = []

#     for i in range(n):
#         wiersz = []

#         for j in range(n):
#             wiersz.append(macierz[i][j])
        
#         for j in range(n):
#             if i == j:
#                 wiersz.append(1)
#             else:
#                 wiersz.append(0)

#         rozszerzona_macierz.append(wiersz)

#     for i in range(n):
#         if rozszerzona_macierz[i][i] == 0:
#             znaleziono = False
#             for k in range(i+1, n):
#                 if rozszerzona_macierz[k][i] != 0:
#                     rozszerzona_macierz[i], rozszerzona_macierz[k] = rozszerzona_macierz[k], rozszerzona_macierz[i]
#                     znaleziono = True
#                     break
#             if not znaleziono:
#                 raise ValueError("Macierz nie ma odwrotności")
            
#         element_glowny = rozszerzona_macierz[i][i]
#         for j in range(2 * n):
#             rozszerzona_macierz[i][j] = rozszerzona_macierz[i][j] / element_glowny

#         for k in range(n):
#             if k != i:
#                 wspolczynnik = rozszerzona_macierz[k][i]
#                 for j in range(2 * n):
#                     rozszerzona_macierz[k][j] = rozszerzona_macierz[k][j] - wspolczynnik * rozszerzona_macierz[i][j]

#     odwrotna = []
#     for i in range(n):
#         wiersz = []
#         for j in range(n, 2 * n):
#             wiersz.append(rozszerzona_macierz[i][j])
#         odwrotna.append(wiersz)

#     return odwrotna

# def mnozenie_macierzy(macierz1, macierz2):
#     ilosc_wierszy_macierz1 = len(macierz1)
#     ilosc_wierszy_macierz2 = len(macierz2)
#     ilosc_kolumn_macierz1 = len(macierz1[0])
#     ilosc_kolumn_macierz2 = len(macierz2[0])

#     if ilosc_kolumn_macierz1 != ilosc_wierszy_macierz2:
#         raise ValueError("Nie da się pomnożyć tych macierzy")
    
#     wynik = []
#     for i in range(ilosc_wierszy_macierz1):
#         wiersz = []
#         for j in range(ilosc_kolumn_macierz2):
#             suma = 0
#             for k in range(ilosc_kolumn_macierz1):
#                 suma += macierz1[i][k] * macierz2[k][j]
#             wiersz.append(suma)
#         wynik.append(wiersz)

#     return wynik

# def rozwiarz_uklad_rownan(macierz_A, wektor_b):
#     b_macierz = [[b] for b in wektor_b]

#     A_odwrotna = macierz_odwrotna_Gaussa_Jordana(macierz_A)

#     wynik = mnozenie_macierzy(A_odwrotna, b_macierz)

#     return wynik

# #punkt a)
# A = [
#     [1, 2, 1],
#     [3, -7, 2],
#     [2, 4, 5]
# ]

# b = [-9, 61, -9]

# wynik = rozwiarz_uklad_rownan(A, b)

# print("Rozwiązanie układu równań a):")
# print("x =", wynik[0])
# print("y =", wynik[1])
# print("z =", wynik[2])
# print(zmierz_czas(rozwiarz_uklad_rownan(A, b)))

# #punkt b)
# def zeros(n,m):
#     macierz = []

#     for i in range(n):
#         wiersz = []
#         for j in range(m):
#             wiersz.append(0)
#         macierz.append(wiersz)

#     return macierz

# def tworzenie_macierzy(n):
#     A = zeros(n, n)
#     b = [11] + [0] * (n - 1)

#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 A[i][j] = 11
#             elif abs(i - j) == 1:
#                 A[i][j] = -5
    
#     return A, b

# n_8_A, n_8_b = tworzenie_macierzy(8)
# n_10_A, n_10_b = tworzenie_macierzy(10)

# wynik = rozwiarz_uklad_rownan(n_8_A, n_8_b)
# print("Rozwiązanie układu równań b) n=8:")
# for i in range(len(wynik)):
#     print(wynik[i])
# print(zmierz_czas(rozwiarz_uklad_rownan(n_8_A, n_8_b)))

# wynik = rozwiarz_uklad_rownan(n_10_A, n_10_b)
# print("Rozwiązanie układu równań b) n=10:")
# for i in range(len(wynik)):
#     print(wynik[i])
# print(zmierz_czas(rozwiarz_uklad_rownan(n_10_A, n_10_b)))

# #punkt c)
# def tworzenie_macierzy_gestej(n, m):
#     A = zeros(n, m)

#     for i in range(n):
#         for j in range(m):
#             if i == j:
#                 A[i][j] = 20.0
#             else:
#                 A[i][j] = float(i + j + 1)

#     x_prawdziwe = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

#     x_macierz = [[x] for x in x_prawdziwe]
#     b_macierz = mnozenie_macierzy(A, x_macierz)

#     b = []
#     for i in range(len(b_macierz)):
#         b.append(b_macierz[i][0])

#     return A, b, x_prawdziwe

# macierz, wektor, x = tworzenie_macierzy_gestej(10, 10)

# wynik = rozwiarz_uklad_rownan(macierz, wektor)
# print("Rozwiązanie układu równań b):")
# for i in range(len(wynik)):
#     print(wynik[i])
# print(zmierz_czas(rozwiarz_uklad_rownan(macierz, wektor)))

# zad2

# def zeros(n, m):
#     macierz = []
#     for i in range(n):
#         wiersz = []
#         for j in range(m):
#             wiersz.append(0.0)
#         macierz.append(wiersz)
#     return macierz


# def rozklad_LU_Doolittle(A):
#     n = len(A)

#     for wiersz in A:
#         if len(wiersz) != n:
#             raise ValueError("Macierz musi być kwadratowa")

#     L = zeros(n, n)
#     U = zeros(n, n)

#     # na przekątnej L są jedynki
#     for i in range(n):
#         L[i][i] = 1.0

#     for i in range(n):
#         # liczenie elementów U
#         for j in range(i, n):
#             suma = 0.0
#             for k in range(i):
#                 suma += L[i][k] * U[k][j]
#             U[i][j] = A[i][j] - suma

#         # liczenie elementów L
#         for j in range(i + 1, n):
#             suma = 0.0
#             for k in range(i):
#                 suma += L[j][k] * U[k][i]

#             if U[i][i] == 0:
#                 raise ValueError("Nie można wykonać rozkładu LU metodą Doolittle’a")

#             L[j][i] = (A[j][i] - suma) / U[i][i]

#     return L, U

# def podstawianie_w_przod(L, b):
#     n = len(L)
#     y = [0.0] * n

#     for i in range(n):
#         suma = 0.0
#         for j in range(i):
#             suma += L[i][j] * y[j]
#         y[i] = b[i] - suma

#     return y


# def podstawianie_w_tyl(U, y):
#     n = len(U)
#     x = [0.0] * n

#     for i in range(n - 1, -1, -1):
#         suma = 0.0
#         for j in range(i + 1, n):
#             suma += U[i][j] * x[j]

#         if U[i][i] == 0:
#             raise ValueError("Dzielenie przez zero w podstawianiu w tył")

#         x[i] = (y[i] - suma) / U[i][i]

#     return x

# def rozwiaz_uklad_Doolittle(A, b):
#     L, U = rozklad_LU_Doolittle(A)
#     y = podstawianie_w_przod(L, b)
#     x = podstawianie_w_tyl(U, y)
#     return x

# A = [
#     [1.0, 2.0, 1.0],
#     [3.0, -7.0, 2.0],
#     [2.0, 4.0, 5.0]
# ]

# b = [-9.0, 61.0, -9.0]

# wynik = rozwiaz_uklad_Doolittle(A, b)

# print("Rozwiązanie metodą Doolittle’a:")
# for i in range(len(wynik)):
#     print("x" + str(i + 1) + " =", wynik[i])

#zad3

# import time

# def zeros(n, m):
#     macierz = []
#     for i in range(n):
#         wiersz = []
#         for j in range(m):
#             wiersz.append(0.0)
#         macierz.append(wiersz)
#     return macierz


# def transpozycja(macierz):
#     liczba_wierszy = len(macierz)
#     liczba_kolumn = len(macierz[0])

#     wynik = []

#     for j in range(liczba_kolumn):
#         nowy_wiersz = []
#         for i in range(liczba_wierszy):
#             nowy_wiersz.append(macierz[i][j])
#         wynik.append(nowy_wiersz)

#     return wynik


# def podstawianie_w_przod(L, b):
#     n = len(L)
#     y = [0.0] * n

#     for i in range(n):
#         suma = 0.0
#         for j in range(i):
#             suma += L[i][j] * y[j]
#         y[i] = (b[i] - suma) / L[i][i]

#     return y


# def podstawianie_w_tyl(U, y):
#     n = len(U)
#     x = [0.0] * n

#     for i in range(n - 1, -1, -1):
#         suma = 0.0
#         for j in range(i + 1, n):
#             suma += U[i][j] * x[j]
#         x[i] = (y[i] - suma) / U[i][i]

#     return x


# def rozklad_Choleskiego(A):
#     n = len(A)

#     for wiersz in A:
#         if len(wiersz) != n:
#             raise ValueError("Macierz musi być kwadratowa")

#     L = zeros(n, n)

#     for i in range(n):
#         for j in range(i + 1):
#             suma = 0.0
#             for k in range(j):
#                 suma += L[i][k] * L[j][k]

#             if i == j:
#                 wartosc = A[i][i] - suma
#                 if wartosc <= 0:
#                     raise ValueError("Macierz nie jest dodatnio określona")
#                 L[i][j] = wartosc ** 0.5
#             else:
#                 L[i][j] = (A[i][j] - suma) / L[j][j]

#     return L


# def rozwiaz_uklad_Choleski(A, b):
#     L = rozklad_Choleskiego(A)
#     Lt = transpozycja(L)

#     y = podstawianie_w_przod(L, b)
#     x = podstawianie_w_tyl(Lt, y)

#     return x


# def wypisz_wektor(wektor):
#     for i in range(len(wektor)):
#         print("x" + str(i + 1) + " =", wektor[i])


# def tworzenie_macierzy_b(n):
#     A = zeros(n, n)
#     b = [11.0] + [0.0] * (n - 1)

#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 A[i][j] = 11.0
#             elif abs(i - j) == 1:
#                 A[i][j] = -5.0
#             else:
#                 A[i][j] = 0.0

#     return A, b


# def zmierz_czas(funkcja, A, b):
#     start = time.perf_counter()
#     wynik = funkcja(A, b)
#     koniec = time.perf_counter()
#     return wynik, koniec - start


# # przykład b) z zadania 1, n = 8
# A8, b8 = tworzenie_macierzy_b(8)
# wynik8, czas8 = zmierz_czas(rozwiaz_uklad_Choleski, A8, b8)

# print("Rozwiązanie metodą Cholesky’ego dla n = 8:")
# wypisz_wektor(wynik8)
# print("Czas:", czas8)


# # przykład b) z zadania 1, n = 10
# A10, b10 = tworzenie_macierzy_b(10)
# wynik10, czas10 = zmierz_czas(rozwiaz_uklad_Choleski, A10, b10)

# print("\nRozwiązanie metodą Cholesky’ego dla n = 10:")
# wypisz_wektor(wynik10)
# print("Czas:", czas10)

#zad 4

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