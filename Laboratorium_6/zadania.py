#zad 1

def norma_max(wektor):
    maksimum = abs(wektor[0])
    for i in range(1, len(wektor)):
        if abs(wektor[i]) > maksimum:
            maksimum = abs(wektor[i])
    return maksimum


def odejmij_wektory(wektor1, wektor2):
    wynik = []
    for i in range(len(wektor1)):
        wynik.append(wektor1[i] - wektor2[i])
    return wynik


def wypisz_wektor(wektor, nazwa="x"):
    for i in range(len(wektor)):
        print(f"{nazwa}{i+1} = {wektor[i]}")


def jacobi(A, b, x0, max_iter=100, epsilon=1e-3, warunek_stopu="iteracje", rozwiazanie_dokladne=None):
    n = len(A)
    x_stare = x0[:]

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("Na przekątnej macierzy nie może być zera")

    for krok in range(1, max_iter + 1):
        x_nowe = [0.0] * n

        for i in range(n):
            suma = 0.0
            for j in range(n):
                if j != i:
                    suma += A[i][j] * x_stare[j]

            x_nowe[i] = (b[i] - suma) / A[i][i]

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x_nowe, krok

        elif warunek_stopu == "roznica":
            roznica = odejmij_wektory(x_nowe, x_stare)
            norma_roznicy = norma_max(roznica)
            norma_biezaca = norma_max(x_nowe)

            if norma_biezaca == 0:
                if norma_roznicy <= epsilon:
                    return x_nowe, krok
            else:
                if (norma_roznicy / norma_biezaca) <= epsilon:
                    return x_nowe, krok

        elif warunek_stopu == "blad":
            if rozwiazanie_dokladne is None:
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")
            blad = odejmij_wektory(x_nowe, rozwiazanie_dokladne)
            if norma_max(blad) < epsilon:
                return x_nowe, krok

        x_stare = x_nowe[:]

    return x_stare, max_iter


print("--------------------ZADANIE 1--------------------")

A = [
    [4.0, -2.0, 0.0, 0.0],
    [-2.0, 5.0, -1.0, 0.0],
    [0.0, -1.0, 4.0, 2.0],
    [0.0, 0.0, 2.0, 3.0]
]

b = [0.0, 2.0, 3.0, -2.0]
x0 = [0.0, 0.0, 0.0, 0.0]
x_dokladne = [0.5, 1.0, 2.0, -2.0]

print("\nDane:")
print("Macierz A:")
for wiersz in A:
    print(wiersz)

print("\nWektor b:")
print(b)

print("\nPrzybliżenie początkowe x^(0):")
print(x0)

print("\nDokładne rozwiązanie:")
print(x_dokladne)

print("\n-------------------- a) LICZBA ITERACJI --------------------")
wynik_a, iteracje_a = jacobi(
    A, b, x0,
    max_iter=10,
    warunek_stopu="iteracje"
)

print("\nWynik końcowy po zadanej liczbie iteracji:")
wypisz_wektor(wynik_a)
print("Liczba iteracji:", iteracje_a)

blad_a = odejmij_wektory(wynik_a, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_a))

print("\n-------------------- b) WARUNEK ZE SLAJDU --------------------")
wynik_b, iteracje_b = jacobi(
    A, b, x0,
    max_iter=100,
    epsilon=1e-3,
    warunek_stopu="roznica"
)

print("\nWynik końcowy:")
wypisz_wektor(wynik_b)
print("Liczba iteracji:", iteracje_b)

blad_b = odejmij_wektory(wynik_b, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_b))

print("\n-------------------- c) BŁĄD UZYSKANEGO PRZYBLIŻENIA --------------------")
wynik_c, iteracje_c = jacobi(
    A, b, x0,
    max_iter=100,
    epsilon=1e-3,
    warunek_stopu="blad",
    rozwiazanie_dokladne=x_dokladne
)

print("\nWynik końcowy:")
wypisz_wektor(wynik_c)
print("Liczba iteracji:", iteracje_c)

blad_c = odejmij_wektory(wynik_c, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_c))

# zad 2
# print("--------------------ZADANIE 2--------------------")

# def norma_max(wektor):
#     maksimum = abs(wektor[0])
#     for i in range(1, len(wektor)):
#         if abs(wektor[i]) > maksimum:
#             maksimum = abs(wektor[i])
#     return maksimum


# def odejmij_wektory(wektor1, wektor2):
#     wynik = []
#     for i in range(len(wektor1)):
#         wynik.append(wektor1[i] - wektor2[i])
#     return wynik


# def wypisz_wektor(wektor, nazwa="x"):
#     for i in range(len(wektor)):
#         print(f"{nazwa}{i+1} = {wektor[i]}")


# def gauss_seidel(A, b, x0, max_iter=100, epsilon=1e-8, warunek_stopu="iteracje", rozwiazanie_dokladne=None):
#     n = len(A)
#     x = x0[:]

#     for i in range(n):
#         if A[i][i] == 0:
#             raise ValueError("Na przekątnej macierzy nie może być zera")

#     for krok in range(1, max_iter + 1):
#         x_stare = x[:]

#         for i in range(n):
#             suma1 = 0.0
#             for j in range(i):
#                 suma1 += A[i][j] * x[j]

#             suma2 = 0.0
#             for j in range(i + 1, n):
#                 suma2 += A[i][j] * x_stare[j]

#             x[i] = (b[i] - suma1 - suma2) / A[i][i]

#         if warunek_stopu == "iteracje":
#             if krok == max_iter:
#                 return x, krok

#         elif warunek_stopu == "roznica":
#             roznica = odejmij_wektory(x, x_stare)
#             if norma_max(roznica) < epsilon:
#                 return x, krok

#         elif warunek_stopu == "blad":
#             if rozwiazanie_dokladne is None:
#                 raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")
#             blad = odejmij_wektory(x, rozwiazanie_dokladne)
#             if norma_max(blad) < epsilon:
#                 return x, krok

#         else:
#             raise ValueError("Niepoprawny warunek stopu")

#     return x, max_iter

# A = [
#     [10.0, -1.0,  2.0,  0.0],
#     [-1.0, 11.0, -1.0,  3.0],
#     [2.0, -1.0, 10.0, -1.0],
#     [0.0,  3.0, -1.0,  8.0]
# ]

# b = [6.0, 25.0, -11.0, 15.0]

# x0 = [0.0, 0.0, 0.0, 0.0]

# x_dokladne = [1.0, 2.0, -1.0, 1.0]

# print("\nDane:")
# print("Macierz A:")
# for wiersz in A:
#     print(wiersz)

# print("\nWektor b:")
# print(b)

# print("\nPrzybliżenie początkowe x^(0):")
# print(x0)

# print("\nDokładne rozwiązanie:")
# print(x_dokladne)

# print("\n-------------------- a) LICZBA ITERACJI --------------------")
# wynik_a, iteracje_a = gauss_seidel(
#     A, b, x0,
#     max_iter=10,
#     warunek_stopu="iteracje"
# )

# print("\nWynik końcowy po zadanej liczbie iteracji:")
# wypisz_wektor(wynik_a)
# print("Liczba iteracji:", iteracje_a)

# blad_a = odejmij_wektory(wynik_a, x_dokladne)
# print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_a))

# print("\n-------------------- b) NORMA RÓŻNICY KOLEJNYCH PRZYBLIŻEŃ --------------------")
# wynik_b, iteracje_b = gauss_seidel(
#     A, b, x0,
#     max_iter=100,
#     epsilon=1e-6,
#     warunek_stopu="roznica"
# )

# print("\nWynik końcowy:")
# wypisz_wektor(wynik_b)
# print("Liczba iteracji:", iteracje_b)

# blad_b = odejmij_wektory(wynik_b, x_dokladne)
# print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_b))

# print("\n-------------------- c) BŁĄD UZYSKANEGO PRZYBLIŻENIA --------------------")
# wynik_c, iteracje_c = gauss_seidel(
#     A, b, x0,
#     max_iter=100,
#     epsilon=1e-6,
#     warunek_stopu="blad",
#     rozwiazanie_dokladne=x_dokladne
# )

# print("\nWynik końcowy:")
# wypisz_wektor(wynik_c)
# print("Liczba iteracji:", iteracje_c)

# blad_c = odejmij_wektory(wynik_c, x_dokladne)
# print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_c))