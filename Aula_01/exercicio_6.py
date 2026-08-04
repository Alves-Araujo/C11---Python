import math

decimal = float(input("Digite um número decimal: "))

raiz = math.sqrt(decimal) #mostra a raiz quadrada
teto = math.ceil(decimal) #mostra o teto
chao = math.floor(decimal) #mostra o chão
inteiro = math.trunc(decimal) #mostra o número inteiro

print(f"Sua raiz: {raiz: .2f}")
print(f"Seu teto: {teto}")
print(f"Seu chao: {chao}")
print(f"Seu inteiro: {inteiro}")
