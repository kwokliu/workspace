#!/usr/bin/env python
"""
  Simple Blackjack (a.k.a. 21)

     This is a simple 2 player implementation of Blackjack (also known as 21).
     In this game, the goal is to be the player with score closest to 21
     without going over.

     The victory conditions are:
       -- If you (the Player) go over 21, you lose.
       -- If the other player (the House) goes over 21, you win.
       -- If you get *exactly* 21, you win.
       -- If the House gets *exactly* 21, you lose.
       -- If you both get 21, you win.

     This version of the game does NOT include:
       >X< betting
       >X< insurance
       >X< splitting
       >X< doubling down
       >X< most of the stuff that makes Blackjack attractive as a game

     ========================================================================
     GENERAL GAME FLOW
     ========================================================================

       [1] Deal 2 cards to the House and the Player.  One of these cards is
           delt face up and the other face down.  The face down card is
           called the "hole card" and can only be seen by its owner---only
           the Player can see the Player's hole card, the Player cannot see
           the House's hole card, and the House cannot see the Player's
           hole card.  All other cards in play for the rest of the game are
           delt face up and are referred to as "showing".

       [2] The Player is given the choice to Hit or Stay.  If the Player
           chooses Hit, the dealer will add another card to the Player's
           hand, increasing the number of cards the Player is "showing".
           If the Player takes a hit which results in his hand totaling
           greater than 21, the Player loses and the game is over.  This is
           called a BUST.  The Player can continue to choose Hit as long
           has he does not BUST.  Once the Player is happy with the score
           of their hand, they may choose to end their turn by choosing
           Stay.

       [3] The House now executes its simple AI routine.  Like the Player,
           the House takes hits until it is happy with its score and Stays
           (or accidentally BUSTs).  If the House BUSTs, you automatically
           win.  Here, the House will operate on a simple AI routine that
           does not consider what the Player is currently showing.  The
           House will simply take Hits as long as its score is below 18.

       [4] Once the House stays, both players' hands are scored and the
           player with the higher score is declared the winner.

       [5] The Player is asked if they want to play again.


       *NOTE*
         The Dealer will deal cards to the Player and the House from a
         single Deck of 52 shuffled cards.  Once the last card in the Deck
         has been dealt, the Dealer will open a new standard Deck of 52
         cards, shuffle them, and then continue to deal cards to the Player
         and House.  This can go on forever... but only a single deck of
         shuffled cards is ever used by the Dealer at any given time.


     ========================================================================
     SCORING
     ========================================================================

       Blackjack is played with a standard deck of 52 cards consisting of 4
       suits: Hearts, Clubs, Diamonds, and Spades.  Each suit consists of
       13 cards: the "standard" cards numbered 2 through 10, a Jack, a
       Queen, a King, and an Ace.  In Blackjack, the suit of a card does
       not matter.

       Scoring in Blackjack is simple:

          >> "standard cards" are worth their numerical value
               Example(s): the 7 of spades is worth 7 points
                           the 3 of diamonds is worth 3 points
                           the 10 of clubs is worth 10 points

          >> "face cards" are worth 10 points
               Example(s): the King of diamonds is worth 10 points
                           the Jack of clubs is worth 10 points
                           the Queen of spades is worth 10 points

          >> Aces have a "hard value" of 1 and a "soft value" of 11.  It is
             beneficial to choose the value that gets your score closest to
             21 without going over.  If counting the Ace with a "soft
             value" of 11 would cause a BUST, the Ace is automatically
             worth 1, which prevents the BUST from occurring.
               Example(s): an Ace and a King total 21
                           an Ace, 7, and 2 total 20
                           an Ace, 10, 7, and 2 total 20

          *NOTE*
             Cards that are NOT Aces effectively have soft values that are
             equal to their hard values.


     ========================================================================
     PROJECT OBJECTIVES (a.k.a. "SO WHAT DO I TYPE IN TO GET AN A?")
     ========================================================================

        A significant amount of skeleton code is being provided to you in
        this file---your goal is to fill in the blanks (and add to it) in
        order to arrive at working Blackjack game.  What needs to be done
        can be broken down into a few smaller objectives:


     Objective 1 -- Build a Card Class Hierarchy
     -------------------------------------------
     Cards should be implemented using inheritance.  Polymorphism will be
     exploited to score cards.  Override methods as necessary.  "Standard"
     number cards will be implemented by the Card class.  Your inheritance
     structure should follow the diagram below:

                                +------------+
                     ---------->|  FaceCard  |
       +--------+  /            +------------+
       |  Card  |--
       +--------+  \            +------------+
                     ---------->|    Ace     |
                                +------------+

     The skeleton of the Card class has been provided and consists of the
     following methods:

       Card
        |--- __init__(self, rank, suit)
        |--- getRank(self)
        |--- softValue(self)
        |--- hardValue(self)
        +--- unicode(self)

     FaceCard and Ace classes inheriting from Card will need to override
     some or all of these methods.


     Objective 2 -- Build a Hierarchy of "Card Groupers"
     ---------------------------------------------------
     Hands of Card objects and Decks of Card objects share a lot in common.
     It makes sense to implement this core "Card Groupiness" into a base
     class that will be used to derive more specific things like Hands and
     Decks.  Your inheritance structure should follow the diagram below:

                                           +--------+
                                 +-------->|  Deck  |
       +-------------------+     |         +--------+
       |   CardContainer   |     |
       |                   |     |
       | +---------------+ |-----+
       | | List of Cards | |     |
       | +---------------+ |     |
       +-------------------+     |         +--------+
                                 +-------->|  Hand  |
                                           +--------+

     Notice that the CardContainer class encapsulates a List of Card
     objects (and stuff derived from Card objects).  The skeleton of the
     CardContainer class has been provided and consists of the following
     methods:

       CardContainer
        |--- __init__(self)
        |--- shuffle(self)
        |--- popCard(self)
        |--- pushCard(self, card)
        |--- __iter__(self)
        +--- next(self)

     More sparse skeletons of the derived classes Deck and Hand have also
     been provided. Fill them in according to the specifications provided
     in the docstrings.


     Objective 3 -- Build the Game Flow Control and AI
     -------------------------------------------------
     The game's flow control and (very) simple House AI will be implemented
     as a class called Game.  The Game class encapsulates two Hands (for
     the House and Player) and a Deck.


                +-------------------+
                |       Game        |
                |                   |
                | +---------------+ |
                | | Deck Instance | |  <--- For Dealer
                | +---------------+ |
                |                   |
                | +---------------+ |
                | | Hand Instance | |  <--- For House
                | +---------------+ |
                |                   |
                | +---------------+ |
                | | Hand Instance | |  <--- For Player
                | +---------------+ |
                +-------------------+


     A base skeleton of the Game class has been provided.  You will need to
     implement the provided public and private methods according to the
     provided docstrings to finally produce a working Blackjack game!


     ========================================================================
     DELIVERABLES
     ========================================================================
     The deliverables are simple:

       [1] A working Blackjack game (submit your OWN WORK *only*)
            -- Your program must run on thanos.ece.drexel.edu without
               needing to install additional software, create virtualenvs,
               perform general funkiness of anykind, etc. I don't care if
               it ran on your aunt's friend's brother's computer a week and
               three days ago last Thursday.  If it doesn't (at the very
               least) run on thanos, your project will not be graded.

                  >>>> YOU HAVE OFFICIALLY BEEN INFORMED <<<<


       [2] A report (in PDF format) with the following sections:
            -- Overview
            -- Implementation Details
                * (should be more detailed than these simple instructions)
            -- How to Run and Play
            -- Gameplay Examples
                * (at least 5 playthroughs with step-by-step annotations)
                * (step annotations can be as short as a single sentence)
"""

# Please read the documentation for the random module.  It will make your
# life much easier... don't reinvent code when a method already exists that
# does what you need to do.
import random

# Dictionary of unicode symbols for playing card suits
#suit_lut = {'clubs': u'\u2663',
#            'diamonds': u'\u2666',
#            'hearts': u'\u2665',
#            'spades': u'\u2660'}

suit_lut = {'clubs': 'clubs',
            'diamonds': 'diamonds',
            'hearts': 'hearts',
            'spades': 'spades'}

# List of suits, may be useful
suits = ['clubs', 'diamonds', 'hearts', 'spades']

# List of valid face cards, may be useful
face_cards = ['J', 'Q', 'K']


class Card(object):
    """
    Represents a standard numerical playing card possessing a suit
    (diamonds, clubs, hearts, spades) and a rank (2 through 10).  For
    standard cards such as these, the softValue and hardValue are both
    simply equal to the rank of the card.
    """
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit_lut[suit]

    def getRank(self):
        """Returns the rank of the Card"""
        return self._rank

    def softValue(self):
        """Returns the softValue of the Card"""
        return self._rank

    def hardValue(self):
        """Returns the hardValue of the Card"""
        return self._rank

    def unicode(self):
        """
        Returns a Unicode string containing the Unicode symbol of the
        suit and the card rank
        """
        return "%s %s" % (self._suit, self._rank)


class FaceCard(Card):
    """
    Represents a Face Card (Jack, Queen, King) possessing a suit.
    """
    #######################################################################
    
    def __init__(self, rank, suit):
        super(FaceCard,self).__init__(rank, suit)
        self._rank=rank
        self._suit=suit_lut[suit]

    def getRank(self):
        """Returns the rank of the Card"""
        return self._rank

    def softValue(self):
        """Returns the softValue of the Card"""
        return 10
    def hardValue(self):
        """Returns the hardValue of the Card"""
        return 10

    def unicode(self):
        """
        Returns a Unicode string containing the Unicode symbol of the
        suit and the card rank
        """
        return "%s %s" % (self._suit, self._rank)

    #######################################################################


class AceCard(Card):
    """
    Represents an Ace Card possessing a suit.
    """
    #######################################################################

    def __init__(self, rank, suit):
      super(AceCard,self).__init__(rank, suit)
      self._rank=rank
      self._suit=suit_lut[suit]

    def getRank(self):
        """Returns the rank of the Card"""
        return self._rank

    def softValue(self):
        """Returns the softValue of the Card"""
        return 11
    def hardValue(self):
        """Returns the hardValue of the Card"""
        return 1

    def unicode(self):
        """
        Returns a Unicode string containing the Unicode symbol of the
        suit and the card rank
        """
        return "%s %s" % (self._suit, self._rank)

    #######################################################################


class CardContainer(object):
    """
    A CardContainer serves as a base class that simply describes a
    collection of cards---CardContainer encapsulates a List of Card
    objects. CardContainers can be shuffled, iterated through, have cards
    added to them (i.e. pushed), and can return cards being removed from
    them (i.e. popped).
    """
    def __init__(self):
        self._index = 0
        self._cards = []

    def shuffle(self):
        """
        Shuffles the cards in the CardContainer
        """
        ###################################################################
        
        random.shuffle(self._cards)

        ###################################################################

    def popCard(self):
        """
        Removes a card from the CardContainer and returns it
        """
        ###################################################################

        temp_card=self._cards[-1]
        self._cards.pop()
        return temp_card

        ###################################################################

    def pushCard(self, card):
        """
        Adds a card to the CardContainer
        """
        ###################################################################
        
        self._cards.append(card)

        ###################################################################

    def __iter__(self):
        """
        Called when an iterator is requested for this object
        """
        self._index = 0
        return self

    def next(self):
        """
        Called when the next() method is called on an iterator of this
        object
        """
        try:
            ret = self._cards[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration
        else:
            return ret


class Deck(CardContainer):
    """
    A Deck represents the dealer's deck of cards, which is used to create
    Hands (collections of cards belonging to individual players).  A deck
    object inherits from CardContainer.  The only public interface method
    offered by Deck objects is dealCard()
    """
    def __init__(self):
        ###################################################################

        super(Deck,self).__init__()
        self._loadDeck()

        ###################################################################

    def _loadDeck(self):
        """
        Generates 52 cards and pushes them onto the Deck. For each of the 4
        suits, 2-10, J, Q, K, A are generated and pushed onto the Deck.
        """
        ###################################################################

        for suit in suits:
            self.pushCard(AceCard('A',suit))
            for fc in face_cards:
                self.pushCard(FaceCard(fc,suit))
            for rank in range(2,11):
                self.pushCard(Card(rank,suit))                        

        ###################################################################

    def dealCard(self):
        """
        Removes a Card object from the Deck object *AND* returns it so that
        it may enter play, be added to another player's deck, etc.  If the
        deck is empty, dealCard() should reload the Deck with a shuffled
        standard 52 card assortment of playing cards.
        """
        ###################################################################

        if self._cards==[]:
            self.shuffle()
            self._loadDeck()
        return self.popCard()

        ###################################################################


class Hand(CardContainer):
    """
    A Hand represents a Blackjack player's current hand of cards.  A Hand
    object inherits from CardContainer.
    """
    def __init__(self):
        ###################################################################
        
        super(Hand,self).__init__()
        self._hole=[]

        ###################################################################

    def getHoleCard(self):
        """
        Returns the hole card (but does not remove it from the Hand)
        """
        ###################################################################
        
        return self._hole[0]

        ###################################################################

    def clear(self):
        """
        Removes all cards from the Hand in preperation for another round
        """
        ###################################################################
        
        self._cards=[]
        self._hole=[]

        ###################################################################

    def getCard(self, card):
        """
        Adds a Card object to the Hand.  If the Hand empty, the card should
        go into the hole; otherwise, the card should be showing.
        """
        ###################################################################
        
        if len(self._hole)==0:
            self._hole.append(card)
        else:
            self.pushCard(card)

        ###################################################################

    def getSoftScore(self):
        """
        Iterates through the Cards in the Hand and returns the soft score
        """
        ###################################################################
        
        get_soft_score=self._hole[0].softValue()
        for card in self._cards:
            get_soft_score=card.softValue()+get_soft_score
        return get_soft_score

        ###################################################################

    def getHardScore(self):
        """
        Iterates through the Cards in the Hand and returns the hard score
        """
        ###################################################################
        
        get_hard_score=self._hole[0].hardValue()
        for card in self._cards:
            get_hard_score=card.hardValue()+get_hard_score
        return get_hard_score

        ###################################################################


class Game(object):
    """
    Represents a two player game of Blackjack.  Consists of a Deck, the
    player's Hand, and the house's Hand.  The only public interface method
    in the class is playHand(), which plays out a hand (i.e. round) of
    Blackjack.
    """
    def __init__(self):
        self._deck = Deck()
        self._player = Hand()
        self._house = Hand()
        self._deck.shuffle()

    def _printPlayer(self):
        """
        Prints state of the Player's hand to the screen.  Displays the hard
        and soft scores for the current state of the Hand, displays the hole
        card, and displays all cards showing.
        """
        print 'Player: [%i, %i]' % (self._player.getHardScore(), self._player.getSoftScore())
        print '     Hole: %s' % self._player.getHoleCard().unicode()
        print '  Showing:',
        for card in self._player:
            print '%s,' % card.unicode(),
        print ''

    def _printHouse(self):
        """
        Prints state of the House's hand to the screen.  Only displays the
        cards showing (i.e. does not display the House's hole card).
        """
        print 'House:'
        print '  Showing:',
        for card in self._house:
            print '%s,' % card.unicode(),
        print ''

    def _dealCardsToPlayer(self, number):
        """
        Gets *number* cards from the Deck and adds them to
        the Player's Hand.
        """
        for _ in xrange(number):
            card = self._deck.dealCard()
            self._player.getCard(card)

    def _dealCardsToHouse(self, number):
        """
        Gets *number* cards from the Deck and adds them to
        the House's Hand.
        """
        ###################################################################
        
        for _ in xrange(number):
            card = self._deck.dealCard()
            self._house.getCard(card)

        ###################################################################

    def _checkHouseBust(self):
        """
        Returns True if the Player has bust (i.e. Hard Score > 21),
        otherwise returns False.
        """
        ###################################################################
        
        if self._house.getHardScore()>21:
            return True
        else:
            return False

        ###################################################################

    def _checkPlayerBust(self):
        """
        Returns True if the Player has bust (i.e. Hard Score > 21),
        otherwise returns False.
        """
        ###################################################################
        
        if self._player.getHardScore()>21:
            return True
        else:
            return False

        ###################################################################

    def _doHouseAi(self):
        """
        Implements the House's strategy.  The House should take hits as
        long as its score is under 18.  If the House has 21, it should stop
        immediately.
        """
        ###################################################################
        
        houseAI=0
        if self._house.getSoftScore()==21:
            houseAI=1
        while houseAI==0 and self._house.getHardScore()<18:
            self._dealCardsToHouse(1)


        ###################################################################

    def _checkWhoWins(self):
        """
        Compute the scores for the House and Player and announce the winner
        """
        ###################################################################

        if self._checkPlayerBust():
          print("HOUSE WIN!")
          print 'House Hole: %s' % self._house.getHoleCard().unicode()

        elif self._checkHouseBust():
          print("PLAYER WIN!")
          print 'House Hole: %s' % self._house.getHoleCard().unicode()

        elif self._player.getSoftScore()==21 or self._player.getHardScore()==21:
          print("PLAYER WIN!")
          print 'House Hole: %s' % self._house.getHoleCard().unicode()

        elif self._house.getSoftScore()==21 or self._house.getHardScore()==21:
          print("HOUSE WIN!")
          print 'House Hole: %s' % self._house.getHoleCard().unicode()

        elif self._player.getSoftScore()==21 or self._player.getHardScore()==21 and self._house.getSoftScore()==21 or self._house.getHardScore()==21:
          print("PLAYER WIN!")
          print 'House Hole: %s' % self._house.getHoleCard().unicode()

        elif self._player.getHardScore()<21 and self._player.getSoftScore()>self._house.getSoftScore():
          print("PLAYER WIN!")
          print 'House Hole: %s' % self._house.getHoleCard().unicode()

        elif self._player.getHardScore()<21 and self._player.getSoftScore()<self._house.getSoftScore():
          print("HOUSE WIN!")
          print 'House Hole: %s' % self._house.getHoleCard().unicode()
        

        ###################################################################

    def _promptChoices(self, prompt, choices):
        """
        Utility method for prompting the user for input.

        Example:
           action = self._promptChoices("Action: [h]it, [s]tay, [q]uit: ', ['h', 's', 'q'])

        will print to the screen:

           Action: [h]it, [s]tay, [q]uit:

        and will return the user's input into the variable 'action'.  If
        the user does not enter a valid choice, the prompt will be
        displayed again:

           Action: [h]it, [s]tay, [q]uit: z
           Invalid Selection. Try Again

           Action: [h]it, [s]tay, [q]uit:

        """
        valid_choice = False
        while True:
            action = str(raw_input('\n'+prompt))
            if action in choices:
                return action
            else:
                print 'Invalid Selection. Try Again'

    def _startNewHand(self):
        """
        Clears the Player and House's Hands and deals 2 new cards to each.
        """
        self._player.clear()
        self._dealCardsToPlayer(2)

        self._house.clear()
        self._dealCardsToHouse(2)

    def playHand(self):
        """
        Plays a new hand.  The general procedure follows:
          [1] Starts a new hand
          [2] Ask the user to hit or stay until they choose to stay
          [3] Execute the House AI
          [4] Figure out who won and display the winner
          [5] Ask the player if they want to play another hand

        Naturally, events such as a BUST (i.e. taking a hit and going over
        21) will prematurely end the hand.
        """
        
        self._startNewHand();

        ###################################################################
        
        self._printPlayer();
        self._printHouse();
        
        gaming=True;

        while gaming:
            action = self._promptChoices("Action: [h]it, [s]tay, [q]uit: ", ['h', 's', 'q']);
            if action=='h':
                self._dealCardsToPlayer(1);
                self._printPlayer();
                if self._checkPlayerBust():
                    self._checkWhoWins();
                    gaming=False;
                self._printHouse();
            if action=='s':
                self._doHouseAi();
                self._printPlayer();
                self._checkWhoWins();
                gaming=False;
                self._printHouse();
            if action=='q':
                gaming=False;
                self._printHouse();



        ###################################################################



        choice = self._promptChoices('Play Again? [y]es, [n]o: ', ['y', 'n'])
        if choice is 'y':
            return True
        elif choice is 'n':
            return False


def main():
    G = Game()

    while G.playHand():
        pass

    print '\nBye Bye!\n'


if __name__ == '__main__':
    main()
