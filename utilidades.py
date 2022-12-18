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

class player:
    def __init__(self, nome, fichas, user_hand, hand_value):
        self.name = input("Qual é o seu nome?\n")
        self.fichas = 1000
        self.user_hand = []
        self.hand_value = 0

    def aposta(fichas):
        aposta = 0
        mesa = 0
        print(f"Você tem {fichas} reais em fichas.")
        aposta = float(input("quanto deseja apostar?\n"))
        mesa = 2 * aposta

    def status(fichas, aposta, mesa):
        print(f"Você tem {fichas} reais em fichas.")
        print(f"Asua aposta é de: {aposta}")
        print(f"valor da mesa: {mesa}")

    def cartas(user_hand, hand_value):
        print(f"cartas: {user_hand}")
        print(f"soma: {hand_value}")
        return