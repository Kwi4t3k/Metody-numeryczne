#zad 1

print("--------------------ZADANIE 1--------------------")

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

    # Sprawdzamy, czy macierz A nie jest pusta
    if n == 0:
        raise ValueError("Macierz A nie może być pusta")

    # Sprawdzamy, czy macierz A jest kwadratowa
    for wiersz in A:
        if len(wiersz) != n:
            raise ValueError("Macierz A musi być kwadratowa")

    # Sprawdzamy, czy wektor b ma dobry rozmiar
    if len(b) != n:
        raise ValueError("Wektor b musi mieć tyle elementów, ile macierz A ma wierszy")

    # Sprawdzamy, czy przybliżenie początkowe x0 ma dobry rozmiar
    if len(x0) != n:
        raise ValueError("Wektor x0 musi mieć tyle elementów, ile jest niewiadomych")

    x_stare = x0[:]
    #     /\
    # normalna wersja tego dla wektora
    # B = []
    #
    # for i in range(len(x0)):
    #     B.append(x0[i])

    # wersja dla macierzy
    # B = []
    #
    # for i in range(len(A)):
    #     nowy_wiersz = []
    #
    #     for j in range(len(A[i])):
    #         nowy_wiersz.append(A[i][j])
    #
    #     B.append(nowy_wiersz)
    #---------------------------------------

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
            
            if len(rozwiazanie_dokladne) != n:
                raise ValueError("Rozwiązanie dokładne musi mieć tyle elementów, ile jest niewiadomych")
            
            blad = odejmij_wektory(x_nowe, rozwiazanie_dokladne)
            if norma_max(blad) <= epsilon:
                return x_nowe, krok

        else:
            raise ValueError("Nieznany warunek stopu")

        x_stare = x_nowe[:]

    return x_stare, max_iter

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
print("--------------------ZADANIE 2--------------------")

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

def gauss_seidel(A, b, x0, max_iter=100, epsilon=1e-3, warunek_stopu="iteracje", rozwiazanie_dokladne=None):
    n = len(A)

    if n == 0:
        raise ValueError("Macierz A nie może być pusta")

    for wiersz in A:
        if len(wiersz) != n:
            raise ValueError("Macierz A musi być kwadratowa")

    if len(b) != n:
        raise ValueError("Wektor b musi mieć tyle elementów, ile macierz A ma wierszy")

    if len(x0) != n:
        raise ValueError("Wektor x0 musi mieć tyle elementów, ile jest niewiadomych")

    if epsilon <= 0:
        raise ValueError("Dokładność epsilon musi być dodatnia")

    if max_iter <= 0:
        raise ValueError("Liczba iteracji musi być dodatnia")

    # x = x0[:]

    x = []

    for i in range(len(x0)):
        x.append(x0[i])

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("Na przekątnej macierzy nie może być zera")

    for krok in range(1, max_iter + 1):
        x_stare = x[:]

        for i in range(n):
            suma1 = 0.0
            for j in range(i):
                suma1 += A[i][j] * x[j]

            suma2 = 0.0
            for j in range(i + 1, n):
                suma2 += A[i][j] * x_stare[j]

            x[i] = (b[i] - suma1 - suma2) / A[i][i]

        if warunek_stopu == "iteracje":
            if krok == max_iter:
                return x, krok

        elif warunek_stopu == "roznica":
            roznica = odejmij_wektory(x, x_stare)
            norma_roznicy = norma_max(roznica)
            norma_biezaca = norma_max(x)

            if norma_biezaca == 0:
                if norma_roznicy <= epsilon:
                    return x, krok
            else:
                if (norma_roznicy / norma_biezaca) <= epsilon:
                    return x, krok

        elif warunek_stopu == "blad":
            if rozwiazanie_dokladne is None:
                raise ValueError("Dla warunku 'blad' trzeba podać dokładne rozwiązanie")
            
            if len(rozwiazanie_dokladne) != n:
                raise ValueError("Rozwiązanie dokładne musi mieć tyle elementów, ile jest niewiadomych")
    
            blad = odejmij_wektory(x, rozwiazanie_dokladne)

            if norma_max(blad) <= epsilon:
                return x, krok

        else:
            raise ValueError("Niepoprawny warunek stopu")

    return x, max_iter

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
wynik_a, iteracje_a = gauss_seidel(
    A, b, x0,
    max_iter=10,
    warunek_stopu="iteracje"
)

print("\nWynik końcowy po zadanej liczbie iteracji:")
wypisz_wektor(wynik_a)
print("Liczba iteracji:", iteracje_a)

blad_a = odejmij_wektory(wynik_a, x_dokladne)
print("Norma błędu względem rozwiązania dokładnego:", norma_max(blad_a))

print("\n-------------------- b) NORMA RÓŻNICY KOLEJNYCH PRZYBLIŻEŃ --------------------")
wynik_b, iteracje_b = gauss_seidel(
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
wynik_c, iteracje_c = gauss_seidel(
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

# zad 3

print("--------------------ZADANIE 3--------------------")

def sprawdz_macierz(A):
    n = len(A)

    if n == 0:
        raise ValueError("Macierz A nie może być pusta")

    for wiersz in A:
        if len(wiersz) != n:
            raise ValueError("Macierz A musi być kwadratowa")

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("Na przekątnej macierzy A nie może być zera")

def zeros(n, m):
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0.0)
        macierz.append(wiersz)
    return macierz

def wypisz_macierz(macierz):
    for wiersz in macierz:
        print(wiersz)

def norma_wierszowa_macierzy(macierz):
    maksimum = 0.0
    for i in range(len(macierz)):
        suma = 0.0
        for j in range(len(macierz[i])):
            suma += abs(macierz[i][j])
        if suma > maksimum:
            maksimum = suma
    return maksimum

def macierz_iteracji_jacobiego(A):
    sprawdz_macierz(A)
    n = len(A)
    W = zeros(n, n)

    for i in range(n):
        for j in range(n):
            if i == j:
                W[i][j] = 0.0
            else:
                W[i][j] = -A[i][j] / A[i][i]

    return W

def rozwiaz_uklad_dolnotrojkatny(LD, b):
    n = len(LD)
    x = [0.0] * n

    for i in range(n):
        suma = 0.0
        for j in range(i):
            suma += LD[i][j] * x[j]

        if LD[i][i] == 0:
            raise ValueError("Dzielenie przez zero w układzie dolnotrójkątnym")

        x[i] = (b[i] - suma) / LD[i][i]

    return x

def macierz_iteracji_gaussa_seidla(A):
    sprawdz_macierz(A)
    n = len(A)

    LD = zeros(n, n)
    U = zeros(n, n)

    for i in range(n):
        for j in range(n):
            if j <= i:
                LD[i][j] = A[i][j]
            else:
                U[i][j] = A[i][j]

    W = zeros(n, n)

    for kolumna in range(n):
        prawa_strona = []
        for i in range(n):
            prawa_strona.append(-U[i][kolumna])

        rozwiazanie = rozwiaz_uklad_dolnotrojkatny(LD, prawa_strona)

        for i in range(n):
            W[i][kolumna] = rozwiazanie[i]

    return W

A = [
    [4.0, -2.0, 0.0, 0.0],
    [-2.0, 5.0, -1.0, 0.0],
    [0.0, -1.0, 4.0, 2.0],
    [0.0, 0.0, 2.0, 3.0]
]

print("\nMacierz A:")
wypisz_macierz(A)

print("\n-------------------- METODA JACOBIEGO --------------------")
WJ = macierz_iteracji_jacobiego(A)
print("Macierz iteracyjna W_J:")
wypisz_macierz(WJ)

norma_WJ = norma_wierszowa_macierzy(WJ)
print("Norma wierszowa ||W_J|| =", norma_WJ)

if norma_WJ < 1:
    print("Metoda Jacobiego jest zbieżna, ponieważ ||W_J|| < 1.")
else:
    print("Metoda Jacobiego może nie być zbieżna, ponieważ ||W_J|| >= 1.")

print("\n-------------------- METODA GAUSSA-SEIDLA --------------------")
WGS = macierz_iteracji_gaussa_seidla(A)
print("Macierz iteracyjna W_GS:")
wypisz_macierz(WGS)

norma_WGS = norma_wierszowa_macierzy(WGS)
print("Norma wierszowa ||W_GS|| =", norma_WGS)

if norma_WGS < 1:
    print("Metoda Gaussa-Seidla jest zbieżna, ponieważ ||W_GS|| < 1.")
else:
    print("Metoda Gaussa-Seidla może nie być zbieżna, ponieważ ||W_GS|| >= 1.")

print("\n-------------------- WNIOSEK KOŃCOWY --------------------")
print("Zbieżność metod z zadania 1 i 2 badamy przez normę macierzy iteracji.")
print("Dla Jacobiego sprawdzamy macierz W_J.")
print("Dla Gaussa-Seidla sprawdzamy macierz W_GS.")
print("Jeżeli ||W|| < 1, to metoda jest zbieżna.")