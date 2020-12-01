import random

class Deck:
  
  def __init__(self):
    # define instance attributes here
    # deck is a list of all the cards in the deck
    self.deckList = list()
    generate_cards()

  def generate_cards(self):
    # define this method here
    # also, where should this method be called?
    suits = ['Diamonds','Clubs','Hearts','Spades']
    ranks = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    for suit in suits:
        for rank in ranks:
            self.deckList.append(Card(suit,rank,"face down"))
  
  def reset_cards(self):
    # define this method here
    # empty whatever is in the deckList
    self.deckList = list()
    generate_cards()
  
  def shuffle_cards(self):
    # define this method here
    # Create a deck to hold the shuffled cards
    shuffledDeck = list()

    # this list will contain all the numbers already chosen
    numsAlreadyChosen = list()
    for i in range(52):
        # choose a random number in the range 0 to 51
        # this number will be our index of the card from deckList
        # that we will put in the ith index of shuffledDeck
        randomNum = random() % 52
        # while the random number we picked in the previous step was
        # already chosen choose a new randomNum
        while(randomNum in numsAlreadyChosen):
            randomNum = random() % 52
        shuffledDeck[i] = self.deckList[randomNum]
        numsAreadyChosen.append(randomNum)
    # set the shuffeled deck to the deckList
    self.deckList = shuffledDeck

class Card:

  def __init__(self,suit,value, faceO):
    # define instance attributes here
    self.suit = suit
    self.value = value
    self.faceOrientation = faceO
  
  def flip_card(self):
    # define this method here
    if(self.faceOrientation == "face down"):
        self.faceOrientation = "face up"
    else:
        self.faceOrientation = "face down"
