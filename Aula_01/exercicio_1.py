nome = input("Por favor, digite seu nome: ") #inserindo nome

print("Nome em maiúsculo: ", nome.upper()) #exibindo nome em maiúsculo
print("Nome em minúsculo: ", nome.lower()) #exibindo nome em minúsculo

#'replace' procura algo para substituir, nesse caso, ele troca os espaços vazios
nome_sem_espacos = nome.replace(" ", "") #tirando os espaços do nome antes de contar
#'len' conta todos os caracteres digitados
tamanho_nome = len(nome_sem_espacos) #armazena a quantidade de letras em uma variável
print("Tamanho do nome: ", tamanho_nome, " letras.") #exibindo o tamanho do nome

vetor_palavras = nome.split()       # Divide o nome em um vetor: ['Nome', 'Meio', 'Sobrenome']
vetor_palavras[-1] = "do Inatel"    # O '-1' acessa direto a última posição e substitui por 'do Inatel'
nome_inatel = " ".join(vetor_palavras) # Junta as palavras do vetor de volta em um único texto
print("Como ficaria no Inatel:", nome_inatel)

# Outra forma de fazer é:
#   partes_do_nome = nome.split() #Divide o nome em uma lista de palavras
#   partes_do_nome.pop() #Remove a última palavra (o último sobrenome)
#   partes_do_nome.append("do Inatel") #Adiciona "do Inatel" no lugar
#   nome_inatel = " ".join(partes_do_nome) #Junta a lista de volta em um texto normal
#   print("Como ficaria no Inatel:", nome_inatel) #exibindo o nome final