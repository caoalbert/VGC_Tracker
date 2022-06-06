import pickle
import sys
from decimal import Decimal

if len(sys.argv) == 2 and sys.argv[1] == "initialize":
    cards = dict()
    with open("vgc.pkl", "wb") as handle:
        pickle.dump(cards, handle, protocol = pickle.HIGHEST_PROTOCOL)

with open("vgc.pkl", "rb") as handle:
    cards = pickle.load(handle)
    
class vgc:
    def __init__(self, initial_balance):
        self.current_balance = initial_balance
    
    def __str__(self):
        output = "The balance is " + repr(self.current_balance) + " dollars"
        return(output)
    
    def spend(self, amount):
        self.current_balance = self.current_balance - amount

    

# Adding new vgc to the dic
if len(sys.argv) == 3 and sys.argv[1] not in cards:
    newcard = vgc(Decimal(sys.argv[2]))
    print("A newcard has been added with a balance of", newcard.current_balance)
    cards[sys.argv[1]] = newcard.current_balance

# Deduct balance    
elif len(sys.argv) == 3 and sys.argv[1] in cards:
    instance = vgc(cards[sys.argv[1]])
    print("The card ends in " + sys.argv[1] + " had an initial balance of ", instance.current_balance)
    print(sys.argv[2] + " dollars spent")
    instance.spend(Decimal(sys.argv[2]))
    print("The card ends in " + sys.argv[1] + " now have a balance of", instance.current_balance)
    cards[sys.argv[1]] = instance.current_balance

    if instance.current_balance == Decimal(0):
        del cards[sys.argv[1]]
        print("Card ends in", sys.argv[1], "is deleted due to 0 balance")

# Reset cards
if len(sys.argv) == 2 and sys.argv[1] == "reset":
    cards = dict()   

# Retrieve the balance
if len(sys.argv) == 2 and sys.argv[1] in cards:
    print("The current balance of the card is:", cards[sys.argv[1]])
    
# List all cards
if len(sys.argv) == 2 and sys.argv[1] == "list":
    for i in cards:
        print(i, "has a balance of", cards[i])

with open("vgc.pkl", "wb") as handle:
    pickle.dump(cards, handle, protocol = pickle.HIGHEST_PROTOCOL)