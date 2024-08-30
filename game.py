import util
import user


player = user.User()
player.type = "Player"
bot = user.User()
bot.type = "Bot"

jogo = "s"
while jogo == "s":
    print("\nVocê tem {:.2f} reais em fichas.".format(player.chips))
    util.apostar(player)
    table_value = player.bet*2
    
    print(f"\nvocê apostou {player.bet:.2f}\ncaso ganhe, o prêmio será de +{table_value}")
    player.show_table_status(table_value)

    for _ in range(2):
        # Ambos os players começam com duas cartas
        player.take_card()
        bot.take_card()

    # Parte do jogador comprar as cartas
    player.show_hand_status()
    cont = input("gostaria de comprar mais uma carta?\n")
    while cont == "s":

        player.take_card()
        player.show_hand_status()        
        util.user_hand_validator(player)
        if player.pass_ == True or player.hand_value == 21:
            break

        cont = input("\ngostaria de comprar mais uma carta? s/n\n")

    # Bot comprando as cartas
    while bot.hand_value < 16:
        bot.take_card()
        util.user_hand_validator(bot)
        if bot.pass_ == True:
            break

    #### final do game ####
    print(f"\nsua mão: {player.user_hand}, soma: {player.hand_value}\nmão do bot: {bot.user_hand}, soma: {bot.hand_value}")

    if bot.pass_ and player.pass_ == False:
        print(f"Parabéns! você ganhou {player.bet}\n")
        player.chips += table_value
    elif player.pass_ and bot.pass_ == False:
        print(f"Você player.pass_ e perdeu {player.bet}...")
    elif player.hand_value > bot.hand_value and player.pass_ == False:
        player.recive_bet(table_value)
        print(f"Parabéns! você ganhou {player.bet}\n")
    elif bot.hand_value > player.hand_value and bot.pass_ == False:
        print(f"Você perdeu {player.bet}...jogue novamente para se recuperar.")
    elif (bot.pass_ == True and player.pass_ == True) or (player.hand_value == bot.hand_value and player.pass_ == False):
        print("Empate!, jogue novamente")
        player.chips += player.bet
    else:
        print("Resultado não esperado!")

    player.reset()
    bot.reset()

    # caso seja digitado qualquer coisa != s, a partida irá encerrar  
    jogo = input("\njogar novamente? s/n  ")