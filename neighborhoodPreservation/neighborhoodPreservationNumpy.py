import numpy as np
from scipy.spatial.distance import pdist, squareform
import Matrix

Caminho ='C:\\Users\\ander\\Documents\\paiva-main\\DataFiles\\mammals-50000.bin-normcols.data'
matriz = Matrix.form_matrix(open(Caminho, 'r'), 5)

print(matriz)
distance_condensed = pdist(matriz)
 
distance = squareform(distance_condensed)

print(distance)

print("#########################################")

CaminhoProj ='C:\\Users\\ander\\Documents\\paiva-main\\resultados\\proj-mammals-50000.bin-normcols.data'
matrizProj = Matrix.form_matrix(open(CaminhoProj, 'r'), 5)

print(matrizProj)
distance_condensed = pdist(matriz)
 
distance = squareform(distance_condensed)

dist = []
for i in range(len(distance)):
    for j in range(len(distance)):
        dist.append(round(distance[i][j], 2))
  
print(dist)