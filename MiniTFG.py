print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

"""                         Code Implementation                                """

import pyttsx4
engine = pyttsx4.init()
engine.setProperty('rate', 125)
engine.say("Welcome to Treasure Island.")
engine.say("Your mission is to find the treasure.")
engine.runAndWait()
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right":').lower()
if choice1 == "right":
    engine.say("You fell into a hole!! Game over")
    engine.runAndWait()
else:
    choice2 = input('You\'ve come to lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "swim":
        engine.say("Attack by trout. Game over")
        engine.runAndWait()
        exit()
    else:
        engine.say("You got a boat and reached next level of game..")
        engine.runAndWait()
    choice3 = input('''You arrive at the island without any harm. There is a house with 3 doors.
                     One for RED, One for BLUE and One for YELLOW.
                    "TYpe Which one you want to try:''').lower()
    if choice3 == "red":
        engine.say("You Burned by fire. Game Over.")
        engine.runAndWait()
    elif choice3 == "blue":
        engine.say("You're eaten by beasts. Game Over")
        engine.runAndWait()
    else:
        engine.say("You found Treasure box, You win")
        engine.runAndWait()
