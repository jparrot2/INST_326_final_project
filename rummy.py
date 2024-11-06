'''Plays the card game rummy'''

class Card: 
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def __eq__(self, other):
        if isinstance (other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False 
    
class Deck:
    def __init__(self): 
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        # this is a list comprehension that involves an instance of the Card class to to couple together suits and ranks.
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
    
    def deal(self, num_cards):
    dealt_cards = [] 
    for card in range(num_cards):
        if self.cards
            dealt_cards.append(self.cards.pop())
        else:
            break 
            
        return dealt_cards 
    
     def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None
        

class Player:
       
class RummyGame: