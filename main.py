import numpy as np

# a = np.arange(0, 10)
#
# print(a)
# print(type(a)) #wypisanie typu zmiennej tablicy (nie jej elementów) -ndarray
# print(a.dtype) #sprawdzenie typu danych tablicy
#
# a = np.arange(2, 10, dtype = 'int64') #inicjalizacja tablicy z konkertnym typem danych
# print(a)
# print(a.dtype)
#
# b = a.astype('float') #zapisywanie kopii tablicy jako tablicy z innym typem
# print(b)
# print(b.dtype)
# print(b.shape) #wypisanie rozmiaru tablicy
# print(a.ndim) # można też sprawdzić ilość wymiarów tablicy
#
# m = np.array([np.arange(5), np.arange(5)]) #stworzenie tablicy wielowymiarowej może wyglądać tak
# print(m)
# print(m.shape)
# print(m.ndim)
# print(type(m))

# zera = np.zeros((3,3))
# jedynki = np.ones((3,3))
#
# print(zera)
# print(jedynki)
#
# print(zera.dtype)
# print(jedynki.dtype)
#
# pusta = np.empty((2,2))
# print(pusta)
#
# poz_1 = pusta[1,1]
# poz_2 = pusta[0,1]
# print(poz_1)
# print(poz_2)

# macierz = np.array([[1,2,3],[3,4,5]])
# print(macierz)
#
# liczby = np.arange(1, 2,0.2)
# print(liczby)
# liczby_lin= np.linspace(1,10,10)
# print(liczby_lin)

# z = np.indices((5,5))
# print(z)

# x, y = np.mgrid[0:4, 0:5]
# print(x)
# print(y)

# mat_diag = np.diag([a for a in range(1,3)])
# print(mat_diag)
#
# mat_diag_k = np.diag([a*2 for a in range(1,5)],-1)
# print(mat_diag_k)

# z = np.fromiter([x for x in range(1,5)], dtype='int32')
# print(z)

# michal = b'Michael'
# mic = np.frombuffer(michal,dtype='S1')
# print(mic)
# mar_2 = np.frombuffer(michal, dtype='S2') ??

# michal = 'Michael'
# mic_3 = np.array(list(michal))
# mic_4 = np.array(list(michal), dtype='S1')
# mic_5 = np.array(list(b'Marcin'))
# mic_6 = np.fromiter(michal,dtype='S1')
# mic_7 = np.fromiter(michal,dtype='U1')
#
# print(mic_3)
# print(mic_4)
# print(mic_5)
# print(mic_6)
# print(mic_7)

# mat = np.ones((2,2))
# mat1 = np.ones((2,2))
# # mat = mat + mat1
# print(mat)
# print(mat + mat1)
# print(mat - mat1)
# print(mat*mat1)
# print(mat/mat1)

# a = np.arange(10)
# print(a)
# s = slice(2,7,2)
# print(a[s])
# slajs = range(2,7,2)
# print(a[slajs])

# print(a[2:7:2])
# print(a[:5])
# print(a[2:5])

# mat = np.arange(20)
# print(mat)
# matm = mat.reshape((5,4))
# print(matm, "\n")
# print(matm[1:])
# print(matm[:,1])
# print(matm[:,-1:])
# print(matm[2:6, 1:3])
# print(matm[:, range(2,4,2)])
# print('')

jd = np.array([[10, 20, 30],[40, 50, 60], [70, 80, 90]])
print(jd,"\n")
wiersze = np.array([[0, 0], [2, 2]])
print(wiersze, "\n")
kolumny = np.array([[0, 2], [0, 2]])
print(kolumny, "\n")
y = jd[wiersze,kolumny]
print(y, "\n")

x = np.array([[10, 20, 30],[40, 50, 60], [70, 80, 90]])
print(x, "\n")

