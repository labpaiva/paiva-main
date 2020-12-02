import numpy as np


def form_matrix(Caminho_matriz, tam=-1):
    matriz = []
    c = 0
    for linha in Caminho_matriz:
        if c < 4:  # servi para pular as 4 primeiras linhas do arquivo .data
            print(linha)
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
