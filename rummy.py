'''Plays the card game rummy'''

class Card: 
    def __init__(self, rank, suit):
        self.rank= rank
        self.suit= suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def __eq__(self, other):
        if isinstance (other, Card):
            return self.rank == other.rank and self.suit==other.suit
        return False 
    
class Deck:

class Player:

class RummyGame: