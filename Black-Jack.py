# import a python module that will be used to randomize numbers in Deck List
import random
import sys

# First we initiate a null list called "Deck"
Deck = []

# now we declare a variable to represent the initial face value of cards in our
# deck, the value is 0
card_val = 0

# set the card counter to 0
counter = 0

# And then we make a for loop that adds 1 to the card-val variable, prints the
# result 4 times(represents the four suits), appends it to the list, and does 
# this until it reaches a value of 9 times
for i in range(4):
    # append the Jacks, Queens, and Kings using a for loop. I have decided to
    # represent the Jacks, Queens, and Kings with their nominal numerical values
    # instead of letters because of technical difficulties
    Deck.append(10)
    Deck.append(10)
    Deck.append(10)
    for n in range(9):
        card_val = card_val + 1
        Deck.append(card_val)
        # reset the card value counter to 0
    card_val = 0

# use the module imported above to shuffle the numbers appended to the Deck List
random.shuffle(Deck)

# define the function that would automatically check the counter if it crossed
# 21 or is on 21
def check_counter():
    if (counter > 21):
        print("You've went past 21")
        sys.exit()
    if (counter == 21):
        print("You got 21!")
        sys.exit()
    
# get the user input on whatever to play or exit
user_input = input("Would you like to play or exit? ")
if user_input == "play":
    while counter <= 21:
        draw_or_not = input("Would you like to draw a card? Yes or No? ")
        if draw_or_not =="No":
            print("You've exited the game")
            sys.exit()
        if draw_or_not == "Yes":
            drawn_card = random.choice(Deck)
            counter = counter + drawn_card
            print(counter)
            check_counter()
