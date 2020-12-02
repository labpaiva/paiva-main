from numba import vectorize, float64, njit
import numpy as np


@vectorize([float64(float64, float64), float64(float64, float64), float64(float64, float64), float64(float64, float64)])
def top(Matriz_Dist, Matriz_proj):
    return (Matriz_Dist - Matriz_proj) ** 2


@njit(fastmath=True, nogil=True)
def somatorio(Matriz_o, Matriz_p):
    #print('calculando stress paralelizado')
    '''Matriz_o: matriz do espaço original
    Matriz_p: matriz do espaço projetado'''
    somab = 0  # somatorio da parte inferior do calculo do stress de kruskal
    somat = 0  # somatorio da parte superior do calculo do stress de kruskal
    shape = np.shape(Matriz_o)  # vai pegar a quantidade de linha e colunas respectivamente
    for i in range(0, shape[0]):
        result = calculation_parts(Matriz_o, Matriz_p, i, i + 1, shape[0])
        somab += result[0]
        somat += result[1]

    return somat / somab


@njit(fastmath=True, nogil=True)
def calculation_parts(Mo, Mp, stance, init, end):
    '''
    Mo: matriz do espaço original
    Mp: matriz do espaço projetado
    stance: equivale o primeiro i do somatorio, onde ele é fixo até terminar o segundo somatorio
    init: equivale a o i do segundo somatorio, onde ele inicia i anterior mais 1 para nao repetir calculo
    end: o valor final de i que pode ser alcançado
    columns: são o número de colunas da matriz original, -2 pq o primeiro e o ultimo valor da linha não entra no calculo
    e o columns sem isso teria a quantidade de colunas
    '''
    somab = 0
    somat = 0
    for j in range(init, end):  # isto serve para não calcular linhas anteriores já calculdas

        # o primeiro parametro da linha não entrar no calculo pq é o indice da matriz e o ultimo era de classificação
        distanciaO = (np.sum(top(Mo[stance], Mo[j]))) ** 0.5
        # o mesmo caso anterior do commit anterior
        distanciap = (np.sum(top(Mp[stance], Mp[j]))) ** 0.5

        somab += distanciaO ** 2  # da formula onde a distancia do espaço projetado na parte inferior é elevado ao
        # quadrado
        somat += top(distanciaO, distanciap)

    return somab, somat
