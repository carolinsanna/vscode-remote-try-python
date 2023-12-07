#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

def obter_escolha_usuario():
    escolha = input("Escolha: pedra, papel ou tesoura? ").lower()
    while escolha not in ['pedra', 'papel', 'tesoura']:
        print("Opção inválida. Por favor, escolha pedra, papel ou tesoura.")
        escolha = input("Escolha: pedra, papel ou tesoura? ").lower()
    return escolha

def obter_escolha_computador():
    return random.choice(['pedra', 'papel', 'tesoura'])

def determinar_vencedor(usuario, computador):
    if usuario == computador:
        return "Empate!"
    elif (usuario == 'pedra' and computador == 'tesoura') or \
         (usuario == 'tesoura' and computador == 'papel') or \
         (usuario == 'papel' and computador == 'pedra'):
        return "Você venceu!"
    else:
        return "Você perdeu!"

def main():
    pontuacao_usuario = 0
    pontuacao_computador = 0

    while True:
        escolha_usuario = obter_escolha_usuario()
        escolha_computador = obter_escolha_computador()

        print(f"Você escolheu: {escolha_usuario}")
        print(f"O computador escolheu: {escolha_computador}")

        resultado = determinar_vencedor(escolha_usuario, escolha_computador)
        print(resultado)

        if resultado == "Você venceu!":
            pontuacao_usuario += 1
        elif resultado == "Você perdeu!":
            pontuacao_computador += 1

        print(f"Pontuação atual - Você: {pontuacao_usuario}, Computador: {pontuacao_computador}")

        jogar_novamente = input("Quer jogar novamente? (sim/não) ").lower()
        if jogar_novamente != 'sim':
            print("Jogo encerrado. Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()

