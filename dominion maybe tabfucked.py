import tkinter as tk
from tkinter import ttk

class DominionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dominion")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to Dominion")
        self.label.pack()

        #self.draw_button = tk.Button(self.root, text="Draw 5 Cards", command=self.draw_cards)
        #self.draw_button.pack()
        
        self.hand_frame = tk.Frame(self.root)
        self.hand_frame.pack()
        
        self.create_horizontal_scrollable_hand_frame()
        
        self.start_button = tk.Button(self.root, text="Start game", command=lambda: self.draw_cards(5))
        self.start_button.pack()

    def draw_cards(self, n):
    	draw(n)
    	self.update_hand_display()
    	self.actionPhase()

    def actionPhase(self):
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

    def update_hand_display(self):
        # Clear the previous hand display
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Create a button for each card in hand
        for card in hand:
            card_button = tk.Button(self.scrollable_frame, text=card.name, command=lambda c=card: self.use_card(c))
            card_button.pack(side=tk.LEFT, padx=5, pady=5)           
            

    def create_horizontal_scrollable_hand_frame(self):
        # Create a canvas and a horizontal scrollbar to scroll the frame
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="top", fill="both", expand=True)
        self.scrollbar.pack(side="bottom", fill="x")

    def use_card(self, card):
        print(f"Using card: {card.name}")
        # Perform the action associated with the card
        func = globals()['play' + card.name]
        if func:
            func()
        inPlay.append(hand.remove(card))
        self.update_hand_display()  # Update the display after using the card
        
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
		
def draw(n): #draw a hand of n cards
	for i in range(n):
		if len(deck) > 0:
			hand.append(deck.pop())
		else:
			deck.extend(discard)
			discard.clear()
			hand.append(deck.pop())

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
def playSmithy():
	draw(3)

def playVillage():
	draw(1)
	player.actions += 2
	
def playCopper():
	player.money += 1
	
def playSilver():
	player.money += 2
	
def playGold():
	player.money += 3

def shuffle(): #reorder all cards in deck. return a shuffled deck
	tempDeck = []
	for i in range(len(deck)):
		n = random.randint(0, len(deck) - 1)
		tempDeck.append(deck.pop(n))
	return tempDeck

root = tk.Tk()
g = DominionGUI(root)
root.mainloop()