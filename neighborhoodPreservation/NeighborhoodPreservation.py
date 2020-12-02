import numpy as np
from numba import njit, prange
from datetime import  datetime
import math


def form_matrix(Caminho_matriz, tam=-1):
  matriz = []
  c = 0
  for linha in Caminho_matriz:
    if c < 4:  # servi para pular as 4 primeiras linhas do arquivo .data
        c += 1
    else:
      new_matriz = list(map(float, linha.split(";")))
      matriz.append(new_matriz[1:len(new_matriz)-1])
      # aki eu vou pergar a linha do arquivo e separar por ; e depois transformar a linha em uma lista e add
      # na minha matriz

  matriz = np.array(matriz)  # ai faço a matriz virar um array numpy
  #print(matriz[0])
  #print(tam)
  if tam == -1:  # tam vai ser usado para delimitar o tamanho da base
    return matriz
  return matriz[:tam]

#calcula as distancia entre todos os vizinhos
def calcNP(espOrig):
  cont = espOrig.shape[1]
  distance = []
  calc = 0

  for i in prange(len(espOrig)):
    distance.append([])
    for j in prange(len(espOrig)):
      for k in prange(cont):
        calc += (espOrig[i][k]-espOrig[j][k])**2
      raiz = (calc)**0.5
      distance[i].append(round(raiz))
      calc = 0
  return distance
  
#Calcula a porcentagem de preservaçao
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

Caminho ='/home/jbs/Downloads/DataFiles/mammals-50000.bin-normcols.data'
matriz = form_matrix(open(Caminho, 'r'), 1000)

CaminhoProj ='/home/jbs/Área de Trabalho/codigosPaiva/paiva-main/resultados/proj-mammals-50000.bin-normcols.data'
matrizProj = form_matrix(open(CaminhoProj, 'r'), 1000)


distEspaceOrigin, distEspaceProj = calcNP(matriz), calcNP(matrizProj)
print(distEspaceOrigin)
print(distEspaceProj)

preservation = neighborhoodPreservation(distEspaceOrigin, distEspaceProj)
print("Taxa de Preservação", preservation,"%")

fim = datetime.now()
print("tempo de execução", fim-ini)

