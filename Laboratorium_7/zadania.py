# zad 1

import math

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def bisekcja(f, a, b, max_iter=100, epsilon=1e-3, warunek_stopu="iteracje"):
    if f(b) * f(a) >= 0:
        raise ValueError("Na krańcach przedziału funkcja musi mieć przeciwne znaki.")

    a0 = a
    b0 = b
    historia = []

    x1 = a
    x2 = b

    historia.append([1, a, b, x1, f(x1), None])
    historia.append([2, a, b, x2, f(x2), None])

    if warunek_stopu == "iteracje" and max_iter == 1:
        return x1, historia
    if warunek_stopu == "iteracje" and max_iter == 2:
        return x2, historia

    for i in range(3, max_iter + 1):
        miejsce_zerowe = a + ((b - a) / 2.0) # punkt środkowy (a+b)/2

        fa = f(a)
        fc = f(miejsce_zerowe)

        blad = (b0 - a0) / (2 ** (i - 2))

        historia.append([i, a, b, miejsce_zerowe, fc, blad])

        if warunek_stopu == "iteracje":
            if i == max_iter:
                return miejsce_zerowe, historia

        elif warunek_stopu == "blad":
            if blad < epsilon: # alternatywnie |b-a| < epsilon
                return miejsce_zerowe, historia

        elif warunek_stopu == "wartosc":
            if abs(fc) < epsilon:
                return miejsce_zerowe, historia

        else:
            raise ValueError("Niepoprawny warunek stopu.")
        
        if fc == 0:
            return miejsce_zerowe, historia

        # if fa * fc < 0: # można też tak
        if sgn(fa) != sgn(fc):
            b = miejsce_zerowe
        else:
            a = miejsce_zerowe

    return miejsce_zerowe, historia

def wypisz_historie(historia):
    print("i         a           b           x          f(x)        blad")
    for krok in historia:
        print(
            f"{krok[0]} "
            f"{krok[1]} "
            f"{krok[2]} "
            f"{krok[3]} "
            f"{krok[4]} "
            f"{krok[5]}"
        )

def f1(x):
    return x**2 - 4

def f2(x):
    return math.sin(x) - 0.5

def f3(x):
    return x**3 - 3*x**2 - 2*x + 5

print("-------------------- ZADANIE 1 --------------------")

print("\n==================== FUNKCJA a) ====================")
print("f(x) = x^2 - 4, przedział [0, 2.2]")

wynik_a_iter, historia_a_iter = bisekcja(f1, 0.0, 2.2, max_iter=12, warunek_stopu="iteracje")
print("\nWarunek stopu: liczba iteracji")
wypisz_historie(historia_a_iter)
print("Przybliżony pierwiastek:", wynik_a_iter)
print("f(x) =", f1(wynik_a_iter))

wynik_a_blad, historia_a_blad = bisekcja(f1, 0.0, 2.2, epsilon=1e-3, warunek_stopu="blad")
print("\nWarunek stopu: dostatecznie mały błąd")
print("Przybliżony pierwiastek:", wynik_a_blad)
print("f(x) =", f1(wynik_a_blad))
print("Liczba iteracji:", len(historia_a_blad))

wynik_a_wartosc, historia_a_wartosc = bisekcja(f1, 0.0, 2.2, epsilon=1e-3, warunek_stopu="wartosc")
print("\nWarunek stopu: wartość funkcji bliska zeru")
print("Przybliżony pierwiastek:", wynik_a_wartosc)
print("f(x) =", f1(wynik_a_wartosc))
print("Liczba iteracji:", len(historia_a_wartosc))

print("\n==================== FUNKCJA b) ====================")
print("f(x) = sin(x) - 1/2, przedział [0, 2.2]")

wynik_b_iter, historia_b_iter = bisekcja(f2, 0.0, 2.2, max_iter=12, warunek_stopu="iteracje")
print("\nWarunek stopu: liczba iteracji")
wypisz_historie(historia_b_iter)
print("Przybliżony pierwiastek:", wynik_b_iter)
print("f(x) =", f2(wynik_b_iter))

wynik_b_blad, historia_b_blad = bisekcja(f2, 0.0, 2.2, epsilon=1e-3, warunek_stopu="blad")
print("\nWarunek stopu: dostatecznie mały błąd")
print("Przybliżony pierwiastek:", wynik_b_blad)
print("f(x) =", f2(wynik_b_blad))
print("Liczba iteracji:", len(historia_b_blad))

wynik_b_wartosc, historia_b_wartosc = bisekcja(f2, 0.0, 2.2, epsilon=1e-3, warunek_stopu="wartosc")
print("\nWarunek stopu: wartość funkcji bliska zeru")
print("Przybliżony pierwiastek:", wynik_b_wartosc)
print("f(x) =", f2(wynik_b_wartosc))
print("Liczba iteracji:", len(historia_b_wartosc))


# test ze slajdów
# print("=====================================")

# wynik_a_iter, historia_a_iter = bisekcja(f3, 1.0, 2.0, max_iter=12, warunek_stopu="iteracje")
# print("\nWarunek stopu: liczba iteracji")
# wypisz_historie(historia_a_iter)
# print("Przybliżony pierwiastek:", wynik_a_iter)
# print("f(x) =", f3(wynik_a_iter))

# wynik_a_blad, historia_a_blad = bisekcja(f3, 1.0, 2.0, epsilon=1e-3, warunek_stopu="blad")
# print("\nWarunek stopu: dostatecznie mały błąd")
# print("Przybliżony pierwiastek:", wynik_a_blad)
# print("f(x) =", f3(wynik_a_blad))
# print("Liczba iteracji:", len(historia_a_blad))

# wynik_a_wartosc, historia_a_wartosc = bisekcja(f3, 1.0, 2.0, epsilon=1e-3, warunek_stopu="wartosc")
# print("\nWarunek stopu: wartość funkcji bliska zeru")
# print("Przybliżony pierwiastek:", wynik_a_wartosc)
# print("f(x) =", f3(wynik_a_wartosc))
# print("Liczba iteracji:", len(historia_a_wartosc))

# zad 2

import math

def newton(f, a, b, df, ddf, max_iter=100, epsilon=1e-3):
    lista_iteracji = []

    if f(a) * f(b) >= 0:
        raise ValueError("Na krańcach przedziału funkcja musi mieć przeciwne znaki.")
    
    c = (a+b) / 2.0 
    iloczyn_pochodnych = df(c) * ddf(c)

    x = 0.0

    if iloczyn_pochodnych < 0:
        x = a
    elif iloczyn_pochodnych > 0:
        x = b
    else:
        raise ValueError("Nie można jednoznacznie wybrać punktu startowego, bo f'(c) * f''(c) = 0.")

    punkt_startowy = x

    for i in range(1, max_iter+1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Pochodna f'(x) = 0, metoda Newtona nie może wykonać kolejnego kroku.")
        
        h = fx / dfx
        x_nowe = x - h

        lista_iteracji.append([i, x, fx, dfx, h, x_nowe])

        if abs(h) < epsilon:
            return punkt_startowy, x_nowe, lista_iteracji
        
        x = x_nowe

    return punkt_startowy, x, lista_iteracji

def wypisz_historie(historia):
    print("i        x               f(x)            f'(x)            h               x_nowe")
    for krok in historia:
        print(
            f"{krok[0]:<2} "
            f"{krok[1]:>14.10f} "
            f"{krok[2]:>14.10f} "
            f"{krok[3]:>14.10f} "
            f"{krok[4]:>14.10f} "
            f"{krok[5]:>14.10f}"
        )

def f1(x):
    return x**2 - 4

def df1(x):
    return 2*x

def ddf1(x):
    return 2

def f2(x):
    return math.sin(x) - 0.5

def df2(x):
    return math.cos(x)

def ddf2(x):
    return -math.sin(x)

print("-------------------- ZADANIE 2 --------------------")

print("\n==================== FUNKCJA a) ====================")
print("f(x) = x^2 - 4, przedział [0, 2.2]")

punkt_startowy_a, wynik_a, historia_a = newton(f1, 0.0, 2.2, df1, ddf1, max_iter=100, epsilon=1e-3)
print("Punkt startowy x0 =", punkt_startowy_a)
wypisz_historie(historia_a)
print("Przybliżony pierwiastek:", wynik_a)
print("f(x) =", f1(wynik_a))
print("Liczba iteracji:", len(historia_a))

print("\n==================== FUNKCJA b) ====================")
print("f(x) = sin(x) - 1/2, przedział [0, 2.2]")

punkt_startowy_b, wynik_b, historia_b = newton(f2, 0.0, 2.2, df2, ddf2, max_iter=100, epsilon=1e-3)
print("Punkt startowy x0 =", punkt_startowy_b)
wypisz_historie(historia_b)
print("Przybliżony pierwiastek:", wynik_b)
print("f(x) =", f2(wynik_b))
print("Liczba iteracji:", len(historia_b))

# zad 3

import math

def sieczne(f, a, b, df, ddf, max_iter=100, epsilon=1e-3):
    lista_iteracji = []

    if f(a) * f(b) >= 0:
        raise ValueError("Na krańcach przedziału funkcja musi mieć przeciwne znaki.")
    
    c = (a+b) / 2.0
    iloczyn_pochodnych = df(c) * ddf(c)

    if iloczyn_pochodnych < 0:
        x0 = a
        x1 = b
    elif iloczyn_pochodnych > 0:
        x0 = b
        x1 = a
    else:
        raise ValueError("Nie można jednoznacznie wybrać punktu startowego, bo f'(c) * f''(c) = 0.")

    x0_startowy = x0
    x1_startowy = x1

    for i in range(1, max_iter+1):
        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            raise ValueError("Mianownik jest równy zero, metoda siecznych nie może wykonać kolejnego kroku.")
        
        x_nowe = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))

        lista_iteracji.append([i, x0, x1, fx0, fx1, x_nowe])

        if abs(x_nowe - x1) < epsilon:
            return x0_startowy, x1_startowy, x0, x1, lista_iteracji
        
        x0 = x1
        x1 = x_nowe

    return x0_startowy, x1_startowy, x0, x1, lista_iteracji

def wypisz_historie(historia):
    print("i        x0              x1              f(x0)           f(x1)           x_nowe")
    for krok in historia:
        print(
            f"{krok[0]:<2} "
            f"{krok[1]:>14.10f} "
            f"{krok[2]:>14.10f} "
            f"{krok[3]:>14.10f} "
            f"{krok[4]:>14.10f} "
            f"{krok[5]:>14.10f}"
        )

def f1(x):
    return x**2 - 4

def df1(x):
    return 2*x

def ddf1(x):
    return 2

def f2(x):
    return math.sin(x) - 0.5

def df2(x):
    return math.cos(x)

def ddf2(x):
    return -math.sin(x)

print("-------------------- ZADANIE 3 --------------------")

print("\n==================== FUNKCJA a) ====================")
print("f(x) = x^2 - 4, przedział [0, 2.2]")

x0a, x1a, wynik0_a, wynik1_a, historia_a = sieczne(f1, 0.0, 2.2, df1, ddf1, max_iter=100, epsilon=1e-3)
print("Punkty startowe: x0 =", x0a, ", x1 =", x1a)
wypisz_historie(historia_a)
print("Ostatnie przybliżenia:", wynik0_a, wynik1_a)
print("Przybliżony pierwiastek:", wynik1_a)
print("f(x) =", f1(wynik1_a))
print("Liczba iteracji:", len(historia_a))

print("\n==================== FUNKCJA b) ====================")
print("f(x) = sin(x) - 1/2, przedział [0, 2.2]")

x0b, x1b, wynik0_b, wynik1_b, historia_b = sieczne(f2, 0.0, 2.2, df2, ddf2, max_iter=100, epsilon=1e-3)
print("Punkty startowe: x0 =", x0b, ", x1 =", x1b)
wypisz_historie(historia_b)
print("Ostatnie przybliżenia:", wynik0_b, wynik1_b)
print("Przybliżony pierwiastek:", wynik1_b)
print("f(x) =", f2(wynik1_b))
print("Liczba iteracji:", len(historia_b))