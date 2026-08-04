numero = int(input("Qual número você quer ver a tabuada? ")) #inserindo o número da tabuada
inicio = int(input("A tabuada deve iniciar em qual número? ")) #inserindo o início do intervalo
fim = int(input("A tabuada deve ir até qual número? ")) #inserindo o fim do intervalo

print(f"\n Tabuada do: {numero} (De {inicio} até {fim})") #exibindo as informações da tabuada
for multiplicador in range(inicio, fim + 1): #criando o laço de repetição
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")


    # -- Considerações: --
    # f" : serve para poder misturar texto e variáveis na mesma frase
    # multiplicador: é o nosso 'i', nosso contador (1,2,3,4,...)
    # range(início, fim): define nosso intervalo, onde ele inicia e onde ele termina
    # fim + 1 : o início é inclusivo, o fim não, então precisamos usar '+1', para incluir o número do intervalo final