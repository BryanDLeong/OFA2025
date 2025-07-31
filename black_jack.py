from turtle import back
import pygame
import random


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

# Card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

# Deals starting hand of 2 cards
def deal_cards(person):
    for i in range(0, 2):
        card = random.choice(deck)
        person.append(card)
        deck.remove(card)

# keeps track on how much your hand is
def hand_total(hand):
    score = 0
    hasAce = False
    for card in hand:
        cardValue = card.value
        try:
            score += cardValue
        except TypeError:
            if cardValue == "Jack" or cardValue == "Queen" or cardValue == "King":
                score += 10
            elif cardValue == "Ace":
                score += 11
                hasAce = True

    if hasAce and score > 21:
        score -= 10

    return score

#deck list
deck = []
money = 100
bet = 0

#returns a "deck" list with 52 unique cards in order
def generateDeck():
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    suits = ["_diamond", "_heart", "_spade", "_club"]
    deck = []
    for value in values:
        for suit in suits:
            deck.append(Card(value, suit))
    return deck

def end_screen(result):
    if result == "lose":
        background_img = pygame.image.load("images/lose_screen.png").convert()
        scaled_end_screen = pygame.transform.scale(
            background_img, (screen_width, screen_height)
        )
        screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
        screen.blit(scaled_end_screen, (0, 0))

    elif result == "win":
        end_screen = pygame.image.load(f"images/win_screen.jpeg").convert_alpha()
        scaled_end_screen = pygame.transform.scale(
            end_screen, (screen_width, screen_height)
        )
        screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
        screen.blit(scaled_end_screen, (0, 0))

    else:
        end_screen = pygame.image.load(f"images/tie_screen.png").convert_alpha()
        scaled_end_screen = pygame.transform.scale(
            end_screen, (screen_width, screen_height)
        )
        screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
        screen.blit(scaled_end_screen, (0, 0))

pygame.init()

# Screen setup
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Black Jack")

font = pygame.font.Font('freesansbold.ttf', 32)

# Load menu assets
menu_background = pygame.image.load("images/menu.png").convert()
play_img = pygame.image.load("black_jack_buttons/play.png").convert_alpha()
instruction_img = pygame.image.load("black_jack_buttons/instrution.png").convert_alpha()
quit_img = pygame.image.load("black_jack_buttons/quit.png").convert_alpha()
deal_img = pygame.image.load("black_jack_buttons/deal.png").convert_alpha()
stand_img = pygame.image.load("black_jack_buttons/stand.png").convert_alpha()
placebet_img = pygame.image.load("black_jack_buttons/placebet.png").convert_alpha()
plus_img = pygame.image.load("black_jack_buttons/plus.png").convert_alpha()
minus_img = pygame.image.load("black_jack_buttons/minus.png").convert_alpha()
freemoney_img = pygame.image.load("black_jack_buttons/freemoney.png").convert_alpha()

# Create menu buttons
play_button = Button(350, 380, play_img, 0.7)
instruction_button = Button(350, 415, instruction_img, 0.7)
quit_button = Button(350, 450, quit_img, 0.7)

def placeBet():
    global money
    startingMoney = money
    runningBetting = True
    bet = 10
    # Back button (using quit image as a placeholder)
    betting_confirm_button = Button(screen_width/2 - placebet_img.get_width()/2, 460, placebet_img, 1)
    betting_plus_button = Button(screen_width/2 - placebet_img.get_width()/2, 200, plus_img, 1)
    betting_minus_button = Button(screen_width/2 - placebet_img.get_width()/2, 275, minus_img, 1)
    freemoney_button = Button(screen_width/2 - placebet_img.get_width()/2, 350, freemoney_img, 1)
    while runningBetting:
        background_img = pygame.image.load("images/betting.png").convert()
        scaled_background = pygame.transform.scale(
            background_img, (screen_width, screen_height)
        )
        screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
        screen.blit(scaled_background, (0, 0))  # Draw blackjack background
        if startingMoney > 0:
            # Back to menu
            if betting_confirm_button.draw(screen):
                return bet
            if betting_plus_button.draw(screen) and bet + 5 <= startingMoney:
                bet += 5
            if betting_minus_button.draw(screen) and bet - 5 > 0:
                bet -= 5

            money = startingMoney - bet

            if money < 0:
                bet += money
                money = 0

            text = font.render('Current money: ' + str(money), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height*3/4 + textRect.height)
            screen.blit(text, textRect)

            text = font.render('Current Bet: ' + str(bet), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height*3/4)
            screen.blit(text, textRect)

        else:
            background_img = pygame.image.load("images/gethelp.png").convert()
            scaled_background = pygame.transform.scale(
                background_img, (screen_width, screen_height)
            )
            screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
            screen.blit(scaled_background, (0, 0))  # Draw blackjack background
            if freemoney_button.draw(screen):
                startingMoney += 100

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

# === Function to run Blackjack Game ===
def run_blackjack():
    global bet
    bet = placeBet()
    global money
    currentMoney = money
    gameState = "blackjack"
    # Load and scale background
    background_img = pygame.image.load("images/bjs.png").convert()
    scaled_background = pygame.transform.scale(
        background_img, (screen_width, screen_height)
    )

    # Load card images for all members
    def load_cards(num, prefix):
        return [pygame.image.load(f"cards/{num}{prefix}.png").convert_alpha()]

    # Back button (using quit image as a placeholder)
    back_button = Button(20, 460, quit_img, 0.5)
    deal_button = Button(675, 300, deal_img, 1)
    stand_button = Button(675, 350, stand_img, 1)

    screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
    screen.blit(scaled_background, (0, 0))  # Draw blackjack background

    dealer_hand = []
    player_hand = []

    deal_cards(dealer_hand)
    deal_cards(player_hand)

    card_num_player = 0
    player_score = hand_total(player_hand)
    for card in player_hand:
        try:
            cardDrawObject = load_cards(
                str(player_hand[card_num_player].value).lower(), player_hand[card_num_player].suit
            )
        except FileNotFoundError:
            cardDrawObject = load_cards(
                str(player_hand[card_num_player].value[0]).lower(),
                player_hand[card_num_player].suit
            )
        card_size = pygame.transform.scale(cardDrawObject[-1], (100, 150))
        screen.blit(card_size, (100 + (card_num_player * 50), 300))
        card_num_player += 1

    card_num_dealer = 0
    #remove_cards(player_hand, "start")
    player_score = hand_total(player_hand)

    if player_score == 21:
        pygame.time.delay(1000)
        round_over = True

    card = load_cards("back", "_card")
    card_size = pygame.transform.scale(card[-1], (100, 150))
    screen.blit(card_size, (100 + (card_num_dealer * 50), 10))
    card_num_dealer += 1

    try:
        cardDrawObject = load_cards(
            str(dealer_hand[card_num_dealer].value).lower(), dealer_hand[card_num_dealer].suit
        )
    except FileNotFoundError:
        cardDrawObject = load_cards(
                str(dealer_hand[card_num_dealer].value[0]).lower(),
                dealer_hand[card_num_dealer].suit
            )
    card_size = pygame.transform.scale(cardDrawObject[-1], (100, 150))
    screen.blit(card_size, (100 + (card_num_dealer * 50), 10))
    card_num_dealer += 1

    # Blackjack loop
    running = True
    while running:

        round_over = False
        player_score = hand_total(player_hand)
        dealer_score = hand_total(player_hand)

        
        # Back to menu
        if back_button.draw(screen):
            return currentMoney # Exit blackjack screen
        if gameState == "blackjack":
            text = font.render('Current Bet: ' + str(bet), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height/2 - textRect.height)
            screen.blit(text, textRect)

            text = font.render('Current Money: ' + str(currentMoney), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height/2 + textRect.height/2)
            screen.blit(text, textRect)

            if deal_button.draw(screen):
                newCard = random.choice(deck)
                player_hand.append(newCard)
                deck.remove(newCard)

                #remove_cards(player_hand, "end")
                player_score = hand_total(player_hand)

                try:
                    cardDrawObject = load_cards(
                        str(player_hand[card_num_player].value).lower(),
                        player_hand[card_num_player].suit,
                    )
                except FileNotFoundError:
                        cardDrawObject = load_cards(
                        str(player_hand[card_num_player].value[0]).lower(),
                        player_hand[card_num_player].suit
                    )
                card_size = pygame.transform.scale(cardDrawObject[-1], (100, 150))
                screen.blit(card_size, (100 + (card_num_player * 50), 300))
                card_num_player += 1

                pygame.display.update()

                if player_score > 21:
                    pygame.time.delay(1000)
                    round_over = True

            if stand_button.draw(screen):
                newCard = random.choice(deck)
                dealer_hand.append(newCard)
                deck.remove(newCard)
                dealer_score = hand_total(dealer_hand)

                card_num_dealer = 0
                for card in dealer_hand:
                    try:
                        cardDrawObject = load_cards(
                            str(card.value).lower(),
                            card.suit,
                        )
                    except FileNotFoundError:
                        cardDrawObject = load_cards(
                            str(card.value[0]).lower(),
                            card.suit
                        )
                    card_size = pygame.transform.scale(cardDrawObject[-1], (100, 150))
                    screen.blit(card_size, (100 + (card_num_dealer * 50), 10))
                    card_num_dealer += 1

                pygame.display.update()

                pygame.time.delay(1000)
                round_over = True
        else:
            text = font.render('Bet: ' + str(bet), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height/8 - textRect.height)
            screen.blit(text, textRect)

            text = font.render('Money: ' + str(currentMoney), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height/8 + textRect.height/2)
            screen.blit(text, textRect)

        pygame.display.update()

        if round_over == True:
            gameState = "endscreen"

            if player_score > 21:
                end_screen("lose")
                text = font.render('You Busted!', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (screen_width/2, screen_height*3/4)
                screen.blit(text, textRect)

            elif dealer_score > 21:
                end_screen("win")
                currentMoney += bet * 2
                text = font.render('Dealer Busted!', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (screen_width/2, screen_height*3/4)
                screen.blit(text, textRect)

            elif player_score > dealer_score:
                end_screen("win")
                currentMoney += bet * 2
                text = font.render('You have more points!', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (screen_width/2, screen_height*3/4)
                screen.blit(text, textRect)

            elif dealer_score > player_score:
                end_screen("lose")
                text = font.render('Dealer has more points!', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (screen_width/2, screen_height*3/4)
                screen.blit(text, textRect)

            elif player_score == dealer_score:
                end_screen("tie")
                currentMoney += bet
                text = font.render('Its a tie!', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (screen_width/2, screen_height*3/4)
                screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def displayInstructions():
    runningInstructions = True
    background_img = pygame.image.load("images/instructions.png").convert()
    scaled_background = pygame.transform.scale(
        background_img, (screen_width, screen_height)
    )
    # Back button (using quit image as a placeholder)
    instructions_back_button = Button(20, 460, quit_img, 0.5)
    while runningInstructions:
        screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
        screen.blit(scaled_background, (0, 0))  # Draw blackjack background
        # Back to menu
        if instructions_back_button.draw(screen):
            runningInstructions = False  # Exit blackjack screen
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


# === Main Game Loop ===
game_state = "menu"
running = True

while running:
    if game_state == "menu":
        scaled = pygame.transform.scale(menu_background, (screen_width, screen_height))
        screen.blit(scaled, (0, 0))

        if play_button.draw(screen):
            game_state = "blackjack"
            deck = generateDeck()
            money = run_blackjack()
            game_state = "menu"  # Return to menu after blackjack

        if instruction_button.draw(screen):
            print("instructions")
            game_state = "instructions"
            displayInstructions()
            game_state = "menu"
        if quit_button.draw(screen):
            running = False

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
