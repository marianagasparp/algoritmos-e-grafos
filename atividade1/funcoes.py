# Mariana Gaspar - 2021032707
import numpy as np


# funcao que le o arquivo de texto e retorna os dados
def ler_arquivo(nome_arquivo):
    local_arquivo = './exemplos/'+ nome_arquivo + '.txt'

    with open(local_arquivo, 'r') as arquivo:
        dado = np.loadtxt(arquivo)

    return dado


# funcao para salvar arquivo usando o nome e o conteudo do mesmo como parametros
def salvar_arquivo(nome_arquivo, conteudo):
    local_arquivo = './' + nome_arquivo
    with open(local_arquivo, 'a') as arquivo:
        arquivo.write(conteudo)
    arquivo.close()
