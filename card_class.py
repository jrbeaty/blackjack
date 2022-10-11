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

    def __init__():
        pass





'''
test_deck = Deck()
test_deck.shuffle()

test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
'''







       



