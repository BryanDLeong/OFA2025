from turtle import back
import pygame
import random

# def game():
#     #Back end
#     def deal_cards(person):
#         for i in range(1,3):
#             person.append(random.choice(deck))
#             for card in person:
#                 if type(card) == dict:
#                     person[i-1] = card.keys()

#     # keeps track on how much your hand is
#     def hand_total(hand):
#         score = 0
#         for card in hand:
#             try:
#                 score += card
#             except TypeError:
#                 if card == "Jack" or card == "Queen" or card == "King":
#                     score += 10
#                 elif card == "Ace":
#                     score += 11
#                 elif card == "Joker":
#                     score += 0

#         if "Ace" in hand and score >21:
#             score -= 10

#         return score

#     cards = [1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
#     deck = cards*4
#     deck.append("joker")
#     deck.append("joker")
#     discard = []

#     money = 100
#     debt = 0

#     def remove_cards(person,mode):
#         # After dealing the hand
#         if mode == "start":
#             for card in person:
#                 discard.append(card)
#                 deck.pop(deck.index(card))

#         # After giving them a card
#         elif mode == "end":
#             discard.append(person[len(person)-1])
#             deck.pop(deck.index(dealer_hand[len(dealer_hand)-1]))

#     def start_game():
#         dealer_hand = []
#         player_hand = []

#         deal_cards(dealer_hand)
#         deal_cards(player_hand)

#         print("")
#         print(f"Player's Money: ${money}")

#         remove_cards(dealer_hand,"start")
#         remove_cards(player_hand,"start")

#         return dealer_hand, player_hand

#     print("")
#     print(f"Player's money: ${money}")

#     dealer_hand = []
#     player_hand = []

#     deal_cards(dealer_hand)
#     deal_cards(player_hand)

#     print("")

#     remove_cards(dealer_hand,"start")
#     remove_cards(player_hand,"start")

#     betting = True

#     while True:
#         game_over = False
#         dealer_turn = False
#         round_over = False
#         end = False
#         player_score = hand_total(player_hand)
#         dealer_score = hand_total(dealer_hand)

#         #betting money
#         while betting == True:
#             try:
#                 bet = int(input("How much would you like bet? "))
#                 if bet >0 and bet <= money:
#                     betting = False
#                     print("")
#                     print(f"Dealer's hand: unkown, {dealer_hand[1]}")
#                     print(f"Player's hand: {str(player_hand)[1:-1]}")
#                 else:
#                     print("Please type a valid number")
#                     continue
#             except ValueError:
#                 print("Please type a valid input")
#                 continue

#         # checks if deck is empty and adds cards to it
#         if deck == []:
#             for card in discard:
#                 deck.append(card)
#             discard = []

#         print("")
#         choice = str(input("Hit or Stand "))
#         if choice.lower() == "hit":
#             player_hand.append(random.choice(deck))
#             remove_cards(player_hand,"end")
#             player_score = hand_total(player_hand)
#             print(f"Player's hand: {player_hand}")

#         elif choice.lower() == "stand":
#             dealer_turn = True

#         elif choice.lower() == "q":
#             break

#         else:
#             choice = str(input("Hit or Stand "))

#         if dealer_turn == True:
#             if dealer_score < 21:
#                 dealer_hand.append(random.choice(deck))
#                 remove_cards(dealer_hand,"end")
#                 dealer_score = hand_total(dealer_hand)
#                 round_over = True

#         if player_score > 21:
#             round_over = True

#         elif dealer_score > 21:
#             round_over = True

#         if round_over == True:
#             print("")
#             print(f"Dealer's hand: {dealer_hand}")
#             print(f"Player's hand: {player_hand}")

#             if player_score > 21:
#                 print("You busted!")
#                 print("You Lose!")
#                 money -= bet
#                 print(f"-${bet}")
#                 game_over = True

#             elif dealer_score > 21:
#                 print("Dealer busted!")
#                 print("You Win!")
#                 money += bet
#                 print(f"+${bet}")
#                 game_over = True

#             if player_score <= 21 and player_score > dealer_score:
#                 print("You Win!")
#                 money += bet
#                 print(f"+${bet}")
#                 game_over = True
#             elif dealer_score<= 21 and dealer_score > player_score:
#                 print("You Lose!")
#                 game_over = True
#                 print(f"-${bet}")
#                 money -= bet
#             elif player_score == dealer_score:
#                 print("It's a Tie")
#                 game_over = True

#             while game_over == True:
#                 replay = str(input("Would you like to play again? Y/N "))

#                 if replay.lower() == "y" or replay.lower() == "n":
#                     if replay.lower() == "y":
#                         game_over = False
#                         dealer_hand, player_hand = start_game()
#                         round_over = False
#                         betting = True

#                     elif replay.lower() == "n":
#                         end = True
#                         break
#                 else:
#                     replay = str(input("Would you like to play again? Y/N "))

#             if end == True:
#                 break

def deal_cards(person):
    for i in range(1, 3):
        person.append(random.choice(deck))
        for card in person:
            if type(card) == dict:
                person[i - 1] = card.keys()

def add_suits(person):
    while len(person) < 2:
        person.append(random.choice(suits))

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

    if "Ace" in hand and score > 21:
        score -= 10

    return score

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
deck = cards * 4
suits = ["_diamond","_heart","_spade","_club"]*4
discard = []

money = 100
debt = 0


def remove_cards(person, mode):
    if mode == "start":
        for card in person:
            discard.append(card)
            deck.pop(deck.index(card))

        # After giving them a card
    elif mode == "end":
        discard.append(person[len(person)-1])
        deck.pop(deck.index(person[len(person)-1]))
        
    

def start_game():
    dealer_hand = []
    dealer_suits = []
    player_hand = []
    player_suits = []

    deal_cards(dealer_hand)
    deal_cards(player_hand)

    add_suits(dealer_suits)
    add_suits(player_suits)

    print("")
    print(f"Player's Money: ${money}")

    remove_cards(dealer_hand,"start")
    remove_cards(player_hand,"start")

    return dealer_hand, player_hand

pygame.init()


def end_screen(result):
    if result == "lose":
        background_img = pygame.image.load("lose_screen.png").convert()
        scaled_end_screen = pygame.transform.scale(
        background_img, (screen_width, screen_height)
        )
        screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
        screen.blit(scaled_end_screen,(0,0)) 

    elif result == "win":
        end_screen = pygame.image.load(f"win_screen.jpeg").convert_alpha()
        scaled_end_screen = pygame.transform.scale(end_screen, (screen_width, screen_height))
        screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
        screen.blit(scaled_end_screen,(0,0))

# Screen setup
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Black Jack")


# Load menu assets
menu_background = pygame.image.load("menu.png").convert()
play_img = pygame.image.load("black_jack_buttons/play.png").convert_alpha()
instruction_img = pygame.image.load("black_jack_buttons/instrution.png").convert_alpha()
quit_img = pygame.image.load("black_jack_buttons/quit.png").convert_alpha()
deal_img = pygame.image.load("black_jack_buttons/deal.png").convert_alpha()
stand_img = pygame.image.load("black_jack_buttons/stand.png").convert_alpha()


# Button class
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
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


# Create menu buttons
play_button = Button(290, 350, play_img, 0.5)
instruction_button = Button(290, 380, instruction_img, 0.5)
quit_button = Button(290, 410, quit_img, 0.5)


# === Function to run Blackjack Game ===
def run_blackjack():
    # Load and scale background
    background_img = pygame.image.load("bjs.png").convert()
    scaled_background = pygame.transform.scale(
        background_img, (screen_width, screen_height)
    )

    # Load card images for all members
    def load_cards(num, prefix):
        return [pygame.image.load(f"cards/{num}{prefix}.png").convert_alpha()]

    #    winter_cards = load_cards("_heart")
    #    giselle_cards = load_cards("_club")
    #    ningning_cards = load_cards("_spade")
    #    karina_cards = load_cards("_diamond")
    #    game()

    # Create card buttons
    def create_buttons(card_list, y):
        buttons = []
        x = 300
        for img in card_list:
            btn = Button(x, y, img, 0.1)
            buttons.append(btn)
            x += 20
        return buttons    
    
    #    winter_buttons = create_buttons(winter_cards, 370)
    #    giselle_buttons = create_buttons(giselle_cards, 250)
    #    ningning_buttons = create_buttons(ningning_cards, 120)
    #    karina_buttons = create_buttons(karina_cards, 20)

    # Back button (using quit image as a placeholder)
    back_button = Button(20, 460, quit_img, 0.5)
    deal_button = Button(675, 300, deal_img, 1)
    stand_button = Button(675, 350, stand_img, 1)

    screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
    screen.blit(scaled_background, (0, 0))  # Draw blackjack background


    dealer_hand = []
    dealer_suits = []
    player_hand = []
    player_suits = []

    deal_cards(dealer_hand)
    deal_cards(player_hand)

    add_suits(dealer_suits)
    add_suits(player_suits)

    print("")

    remove_cards(dealer_hand, "start")
    remove_cards(player_hand, "start")

    card_num_player = 0                             
    player_score = hand_total(player_hand)
    for card in player_hand:
        try:
            card = load_cards(str(player_hand[card_num_player]).lower(), player_suits[card_num_player])
        except FileNotFoundError:
            card = load_cards(str(player_hand[card_num_player][0]).lower(), player_suits[card_num_player])
        card_size = pygame.transform.scale(card[-1], (100, 150))
        screen.blit(card_size, (100+(card_num_player*50), 300))
        card_num_player += 1

    card_num_dealer = 0
    remove_cards(player_hand, "start")
    player_score = hand_total(player_hand)
    
    card = load_cards("back", "_card")
    card_size = pygame.transform.scale(card[-1], (100, 150))
    screen.blit(card_size, (100+(card_num_dealer*50), 10))
    card_num_dealer += 1   

    try:
        card = load_cards(str(dealer_hand[card_num_dealer]).lower(), dealer_suits[card_num_dealer])
    except FileNotFoundError:
        card = load_cards(str(dealer_hand[card_num_dealer][0]).lower(), dealer_suits[card_num_dealer])
    card_size = pygame.transform.scale(card[-1], (100, 150))
    screen.blit(card_size, (100+(card_num_dealer*50), 10))
    card_num_dealer += 1   

    # Blackjack loop
    running = True
    while running:

        round_over = False
        player_score = hand_total(player_hand)
        dealer_score = hand_total(player_hand)     

        #    # Draw all card buttons
        #    for i, btn in enumerate(winter_buttons):
        #        if btn.draw(screen):
        #            print(f"Winter card: {i + 1}")
        #    for i, btn in enumerate(giselle_buttons):
        #        if btn.draw(screen):
        #            print(f"Giselle card: {i + 1}")
        #    for i, btn in enumerate(ningning_buttons):
        #        if btn.draw(screen):
        #            print(f"NingNing card: {i + 1}")
        #    for i, btn in enumerate(karina_buttons):
        #        if btn.draw(screen):
        #            print(f"Karina card: {i + 1}")

        # Back to menu
        if back_button.draw(screen):
            return  # Exit blackjack screen
        if deal_button.draw(screen):
            player_hand.append(random.choice(deck)) 
            player_suits.append(random.choice(suits)) 
            remove_cards(player_hand, "end")
            player_score = hand_total(player_hand)

            try:
                card = load_cards(str(player_hand[card_num_player]).lower(), player_suits[card_num_player])
            except FileNotFoundError:
                card = load_cards(str(player_hand[card_num_player][0]).lower(), player_suits[card_num_player])
            card_size = pygame.transform.scale(card[-1], (100, 150))
            screen.blit(card_size, (100+(card_num_player*50), 300))
            card_num_player += 1
            print(player_hand)

        if stand_button.draw(screen):
            dealer_hand.append(random.choice(deck))
            dealer_suits.append(random.choice(suits))   
            remove_cards(dealer_hand, "end")
            dealer_score = hand_total(dealer_hand)

            try:
                card = load_cards(str(dealer_hand[card_num_dealer]).lower(), dealer_suits[card_num_dealer])
            except FileNotFoundError:
                card = load_cards(str(dealer_hand[card_num_dealer][0]).lower(), dealer_suits[card_num_dealer])
            card_size = pygame.transform.scale(card[-1], (100, 150))
            screen.blit(card_size, (100+(card_num_dealer*50), 10))

            try:
                card = load_cards(dealer_hand[0], dealer_suits[0])
            except:
                card = load_cards(str(dealer_hand[0][0]).lower(), dealer_suits[0])
                
            card_size = pygame.transform.scale(card[-1], (100, 150))
            screen.blit(card_size, (100, 10))
            pygame.display.update()

            pygame.time.delay(1000)
            round_over = True

        pygame.display.update()

        if player_score > 21:  
            pygame.time.delay(1000)                                     
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
                end_screen("lose")

            elif dealer_score > 21:
                print("Dealer busted!")
                print("You Win!")  
                end_screen("win")

            if player_score <= 21 and player_score > dealer_score:
                print("You Win!")
                end_screen("win")

            elif dealer_score<= 21 and dealer_score > player_score:
                print("You Lose!")
                end_screen("lose")

            elif player_score == dealer_score:
                print("It's a Tie")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



# === Main Game Loop ===
game_state = "menu"
running = True

while running:
    if game_state == "menu":
        screen.blit(menu_background, (0, 0))

        if play_button.draw(screen):
            game_state = "blackjack"
        if instruction_button.draw(screen):
            print("praise winter")
        if quit_button.draw(screen):
            running = False

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    elif game_state == "blackjack":
        deck = cards*4
        run_blackjack()
        game_state = "menu"  # Return to menu after blackjack


pygame.quit()
