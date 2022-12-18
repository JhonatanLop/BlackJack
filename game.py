from random import choice
import sys

nome = input("\nOlá, bem vindo ou meu projeto de BlackJack\nQual é o seu nome?\n")

user_hand, hand_value, fichas, bot_hand, bot_hand_value, mesa, play = [], 0, 1000, [], 0, 0, "s"

while play == "s":
    from utilidades import restart, status, bet, buy, initialize_hand, cards, bot, validate
    
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
        
    bot_hand, bot_hand_value, bot_estourou = bot(bot_hand, bot_hand_value)
    
    # validação de resultados
    win = validate(user_hand,hand_value,estourou,bot_hand,bot_hand_value,bot_estourou)
    if win == "true":
        fichas += mesa
    elif win == "not_exactly":
        fichas += aposta
    else:
        pass
    jogo = input("\njogar novamente? s/n  ")