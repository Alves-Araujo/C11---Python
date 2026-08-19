import numpy as np

# cria a matriz 2x2 só com zeros
campo = np.zeros((2, 2), dtype=int)

# escolhe uma posição aleatória pra colocar a bomba (1)
linha_bomba = np.random.randint(2)
coluna_bomba = np.random.randint(2)
campo[linha_bomba, coluna_bomba] = 1

# variavel pra rastrear se o jogador sobreviveu até o final
venceu = True

print("Mini Campo Minado 2x2")
print("Lembrete: as posições vão de 0 a 1 (ex: Linha 0, Coluna 1)\n")

# o jogo tem no máximo 3 rodadas (para achar os 3 zeros)
for i in range(3):
    print(f"--- Rodada {i+1} ---")

    # pegando a jogada
    l = int(input("Escolha a linha: "))
    c = int(input("Escolha a coluna: "))

    # verifica se pisou na bomba
    if campo[l, c] == 1:
        print("\nGame Over! :( Try Again!")
        venceu = False
        break # pisou na bomba, para o loop na hora
    else:
        print("Safe! Mandou bem.\n")

# se completou o loop de 3 jogadas sem a variavel 'venceu' virar False
if venceu:
    print("Congratulations! You beat the game! :)")