import numpy as np
from scipy import linalg
import random

#funkcja zamieniajaca macierz hermitowska na macierz unitarna
def unitary_matrix(H):
        H = H*1.j
        unitarna = np.matrix(linalg.expm(H))
        return unitarna

#losowanie macierzy hermitowskiej(wg programu Mathematica)
def LosujMacierzHermitowska(WymiarN: int):
    Wynik = np.random.random((WymiarN, WymiarN)) + 1J*np.random.random((WymiarN, WymiarN))
    Wynik = 0.5 * (Wynik + np.matrix.getH(Wynik))
    return Wynik

#losuje macierz D
def LosujMacierzD(WymiarN: int, IleJedynek: int):
    Wynik = np.zeros((WymiarN,WymiarN))
    a = list(range(WymiarN))
    random.shuffle(a)
    for IxDiagonalny in range(IleJedynek):
        i = a.pop()
        Wynik[i][i]=1
    return Wynik

def normalizacja_wierszowa(matrix, N, n):
    for i in range (N):
        suma = np.zeros((n, n), complex)
        for j in range(N):
            suma += matrix[i, j]
        suma = linalg.inv(suma)#odwrotnosc
        suma = linalg.sqrtm(suma)#suma do 1/2
        for j in range (N):
            matrix[i, j] = np.dot(matrix[i, j], suma)
            matrix[i, j] = np.dot(suma, matrix[i, j])
            
def normalizacja_kolumnowa(matrix, N, n):
    for i in range (N):
        suma = np.zeros((n, n), complex)
        for j in range(N):
            suma += matrix[j, i]
        suma = linalg.inv(suma)#odwrotnosc
        suma = linalg.sqrtm(suma)#suma do 1/2
        for j in range(N):
            matrix[j, i] = np.dot(matrix[j, i], suma)

            matrix[j, i] = np.dot(suma, matrix[j, i])



#test sumowania do macierzy identycznosciowej
def TestNormalizacji(Macierz, WymiarN: int, Wymiarn: int):
    # sumy wierszowe
    for wrsMinorów in range(WymiarN):
        sumaWrs = numpy.zeros((Wymiarn,Wymiarn), complex)
        for kolMinorów in range(WymiarN):
            sumaWrs += Macierz[wrsMinorów][kolMinorów]
        if (CzyMacierzeRówneZDokładnością(sumaWrs, numpy.identity(Wymiarn), Wymiarn)==0):
            return False

    # sumy kolumnowe
    for kolMinorów in range(WymiarN):
        sumaKol = numpy.zeros((Wymiarn,Wymiarn), complex)
        for wrsMinorów in range(WymiarN):
            sumaKol += Macierz[wrsMinorów][kolMinorów]
        if (CzyMacierzeRówneZDokładnością(sumaKol, numpy.identity(Wymiarn), Wymiarn)==0):
            return False

    return True

#wykorzystywane w TestNormalizacji
def CzyMacierzeRówneZDokładnością(M1, M2, Wymiar):
    epsilon_TestNormalizacji = 0.1

    for wrs in range(Wymiar):
        for kol in range(Wymiar):
            if abs(M1[wrs][kol]-M2[wrs][kol]) > epsilon_TestNormalizacji:
                return False
    return True
