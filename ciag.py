def jed():
    ilosc = int(input("wybierz ktora liczbe mam wyswietlic max 100:"))
    ilosc -= 1
    p = 0
    i = 1
    o = 0
    n = 0
    def pr(p, i, o, n):
        if o == 0:
            o += 1
            pr(p, i, o, n)
        elif o < ilosc:
            n = i
            i = p + i
            p = n
            o += 1
            pr(p, i, o, n)
        elif o == ilosc:
            print(i)
    pr(p, i, o, n)
def wsz():
    ilosc = int(input("wybierz ile liczb mam wyswietlic max 100:"))
    p = 0
    i = 1
    o = 0
    n = 0
    def pr(p, i, o, n):
        if o == 0:
            print(p)
            o += 1
            pr(p, i, o, n)
        elif o < ilosc:
            print(i)
            n = i
            i = p + i
            p = n
            o += 1
            pr(p, i, o, n)
    pr(p, i, o, n)
print("wybierz czy mam wyswietlic ostatnia czy wszystkie liczby z ciagu fibonaciego")
def wy():
    wyb = int(input("wpisz 0 jesli mam wyswietlic ostatnia, lub 1 jesli mam wyswietlic wszystkie:"))
    if wyb == 0:
        jed()
    elif wyb == 1:
        wsz()
    else:
        print("zly zakres, jeszcze raz")
        wy()
wy()
