'''Plays the card game rummy'''
import random
from argparse import ArgumentParser
import sys 

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', 'Jokers']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

class Card: 
    '''
    Represents a card with a rank and suit
    Attributes: 
        rank (str): rank of the card (2, 3, 4, ... 10, Jack, ... Ace)
        suit (str): suit of the card (hearts, diamonds, spades, clubs)
        
    Author: Anna Carpenter
    '''
    def __init__(self, rank, suit):
        '''
        Initializes a Card instance with a given rank and suit
        
        Args: 
            rank(str): rank of the card (see attributes in Card class)
            suit (str): suit of the card (see attributes in Card class)
        
        Side effects:
            creates an object that can be modified within the program 
        
        Author: Anna Carpenter
            '''
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        '''
        String representation of a card
        
        Returns: 
            (str) string in the format 'rank of suit' 
        
        Techniques: 
            Magic method. Creates a string representation of the card.
        
        Author: Anna Carpenter
            '''
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        '''
        Checks if two cards are equal by comparing rank and suit
        
        Returns: 
            (bool) True if the cards match exactly, False otherwise
            
        Author: Anna Carpenter
            '''
        if isinstance (other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False 
    
class Deck:
    """
    Deals with combining suits and ranks, shuffling cards, dealing the cards, and drawing them."
    """
    def __init__(self):
        """
        Initializes a card deck that combines ranks and suits. Makes a list of Card objects 
        with ranks and suits. 
        
        Attributes: 
        cards (list): A shuffled and randomized list of Card objects for the deck. 
        
        Side Effects: 
        Shuffles the cards attribute
        
        Author: 
        Jayla Parrott 
        """ 
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.shuffle()
    
    def shuffle(self):
        """
        Shuffles the card object using the shuffle method from the random module. 
        
        Side Effects: 
        Alters the arrangement of the card object. 
        
        Author: 
        Jayla Parrott 
        """
        random.shuffle(self.cards)
        
    def deal(self, num_cards):
        """
        Deals a specified number of cards from the deck. 

        This method removes the top cards from the deck and returns them in list form. If there are fewer than 'num_cards' remaining in the deck, it will just deal as many cards as available. 

        Args:
            list: a list of cards that were dealt from the deck. 

        Author: Samvitti Nag
        """
        dealt_cards = [self.cards.pop() for _ in range(num_cards) if self.cards]
        return dealt_cards 
    
    def draw(self):
        """
        Draws a single card from the deck.

        This method removes and returns the last card from the deck. If the deck is empty, it returns none. 

        Returns:
            Card or None: The last card in the deck or None if the deck is empty.

        Author: Samvitti Nag
        """
        return self.cards.pop() if self.cards else None
      
class Player:
    """
    A class representing a player in the game.
    
    Attributes:
        hand (list): The cards the player currently holds.
        name (str): name of the player.
    """
    def __init__(self, name):
        """
        Initializes a new player with an empty hand of cards.
        
        Side effects: 
            Sets the hand attribute equal to an empty list.
        
        Author: Alex Britton
        """
        self.hand = []
        self.name = name
    
    def draw_card(self, deck):
        """
        Allows the player to draw a card from the deck.

        Args:
            deck (Deck): The deck to draw from.
        
        Side effects:
            Appends a card to the hand list from the deck.
        
        Author: Alex Britton
        """
        self.hand.append(deck.draw())
    
    def discard_card(self, card, discard_pile):
        """
        Discards a specified card from the player's hand to the discard pile.

        Args:
            card (Card): The card to discard.
            discard_pile (list): The discard pile where the card is placed.
        
        Side effects: 
            adds the card removed to the discard pile 
            
        Author: Anna Carpenter
        """
        if card in self.hand:
            self.hand.remove(card)
            discard_pile.append(card)
            
    def sort_hand(self):
        """
        Sorts the player's hand by rank and suit for easier viewing.
        
        Side effects:
            Sorts players hand by the rank and suit.
        
        Author: Alex Britton
        """
        self.hand.sort(key=lambda x: (ranks.index(x.rank), suits.index(x.suit)))
        
    def is_run(self, cards):
        """
        Checks if a given list of cards forms a valid run in a particular suit.

        A "run" is defined as a sequence of cards with consecutive ranks all belonging to the same suit. 
        This method will check that the list qualifies as a run if it contains at least three cards, has all cards in the same suit, and has ranks that are consecutive in order.

        Args: 
            card (list): A list of 'Card' objects where each card has a rank and suit attribute. 

        Returns: 
            bool: True if the cards form a valid run and False otherwise

        Author: Samvitti Nag

        """
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
    
    def is_set(self, cards, allow_jokers= False):
        '''
        Determines if there is a valid set within the players hand
        
        A valid set is
        - 3 or 4 cards
        - if jokers are not allowed, all cards must have the same rank
        - if jokers are allowed, cards must consist of either:
            - cards having the same rank
            - some cards having the same rank and others being jokers
        - no two cards can have the same suit
        
        Args:
            cards (list): list of card objects to check 
            allow_jokers (bool): flag to indicate whether jokers are allowed 
            in the set
            
        Returns:
            bool: True if the cards are a valid set, otherwise False
            
        Techniques: 
            optional parameters: The player can choose to use jokers or they
            can choose to play as normal. 
        
        Author: Anna Carpenter    
        '''
        if len(cards) < 3 or len(cards) > 4:
            return False
        first_rank = cards[0].rank
        if not allow_jokers:
            for card in cards:
                if card.rank != first_rank:
                    return False
        else: 
            jokers = []
            non_jokers= []
            for card in cards:
                if card.rank == "Joker":
                    jokers.append(card)
                else:
                    non_jokers.append(card)
            if len(non_jokers)> 0 and non_jokers[0].rank != first_rank:
                return False
            if len(jokers) + len(non_jokers) != len(cards): 
                return False
        suits = set()
        for card in cards:
            if card.suit in suits:
                return False
            suits.add(card.suit)
        return True
    
    def declare_win(self):
        """
        Determines whether the current player has won the game based on their hand of cards.

        A player wins if they have either:
        - a run of at lest three cards of the same suit 
        - a set of at least three cards of the same rank

        The method checks the player's hand, categorizing the cards by suit and rank, then verifies if any suit group forms a valid run or any rank group forms a valid set.

        Returns: 
            bool: True if the player has a valid winning hand, False otherwise. 
        
        Author: Samvitti Nag
        """
        suit_groups = {}
        rank_groups = {}
        for card in self.hand:
            suit_groups.setdefault(card.suit, []).append(card)
            rank_groups.setdefault(card.rank, []).append(card)
        for cards in suit_groups.values():
            if len(cards) >= 3 and self.is_run(cards):
                return True
        for cards in rank_groups.values():
            if len(cards) >= 3 and self.is_set(cards):
                return True
        return False

class RummyGame:
    """
    Handles and carries out the functionality of the game. 
    """
    def __init__(self, player1_name, player2_name):
        """
        Initializes a RummyGame object with two players, a shuffled deck of cards, and a game state.
        
        Args:
        player1_name (str): The name of the first player for the game.
        player2_name (str): The name of the second player for the game.
            
        Attributes: 
        player1 (Player): The first player with the name provided at the command line. 
        player2 (Player): The second player with the name provided at the command line.
        players (list): A list that contains the names of players 1 and 2. 
        discard_pile (list): A list that shows the pile of discarded cards in the game. 
        turn (int): A tracker that keeps track of each player's turn. Initialized at 0. 
        
        Author: 
        Jayla Parrott 
        
        Techniques: 
        Composition. The RummyGame class is using instances of the Player and Deck 
        class to provide functionality.   
        """
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.players = [self.player1, self.player2]
        self.deck = Deck()
        self.discard_pile = []
        self.turn = 0

    def deal_cards(self):
        """
        Ensures that both players draw 7 cards from the deck, one card a time. 
        
        Side Effects: 
        Calls the draw_card method on players 1 and 2 and also reduces the number of cards in the deck.
        
        Author: 
        Jayla Parrott 
        """
        for _ in range(7):
            self.player1.draw_card(self.deck)
            self.player2.draw_card(self.deck)
            
    def display_game_state(self, player):
        """
        Displays the current state of the game for players to decide their move.
        
        Args:
            player (player class instance): the player that needs their gamestate displayed.
            
        Side effects:
            Prints the players cards in their hand and 
            the card on top of the discard pile.
        
        Author: Alex Britton
        """
        print(f"Your hand: {[str(card) for card in player.hand]}")
        if self.discard_pile:
            print(f"Top of discard pile: {self.discard_pile[-1]}")
        else:
            print("The discard pile is empty.")
    
    def handle_draw(self, player):
        """
        Allows the player to draw a card from the deck or discard pile.
        
        The player can select one of two options
            1. Deck
            2. Discard pile
            
        Args: 
            player (Player): player object that will draw a card 
        
        Side effects:
            draws a card from whichever deck the player specifies 
            and adds it to that players hand. prints an invalid choice statement
            if the player chooses an invalid choice
            
        Author: Anna Carpenter
        """
        print("Do you want to draw from the deck or the discard pile?")
        print("1. Deck")
        print("2. Discard pile")
        while True:
            choice = input("Enter 1 or 2: ")
            if choice == "1":
                player.draw_card(self.deck)
                break
            elif choice == "2" and self.discard_pile:
                player.hand.append(self.discard_pile.pop())
                break
            else:
                print("Invalid choice. Please try again.")
    
    def handle_discard(self, player):
        """
        Handles how the player discards their card of choice.
        
        Args:
            player (player class instance): the player that is up and needs to discard.
        
        Raises:
            A ValueError if the input is invalid.
        
        Side effects:
            Prints the players hand to decide what they need to discard. 
            Also prints the card the player discarded.
        
        Author: Alex Britton
        """
        while True:
            print(f"Your hand: {[str(card) for card in player.hand]}")
            try:
                discard_index = int(input(f"{player.name}, choose a card to discard (0-{len(player.hand) - 1}): "))
                if 0 <= discard_index < len(player.hand):
                    discarded_card = player.hand.pop(discard_index)
                    self.discard_pile.append(discarded_card)
                    print(f"You discarded: {discarded_card}")
                    break
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                    
    def take_turns(self, player): 
        """
        Carries out a turn for either player 1 or 2, managing their drawing and discarding of cards. 
        The current game state for the player is shown, then the player is promped to draw a crad from the deck 
        or discard pile. Then the player is allowed to discard a card. 
        
        Args: 
        player (Player): The player whose turn it is. 
        
        Returns: 
        bool: True condition if the player meets the criteria for a win and False if they do not.
        
        Side Effects: 
        Modifies the player's hand by adding a card from the deck or discard pile 
        Removes a card from the player's hand and adds it to the discard pile. 
        Updates the game state
        
        Author: 
        Jayla Parrott 
        """
        print(f"It's {player.name}'s turn!")
        self.display_game_state(player)
        self.handle_draw(player)
        self.handle_discard(player)
        return self.check_win_condition(player)
    
    def check_win_condition(self, player):
        """
        Checks if the player has won by calling declare_win.
        
        Args:
            player (player class instance): the player to be checked.

        Returns:
            A player declare win object which 
            determines if the player won or not.
        
        Author: Alex Britton
        """
        return player.declare_win() 
          
    def play_game(self):
        '''
        starts and manages gameplay, the players take turns until one of them wins 
        
        Steps of the game:
        1. deals cards to all the players
        2. each player takes a turn
        3. after the player's turn, check if they have won the game
        4. if a player wins, the game ends
        5. if no player has won, the next player takes their turn
        
        Side effect:
            modifies the state of the game, updating the turn and checking for a winner, prints the winner
            of the game
            
        Author: Anna Carpenter
        '''
        self.deal_cards()
        game_over = False
        while not game_over:
            current_player = self.players[self.turn]
            if self.take_turns(current_player):
                print(f"\n{current_player.name} wins the game!")
                game_over = True
            else:
                self.turn = (self.turn + 1) % len(self.players)

def parse_args(arglist): 
    """
    Parses the command line arguments for the game.
    
    Args:
    arglist (list of str): List of command-line arguments to parse.

    Returns:
     Namespace: Parsed arguments of the game as attributes.
        
    Author: 
    Jayla Parrott 
    
    Techniques: 
    Using the ArgumentParser class from the argparse module. 
    """
    parser = ArgumentParser(description="Play the card game Rummy.")
    parser.add_argument("-player1", type=str, default="Player 1", help="Name of the first player (default: Player 1)")
    parser.add_argument("-player2", type=str, default="Player 2", help="Name of the second player (default: Player 2)")
    parser.add_argument("-shuffle", action="store_true", help="Shuffle the deck before starting the game.")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    
    game = RummyGame(args.player1, args.player2)
    if args.shuffle:
        game.deck.shuffle()
    
    print(f"Welcome to Rummy! {args.player1} vs {args.player2}")
    game.play_game()