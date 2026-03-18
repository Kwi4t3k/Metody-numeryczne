#zad1
# import math

# def minor(macierz, usun_wiersz, usun_kolumne):
#     wynik = []

#     for i in range(len(macierz)):
#         if i == usun_wiersz:
#             continue

#         nowy_wiersz = []
#         for j in range(len(macierz[i])):
#             if j == usun_kolumne:
#                 continue
#             nowy_wiersz.append(macierz[i][j])

#         wynik.append(nowy_wiersz)

#     return wynik

# def wyznacznik_macierzy(macierz):
#     n = len(macierz)
    
#     for wiersz in macierz:
#         if len(wiersz) != n:
#             raise ValueError("Nie da się policzyc wyznacznika macierzy, która nie jest kwadratowa")
        
#     if n == 1:
#         return macierz[0][0]
    
#     if n == 2:
#         return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]
    
#     det = 0
#     for j in range(n):
#         podmacierz = minor(macierz, 0, j)
#         det += math.pow((-1), 0+j) * macierz[0][j] * wyznacznik_macierzy(podmacierz)

#     return det

# macierz = [
#     [2, 4, 6],
#     [0, 2, -1],
#     [-3, 3, 3]
# ]

# print("Wyznacznik macierzy: ", wyznacznik_macierzy(macierz))


#zad2
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


# macierz = [
#     [2, 4, 6],
#     [0, 2, -1],
#     [-3, 3, 3]
# ]

# print("Przed transpozycją macierzy:")
# for wiersz in macierz:
#     print(wiersz)

# wynik = transpozycja(macierz)

# print("Po transpozycji macierzy:")
# for wiersz in wynik:
#     print(wiersz)

#zad3
import math

def minor(macierz, usun_wiersz, usun_kolumne):
    wynik = []

    for i in range(len(macierz)):
        if i == usun_wiersz:
            continue

        nowy_wiersz = []
        for j in range(len(macierz[i])):
            if j == usun_kolumne:
                continue
            nowy_wiersz.append(macierz[i][j])

        wynik.append(nowy_wiersz)

    return wynik

def wyznacznik_macierzy(macierz):
    n = len(macierz)
    
    for wiersz in macierz:
        if len(wiersz) != n:
            raise ValueError("Nie da się policzyc wyznacznika macierzy, która nie jest kwadratowa")
        
    if n == 1:
        return macierz[0][0]
    
    if n == 2:
        return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]
    
    det = 0
    for j in range(n):
        podmacierz = minor(macierz, 0, j)
        det += math.pow((-1), 0+j) * macierz[0][j] * wyznacznik_macierzy(podmacierz)

    return det

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

def zeros(n,m):
    macierz = []

    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0)
        macierz.append(wiersz)

    return macierz

def macierz_odwrotna(macierz):
    n = len(macierz)
    d = wyznacznik_macierzy(macierz)

    if d == 0:
        raise ValueError("Macierz jest osobliwa, nie ma odwrotności")
    
    C = zeros(n, n)

    for i in range(n):
        for j in range(n):
            M = minor(macierz, i, j)
            C[i][j] = math.pow(-1, i+j) * wyznacznik_macierzy(M)

    Adj = transpozycja(C)
    
    wynik = zeros(n, n)
    for i in range(n):
        for j in range(n):
            wynik[i][j] = Adj[i][j] / d

    return wynik

macierz = [
    [2, 4, 6],
    [0, 2, -1],
    [-3, 3, 3]
]

wynik = macierz_odwrotna(macierz)

print("Macierz odwrotna Laplace:")
for wiersz in wynik:
    print(wiersz)





# # =========================
# # Zadanie 2
# # Transpozycja macierzy dowolnego rozmiaru
# # =========================
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


# # =========================
# # Funkcja pomocnicza:
# # dopełnienie algebraiczne
# # =========================
# def dopelnienie_algebraiczne(macierz, i, j):
#     return ((-1) ** (i + j)) * wyznacznik(minor(macierz, i, j))


# # =========================
# # Zadanie 3a
# # Macierz odwrotna metodą Laplace'a
# # =========================
# def odwrotna_laplace(macierz):
#     n = len(macierz)

#     # sprawdzenie, czy macierz jest kwadratowa
#     for wiersz in macierz:
#         if len(wiersz) != n:
#             raise ValueError("Macierz odwrotna istnieje tylko dla macierzy kwadratowej.")

#     det = wyznacznik(macierz)

#     if det == 0:
#         raise ValueError("Macierz nie ma odwrotności, bo wyznacznik jest równy 0.")

#     # przypadek 1x1
#     if n == 1:
#         return [[1 / macierz[0][0]]]

#     # macierz dopełnień algebraicznych
#     macierz_dopelnien = []
#     for i in range(n):
#         wiersz = []
#         for j in range(n):
#             wiersz.append(dopelnienie_algebraiczne(macierz, i, j))
#         macierz_dopelnien.append(wiersz)

#     # macierz dołączona = transpozycja macierzy dopełnień
#     macierz_dolaczona = transpozycja(macierz_dopelnien)

#     # mnożenie przez 1/det
#     wynik = []
#     for i in range(n):
#         wiersz = []
#         for j in range(n):
#             wiersz.append(macierz_dolaczona[i][j] / det)
#         wynik.append(wiersz)

#     return wynik


# # =========================
# # Zadanie 3b
# # Macierz odwrotna metodą Gaussa-Jordana
# # =========================
# def odwrotna_gauss_jordan(macierz):
#     n = len(macierz)

#     # sprawdzenie, czy macierz jest kwadratowa
#     for wiersz in macierz:
#         if len(wiersz) != n:
#             raise ValueError("Macierz odwrotna istnieje tylko dla macierzy kwadratowej.")

#     # tworzymy kopię macierzy jako float
#     A = []
#     for i in range(n):
#         wiersz = []
#         for j in range(n):
#             wiersz.append(float(macierz[i][j]))
#         A.append(wiersz)

#     # tworzymy macierz jednostkową
#     I = []
#     for i in range(n):
#         wiersz = []
#         for j in range(n):
#             if i == j:
#                 wiersz.append(1.0)
#             else:
#                 wiersz.append(0.0)
#         I.append(wiersz)

#     # łączymy [A | I]
#     rozszerzona = []
#     for i in range(n):
#         rozszerzona.append(A[i] + I[i])

#     # algorytm Gaussa-Jordana
#     for i in range(n):
#         # jeśli element główny jest równy 0, zamieniamy wiersze
#         if rozszerzona[i][i] == 0:
#             znaleziono = False
#             for k in range(i + 1, n):
#                 if rozszerzona[k][i] != 0:
#                     rozszerzona[i], rozszerzona[k] = rozszerzona[k], rozszerzona[i]
#                     znaleziono = True
#                     break
#             if not znaleziono:
#                 raise ValueError("Macierz nie ma odwrotności.")

#         # dzielenie całego wiersza przez element główny
#         element_glowny = rozszerzona[i][i]
#         for j in range(2 * n):
#             rozszerzona[i][j] = rozszerzona[i][j] / element_glowny

#         # zerowanie pozostałych elementów w kolumnie
#         for k in range(n):
#             if k != i:
#                 wspolczynnik = rozszerzona[k][i]
#                 for j in range(2 * n):
#                     rozszerzona[k][j] = rozszerzona[k][j] - wspolczynnik * rozszerzona[i][j]

#     # prawa część to macierz odwrotna
#     odwrotna = []
#     for i in range(n):
#         wiersz = []
#         for j in range(n, 2 * n):
#             wiersz.append(rozszerzona[i][j])
#         odwrotna.append(wiersz)

#     return odwrotna


# # =========================
# # Zadanie 4
# # Mnożenie dwóch macierzy
# # =========================
# def mnozenie_macierzy(macierz1, macierz2):
#     liczba_wierszy_1 = len(macierz1)
#     liczba_kolumn_1 = len(macierz1[0])
#     liczba_wierszy_2 = len(macierz2)
#     liczba_kolumn_2 = len(macierz2[0])

#     if liczba_kolumn_1 != liczba_wierszy_2:
#         raise ValueError("Nie można pomnożyć tych macierzy.")

#     wynik = []

#     for i in range(liczba_wierszy_1):
#         wiersz = []
#         for j in range(liczba_kolumn_2):
#             suma = 0
#             for k in range(liczba_kolumn_1):
#                 suma += macierz1[i][k] * macierz2[k][j]
#             wiersz.append(suma)
#         wynik.append(wiersz)

#     return wynik


# # =========================
# # Funkcja pomocnicza
# # ładne wypisywanie macierzy
# # =========================
# def wypisz_macierz(macierz):
#     for wiersz in macierz:
#         print(wiersz)


# # =========================
# # Zadanie 5
# # A * A^-1 oraz A^-1 * A
# # =========================
# A = [
#     [2, 1, 1],
#     [1, 3, 2],
#     [1, 0, 0]
# ]

# print("Macierz A:")
# wypisz_macierz(A)

# print("\nZadanie 1 - wyznacznik macierzy A:")
# print(wyznacznik(A))

# print("\nZadanie 2 - transpozycja macierzy A:")
# wypisz_macierz(transpozycja(A))

# print("\nZadanie 3a - macierz odwrotna metodą Laplace'a:")
# A_odwrotna_laplace = odwrotna_laplace(A)
# wypisz_macierz(A_odwrotna_laplace)

# print("\nZadanie 3b - macierz odwrotna metodą Gaussa-Jordana:")
# A_odwrotna_gauss = odwrotna_gauss_jordan(A)
# wypisz_macierz(A_odwrotna_gauss)

# print("\nZadanie 4 - przykład mnożenia dwóch macierzy:")
# B = [
#     [1, 2, 0],
#     [0, 1, 1],
#     [4, 0, 1]
# ]
# print("Macierz B:")
# wypisz_macierz(B)

# print("\nA * B:")
# wypisz_macierz(mnozenie_macierzy(A, B))

# print("\nZadanie 5 - A * A^-1:")
# wypisz_macierz(mnozenie_macierzy(A, A_odwrotna_laplace))

# print("\nZadanie 5 - A^-1 * A:")
# wypisz_macierz(mnozenie_macierzy(A_odwrotna_laplace, A))

# print("\nPorównanie:")
# print("Oba wyniki powinny dać macierz jednostkową albo bardzo do niej zbliżoną.")