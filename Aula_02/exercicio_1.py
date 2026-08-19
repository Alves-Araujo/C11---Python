import numpy as np

# criando os arrays de tamanho 8
arr_uns = np.ones(8, dtype=int)
arr_aleatorio = np.random.randint(0, 10, 8)

# soma e guarda no terceiro array
arr_resultado = arr_uns + arr_aleatorio

soma_total = arr_resultado.sum()

print("Array resultante:", arr_resultado)
print("Soma dos elementos:", soma_total)

# remodela dependendo da soma
if soma_total >= 40:
    # 4 linhas, 2 colunas (mais linhas)
    matriz = arr_resultado.reshape(4, 2)
else:
    # 2 linhas, 4 colunas (mais colunas)
    matriz = arr_resultado.reshape(2, 4)

print("\nMatriz remodelada:")
print(matriz)