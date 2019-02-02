import random

'''
Project : Blackjack game
Global variables
'''
suits = ('Hearts','Clubs','Spades','Diamonds')
ranks = ('Ace','King','Queen','Jack','Ten','Nine','Eight','Seven','Six','Five','Four','Three','Two','One')
values = {'Ace':11,'King':10,'Queen':10,'Jack':10,'Ten':10,'Nine':9,'Eight':8,'Seven':7,'Six':6,'Five':5,
'Four':4,'Three':3,'Two':2}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    
    def __str__(self):
        return "Suit : {} Rank: {} Value: {}".format(self.suit,self.rank,self.value)


if __name__ == "__main__":
    #create 52 cards and add to deck
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit,rank))
