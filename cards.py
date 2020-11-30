class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.representation = self.defineRepresentation()

    def defineRepresentation(self):
        if self.number == 1:
            return "A"
        elif self.number == 11:
            return "J"
        elif self.number == 12:
            return "Q"
        elif self.number == 13:
            return "K"
        else:
            return str(self.number)
        return

class Deck:
    def __init__(self):
        self.cards = self.newDeck()

    def removeCard(self, card):
        self.cards.remove(card)
        return

    def pullACard(self):
        import random
        if len(self.cards) == 0:
            return Card("", "", representation = "Teste")
        card = random.choice(self.cards)
        self.removeCard(card)
        return card

    def newDeck(self):
        deck = []
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        for suit in suits:
            for number in range(1, 14):
                newCard = Card(number, suit)
                deck.append(newCard)
        return deck

    def length(self):
        return len(self.cards)

# Para sortear uma única carta / To pick a single card
if __name__ == "__main__":
    deck = Deck()
    while True:
        card = deck.pullACard()
        print(f"Your card is a {card.representation} of {card.suit}")
        confirmation = input(f"Press 'n' to quit or 'Enter' to pull a card again. {deck.length()} cards remaining.")
        if confirmation == "n":
            break
        else:
            continue