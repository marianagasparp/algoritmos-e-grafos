# Mariana Gaspar - 2021032707
import sys
import funcoes as f


if __name__ == '__main__':

    arquivo = sys.argv[1]
        
    # cria matriz do arquivo
    matriz = f.ler_arquivo(arquivo)

    # imprime no me do arquivo
    print(f'Nome do arquivo: {arquivo} ')

    # imprime matriz
    print(matriz)

    # cria string com o nome do arquivo + dimensao da matriz
    resultado = arquivo + str(matriz.shape) + '\n'

    # imprime o resultado
    print(f'Resultado: {resultado}')

    # salva resultado
    f.salvar_arquivo('resultado.txt', resultado)
