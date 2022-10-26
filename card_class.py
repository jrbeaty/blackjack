# BLACK JACK GAME

import random

# *********************************************************************************************************************************************************
#GLOBAL VARIBALES

#tuple
suits = ('Hearts','Spades','Clubs','Diamonds')
#tuple
cards = ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace')
#dictionary values['Two'] > 2. Can pass in suits / cards variable and get back number value. 
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

# Game on, set to false when game is over.
playing = True

# *********************************************************************************************************************************************************
# CARD CLASS

class Card():

    def __init__(self, suit, card):

        self.suit = suit
        #card = rank
        self.card = card
    
    # string representation
    def __str__(self):

        return self.card + ' of ' + self.suit

# *********************************************************************************************************************************************************
# DECK CLASS

class Deck():

    def __init__(self):

        # creating an empty list
        self.deck = []

        #looping through suits list
        for suit in suits:
            #looping through values dictionary grabbing string value
            for value in values:
                #Calling the Card Class __str__ method and appending the results to the currently empty self.deck list
                self.deck.append(Card(suit, value))
    
    # defining the string method allows you call this method and return a pre-determined string pulling the items in a list created in the __init__()
    def __str__(self):

        #We need to start with an empty string
        deck_str = ''
        # looping through the 52 deck
        for card in self.deck:
            deck_str += '\n' + card.__str__()
        return 'The deck has ' + deck_str

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

# *********************************************************************************************************************************************************
# HAND CLASS

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        #calling deal from the Deck class which pops off a single card
        self.cards.append(card)
        #assigning value of hand from values dictionary **card = rank**
        self.value += values[card.card]

        if card.card == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        #'self.aces' is checking to see if self.aces is = to zero which returns a boolean false. 
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# *********************************************************************************************************************************************************
# CHIPS CLASS

class Chips():

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# *********************************************************************************************************************************************************
# FUNCTIONS

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break
            
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

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

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
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
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break







       



