from random import shuffle 
from operator import itemgetter, attrgetter

class Deck:
  
  def __init__(self):
    self.cards = [] 
    self.generate_cards()
    self.reset_cards()
    self.shuffle_cards()

  def generate_cards(self):
    print("generate_cards")
    for suit in ["Clubs", "Diamonds", "Heart", "Spades"]:  
        for rank in range (1, 14):                         
            card = str(rank) + " " + "of" + " " + suit 
            self.cards.append(card)
    print(*self.cards, sep = "\n")
  
  def reset_cards(self):
    print("reset cards")
    sorted(self.cards, key=itemgetter(0))
    print(self.cards)
  
  def shuffle_cards(self):
    print("shuffle cards")
    shuffle(self.cards)   
    print(*self.cards, sep = "\n")
    
deck = Deck() 
deck.reset_cards()
deck.shuffle_cards()

class Card:

  def __init__(self):
    self.suit = suit
    self.value = value
    self.is_face_up = is_face_up 
    self.flip_card()
    
  def face_up(self):
    if self.is_face_up == True:          
      return "Is faced up"
    else:
      return "Is faced down"

  def flip_card(self):   
    if self.face_up() == "Is faced down":
      return "Face up"
    elif self.face_up() == "Is faced up":
      return "Face down"

card1.face_up()
print(card1.flip_card())
   
  
