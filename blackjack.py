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
    
    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.deck)
        

    def __str__(self):
        str_deck = ''
        for card in self.deck:
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
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
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
            bet_value = int(input("Please, enter your bet :: "))
        except:
            print("Not a valid entery, provide an integer")
        else:
            if bet_value <= chips.total:
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
            choice = input("Do you want to hit(H) or stand(S), enter your choice H or S ? :: ")
        except:
            print("Not a valid choice, try again")
        else:
            if choice[0].lower() == 'h':
                hit(deck,hand)
                break
            elif choice[0].lower() == 's':
                print("Dealers turn start......")
                playing = False
                break
            else:
                print("Not a valid choice, try again")

def player_busts(player,dealer,chips):
    print("Player is busted, bet is lost")
    chips.loos_bet()

def player_wins(player,dealer,chips):
    print("Player Win.")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer is busted.Player Win.")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer Win, player looses the bet")
    chips.loos_bet()
    
def push(player,dealer):
    print("Dealer and Player Tie!!")

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

#Start the game play
while True:
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17 :
            hit_or_stand(deck,dealer_hand)
            show_all(player_hand,dealer_hand)
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
    
    print("Player value :: {}".format(player_hand.value))
    play_again = input("Play again ? Enter Y")
    if play_again[0].lower() == 'Y':
        playing = True
        continue
    else:
        print("Thanks for playing.")
        playing = False
        break

