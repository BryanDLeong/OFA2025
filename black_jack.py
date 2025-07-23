import pygame
import random


def deal_cards(person):
    for i in range(1,3):
        person.append(random.choice(deck))
        for card in person:
            if type(card) == dict:
                person[i-1] = card.keys()

def hand_total(hand):
    score = 0
    for card in hand:
        try:
            score += card
        except TypeError:
            if card == "Jack" or card == "Queen" or card == "King":
              score += 10
            elif card == "Ace":
               score += 11
    
    if "Ace" in hand and score >21:
        score -= 10

    return score

cards = [1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
deck = cards*4
discard = []

def remove_cards(person,mode):
    #After dealing the hand
    if mode == "start":
        for card in person:
            discard.append(card)
            deck.pop(deck.index(card))  
    
    #after giving them a card
    elif mode == "end":
        discard.append(person[len(person)-1])
        deck.pop(deck.index(dealer_hand[len(dealer_hand)-1]))         

def start_game():
    dealer_hand = []
    player_hand = []

    deal_cards(dealer_hand)
    deal_cards(player_hand)
    print("")
    print(f"Dealer's hand: {dealer_hand}")
    print(f"Player's hand: {player_hand}")   

    remove_cards(dealer_hand,"start")
    remove_cards(player_hand,"start")  

    return dealer_hand, player_hand

dealer_hand = []
player_hand = []

deal_cards(dealer_hand)
deal_cards(player_hand)

print("")
print(f"Dealer's hand: {dealer_hand}")
print(f"Player's hand: {player_hand}")

remove_cards(dealer_hand,"start")
remove_cards(player_hand,"start")

print(hand_total(dealer_hand))

while True:
    game_over = False
    dealer_turn = False
    round_over = False

    if deck == []:
        for card in discard:
            deck.append(card)
        discard = []

    print("")
    choice = str(input("Hit or Stand "))
    if choice.lower() == "hit":
        player_hand.append(random.choice(deck))
        remove_cards(player_hand,"end")
        print(f"Player's hand: {player_hand}")

    elif choice.lower() == "stand":
        dealer_turn = True
        
    elif choice.lower() == "q":
        break

    else: 
        choice = str(input("Hit or Stand "))

    player_score = hand_total(player_hand)
    dealer_score = hand_total(dealer_hand)

    if player_score > 21:
        print("You busted!")
        round_over = True
        game_over = True

    elif dealer_score > 21:
        print("Dealer busted!")
        round_over = True
        game_over = True        

    if dealer_turn == True:
        if dealer_score < 21:
            dealer_hand.append(random.choice(deck))
            remove_cards(dealer_hand,"end")
            round_over = True
    

    if round_over == True:
        print("")
        print(f"Dealer's hand: {dealer_hand} + {dealer_score}")
        print(f"Player's hand: {player_hand} + {player_score}") 
        if player_score <= 21 and player_score > dealer_score:
            print("You Win!")
            game_over = True
        elif dealer_score<= 21 and dealer_score > player_score:
            print("You Lose!")
            game_over = True
        elif player_score == dealer_score:
            print("It's a Tie")
            game_over = True
        
        if game_over == True:
            replay = str(input("Would you like to play again? Y/N "))

            if replay.lower() == "y":
                game_over = False
                dealer_hand, player_hand = start_game()
                round_over = False

            elif replay.lower() == "n":
                break    
