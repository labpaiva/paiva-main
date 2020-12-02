import numpy as np
from numba import jit, njit, prange, float64, vectorize
from numba.typed import  List
from datetime import datetime
import Matrix
import numba

#calcula as distancia entre todos os vizinhos
#@jit(forceobj=True)
def calcNP(espOrig):
  cont = len(espOrig[0])
  distance = []
  for i in range(len(espOrig)):
    distance.append([])
    distance[i].append(calcNP2(cont,espOrig, i))
  return distance

@njit(fastmath=True, nogil=True)
def calcNP2(cont, espOrig, i):
  calc = 0
  for j in range(len(espOrig)):
    calc += calcNP3(cont, espOrig, i, j)
    raiz = calc ** 0.5
  return round(raiz)

@njit(fastmath=True, nogil=True)
def calcNP3(cont, espOrig, i, j):
  calc = 0
  for k in range(cont):
    calc += (espOrig[i][k] - espOrig[j][k]) ** 2
  return calc

#Calcula a porcentagem de preservaçao
#@numba.jit(forceobj=True)
#@njit
def neighborhoodPreservation(distOrig, distProj):
  porcent, quant = 0, 0
  porcent = 0
  for i in range(len(distOrig)):
    quant += len(distOrig[i])
    for j in range(len(distOrig[0])):
      if distOrig[i][j] == distProj[i][j]:
        porcent += 1
  
  resultPreservation = round((porcent/quant)*100, 2)
  return resultPreservation

#######################################################################
ini = datetime.now()

Caminho ='C:\\Users\\ander\\Documents\\paiva-main\\DataFiles\\mammals-50000.bin-normcols.data'
matriz = Matrix.form_matrix(open(Caminho, 'r'), 1000)

CaminhoProj ='C:\\Users\\ander\\Documents\\paiva-main\\resultados\\proj-mammals-50000.bin-normcols.data'
matrizProj = Matrix.form_matrix(open(CaminhoProj, 'r'), 1000)

distEspaceOrigin, distEspaceProj = calcNP(matriz), calcNP(matrizProj)
#print(distEspaceOrigin)
#print(distEspaceProj)

'''
typed_dO = List()
[typed_dO.append(x) for x in distEspaceOrigin]

typed_dP = List()
[typed_dP.append(x) for x in distEspaceProj]
'''

preservation = neighborhoodPreservation(distEspaceOrigin, distEspaceProj)
print("Taxa de Preservação", preservation,"%")

fim = datetime.now()
print("tempo de execução", fim-ini)

