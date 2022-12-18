from utilidades import baralho
from random import choice
import sys

# declara valor inicial das fichas
fichas = 1000.00

## player ##
user_hand = []
hand_value = 0
## bot ##
bot_hand = []
bot_hand_value = 0

print("")
print("Olá, bem vindo ou meu projeto de BlackJack")
nome = input("Qual é o seu nome?\n")

jogo = "s"

while jogo == "s":
    
    ################# parte da aposta ###################
    # define quanto será a aposta
    print("")
    print("Você tem {:.2f} reais em fichas.".format(fichas))
    
    if fichas > 0:
        print("")
        aposta = float(input("quanto será a posta dessa rodada?  "))
        if aposta <= fichas:
            fichas -= aposta
            premio = 2*aposta
        else:
            raise Exception("forçando except")
        # verifica se a variável é nula
    else:
        print("parece que suas fichas acabaram...")
        print("saia e entre novamente para poder reiniciar a quantidade de fichas")
        sys.exit()
    ################# parte do jogo ###################
    # zera a mão do jogador
    user_hand = []
    hand_value = 0
    bot_hand = []
    bot_hand_value = 0
    estourou = False
    bot_estourou = False
    
    print("")
    print(f"o senhor apostou {aposta:.2f}\nCaso ganhe, o prêmio será de +{aposta}")
    print("")
    print(f"aposta: {aposta:.2f}\npremio: {premio}\nfichas: {fichas:.2f}")

    for i in range(2):
        # transforma o dicionário em uma tupla com 2 valores, para 
        # variável = escolha(transforma em lista(pega key e valor do dicionário))
        # retorna 2 valores, a key e o valor
        random_card = choice(list(baralho.items()))
        
        # atribui respectivamente a key da carta e o valor aos valores corretos
        carta, valor = random_card

        # adiciona carta
        user_hand.append(carta)
        hand_value += valor
        
        random_card = choice(list(baralho.items()))
        carta, valor = random_card
        bot_hand.append(carta)
        bot_hand_value += valor


    print("") # enter
    print(f"cartas: {user_hand}")
    print(f"soma: {hand_value}")

    print("")
    cont = input("gostaria de comprar mais uma carta?\n")
    while cont == "s":
        random_card = choice(list(baralho.items()))
        carta, valor = random_card

        user_hand.append(carta)
        hand_value += valor
        
        print(f"cartas: {user_hand}")
        print(f"soma: {hand_value}")
        
        # verifica se ele já não estourou
        if hand_value > 21:
            print("")
            print("Sua mão estourou!")
            estourou = True
            print(f"você perdeu: {aposta}")
            break
        elif hand_value == 21:
            print("")
            print("21!")
            print(f"você ganhou: {aposta}")
            break

        print("")
        cont = input("gostaria de comprar mais uma carta? s/n\n")
        
# agora falta add a possibilidade de jogar contra um bot
# o bot será simples
# ele irá continuar comprando cartas até chegar o número de 17
# isso quer dizer que enquanto o valor na mão dele for menor ou igual a 17 ele continuará comprando cartas

    while bot_hand_value < 16:
        random_card = choice(list(baralho.items()))
        carta, valor = random_card
        bot_hand.append(carta)
        bot_hand_value += valor
        if bot_hand_value > 21:
            bot_estourou = True
            break

    #### final do game ####
    print("")
    # imprime mensagens de felicidade, caso tenha ganhado e de tristesa, caso tenha perdido.
    if bot_estourou and estourou == False:
        print(f"sua mão: {user_hand}, soma: {hand_value}\nmão do bot: {bot_hand}, soma: {bot_hand_value}")
        print(f"Parabéns! você ganhou {aposta}\n")
        fichas += premio
    elif estourou and bot_estourou == False:
        print(f"sua mão: {user_hand}, soma: {hand_value}\nmão do bot: {bot_hand}, soma: {bot_hand_value}")
        print("")
        print(f"Você estourou e perdeu {aposta}... jogue novamente para se recuperar.")
    elif hand_value > bot_hand_value and estourou == False:
        fichas += premio
        print(f"sua mão: {user_hand}, soma: {hand_value}\nmão do bot: {bot_hand}, soma: {bot_hand_value}")
        print(f"Parabéns! você ganhou {aposta}\n")
    elif bot_hand_value > hand_value and bot_estourou == False:
        print(f"sua mão: {user_hand}, soma: {hand_value}\nmão do bot: {bot_hand}, soma: {bot_hand_value}")
        print("")
        print(f"Você perdeu {aposta}...jogue novamente para se recuperar.")
    elif bot_estourou == True and estourou == True:
        print(f"sua mão: {user_hand}, soma: {hand_value}\nmão do bot: {bot_hand}, soma: {bot_hand_value}")
        print(f"Empate!, jogue novamente")
        fichas += aposta
    else:
        print(f"sua mão: {user_hand}, soma: {hand_value}\nmão do bot: {bot_hand}, soma: {bot_hand_value}")
        print(f"Empate!, jogue novamente")
        fichas += aposta

    # caso seja digitado qualquer coisa != s, a partida irá encerrar  
    jogo = input("\njogar novamente? s/n  ")