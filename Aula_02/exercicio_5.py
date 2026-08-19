import numpy as np

# fixando a semente pra gerar sempre o mesmo resultado, como pede o exercício
np.random.seed(10)

# criando a matriz 4x4 com números de 1 a 50 (usando 51 pro 50 ser incluso)
matriz = np.random.randint(1, 51, (4, 4))
print("Matriz original:")
print(matriz)
print("\n")

# a) médias de cada linha (axis=1) e coluna (axis=0)
medias_linhas = matriz.mean(axis=1)
medias_colunas = matriz.mean(axis=0)

print("a) Médias:")
print("Linhas:", medias_linhas)
print("Colunas:", medias_colunas)
print("\n")

# b) pegando o valor máximo dessas médias
print("b) Maiores médias:")
print("Maior média das linhas:", medias_linhas.max())
print("Maior média das colunas:", medias_colunas.max())
print("\n")

# c) contando as aparições de cada número
# a função unique com return_counts já devolve os números e quantas vezes apareceram
numeros, contagens = np.unique(matriz, return_counts=True)

print("c) Quantidade de aparições:")
for n, qtd in zip(numeros, contagens):
    print(f"O número {n} aparece {qtd} vez(es)")

# filtrando só a galera que apareceu exatamente 2 vezes
aparecem_duas_vezes = numeros[contagens == 2]

print("\nNúmeros que aparecem exatamente 2 vezes:", aparecem_duas_vezes)