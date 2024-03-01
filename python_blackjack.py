#Importing Module

import random

# commenting the below Data structure as we are redefining under play_black_jack_game function
'''

# Data structure of decks of card

decks_card = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4

# let's start with one player and dealer

dealer_hand_card    = []
player_1_hand_card  = []

'''

# Function for click_deal

def click_deal(pack_of_cards, hand_card):        # Parameter decks_card and list of hand cards
    
    #Remove one card from deck and add that card to player/delaers hand
    card = pack_of_cards.pop()
    hand_card.append(card)
    #Remove 2nd card from deck and add that card to player/delaers hand
    card = pack_of_cards.pop()
    hand_card.append(card)
    
    return pack_of_cards,hand_card

# function to sum the value of cards in players/dealers hand

def calc_hands_value(hand_card):
    
    sum_of_card_value = sum(hand_card)      # Add the value of all cards in hands
    
    if sum_of_card_value > 21:    # if sum of cards value exceed to 21
        if 11 in hand_card:       # if ace(11) present in hands
            sum_of_card_value -= 10      # treating ace as 1 because sum exceeds 21
            
    return sum_of_card_value


# function for hit : To receive another card from deck

def click_hit(pack_of_cards, hand_card):        # Parameter decks_card and list of hand cards
    #Remove one card from deck and add that card to player/delaers hand
    card = pack_of_cards.pop()
    hand_card.append(card)
    
    return pack_of_cards,hand_card
    
    
# function to play the game

def play_black_jack_game(total_amount_to_spend):
    
    # step_1  : Take one decks of card
    
    decks_card = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    
    # Step_2 : Take four decks of card to play the game(Casino uses 4-6 sets of 52 card)
    
    pack_of_cards = decks_card * 4
    
    # Step_3  : let's start with one player and dealer
    
    dealer_hand_card    = []
    player_1_hand_card  = []
    
    # step_4 : Shuffle the packs of card
    
    random.shuffle(pack_of_cards)
    
    # Step_5 : Add bet  : We are not implementing it as of now
    game_bet = float(input("How Much You want to bet for this Game ? : "))
    
    # Step_6 : click deals
    
    #Give 2 cards to player_1
    
    pack_of_cards , player_1_hand_card = click_deal(pack_of_cards, player_1_hand_card)
    
    #Give 2 cards to dealers
    
    pack_of_cards , dealer_hand_card = click_deal(pack_of_cards, dealer_hand_card)
    
    # Step_7 : Player has to choose hit or stand
    #option = input("Hey Player_1, Please choose your options : hit(1) or stand(2).....: ")
    
    #Before choosing hit/stand , player check his card and value
    
    player_1_hand_value = calc_hands_value(player_1_hand_card)
       
    while player_1_hand_value < 22:
        print(f"Before chooisng hit/stand : The player's card in  hand is : {player_1_hand_card}")
        
        #Calculate player's hand
        
        option = input("Hey Player_1, Please choose your options : hit(1) or stand(2).....: ")
        
        option = option.lower()
        
        if option == '1' or option == 'hit' :
            #To receive another card from deck
            
            pack_of_cards , player_1_hand_card = click_hit(pack_of_cards, player_1_hand_card) 
            player_1_hand_value = calc_hands_value(player_1_hand_card)
            
        elif option == '2' or option == 'stand' :
            
            break
        else :
            print(f"You have entered wrong choice, try again\n")
            
    #step_8 : Calculate player's hand
    
    player_1_hand_value = calc_hands_value(player_1_hand_card)
    
    if player_1_hand_value == 21 :
        
        print(f"Player_1 win as blackjack , his cards in hand is : {player_1_hand_card}")  
        
        total_amount_to_spend +=  ( game_bet * 1.5 )
        
        return "Player win" , total_amount_to_spend
        
    if player_1_hand_value > 21 :
        print(f"Player_1 loose as hand value exceed 21 , his cards in hand is : {player_1_hand_card}")
        
        total_amount_to_spend -=  game_bet 
        
        return "Player loose" , total_amount_to_spend
    
    # After completion of player's hand,it's dealer's turn  now
    
    # Step_9 : Calculate dealer's hand
    
    dealer_hand_value = calc_hands_value(dealer_hand_card)
    
    # Step_10 : dealer hits until their hand is worth at least 17
    
    while dealer_hand_value <  17 :
        
        # Dealers clicked hit
        pack_of_cards , dealer_hand_card = click_hit(pack_of_cards, dealer_hand_card)
        
        # Calculate dealer hand value
        dealer_hand_value = calc_hands_value(dealer_hand_card)
        
    if dealer_hand_value > 21 :
        print(f"Dealer loose as hand value exceed 21 , his cards in hand is : {dealer_hand_card}")
        
        total_amount_to_spend +=  game_bet  
        
        return "Dealer loose" , total_amount_to_spend
    
    if dealer_hand_value > player_1_hand_value :
        print(f"Dealer win as hand value is more than players hand va;ue , dealer's card : {dealer_hand_card}  , player_1's card : {player_1_hand_card}")
        total_amount_to_spend -=  game_bet
        return "Dealer win" , total_amount_to_spend
    
    elif dealer_hand_value < player_1_hand_value :
        print(f"Player win as hand value is more than Dealers hand va;ue , dealer's card : {dealer_hand_card}  , player_1's card : {player_1_hand_card}")
        total_amount_to_spend +=  game_bet 
        return "Player win" , total_amount_to_spend
    
    else :
        print(f"Draw , dealer's card : {dealer_hand_card}  , player_1's card : {player_1_hand_card}")
        
        return "Draw" , total_amount_to_spend

        

# Define the function once your quiz game starts
def my_black_jack_game():
    print("*******************************************************************")
    print("*******SKYLER CASINO WELCOMES ALL OF YOU FOR GAME OF LUCK *********")
    print("*                                                                 *")
    print("*******************************************************************")
    print("\n")
    
    isFirstTime = True
    # Take user input to proceed
    while True:
        my_game_menu_display()    # Display the menu
        choice = input("Enter your choice: ")
        if choice == '1':
            if isFirstTime :                
                pname = input("Enter your Name :")
                total_amount_to_spend = float(input("How much money do you have (in rupees) ? : "))
                welcome_player(pname,total_amount_to_spend)
                
            if total_amount_to_spend > 100 :
                game_status, total_amount_to_spend = play_black_jack_game(total_amount_to_spend)    # Play the game
                print(f"Your total money in hand at end of this game : {total_amount_to_spend}")
                if isFirstTime : 
                    isFirstTime = False                    
                
                continue
            else :
                print("You do not have enough money in hand to play")
                final_message(total_amount_to_spend)
                my_game_exit()    # Terminate the game
                break
        elif choice == '2':
            final_message(total_amount_to_spend)
            my_game_exit()    # Terminate the game
            break
        else:
            print("You have choosen wrong choice, please use '1' or '2' ")
            continue
            

def final_message(total_amount_to_spend):
    print(f"Thank You for your Game Time. Your Balance in HAND IS : {total_amount_to_spend}\n")
    
    print("Good BYE......See You Next Time")
    

def welcome_player(pname , total_amount_to_spend):
    print(f"Welecome {pname} to Black jack Game")
    print(f"You have Total money in hand : Rs {total_amount_to_spend}")
    
# Function to display the quiz menu
def my_game_menu_display():
    print("1. Play the Black Jack game")
    print("2. Exit the Game")

# Exit the quiz

def my_game_exit():
    print("Going to exit the game")

# Play the game
my_black_jack_game()