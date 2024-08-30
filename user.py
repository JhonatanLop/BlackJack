import util

class User:
    def __init__(self):
        self.user_hand = []
        self.hand_value = 0
        self.pass_ = False
        self.chips = 1000
        self.bet = 0
        self.type = ""

    def update_hand(self, obj):
        self.user_hand.append(obj)
    
    def update_hand_value(self, obj):
        self.hand_value += obj
    
    def update_status(self):
        self.pass_ = True
    
    def reset(self):
        self.user_hand = []
        self.hand_value = 0
        self.pass_ = False
        self.bet = 0

    def pay_bet(self, value):
        self.chips -= value

    def recive_bet(self, value):
        self.chips += value

    def take_card(self):
        card, value = util.take_card()
        self.user_hand.append(card)
        self.hand_value += value

    def show_table_status(self, table_value):
        print(f"\naposta: {self.bet:.2f}\npremio: {table_value}\nfichas: {self.chips:.2f}")

    def show_hand_status(self):
        print(f"\ncartas: {self.user_hand}")
        print(f"soma: {self.hand_value}\n")