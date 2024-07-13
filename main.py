import random

class Card:
	def __init__(self, name, type, cost, value, vp):
		self.name = name
		self.type = type
		self.cost = cost
		self.value = value
		self.vp = vp
		
	def __repr__(self):
		return f"{self.name}"
		
class Pile:
	def __init__(self, name, size):
		self.name = name
		self.size = size
	
	def __repr__(self):
		return f"{self.name}"

copper = Card("Copper", "Treasure", 0, 1, 0)
copperPile = Pile("Coppers", 40)
silver = Card("Silver", "Treasure", 3, 2, 0)
gold = Card("Gold", "Treasure", 6, 3, 0)
		
estate = Card("Estate", "Victory", 2, 1, 0)
estatePile = Pile("Estates", 8)
duchy = Card("Duchy", "Victory", 5, 3, 0)
province = Card("Province", "Victory", 8, 6, 0)

smithy = Card("Smithy", "Action", 4, 0, 0)

deck = [copper, copper, copper, copper, copper, copper, copper, estate, estate, estate, smithy]
hand = []
inPlay = []
discard = []
trash = []

def shuffle(): #reorder all cards in deck
	tempDeck = []
	for i in range(len(deck)):
		n = random.randint(0, len(deck) - 1)
		tempDeck.append(deck.pop(n))
	return tempDeck

def drawHand(): #draw a hand of 5 cards
	for i in range(5):
		hand.append(deck.pop())

def actionPhase():
	if any(x.type == "Action" for x in hand):
		choice = input("Choose an action.")
	match 


print(deck)
deck = shuffle()
drawHand()
print(hand)
actionPhase()

