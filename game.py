
nome = input("\nOlá, bem vindo ou meu projeto de BlackJack\nQual é o seu nome?\n")

user_hand, hand_value, fichas, bot_hand, bot_hand_value, mesa, play, estourou, bot_estourou, win = [], 0, 1000, [], 0, 0, "s", False, False, False
while play == "s":
    from utilidades import restart, status, bet, buy, initialize_hand, bot, validate, hand
    
    # zera todas as variáveis
    user_hand, hand_value, estourou = restart(user_hand, hand_value, estourou)
    bot_hand, bot_hand_value, bot_estourou = restart(bot_hand, bot_hand_value, bot_estourou)
    
    # mostra status do jogo
    status(fichas,None,None)
    
    # define apostas e atualiza valor das variáveis
    fichas, mesa, aposta = bet(fichas, 0)

    # inicializa a mão do jogador com duas cartas
    user_hand, hand_value = initialize_hand(user_hand, hand_value)
    status(fichas,aposta,mesa)
    hand(user_hand,hand_value)

    cont = input("Gostaria de comprar mais uma carta?\n")
    while cont == "s":
        user_hand, hand_value = buy(user_hand,hand_value)
        hand(user_hand,hand_value)
        
        # verifica se ele já não estourou
        if hand_value > 21:
            print(f"\nSua mão estourou!\nVocê perdeu: {aposta}\n")
            estourou = True
            break
        elif hand_value == 21:
            print(f"\n21!\nVocê ganhou: {mesa}\n")
            break
        cont = input("\nGostaria de comprar mais uma carta? s/n\n")
    bot_hand, bot_hand_value, bot_estourou = bot(bot_hand, bot_hand_value)
    
    # validação de resultados
    win = validate(user_hand,hand_value,estourou, aposta, bot_hand,bot_hand_value,bot_estourou, win)
    if win == "true":
        fichas += mesa
    elif win == "not_exactly":
        fichas += aposta
    else:
        pass

    play = input("\nJogar novamente? s/n  ")