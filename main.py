import funkcje as f
import numpy as np
from scipy import linalg
import magical_square as ms

N_size = []
for i in range(1):#wymiary kolejnych macierzy
    N_size.append(2*i+3)
zbieganie = []
for N in N_size:
    magicSquare = ms.generateSquare(N)#magiczny kwadrat
    n = 0
    for i in range(N):
        n += magicSquare[0][i]# n = suma wierszowa mmagicznego kwadratu
    H = f.LosujMacierzHermitowska(n)#losowanie macierzy hermitowskiej
    H = f.unitary_matrix(H)#tworzenie macierzy unitarnej
    H_sprz = np.matrix.getH(H)#sprzezenie(hermitowskie?)
   # print((N, N, n, n))
    A = np.array(np.zeros((N, N, n, n), complex))
    for i in range (N):
        for j in range (N):
            D =  f.LosujMacierzD(n, magicSquare[i][j])#losowa macierz D
            A[i, j] = np.dot(H, np.dot(D, H_sprz))#uzupelnienie macierzy A
    #normalizacja
    for i in range(255):#maksimum 255  krokow
        if(f.TestNormalizacji!=0):#warunek sumowania do macierzy jednostkowych
                if(i%2==1):#normalizacja wierszowa i kolumnowa na zmiane
                    f.normalizacja_wierszowa(A, N, n)
                else:
                    f.normalizacja_kolumnowa(A, N, n)
#wypisanie elementu A[0, 0, 0, 0] - w granicy powinien wynosic 1
        suma = np.zeros((n, n), complex)
        for j in range(N):
            suma += A[0, j]
        print(abs(suma[0, 0]))
