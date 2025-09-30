# Loteria-Babil-nica
🎲 Jogo de Adivinhação — Número Secreto
📌 Descrição

Este projeto é um jogo simples de adivinhação feito em Python.
O programa sorteia um número entre 1 e 15, e o jogador tem 3 tentativas para adivinhar qual é esse número.
Durante o jogo, o programa dá dicas informando se o palpite do jogador foi maior ou menor que o número sorteado.

🧠 Funcionamento do programa

O programa utiliza a função randint() da biblioteca random para gerar um número aleatório entre 1 e 15.

O jogador tem 3 chances para acertar.

A cada tentativa:

✅ Se o número for igual ao sorteado → o jogador vence e o jogo termina.

📉 Se for maior → o programa informa que o palpite foi maior.

📈 Se for menor → o programa informa que o palpite foi menor.

Se o jogador não acertar em 3 tentativas, o número sorteado será revelado no final.
