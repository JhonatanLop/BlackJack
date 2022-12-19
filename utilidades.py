import sys
from random import choice

baralho = {
    "A" : 1,
    "A" : 1,
    "A" : 1,
    "A" : 1,
    "2" : 2,
    "2" : 2,
    "2" : 2,
    "2" : 2,
    "3" : 3,
    "3" : 3,
    "3" : 3,
    "3" : 3,
    "4" : 4,
    "4" : 4,
    "4" : 4,
    "4" : 4,
    "5" : 5,
    "5" : 5,
    "5" : 5,
    "5" : 5,
    "6" : 6,
    "6" : 6,
    "6" : 6,
    "6" : 6,
    "7" : 7,
    "7" : 7,
    "7" : 7,
    "7" : 7,
    "8" : 8,
    "8" : 8,
    "8" : 8,
    "8" : 8,
    "9" : 9,
    "9" : 9,
    "9" : 9,
    "9" : 9,
    "Q" : 10,
    "Q" : 10,
    "Q" : 10,
    "Q" : 10,
    "J" : 10,
    "J" : 10,
    "J" : 10,
    "J" : 10,
    "K" : 10,
    "K" : 10,
    "K" : 10,
}
baralho2 ={
    "A" : 1,
    "A" : 1,
    "A" : 1,
    "A" : 1,
    "2" : 2,
    "2" : 2,
    "2" : 2,
    "2" : 2,
    "3" : 3,
    "3" : 3,
    "3" : 3,
    "3" : 3,
    "4" : 4,
    "4" : 4,
    "4" : 4,
    "4" : 4,
    "5" : 5,
    "5" : 5,
    "5" : 5,
    "5" : 5,
    "6" : 6,
    "6" : 6,
    "6" : 6,
    "6" : 6,
    "7" : 7,
    "7" : 7,
    "7" : 7,
    "7" : 7,
    "8" : 8,
    "8" : 8,
    "8" : 8,
    "8" : 8,
    "9" : 9,
    "9" : 9,
    "9" : 9,
    "9" : 9,
    "Q" : 10,
    "Q" : 10,
    "Q" : 10,
    "Q" : 10,
    "J" : 10,
    "J" : 10,
    "J" : 10,
    "J" : 10,
    "K" : 10,
    "K" : 10,
    "K" : 10,
}

### em estudo ###
# class player:
#     def __init__(self, nome, fichas, user_hand, hand_value):
#         self.name = input("Qual é o seu nome?\n")
#         self.fichas = 1000
#         self.user_hand = []
#         self.hand_value = 0

def restart(player_hand, player_hand_value, estourou):
    player_hand = []
    player_hand_value = 0
    estourou = False
    return player_hand, player_hand_value, estourou

def bet(fichas, mesa):
    if fichas > 0:
        aposta = float(input("\nQuanto deseja apostar?\n"))
        if aposta <= fichas:
            fichas -= aposta
            mesa = 2*aposta
            print("")
            print(f"\nO senhor apostou {aposta:.2f}\nCaso ganhe, o prêmio será de +{aposta}\n \nAposta: {aposta:.2f}\nValor da mesa: {mesa}\nFichas: {fichas:.2f}\n")
        else:
            print("\nSuas fichas são insuficientes para essa aposta.\n")    
            return
    else:
        print("\nSuas fichas acabaram.\nReinicie o jogo para recomeçar")
        sys.exit()
    return fichas, mesa, aposta

def status(fichas, aposta, mesa):
    try:
        if not fichas == None:
           print(f"\nVocê tem {fichas} reais em fichas.")
        if not aposta == None:
           print(f"Asua aposta é de: {aposta}")
        if not mesa == None:
            print(f"Valor da mesa: {mesa}\n")
    except:
        print("Erro em: utilidades.py, // função (status)")
    return " "
    
def buy(user_hand, hand_value):
    # pega carta aleatória do baralho
    random_card = choice(list(baralho.items()))
    card, value = random_card
    
    # add carta e soma à mão do player
    user_hand.append(card)
    hand_value += value
    return user_hand, hand_value

def initialize_hand(user_hand, hand_value):
    for i in range (2):
        user_hand, hand_value = buy(user_hand,hand_value)
    return user_hand, hand_value

def bot(bot_hand, bot_hand_value):
    global bot_estourou
    bot_estourou = False
    while bot_hand_value < 16:
        bot_hand,bot_hand_value = buy(bot_hand,bot_hand_value)
        if bot_hand_value > 21:
            bot_estourou = True
            break
    return bot_hand, bot_hand_value, bot_estourou

def validate(user_hand, hand_value, estourou, aposta, bot_hand, bot_hand_value, bot_estourou, win):
    mesa = 2 * aposta
    if bot_estourou and estourou == False:
        print(f"Sua mão: {user_hand}, Soma: {hand_value}\nMão do bot: {bot_hand}, Soma: {bot_hand_value}\nParabéns! Você ganhou {mesa}\n")
        win = "true"
    elif estourou and bot_estourou == False:
        print(f"Sua mão: {user_hand}, Soma: {hand_value}\nMão do bot: {bot_hand}, Soma: {bot_hand_value}\nVocê estourou e perdeu {aposta}\nJogue novamente para se recuperar.\n")
    elif hand_value > bot_hand_value and estourou == False:
        print(f"Sua mão: {user_hand}, Soma: {hand_value}\nMão do bot: {bot_hand}, Soma: {bot_hand_value}\nParabéns! você ganhou {mesa}\n")
        win = "true"
    elif bot_hand_value > hand_value and bot_estourou == False:
        print(f"Sua mão: {user_hand}, Soma: {hand_value}\nMão do bot: {bot_hand}, Soma: {bot_hand_value}\nVocê perdeu {aposta}\n ogue novamente para se recuperar.\n")
    elif bot_estourou == True and estourou == True:
        print(f"Sua mão: {user_hand}, Soma: {hand_value}\nMão do bot: {bot_hand}, Soma: {bot_hand_value}\nEmpate! Ambos estouraram, jogue novamente\n")
        win = "not_exactly"
    else:
        print(f"Sua mão: {user_hand}, Soma: {hand_value}\nMão do bot: {bot_hand}, Soma: {bot_hand_value}\nEmpate!, jogue novamente\n")
        win = "not_exactly"
    return win

def hand(user_hand, hand_value):
    print(f"\nCartas: {user_hand}\nSoma: {hand_value}\n")
    return " "