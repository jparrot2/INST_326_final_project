'''Plays the card game rummy'''
import random
from argparse import ArgumentParser
import sys 

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
        """Initializes a card deck that combines ranks and suits. Makes a list of Card objects 
        with ranks and suits. 
        
        Attributes: 
        cards (list): A shuffled and randomized list of Card objects for the deck. 
        
        Side Effects: 
        Shuffles the cards attribute
        
        """ 
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.cards.shuffle()
        
    def deal(self, num_cards):
        dealt_cards = [self.cards.pop() for _ in range(num_cards) if self.cards]

        return dealt_cards 
    
    def draw(self):
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
    def is_run(cards):
        if len(cards) < 3:
            return False
        first_suit = cards[0].suit
        for card in cards:
            if card.suit != first_suit:
                return False
        cards.sort(key=lambda x: ranks.index(x.rank)) 
        for i in range(len(cards) - 1):
            if ranks.index(cards[i + 1].rank) != ranks.index(cards[i].rank) + 1:
                return False 
        return True
    def is_set(cards):
        if len(cards) < 3 or len(cards) > 4:
            return False
        first_rank = cards[0].rank
        for card in cards:
            if card.rank != first_rank:
                return False
        suits=[]
        for card in cards:
            return False if card.suit in suits else suits.append(card.suit)
        return True   
    
    def declare_win(self):
        suit_groups = {}
        rank_groups = {}

        for card in self.hand:
            suit_groups.setdefault(card.suit, []).append(card)
            rank_groups.setdefault(card.rank, []).append(card)

        for cards in suit_groups.values():
            if len(cards) >= 3:
                ranks_in_suit = [ranks.index(card.rank) for card in cards]
                ranks_in_suit.sort(key=lambda x: x)  

                for i in range(1, len(ranks_in_suit)):
                    if ranks_in_suit[i] != ranks_in_suit[i - 1] + 1:
                        return False  

        for cards in rank_groups.values():
            if len(cards) >= 3:
                suits_in_set = {card.suit for card in cards}
                if len(suits_in_set) != len(cards):
                    return False  

        all_suits_in_hand = set()  
        for cards in rank_groups.values():
            all_suits_in_hand |= {card.suit for card in cards}  # Union using the | operator
        
        print(f"Union of all suits in hand: {all_suits_in_hand}")

        print(f"{self.name} wins with {len(self.hand)} cards!")

        return True

class RummyGame:
    def __init__(self, player1_name, player2_name):
        """Initializes a RummyGame object with two players.
        Args:
            player1_name (str): The name of the first player.
            player2_name (str): The name of the second player. """
            
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()
        self.deck.shuffle()
    
    def deal_cards(self):
        """Deals 7 cards to each player 1 and player 2.
        """
        for _ in range(7):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)

    def take_turns(self, player): 
        print(f"It's {player.name}'s turn!")
        drawn_card = self.deck.draw()
        if drawn_card:
            print(f"{player.name} drew {drawn_card}")
            player.hand.append(drawn_card)
        else: 
            print("So sorry! The deck is empty, no cards to draw.")
        
    def display_game_state(self, player):
        print(f"Your hand: {[str(card) for card in player.hand]}")
        if self.discard_pile:
            print(f"Top of discard pile: {self.discard_pile[-1]}")
        else:
            print("The discard pile is empty.")

    def handle_discard(self, player):
        while True:
            print(f"Your hand: {[str(card) for card in player.hand]}")
            discard_index = input("Choose a card to discard (index): ")
            if discard_index.isdigit():
                discard_index = int(discard_index)
                if 0 <= discard_index < len(player.hand):
                    discarded_card = player.hand.pop(discard_index)
                    self.discard_pile.append(discarded_card)
                    print(f"You discarded: {discarded_card}")
                    break
            print("Invalid index. Please try again.")
            

def parse_args(arglist): 
    """Parses the command line arguments for the game.
    
    Args:
        arglist (list of str): List of command-line arguments to parse.

    Returns:
        Namespace: Parsed arguments of the game as attributes.
    """
    parser = ArgumentParser(description="Play the card game Rummy.")
    parser.add_argument("--player1", type=str, default="Player 1", help="Name of the first player (default: Player 1)")
    parser.add_argument("--player2", type=str, default="Player 2", help="Name of the second player (default: Player 2)")
    parser.add_argument("--shuffle", action="store_true", help="Shuffle the deck before starting the game.")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    
    game = RummyGame(args.player1, args.player2)
    if args.shuffle:
        game.deck.shuffle()
    
    print(f"Welcome to Rummy! {args.player1} vs {args.player2}")
    game.deal_cards()
