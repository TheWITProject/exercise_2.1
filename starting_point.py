class Card:
    def __init__(self, rank, suit):  # this method returns a formatted string of rank and suit
        self.suit = suit
        self.rank = rank
    def generate_cards(self):
        return self.suit+" of "+self.rank

class Deck:
    def __init__(self):
        self.__deck = [] # intilize an empty deck
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace"] #list of ranks
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]  # list of suits
        for suit in suits: # loops over the 2 lists to get each permutation
            for rank in ranks: # appends the curretn combination to the deck list
                self.__deck.append(Card(rank, suit))

    # this radnomizes the deck list
    def shuffle(self):
        import random
        random.shuffle(self.__deck)

    # this removes the card from the top and returns it
    def dealCard(self):
        return self.__deck.pop()

    def count(self):
        return len(self.__deck)

def main(): #main for input 
    deck = Deck() # new deck
    deck.shuffle()
    num = int(input("Enter the number of cards to deal: "))
    print("\nHere are your cards:")
  
    for i in range(num):
        card = deck.dealCard()
        print(card.generate_cards())

    print("\nThere are "+str(deck.count())+" cards left in the deck.")

if __name__ == "__main__":
    main()

