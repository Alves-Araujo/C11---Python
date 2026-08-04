distancia = float(input("Qual a distância da viagem? "))

if distancia <= 200.00:
    valor = distancia * 0.50
elif distancia > 200.00:
    valor = distancia * 0.45

print(f"O valor da viagem ficará em R${valor:.2f}") #'.2f' para exibir 2 casas depois da vírgula