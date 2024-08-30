import secrets
import user

baralho = {
    "A♣️" : 1,
    "A♦️" : 1,
    "A♥️" : 1,
    "A♠️" : 1,
    "2♣️" : 2,
    "2♦️" : 2,
    "2♥️" : 2,
    "2♠️" : 2,
    "3♣️" : 3,
    "3♦️" : 3,
    "3♥️" : 3,
    "3♠️" : 3,
    "4♣️" : 4,
    "4♦️" : 4,
    "4♥️" : 4,
    "4♠️" : 4,
    "5♣️" : 5,
    "5♦️" : 5,
    "5♥️" : 5,
    "5♠️" : 5,
    "6♣️" : 6,
    "6♦️" : 6,
    "6♥️" : 6,
    "6♠️" : 6,
    "7♣️" : 7,
    "7♦️" : 7,
    "7♥️" : 7,
    "7♠️" : 7,
    "8♣️" : 8,
    "8♦️" : 8,
    "8♥️" : 8,
    "8♠️" : 8,
    "9♣️" : 9,
    "9♦️" : 9,
    "9♥️" : 9,
    "9♠️" : 9,
    "Q♣️" : 10,
    "Q♦️" : 10,
    "Q♥️" : 10,
    "Q♠️" : 10,
    "J♣️" : 10,
    "J♦️" : 10,
    "J♥️" : 10,
    "J♠️" : 10,
    "K♣️" : 10,
    "K♦️" : 10,
    "K♥️" : 10,
    "K♠️" : 10,
}
    
def take_card():
    return secrets.choice(list(baralho.items()))

def apostar (player):
    bet_value = float(input("\nquanto será a aposta dessa rodada?  "))
    if bet_value < 0:
        return "o valor tem que ser maior ou igual a 0"
    if player.chips > 0:
        if bet_value <= player.chips and bet_value > 0:
            player.bet = bet_value
            player.pay_bet(bet_value)
        else:
            return "não há fichas suficientes!"
    else:
        return "parece que suas fichas acabaram..."

def user_hand_validator(player):
    if player.type == "Player":
        if player.hand_value > 21:
            print("\nSua mão estourou!")
            player.pass_ = True
            print(f"você perdeu: {player.bet}")
        elif player.hand_value == 21:
            print("\n21!")
            print(f"você ganhou: {player.bet}")
    else:
        if player.hand_value > 21:
            player.pass_ = True
        elif player.hand_value == 21:
            return