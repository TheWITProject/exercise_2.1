class Card:
    def __init__(self, rank, suit):  # returns a formatted string of suit and rank
        self.suit = suit
        self.rank = rank
    def generate_cards(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.__deck = [] # starts with empty deck
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace"] #ranks
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]  #suits
        for suit in suits: #loops over suit list
            for rank in ranks: #loops over rank list
                self.__deck.append(Card(rank, suit)) #adds the combination to the empty deck

    def shuffle(self):
        import random
        random.shuffle(self.__deck)

    #Removes the card from the top and returns it
    def dealCard(self):
        return self.__deck.pop()

    def count(self):
        return len(self.__deck)

def main():
    deck = Deck() # new deck
    deck.shuffle()
    num=int(input("Enter the number of cards to deal: "))
    print("\nHere are your cards:")
  
    for i in range(num):
        card = deck.dealCard()
        print(card.generate_cards())

    print("\nThere are "+str(deck.count())+" cards left in the deck.")

if __name__ == "__main__":
    main()
