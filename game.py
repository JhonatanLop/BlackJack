from random import choice
import sys

nome = input("\nOlá, bem vindo ou meu projeto de BlackJack\nQual é o seu nome?\n")

user_hand, hand_value, fichas, bot_hand, bot_hand_value, mesa, play = [], 0, 1000, [], 0, 0, "s"

while play == "s":
    from utilidades import restart, status, bet, buy, initialize_hand, cards
    
    # zera todas as variáveis
    restart(user_hand, hand_value, bot_hand, bot_hand_value, mesa)
    
    # mostra status do jogo
    status(fichas,None,None)
    
    # define apostas e atualiza valor das variáveis
    fichas, mesa, aposta = bet(fichas, 0)

    # inicializa a mão do jogador com duas cartas
    user_hand, hand_value = initialize_hand()

    cards(user_hand, hand_value)

    print("")
    cont = input("gostaria de comprar mais uma carta?\n")
    while cont == "s":
        buy(user_hand,hand_value)
        cards(user_hand,hand_value)
        
        # verifica se ele já não estourou
        if hand_value > 21:
            print("\nSua mão estourou!\nvocê perdeu: {aposta}\n")
            estourou = True
            break
        elif hand_value == 21:
            print(f"\n21!\nvocê ganhou: {mesa}\n")
            break
        cont = input("\ngostaria de comprar mais uma carta? s/n\n")
        
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
        fichas += mesa
    elif estourou and bot_estourou == False:
        print(f"sua mão: {user_hand}, soma: {hand_value}\nmão do bot: {bot_hand}, soma: {bot_hand_value}")
        print("")
        print(f"Você estourou e perdeu {aposta}... jogue novamente para se recuperar.")
    elif hand_value > bot_hand_value and estourou == False:
        fichas += mesa
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