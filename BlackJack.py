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


def play_again():
    resposta = input("Do you want to keep playing?")

    if resposta.lower() == "yes" or resposta.lower() == "y":

        return True
    elif resposta.lower() == "no" or resposta.lower() == "n":

        return False
    else:
        print("That is not a valid answer")
        return play_again()


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


def bet(money):
    resposta = input("How much you want to bet?")
    if resposta.isnumeric() and int(resposta) > 0:
        if int(resposta) >= money:
            print("You cant afford that")
            return player_pick_money()
        else:
            return int(resposta)
    else:
        print("That is an invalid number")
        return player_pick_money()


'''
Here starts the code
'''

# Money = player_pick_money()
money = 100



keep_playing = True
while keep_playing:
    print(f"You have: {money} credits")
    bet_value = bet(money)
    money = money - bet_value
    print(f"Now you have {money} credits")

    deck1 = new_deck()

    # Getting the dealers hand
    dealer_hand = []
    dealer_hand.insert(len(dealer_hand), pick_card(deck1))
    print("Dealer  hand is: ", dealer_hand)
    dealer_total = total(dealer_hand)
    print("The total of the dealer is:  ", dealer_total)
    dealer_hand.insert(len(dealer_hand), pick_card(deck1))
    dealer_total = total(dealer_hand)

    # Picking card for the player
    player_hand = []
    player_hand.insert(len(player_hand), pick_card(deck1))
    player_hand.insert(len(player_hand), pick_card(deck1))
    print("Your hand is: ", player_hand)

    # Getting the total of the player
    player_total = total(player_hand)
    print("Your total is: ", player_total)

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

    else:
        print("Dealer will play")
        print("Dealer  hand is: ", dealer_hand)
        dealer_total = total(dealer_hand)
        print("The total of the dealer is:  ", dealer_total)
        while dealer_total < 17:
            dealer_hand.insert(len(dealer_hand), pick_card(deck1))
            print("Dealer  hand is: ", dealer_hand)
            dealer_total = total(dealer_hand)
            print("The total of the dealer is:  ", dealer_total)
            if dealer_total == 21:
                print("The dealer did a Black Jack")
            elif dealer_total > 21:
                print("Dealer busted")

        if player_total > dealer_total or dealer_total > 21:
            print("\nYou win", end=" ")
            if player_total == 21:
                money = money + 3 * bet_value
                print(f"You just got {2*bet_value}. Your total money is {money}")
            else:
                money = money + 2 * bet_value
                print(f"You just got {bet_value}. Your total money is {money}")
        elif player_total == dealer_total:
            print("\nYou draw", end=" ")
            money = money + bet_value
            print(f"You got your money back. Your total money is {money}")
        else:
            print("\nYou lose", end=" ")
            print(f"You just lost {bet_value}. Your total money is {money}")
    if money == 0:
        print("You run out of money, game over for you :(")
        break

    if not play_again():
        keep_playing = False
# end of the file
input("The game is over. Press enter to leave \n")


