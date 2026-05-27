# zad 1
import random, sys

MAX = sys.maxsize

def rand():
    return random.randint(0, MAX)

def losuj_0_MAX():
    return rand()

def losuj_0_max(max_wartosc):
    X = rand()
    return int((X / (MAX + 1) * (max_wartosc + 1)))

def losuj_min_max(min_wartosc, max_wartosc):
    X = rand()
    return min_wartosc + int((X / (MAX + 1)) * (max_wartosc - min_wartosc + 1))

def losuj_0_1():
    X = rand()
    return X / (MAX) # przedział [0,1]
    # return X / (MAX + 1) # przedział [0,1)

print("--------------------ZADANIE 1--------------------")

print("a) <0, MAX>:", losuj_0_MAX())
print("b) <0, max>:", losuj_0_max(10))
print("c) <min, max>:", losuj_min_max(5, 15))
print("d) <0, 1>:", losuj_0_1())

# zad 2

def generator_LCG(a, c, X0, M, ile):
    liczby = []
    X = X0

    for i in range(ile):
        liczby.append(X)
        X = (a * X + c) % M

    return liczby

def utworz_punkty(liczby):
    punkty = []

    for i in range(0, len(liczby) - 1, 2):
        punkty.append((liczby[i], liczby[i + 1]))

    return punkty

def zapisz_svg(punkty, M, nazwa_pliku):
    szerokosc = 500
    wysokosc = 500
    margines = 20

    svg = f'<svg width="{szerokosc}" height="{wysokosc}" viewBox="0 0 {szerokosc} {wysokosc}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += '<rect width="100%" height="100%" fill="white"/>\n'
    svg += f'<rect x="{margines}" y="{margines}" width="{szerokosc - 2*margines}" height="{wysokosc - 2*margines}" fill="none" stroke="black"/>\n'

    for x, y in punkty:
        x_svg = margines + (x / (M - 1)) * (szerokosc - 2 * margines)
        y_svg = wysokosc - margines - (y / (M - 1)) * (wysokosc - 2 * margines)

        svg += f'<circle cx="{x_svg}" cy="{y_svg}" r="3" fill="blue"/>\n'

    svg += '</svg>'

    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        plik.write(svg)

# print("--------------------ZADANIE 2--------------------")

a = 100000
c = 12345
M = 1515151
X0 = 2

liczby = generator_LCG(a, c, X0, M, 1000)
punkty = utworz_punkty(liczby)

# print("Pierwsze 20 liczb:")
# print(liczby[:20])

# print("Pierwsze 10 punktów:")
# print(punkty[:10])

zapisz_svg(punkty, M, "punkty_LCG.svg")

# zad 3

def generator_LFG(p, q, M, poczatkowe, ile):
    if not (p > q >= 1):
        raise ValueError("Musi być spełniony warunek p > q >= 1.")

    if len(poczatkowe) < p:
        raise ValueError("Trzeba podać co najmniej p wartości początkowych.")

    liczby = poczatkowe.copy()

    for n in range(p, ile):
        Xn = (liczby[n - p] + liczby[n - q]) % M
        liczby.append(Xn)

    return liczby


print("--------------------ZADANIE 3--------------------")

M = 17
p = 3
q = 1

poczatkowe = [7, 16, 5]

liczby = generator_LFG(p, q, M, poczatkowe, 12)

print("Wygenerowany ciąg:")
print(liczby)