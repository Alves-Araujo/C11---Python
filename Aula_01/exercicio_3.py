while True:

    sexo = input("Digite o sexo (M para homem ou F para mulher): ").upper()

    if sexo == "M":
        print("Você é homem.")
        break

    elif sexo == "F":
        print("Você é mulher.")
        break

    else:
        # Se não for nem M nem F, ele cai aqui, avisa o erro e o laço recomeça!
        print("Entrada inválida! Por favor, digite apenas M ou F.\n")