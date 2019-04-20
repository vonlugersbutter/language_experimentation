class character():
    def __init__(self, name, rupees, items):
        self.name = name
        self.rupees = 0
        self.items = []

p1name = raw_input("Enter Player 1 Name: ")
p2name = raw_input("Enter Player 2 Name: ")

player1 = character(p1name, 0, [])
player2 = character(p2name, 0, [])

print(player1.name + " now has a crossbow.")
player1.items.append("crossbow")
print(player1.name + " also earned 50 rupees.")
player1.rupees += 50

print
print(player2.name + " now has a ball and chain.")
player2.items.append("ball and chain")
print(player2.name + " also earned 80 rupees.")
player2.rupees += 80

print
print(player1.name + "'s items: ")
for i in range(1,len(player1.items)+1, 1):
    for item in player1.items:
        print(str(i) + ". "+item)

print
print(player2.name + "'s items: ")
for i in range(1,len(player2.items)+1, 1):
    for item in player2.items:
        print(str(i) + ". "+item)
