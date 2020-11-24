import random

class Deck:
    def __init__(self,cards,generate_cards):
        self.cards = []
        self.generate_cards()

    def generate_cards(self):
        for s in ["Spades", "Diamonds", "Hearts", "Clubs"]:
            for v in range(1,14):
                self.cards.append(Card(s, v))
                
    def flip(self):
        for c in self.cards:
            c.flip()

    def shuffle_cards(self):
        for i in range(len(self.cards)):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def flip_card(self):
        print(f"{self.rank} of {self.suit}")

