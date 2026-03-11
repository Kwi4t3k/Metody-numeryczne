#zad1

import math

def normy_wektora(wektor):

    # norma euklidesowa
    suma_kwadratow = 0
    for x in wektor:
        suma_kwadratow += x**2
    norma_euklidesowa = math.sqrt(suma_kwadratow)

    # norma Manhattan
    norma_manhattan = 0
    for x in wektor:
        norma_manhattan += abs(x)

    # norma maximum
    # norma_max = max(abs(x) for x in wektor)
    norma_max = 0

    for x in wektor:
        wartosc_bezwzgledna = abs(x)

        if wartosc_bezwzgledna > norma_max:
            norma_max = wartosc_bezwzgledna

    return norma_euklidesowa, norma_manhattan, norma_max

wektor = [3, 4, 5]

euklidesowa, manhattan, maksimum = normy_wektora(wektor)

print("Norma euklidesowa:", euklidesowa)
print("Norma Manhattan:", manhattan)
print("Norma maximum:", maksimum)

#zad2

import math

def odleglosci(P, Q):
    p1, p2 = P
    q1, q2 = Q

    # metryka euklidesowa
    euklidesowa = math.sqrt(math.pow((q1 - p1), 2) + math.pow((q2 - p2), 2))

    #matryka Manhattan
    manhattan = abs(p1 - q1) + abs(p2 - q2)

    #metryka rzeka
    if p1 == q1:
        rzeka = abs(p2 - q2)
    else:
        rzeka = abs(p1 - q1) + abs(p2) + abs(q2)

    # metryka kolejowa
    det = p1 * q2 - p2 * q1
    if det == 0:
        kolejowa = math.sqrt(math.pow((q1 - p1), 2) + math.pow((q2 - p2), 2))
    else:
        kolejowa = math.sqrt(math.pow((0 - p1), 2) + math.pow((0 - p2), 2)) + math.sqrt(math.pow((0 - q1), 2) + math.pow((0 - q2), 2))

    return euklidesowa, manhattan, rzeka, kolejowa

punktP = (2, 3)
punktQ = (5, 7)

euklidesowa, manhattan, rzeka, kolejowa = odleglosci(punktP, punktQ)

print("Norma euklidesowa:", euklidesowa)
print("Norma Manhattan:", manhattan)
print("Norma rzeka:", rzeka)
print("Norma kolejowa/centrum:", kolejowa)

#zad3

import math

def normy_macierzy(macierz):
    wiersze = len(macierz)
    kolumny = len(macierz[0])

    # norma Frobeniusa
    suma_kwadratow = 0
    for i in range(wiersze):
        for j in range(kolumny):
            suma_kwadratow += math.pow(macierz[i][j], 2)
    Frobeniusa = math.sqrt(suma_kwadratow)

    # norma Manhattan
    suma_modulow = 0
    for i in range(wiersze):
        for j in range(kolumny):
            suma_modulow += abs(macierz[i][j])
    Manhattan = suma_modulow

    # norma maksimum
    maksimum = 0
    for i in range(wiersze):
        for j in range(kolumny):
            if abs(macierz[i][j]) > maksimum:
                maksimum = abs(macierz[i][j])

    return Frobeniusa, Manhattan, maksimum

macierz = [
    [1, -2, 3],
    [4, 5, -6]
]

Frobeniusa, Manhattan, maksimum = normy_macierzy(macierz)

print("Norma Frobeniusa:", Frobeniusa)
print("Norma Manhattan:", Manhattan)
print("Norma maksimum:", maksimum)

#zad4

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

macierz1 = [
    [1, 2],
    [3, 4]
]

macierz2 = [
    [5, 6],
    [7, 8]
]

wynik = mnozenie_macierzy(macierz1, macierz2)

print("Wynik mnożenia:")
for wiersz in wynik:
    print(wiersz)

#zad5 sprawdzić

# class Macierz:
#     def __init__(self, dane):
#         self.dane = dane
#         self.wiersze = len(dane)
#         self.kolumny = len(dane[0])

#     def __str__(self):
#         napis = ""
#         for wiersz in self.dane:
#             napis += str(wiersz) + "\n"
#         return napis

#     def mnozenie_przez_stala(self, stala):
#         wynik = []
#         for wiersz in self.dane:
#             nowy_wiersz = []
#             for element in wiersz:
#                 nowy_wiersz.append(element * stala)
#             wynik.append(nowy_wiersz)
#         return Macierz(wynik)

#     def dodawanie(self, inna):
#         if self.wiersze != inna.wiersze or self.kolumny != inna.kolumny:
#             raise ValueError("Macierze muszą mieć te same wymiary.")

#         wynik = []
#         for i in range(self.wiersze):
#             wiersz = []
#             for j in range(self.kolumny):
#                 wiersz.append(self.dane[i][j] + inna.dane[i][j])
#             wynik.append(wiersz)
#         return Macierz(wynik)

#     def mnozenie(self, inna):
#         if self.kolumny != inna.wiersze:
#             raise ValueError("Nie można pomnożyć tych macierzy.")

#         wynik = []
#         for i in range(self.wiersze):
#             wiersz = []
#             for j in range(inna.kolumny):
#                 suma = 0
#                 for k in range(self.kolumny):
#                     suma += self.dane[i][k] * inna.dane[k][j]
#                 wiersz.append(suma)
#             wynik.append(wiersz)
#         return Macierz(wynik)


# A = Macierz([[1, 2], [3, 4]])
# B = Macierz([[5, 6], [7, 8]])

# print("Macierz A:")
# print(A)

# print("Macierz B:")
# print(B)

# print("A + B:")
# print(A.dodawanie(B))

# print("A * 2:")
# print(A.mnozenie_przez_stala(2))

# print("A * B:")
# print(A.mnozenie(B))