'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

import numpy as np

 #verifica simetria comparando a matriz com a sua transposta
def simetrica(matriz):
    qtdVertices = np.shape(matriz)[0]
    transposta = np.empty((qtdVertices, qtdVertices))
    for l in range(qtdVertices):
        for c in range(qtdVertices):
            transposta[c][l] = matriz[l][c]
    if (matriz == transposta).all():
        return True
    else:
        return False



'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


def tipoGrafo(matriz):

    if not simetrica(matriz):
        return 1 # é digrafo

    for linha in matriz:
        for item in linha:
            if item > 1 : # possui arestas paralenas
                 for item in matriz.diagonal():
                     if item > 0: # possui laços
                         return 3
                     else:
                         return 2

    # é grafo simpls
    return 0




def calcDensidade(matriz):
    qtdVertices = np.shape(matriz)[0]
    qtdArestas = 0
    for linha in matriz:
        for item in linha:
            qtdArestas += item #soma arestas

    densidade = qtdArestas / (qtdVertices*(qtdVertices-1)) # formula
    densidade = np.round(densidade,3)
    return densidade




def insereAresta(matriz, vi, vj):
    matriz[vi-1][vj-1] += 1
    if not tipoGrafo(matriz) == 1:
        matriz[vj-1][vi-1] += 1
    return matriz

def insereVertice(matriz, vi):
    qtdVertices = np.shape(matriz)[0]
    if vi > qtdVertices:
        np.append(matriz, qtdVertices ,0, axis=0)
        np.append(matriz, qtdVertices ,0, axis=1)
    return matriz

def removeAresta(matriz, vi, vj):
    if matriz[vi - 1][vj - 1] != 0:
        matriz[vi][vj] -= 1
        if not tipoGrafo(matriz) == 1:
            matriz[vj][vi] -= 1
    else:
        print("A aresta não existe ")
    return matriz


def removeVertice(matriz, vi):
    qtdVertices = np.shape(matriz)[0]
    if vi < qtdVertices:
        np.delete(matriz, vi, axis=0)
        np.delete(matriz, vi, axis=1)






