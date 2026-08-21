palavra = input("Digite uma palavra: ")

total_vogais = 0 #nosso contador de vogal

print("\n--- Letras da Palavra ---")

for letra in palavra: #'letra' é uma varável temporária

    letra_maiuscula = letra.upper()
    print(letra_maiuscula) # Imprime a letra da vez em maiúsculo

    # Se a letra da vez estiver "dentro" do grupo de vogais, somamos 1 no contador
    if letra_maiuscula in "AEIOU":
        total_vogais += 1  # total_vogais = total_vogais + 1

print(f"Total de vogais na palavra: {total_vogais}") #total de vogais

if "A" in palavra.upper(): #verifica se a letra 'A' está presente, usei o upper para contar mesmo se o 'a' for minúsculo
    print("A letra 'A' está presente na palavra? Sim!")
else:
    print("A letra 'A' está presente na palavra? Não!")