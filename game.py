import util


    # declara valor inicial das fichas
fichas = 1000.00

## player ##
user_hand = []
hand_value = 0
## bot ##
bot_hand = []
bot_hand_value = 0
jogo = "s"
while jogo == "s":
    
    ################# parte da aposta ###################
    print("\nVocê tem {:.2f} reais em fichas.".format(fichas))
    aposta = float(input("\nquanto será a aposta dessa rodada?  "))
    aposta, fichas = util.apostar(aposta, fichas)
    premio = aposta*2
    ################# parte do jogo ###################
    # zera a mão do jogador
    user_hand = []
    hand_value = 0
    bot_hand = []
    bot_hand_value = 0
    estourou = False
    bot_estourou = False
    
    print(f"\nvocê apostou {aposta:.2f}\ncaso ganhe, o prêmio será de +{aposta}")
    print(f"\naposta: {aposta:.2f}\npremio: {premio}\nfichas: {fichas:.2f}")

    for _ in range(2):
        # transforma o dicionário em uma tupla com 2 valores, para 
        # variável = escolha(transforma em lista(pega key e valor do dicionário))
        # retorna 2 valores, a key e o valor
        carta, valor = util.take_card()

        # adiciona carta
        user_hand.append(carta)
        hand_value += valor
        
        random_card = util.take_card()
        carta, valor = random_card
        bot_hand.append(carta)
        bot_hand_value += valor


    print("") # enter
    print(f"cartas: {user_hand}")
    print(f"soma: {hand_value}")

    print("")
    cont = input("gostaria de comprar mais uma carta?\n")
    while cont == "s":
        carta, valor = util.take_card()

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
        carta, valor = util.take_card()
        bot_hand.append(carta)
        bot_hand_value += valor
        if bot_hand_value > 21:
            bot_estourou = True
            break

    #### final do game ####
    print(f"\nsua mão: {user_hand}, soma: {hand_value}\nmão do bot: {bot_hand}, soma: {bot_hand_value}")

    # imprime mensagens de felicidade, caso tenha ganhado e de tristesa, caso tenha perdido.
    if bot_estourou and estourou == False:
        print(f"Parabéns! você ganhou {aposta}\n")
        fichas += premio
    elif estourou and bot_estourou == False:
        print(f"Você estourou e perdeu {aposta}... jogue novamente para se recuperar.")
    elif hand_value > bot_hand_value and estourou == False:
        fichas += premio
        print(f"Parabéns! você ganhou {aposta}\n")
    elif bot_hand_value > hand_value and bot_estourou == False:
        print(f"Você perdeu {aposta}...jogue novamente para se recuperar.")
    elif (bot_estourou == True and estourou == True) or (hand_value == bot_hand_value and estourou == False):
        print("Empate!, jogue novamente")
        fichas += aposta
    else:
        print("Resultado não esperado!")

    # caso seja digitado qualquer coisa != s, a partida irá encerrar  
    jogo = input("\njogar novamente? s/n  ")