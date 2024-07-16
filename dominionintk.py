import tkinter as tk

class DominionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dominion")
        self.root.geometry("800x600")
        self.create_widgets()
        
        # Add game logic initialization here
        self.player = Player()
        self.deck = [copper, copper, copper, copper, copper, copper, copper, estate, estate, smithy, village]
        self.hand = []
        self.discard = []
        self.inPlay = []

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to Dominion")
        self.label.pack()

        self.draw_button = tk.Button(self.root, text="Draw 5 Cards", command=self.draw_cards)
        self.draw_button.pack()

    def draw_cards(self):
        draw(5)  # Use your draw function
        self.update_hand_display()

    def update_hand_display(self):
        hand_text = "Hand: " + ", ".join(card.name for card in self.hand)
        self.label.config(text=hand_text)

root = tk.Tk()
app = DominionGUI(root)
root.mainloop()
