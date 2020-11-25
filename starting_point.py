class Deck:
  
  def __init__(self, type_of_deck):
    number_of_cards = 52
    # define instance attributes here
    self.type_of_deck = type_of_deck    

  def generate_cards(self):
    # define this method here
    # also, where should this method be called?
  
  def reset_cards(self):
    # define this method here
  
  def shuffle_cards(self):
    # define this method here


class Card:

  def __init__(self, suit, value, orientation):
    # define instance attributes here
    self.suit = suit
    self.value = value
    self.orientation = orientation #orientation means facing up or down
  
  def flip_card(self):
    # define this method here
    
  
