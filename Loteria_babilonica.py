
import random

numero_sorteado = random.randint(1,15)

for tentativa in range(1, 4):

    escolha = int(input(f"Tentativa {tentativa}/3 - Escolha um número de 1 a 15: "))

    if(escolha == numero_sorteado):
        print(f"Você acertou na mosca! O número era {numero_sorteado}. Parabéns!")
        break

    elif(escolha > numero_sorteado):
        print("Errou! O número escolhido é maior que o número sorteado.")
    
    else:
        print("Errou! O número escolhido é menor que o número sorteado.")

else:
    print(f"Suas chances acabaram! O número sorteado foi {numero_sorteado}. Mais sorte da próxima vez!")







