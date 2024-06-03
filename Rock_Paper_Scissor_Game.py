import random
points = 0
choices = ["rock","paper","scissor"]
computer = random.choice(choices)
player = None
while points <= 10:
    player = input(" Choose between rock, paper, scissors ?:")
    print ("Computer: ",computer)
    print ("Player:",player)
    if computer == player:   
       points += 1
    print ("Points:",points)