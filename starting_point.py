class Deck:
  
  def __init__(self,number_cards):
    # define instance attributes here
    self.decks = list();
    self.number_cards = 52
    
    
  def generate_cards(self):
    # define this method here
    suits = ['Hearts','Spades','Clubs','Diamonds']
    num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # also, where should this method be called?
  
  def reset_cards(self):
    # define this method here
    self.decks = list();
  
  def shuffle_cards(self):
    # define this method here
    shuffle_cards = list();


class Card:

  def __init__(self):
    # define instance attributes here
    self.suits = suits
    self.value = value 
    self.face = face
  
  def flip_card(self):
    # define this method here
  
