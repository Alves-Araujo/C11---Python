import numpy as np

# criando uma matriz de tamanho qualquer (aqui escolhi 3x5 com números aleatórios de 1 a 9)
matriz = np.random.randint(1, 10, (3, 5))

# pegando a quantidade de linhas e colunas pelo .shape
linhas, colunas = matriz.shape

# multiplicando pra saber o total de itens
total_elementos = linhas * colunas

print(f"Matriz original ({linhas} linhas x {colunas} colunas):")
print(matriz)
print(f"\nTotal de elementos: {total_elementos}")

# checando se o total é par ou ímpar (o resto da divisão por 2 tem que ser zero pra ser par)
if total_elementos % 2 == 0:
    print("Essa matriz viraria um vetor unidimensional com um número PAR de elementos.")
else:
    print("Essa matriz viraria um vetor unidimensional com um número ÍMPAR de elementos.")