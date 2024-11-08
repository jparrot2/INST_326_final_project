'''Plays the card game rummy'''

class Card: 
    '''represents a card with a rank and suit
    Attributes: 
        rank (str): rank of the card (2, 3, 4, ... 10, Jack, ... Ace)
        suit (str): suit of the card (hearts, diamonds, spades, clubs)'''
    def __init__(self, rank, suit):
        '''initializes a Card instance with a given rank and suit
        Args: 
            rank(str): rank of the card (see attributes in Card class)
            suit (str): suit of the card (see attributes in Card class)'''
        self.rank = rank
        self.suit = suit
    def __str__(self):
        '''string representation of a card
        Returns: 
            (str) string in the format 'rank of suit' '''
        return f"{self.rank} of {self.suit}"
    def __eq__(self, other):
        '''checks if two cards are equal by comparing rank and suit
        Returns: 
            (bool) True if the cards match exactly, False otherwise '''
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
            if self.cards:
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