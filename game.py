
ok = input("\nOlá, bem vindo ou meu projeto de BlackJack.  (press enter)\n")

user_hand, hand_value, fichas, bot_hand, bot_hand_value, mesa, play, estourou, bot_estourou, win, aposta = [], 0, 1000, [], 0, 0, "s", False, False, "None", 0
while play == "s":
    from utilidades import restart, status, bet, buy, initialize_hand, validate, hand
    # zera todas as variáveis
    user_hand, hand_value, estourou, win = restart(user_hand, hand_value, estourou, win)
    bot_hand, bot_hand_value, bot_estourou, Joker = restart(bot_hand, bot_hand_value, bot_estourou, None)
    
    # limpa o terminal
    
    # mostra status do jogo
    status(fichas,None,None)
    
    # define apostas e atualiza valor das variáveis
    fichas, mesa, aposta = bet(fichas, 0, aposta)

    # inicializa a mão do jogador com duas cartas
    user_hand, hand_value = initialize_hand(user_hand, hand_value)
    bot_hand, bot_hand_value = initialize_hand(bot_hand, bot_hand_value)
    status(fichas,aposta,mesa)
    hand(user_hand,hand_value,bot_hand)
    
    new_bet = input(f"\nFichas: {fichas}\nGostaria de almentar a aposta? s/n   ")
    if new_bet.lower() == "s":
        fichas, mesa, aposta = bet(fichas, mesa, aposta)

    cont = input(f"\nCartas: {user_hand}\nGostaria de comprar mais uma carta?     ")
    while cont == "s":
        user_hand, hand_value = buy(user_hand,hand_value)
        hand(user_hand,hand_value, bot_hand)
        # verifica se ele já não estourou
        if hand_value > 21:
            print(f"\nSua mão estourou!\nVocê perdeu: {aposta}\n")
            estourou = True
            break
        elif hand_value == 21:
            print(f"\n21!\nVocê ganhou: {mesa}\n")
            break
        
        new_bet = input(f"\nFichas: {fichas}\nGostaria de almentar a aposta? s/n   ")
        if new_bet.lower() == "s":
            fichas, mesa, aposta = bet(fichas, mesa, aposta)
            
        cont = input(f"\nCartas: {user_hand}\nGostaria de comprar mais uma carta?     ")
        
    while bot_hand_value < 16:
        bot_hand, bot_hand_value= buy(bot_hand, bot_hand_value)
        if bot_hand_value > 21:
            bot_estourou = True
            break
        elif bot_hand_value == 21:
            break
    
    # validação de resultados
    win = validate(user_hand,hand_value,estourou, aposta, bot_hand,bot_hand_value,bot_estourou, win)
    if win == "true":
        fichas += mesa
    elif win == "not_exactly":
        fichas += aposta
    else:
        pass

    play = input("\nJogar novamente? s/n  ")