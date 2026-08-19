import numpy as np

# pares de 0 a 51 (usando 52 pro 50 entrar na lista)
arr1 = np.arange(0, 52, 2)

# pares de 100 a 50 descendo (usando 49 pro 50 entrar)
arr2 = np.arange(100, 49, -2)

# junta os dois
arr_concatenado = np.concatenate((arr1, arr2))

# ordena o resultado
resultado_final = np.sort(arr_concatenado)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("\nArray final ordenado:")
print(resultado_final)