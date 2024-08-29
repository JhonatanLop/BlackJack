import secrets

baralho = {
    "A-P" : 1,
    "A-O" : 1,
    "A-C" : 1,
    "A-E" : 1,
    "2-P" : 2,
    "2-O" : 2,
    "2-C" : 2,
    "2-E" : 2,
    "3-P" : 3,
    "3-O" : 3,
    "3-C" : 3,
    "3-E" : 3,
    "4-P" : 4,
    "4-O" : 4,
    "4-C" : 4,
    "4-E" : 4,
    "5-P" : 5,
    "5-O" : 5,
    "5-C" : 5,
    "5-E" : 5,
    "6-P" : 6,
    "6-O" : 6,
    "6-C" : 6,
    "6-E" : 6,
    "7-P" : 7,
    "7-O" : 7,
    "7-C" : 7,
    "7-E" : 7,
    "8-P" : 8,
    "8-O" : 8,
    "8-C" : 8,
    "8-E" : 8,
    "9-P" : 9,
    "9-O" : 9,
    "9-C" : 9,
    "9-E" : 9,
    "Q-P" : 10,
    "Q-O" : 10,
    "Q-C" : 10,
    "Q-E" : 10,
    "J-P" : 10,
    "J-O" : 10,
    "J-C" : 10,
    "J-E" : 10,
    "K-P" : 10,
    "K-O" : 10,
    "K-C" : 10,
    "K-E" : 10,
}
    
def take_card():
    return secrets.choice(list(baralho.items()))

def apostar (aposta, fichas):
    if aposta < 0:
        print("o valor tem que ser maior ou igual a 0")
        return 0, fichas
    if fichas > 0:
        if aposta <= fichas and aposta > 0:
            fichas -= aposta
        else:
            print("não há fichas suficientes!")
    else:
        print("parece que suas fichas acabaram...")
    return aposta, fichas