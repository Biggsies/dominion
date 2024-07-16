#pylint:disable=E1121
import random

class Card: 
#class for all cards in game
	def __init__(self, name, type, cost, value, vp):
		self.name = name
		self.type = type #may fall apart with multi type cards
		self.cost = cost
		self.value = value
		self.vp = vp
		
	def __repr__(self):
		return f"{self.name}"
		
	def __eq__(self, other):
		if isinstance(other, Card):
			return self.name == other
		return False
		
class Player: 
#class for values associated with the player
	def __init__(self):
		self.actions = 1
		self.buys = 1
		self.vp = 0
		self.money = 0

def fill(amount, card): 
#used to create a pile (array) with amount number of card
	pile = []
	for i in range(amount):
		pile.append(card)
	return pile

player = Player()

#initialise all implemented cards and piles for each card
copper = Card("Copper", "Treasure", 0, 1, 0)
copperPile = fill(40, copper)
silver = Card("Silver", "Treasure", 3, 2, 0)
silverPile = fill(30, silver)
gold = Card("Gold", "Treasure", 6, 3, 0)
goldPile = fill(20, gold)
		
estate = Card("Estate", "Victory", 2, 1, 0)
estatePile = fill(8, estate)
duchy = Card("Duchy", "Victory", 5, 3, 0)
duchyPile = fill(8, duchy)
province = Card("Province", "Victory", 8, 6, 0)
provincePile = fill(8, province)

smithy = Card("Smithy", "Action", 4, 0, 0)
smithyPile = fill(10, smithy)
village = Card("Village", "Action", 3, 0, 0)
villagePile = fill(10, village)

#initialise needed containers for cards in different states of play
deck = [copper, copper, copper, copper, copper, copper, copper, estate, estate, smithy, village]
kingdom = [copperPile, silverPile, goldPile, estatePile]
hand = []
inPlay = []
setAside = []
discard = []
trash = []

#every card gets a function that begins with "card_" to accomodate user input
def card_smithy():
	draw(3)

def card_village():
	draw(1)
	player.actions += 2
	
def card_copper():
	player.money += 1
	
def card_silver():
	player.money += 2
	
def card_gold():
	player.money += 3

def shuffle(): #reorder all cards in deck. return a shuffled deck
	tempDeck = []
	for i in range(len(deck)):
		n = random.randint(0, len(deck) - 1)
		tempDeck.append(deck.pop(n))
	return tempDeck

def draw(n): #draw a hand of n cards
	for i in range(n):
		if len(deck) > 0:
			hand.append(deck.pop())
		else:
			deck.extend(discard)
			discard.clear()
			hand.append(deck.pop())

def actionPhase():
	while player.actions > 0:
		if any(x.type == "Action" for x in hand):
			choice = input("Choose an action. ")
			player.actions -= 1
			for index, card in enumerate(hand):
				if str.lower(card.name) == choice:
					inPlay.append(hand.pop(index))
					func = globals()['card_' + choice]
					func()
			print(hand)
		else:
			print("No actions to play.")
			break
					
def buyPhase():
	choice = ""
	while choice != "stop" and any(x.type == "Treasure" for x in hand):
		choice = input("Choose treasure to play. ")
		for index, card in enumerate(hand):
			if str.lower(card.name) == choice:
				inPlay.append(hand.pop(index))
				func = globals()['card_' + choice]
				func()
				break
		print(hand)
		print(player.money)
	choice = ""
	while (choice != "stop") and (player.buys > 0):
			choice = input("Choose card to buy. ")
			choicePile = globals()[choice + "Pile"]
			if player.money >= choicePile[0].cost:
				discard.append(choicePile.pop())
				player.money -= choicePile[0].cost
				player.buys -= 1

def cleanupPhase():
	discard.extend(inPlay)
	inPlay.clear()
	discard.extend(hand)
	hand.clear()
	draw(5)
	player.actions = 1
	player.buys = 1
	player.money = 0
	
print(deck)
draw(5)
while provincePile != []:
	print(hand)
	actionPhase()
	buyPhase()
	cleanupPhase()
