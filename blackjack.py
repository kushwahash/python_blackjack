import random

'''
Project : Blackjack game
Global variables
'''
suits = ('Hearts','Clubs','Spades','Diamonds')
ranks = ('Ace','King','Queen','Jack','Ten','Nine','Eight','Seven','Six','Five','Four','Three','Two','One')
values = {'Ace':11,'King':10,'Queen':10,'Jack':10,'Ten':10,'Nine':9,'Eight':8,'Seven':7,'Six':6,'Five':5,
'Four':4,'Three':3,'Two':2}
playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    
    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.deck)
        

    def __str__(self):
        str_deck = ''
        for card in deck:
            str_deck += "\n "+print(card)
        
        return str_deck
    
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        #check for ace
        if(card.rank == "Ace"):
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def loos_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            bet_value = int(input("Please, enter your bet"))
        except:
            print("Not a valid entery, provide an integer")
        else:
            if bet_value <= chips.bet:
                break
            else:
                print("Your bet cannot exceed your reserve of {}".format(chips.bet))
    
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        try:
            choice = input("Do you want to hit(H) or stand(S), enter your choice H or S?")
        except:
            print("Not a valid choice, try again")
        else:
            if choice[0].lower() == 'h':
                hit(deck,hand)
                break
            elif choice[0].lower() == 's':
                print("Dealers turn start......")
                global playing = False
                break
            else:
                print("Not a valid choice, try again")

if __name__ == "__main__":
    #create 52 cards and add to deck
    
