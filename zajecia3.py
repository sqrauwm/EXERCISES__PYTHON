import math
# #kwadraty liczb od 0 do 9
# a=[]
# for x in range (0, 10):             #dwuliniowa skladnia
#     a.append(x**2)
# print(a)
#
# a2 = [x**2 for x in range(0,10)]    #jednoliniowa skladnia
#
# print(a2)
#
# ###
# b=[]                                #dwuliniowa skladnia
# for x in range (0,6):
#     b.append(3**x)
# print(b)
#
# ###
#
# c=[]
# for x in a:                         #dwuliniowa skladnia
#     if(x%2==0):
#         c.append(x)
# print(c)
#
# ###
#
# c2 = [x for x in a if x % 2 == 1]  #jednoliniowa skladnia
# print(c2)

# ###
#
# lista=[]
# for a in [1,2,3]:
#     for b in [4,5,6]:
#         lista.append((a,b))
# print(lista)
#
# ###
#
# lista2=[(a,b,x) for a in [1,2,3] for b in [4,5,6] for x in [10,11,12]]
# print(lista2)
#
# ###

# slownik = {"PZU":"Panstwowy zaklad ubezpieczen",
#            "ZUS":"Zaklad ubezpieczen spoelcznych",
#            "PKO":"Panstwowa kasa oszczednosci"}
# slownik_re={}
# for key,value in slownik.items():
#     slownik_re[value]=key
# print(slownik)
# slownik_re["PZPN"]="Polski zwiazek pilki noznej"
# print(slownik_re)
#
# ###
#
# slownik2={value:key for value, key in slownik.items()}
# print(slownik2)
#
# ###

# napis =input("Wprowadz napis: ")
# print(napis)
# print(type(napis))

# ###
#
# def row_kwadratowe(a,b,c):
#     delta=(b**2)-(4*a*c)
#     print(" ")
#     if delta<0:
#         print("brak rozwiazan (delta mniejsza od zera)")
#         return -1
#     elif delta==0:
#         print("rozwiazanie ma 1 rozwiazanie:")
#         x=(-b)/(2*a)
#         return x
#     else:
#         print("rownanie ma 2 rozwiazania:")
#         x1=((-b)-math.sqrt(delta))/(2*a)
#         x2=((-b)+math.sqrt(delta))/(2*a)
#         return x1, x2
#
# print(row_kwadratowe(6,1,3))
# print(row_kwadratowe(1,2,1))
# print(row_kwadratowe(1,4,1))
#
# ###
# print(" ")
# def funkcja_parz(z):
#     if (z%2==1):
#         return (str(z) + " to liczba nieparzysta.")
#     else:
#         return (str(z)+ " to liczba parzysta.")
#
# print(funkcja_parz(2115))
# print(funkcja_parz(997))
# print(funkcja_parz(420))
# print(funkcja_parz(666))
#
# ###

# def dlugosc_odcinka(x1=8, y1=0,x2=0,y2=0):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
#
# #argumenty domyslne
# print(dlugosc_odcinka())
#
# #argumenty pozycyjne
# print(dlugosc_odcinka(0,0,8,8))
#
# #dwa argumenty pozycyjne, dwa z nowa wartoscia
# print(dlugosc_odcinka(2,2,y2=2,x2=1))
#
# #argumenty z nowa wartoscia, w roznej kolejnosci
# print(dlugosc_odcinka(y1=2, x1=5,y2=5,x2=3))
#
# #dwa argumenty z nowymi wartosciami, pozostale przyjmuja wartosc domyslna
# print(dlugosc_odcinka(x2=2, y2=3))
#
# ###

# def ciag(* liczby):
#     if len(liczby)==0:
#         return 0
#     else:
#         suma =0
#         for i in liczby:
#             suma+=i
#         return suma
# print(ciag())
# print(ciag(5,4,3,2,1))

###

def co_lubie(** rzeczy):
    for cos in rzeczy:
        print(' to jest ')
        print( cos)
        print(' co lubie ')
        print( rzeczy[cos] )
        print(' ')

co_lubie(gry=['lol', 'cs'])
co_lubie(sport=['siateczka', 'pileczka'])




