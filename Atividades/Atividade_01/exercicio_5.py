numero = input("Digite um número entre 1000 e 9999: ") #Lendo o número como texto mesmo (sem o int!)

# Como tem 4 dígitos, as posições são 0, 1, 2 e 3.
# O milhar é o primeiro dígito (posição 0) e a unidade é o último (posição 3)

print(f"Unidade: {numero[3]}")
print(f"Dezena:  {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar:  {numero[0]}")
