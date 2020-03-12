import random

'''
Functions
'''


# ask how much money the player starts with
def player_pick_money():
    resposta = input("How much money you want to start with?")
    if resposta.isnumeric() and int(resposta) > 0:
        return int(resposta)
    else:
        print("That is an invalid number")
        return player_pick_money()


# gets a card from the deck and removes it from the list
def pick_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))


# creates a new deck
def new_deck():
    card_deck = []

    for i in range(2, 11):
        card_deck.extend([i] * 4)
    for c in ['Jack', 'Queen', 'King', 'Ace']:
        card_deck.extend([c] * 4)

    return card_deck


# gets the value on the hand of the player
def total(hand):
    total = 0
    have_ace = False;
    for i in hand:
        if isinstance(i, int):
            total = total + i
        elif i == 'Ace':
            have_ace = True
            total = total + 1

        else:
            total = total + 10

    if have_ace == True and total + 10 < 22:
        total = total + 10

    return total


'''
Here starts the code
'''

# Money = player_pick_money()
# print("You have: ", Money, " credits")
keep_playing = True

deck1 = new_deck()

# Picking card for the player
player_hand = []
player_hand.insert(len(player_hand), pick_card(deck1))
player_hand.insert(len(player_hand), pick_card(deck1))
print("Your hand is: ", player_hand)

# Getting the total of the player
player_total = total(player_hand)
print("Your total is: ", player_total)

# Getting the dealers hand
dealer_hand = []
dealer_hand.insert(len(dealer_hand), pick_card(deck1))
print("Dealer  hand is: ", dealer_hand)
dealer_total = total(dealer_hand)
print("The total of the dealer is:  ", dealer_total)
while player_total < 22:

    # Check if game is already over on 1º turn
    if player_total == 21:
        print("You did a Blackjack ")
        break
    else:

        def pick_move():
            global player_total
            player_move = input("You want to hit or stand? \n")
            if player_move == "hit":
                print("You choose to hit")
                player_hand.insert(len(player_hand), pick_card(deck1))
                print("Your hand is: ", player_hand)
                player_total = total(player_hand)
                print("Your total is: ", player_total)
                return False

            elif player_move == "stand":
                print("You choose to stand")
                return True

            else:
                print("That is not a valid answer")
                return pick_move()


        if pick_move():
            break

if player_total > 21:
    print("You busted, soo you lost")
    # TODO: remove credits when lose
else:
    print("Dealer will play")
    while dealer_total < 17:
        dealer_hand.insert(len(dealer_hand), pick_card(deck1))
        print("Dealer  hand is: ", dealer_hand)
        dealer_total = total(dealer_hand)
        print("The total of the dealer is:  ", dealer_total)
    # TODO: Make dealer moves

# end of the file
input("Press enter to leave \n")
