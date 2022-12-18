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

def restart(player_hand, player_hand_value, bot_hand, bot_hand_value, table):
    user_hand = []
    hand_value = 0
    bot_hand = []
    bot_hand_value = 0
    mesa = 0
    return user_hand, hand_value, bot_hand, bot_hand_value, mesa

def bet(fichas, mesa):
    if fichas > 0:
        aposta = float(input("quanto deseja apostar?\n"))
        if aposta <= fichas:
            fichas -= aposta
            mesa = 2*aposta
            print("")
            print(f"\nO senhor apostou {aposta:.2f}\nCaso ganhe, o prêmio será de +{aposta}\n \nAposta: {aposta:.2f}\nPremio: {mesa}\nFichas: {fichas:.2f}")
        else:
            print("Suas fichas são insuficientes para essa aposta.")    
            return
    else:
        print("Suas fichas acabaram.\nReinicie o jogo para recomeçar")
        sys.exit()
    return fichas, mesa, aposta

def status(fichas, aposta, mesa):
    try:
        if not fichas == None:
           print(f"Você tem {fichas} reais em fichas.")
        if not aposta == None:
           print(f"Asua aposta é de: {aposta}")
        if not mesa == None:
            print(f"valor da mesa: {mesa}")
    except:
        print("erro em: utilidades.py, // função (status)")
    return " "
    
def cards(user_hand, hand_value):
    return f"\ncartas: {user_hand}\nsoma: {hand_value}\n"

def buy(user_hand, hand_value):
    # pega carta aleatória do baralho
    random_card = choice(list(baralho.items()))
    carta, value = random_card
    
    # add carta e soma à mão do player
    user_hand.append(carta)
    hand_value += value
    return user_hand, hand_value 

def initialize_hand(user_hand, hand_value):
    for i in range (2):
        buy(user_hand,hand_value)

def bot(bot_hand, bot_hand_value):
    while bot_hand_value < 16:
        buy(bot_hand,bot_hand_value)