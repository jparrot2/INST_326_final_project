'''Plays the card game rummy'''
import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']


class Card: 
    '''Represents a card with a rank and suit
    
    Attributes: 
        rank (str): rank of the card (2, 3, 4, ... 10, Jack, ... Ace)
        suit (str): suit of the card (hearts, diamonds, spades, clubs)'''
    
    def __init__(self, rank, suit):
        '''Initializes a Card instance with a given rank and suit
        
        Args: 
            rank(str): rank of the card (see attributes in Card class)
            suit (str): suit of the card (see attributes in Card class)'''
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        '''String representation of a card
        
        Returns: 
            (str) string in the format 'rank of suit' '''
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        '''Checks if two cards are equal by comparing rank and suit
        Returns: 
            (bool) True if the cards match exactly, False otherwise '''
        if isinstance (other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False 
    
class Deck:
    def __init__(self): 
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.cards.shuffle()
        
     def deal(self, num_cards):
        """Deal cards from the deck and sorted by rank."""
        self.cards = sorted(self.cards, key=lambda card: (card.rank, card.suit))
        dealt_cards = [self.cards.pop() for _ in range(num_cards) if self.cards]
        return dealt_cards
    
    def draw(self):
    """Draws a single card from the deck."""
    return self.cards.pop() if self.cards else None
        
class Player:
    """A class representing a player in the game.
    
    Attributes:
        hand (list): The cards the player currently holds.
    """
    def __init__(self):
        """Initializes a new player with an empty hand of cards.
        
        Side effects: 
            Sets the hand attribute equal to an empty list.
        """
        self.hand = []
    
    def draw_card(self, deck):
        """Allows the player to draw a card from the deck.

        Args:
            deck (Deck): The deck to draw from.
        """
        self.hand.append(deck.draw())
    
    def discard_card(self, card, discard_pile):
        """Discards a specified card from the player's hand to the discard pile.

        Args:
            card (Card): The card to discard.
            discard_pile (list): The discard pile where the card is placed.
        """
        if card in self.hand:
            self.hand.remove(card)
            discard_pile.append(card)
    def sort_hand(self):
        """Sorts the player's hand by rank and suit for easier viewing.

        The cards are sorted first by rank and then by suit.
        """
        self.hand.sort(key=lambda x: (ranks.index(x.rank), suits.index(x.suit)))
       
class RummyGame: