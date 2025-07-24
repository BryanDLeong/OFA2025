import pygame
import random

import pygame

def game():
    #Back end
    def deal_cards(person):
        for i in range(1,3):
            person.append(random.choice(deck))
            for card in person:
                if type(card) == dict:
                    person[i-1] = card.keys()

    # keeps track on how much your hand is
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
                elif card == "Joker":
                    score += 0
        
        if "Ace" in hand and score >21:
            score -= 10

        return score

    cards = [1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
    deck = cards*4
    deck.append("joker")
    deck.append("joker")
    discard = []

    money = 100
    debt = 0

    def remove_cards(person,mode):
        # After dealing the hand
        if mode == "start":
            for card in person:
                discard.append(card)
                deck.pop(deck.index(card))  
        
        # After giving them a card
        elif mode == "end":
            discard.append(person[len(person)-1])
            deck.pop(deck.index(dealer_hand[len(dealer_hand)-1]))         

    def start_game():
        dealer_hand = []
        player_hand = []

        deal_cards(dealer_hand)
        deal_cards(player_hand)

        print("")
        print(f"Player's Money: ${money}")
        print("")
        print(f"Dealer's hand: {dealer_hand}")
        print(f"Player's hand: {player_hand}")   

        remove_cards(dealer_hand,"start")
        remove_cards(player_hand,"start")  

        return dealer_hand, player_hand

    print("")
    print(f"Player's money: ${money}")

    dealer_hand = []
    player_hand = []

    deal_cards(dealer_hand)
    deal_cards(player_hand)

    print("")
    print(f"Dealer's hand: unkown, {dealer_hand[1]}")
    print(f"Player's hand: {str(player_hand)[1:-1]}")

    remove_cards(dealer_hand,"start")
    remove_cards(player_hand,"start")

    betting = True

    while True:
        game_over = False
        dealer_turn = False
        round_over = False
        end = False
        player_score = hand_total(player_hand)
        dealer_score = hand_total(dealer_hand)    

        #betting money
        while betting == True:
            try:
                bet = int(input("How much would you like bet? "))      
                if bet >0 and bet <= money:
                    betting = False
                else:
                    print("Please type a valid number")
                    bet = int(input("How much would you like bet? ") )        
            except ValueError:
                print("Please type a valid input")
                continue

        # checks if deck is empty and adds cards to it
        if deck == []:
            for card in discard:
                deck.append(card)
            discard = []

        print("")
        choice = str(input("Hit or Stand "))
        if choice.lower() == "hit":
            player_hand.append(random.choice(deck))
            remove_cards(player_hand,"end")
            player_score = hand_total(player_hand)
            print(f"Player's hand: {player_hand}")

        elif choice.lower() == "stand":
            dealer_turn = True
            
        elif choice.lower() == "q":
            break

        else: 
            choice = str(input("Hit or Stand "))

        if dealer_turn == True:
            if dealer_score < 21:
                dealer_hand.append(random.choice(deck))
                remove_cards(dealer_hand,"end")
                dealer_score = hand_total(dealer_hand)    
                round_over = True

        if player_score > 21:
            round_over = True

        elif dealer_score > 21:
            round_over = True        

        if round_over == True:
            print("")
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Player's hand: {player_hand}") 

            if player_score > 21:
                print("You busted!")
                print("You Lose!")
                money -= bet
                print(f"-${bet}")
                game_over = True

            elif dealer_score > 21:
                print("Dealer busted!")
                print("You Win!")
                money += bet
                print(f"+${bet}")                
                game_over = True

            if player_score <= 21 and player_score > dealer_score:
                print("You Win!")
                money += bet
                print(f"+${bet}")                
                game_over = True
            elif dealer_score<= 21 and dealer_score > player_score:
                print("You Lose!")
                game_over = True
                print(f"-${bet}")                
                money -= bet
            elif player_score == dealer_score:
                print("It's a Tie")
                game_over = True
            
            while game_over == True:
                replay = str(input("Would you like to play again? Y/N "))

                if replay.lower() == "y" or replay.lower() == "n":
                    if replay.lower() == "y":
                        game_over = False
                        dealer_hand, player_hand = start_game()
                        round_over = False
                        betting = True

                    elif replay.lower() == "n":
                        end = True
                        break    
                else:
                    replay = str(input("Would you like to play again? Y/N "))

            if end == True:
                break



# Front end
pygame.init()

# Screen setup
screen_height = 500
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Black Jack')

# Load images
background_img = pygame.image.load('menu.png').convert()
play_img = pygame.image.load('play.png').convert_alpha()
instrution_img = pygame.image.load('instrution.png').convert_alpha()
quit_img = pygame.image.load('quit.png').convert_alpha()

# Button class (same as before)
class Button():
   def __init__(self, x, y, image, scale):
       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
       self.clicked = False

   def draw(self, surface):
       action = False
       pos = pygame.mouse.get_pos()
       if self.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
               self.clicked = True
               action = True
       if pygame.mouse.get_pressed()[0] == 0:
           self.clicked = False
       surface.blit(self.image, (self.rect.x, self.rect.y))
       return action

# Create buttons
play_button = Button(290, 350, play_img, 0.5)
instrution_button = Button(290, 380, instrution_img, 0.5)
quit_button = Button(290, 410, quit_img, 0.5)

# Game loop
running = True
while running:
   screen.blit(background_img, (0, 0))  # Draw background first

   if play_button.draw(screen):
       game()
       
   if instrution_button.draw(screen):
    
#Rules       
       print(fr'''
Rules:

1.Place your bet: Before the cards are dealt, players must place a bet.The minimum and maximum bets are usually posted on the table.

2.Receive your cards: Once all bets have been placed, the dealer will deal two cards to each player, face up.

3.Decide to hit or stand: After receiving your two cards, you can choose to “hit” and receive additional cards or “stand” and keep your current hand.

4.Dealer’s turn: After all players have had their turn, the dealer will reveal their face-down card and hit or stand according to predetermined rules.

5.Determine the winner: If neither the player nor the dealer busts, the person with the highest hand value wins. A player busts when their hand is greater than 21.
______________________________________________________________________________________________________________________________________

Card Values:

The number corresponds to the amount of points given. 
Face cards and Aces have different values.

Face cards: 10pt
Ace: 1pt or 11pt depending on your score''')

   if quit_button.draw(screen):
       print("Quit")
       running = False

   pygame.display.update()

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

pygame.quit()
