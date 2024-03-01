https://medium.com/@iamabhishekforcommonuse/casino-black-jack-game-in-python-text-based-game-7b7e74bb1843

Casino Black Jack Game in python(Text Based game)

Before jumping into project, let’s understand this Black Jack Game
1) Cards are counted as their respective numbers, face cards as ten, and ace as either eleven or one.
2) The goal of the game is to get a hand of cards that is as close to 21 as possible without going over.
3) Bet for Game : In Blackjack,the player must decide what to bet before the hand. Add money for betting . Once you click "deal" your bet is set.
4) How this Game is being Played:
    a) Bet is set
    b) Once you click "deal" your bet is set, and two cards are dealt to the player face up and two cards are dealt to the dealer, one face up and one face down. 
    c) Players can choose to "hit" (receive another card) or "stand" (keep their current hand).
    d) If a player's hand exceeds 21, they "bust" and lose the game.
    e) Once all players have finished their turn, the dealer reveals their face-down card and hits until their hand is worth at least 17
    f) If the dealer's hand exceeds 21, all remaining players win. Otherwise, players with a higher hand than the dealer win.

Technical side
1)	Game is being played with pack of cards. Pack of Cards consist of one or more Deck of Cards. Each Deck of Cards has 4 suits( Heart , spade , club and diamond) . Each suits have 4 face cards( king,Jack,Queen and Ace) and 9  non Face cards ( 2,3 4,5,6,7,8,9,10)

Since, in blackjack each Face Card has value 10 and ace has 11 or 1. 

So, each suit will have value (2,3,4,5,6,7,8,9,10,10,10,10,11)

Note: As of now, we are taking Ace’s Value as 11 but will wisely decide as1 or 11 for winning case later in project flow.

We can represent this value via list ( King ,Queen ,Jack = 10 and Ace = 11)

Each suit will be represented by [ 2,3,4,5,6,7,8,9,10,10,10,10,11]

So, decks of card will be represented as

decks_card =  [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4

and so pack of cards

pack_of_cards = decks_card * 4

2)	For shuffeling the packs of card, we will use shuffle method of random module

random.shuffle(pack_of_cards)

3)	We will use list to represent  dealer’s hand and Player’s hand

    dealer_hand_card    = []
    player_1_hand_card  = []

4)	Once click deals:
Once you click "deal" your bet is set, and two cards are dealt to the player face up and two cards are dealt to the dealer, one face up and one face down. 
We will write click_deal function which will remove 2 cards from pack of card and add to player/dealer’s hand

# Function for click_deal

def click_deal(pack_of_cards, hand_card):        # Parameter: pack_of_cards and list of hand cards
    
    #Remove one card from deck and add that card to player/delaers hand
    card = pack_of_cards.pop()
    hand_card.append(card)
    #Remove 2nd card from deck and add that card to player/delaers hand
    card = pack_of_cards.pop()
    hand_card.append(card)
    
    return pack_of_cards,hand_card

5)	Player has to choose hit or stand, but before choosing hit/stand , player checks hid hand value

We will write a function to calculate Card’s value in hand

# function to sum the value of cards in players/dealers hand

def calc_hands_value(hand_card):
    
    sum_of_card_value = sum(hand_card)      # Add the value of all cards in hands
    
    if sum_of_card_value > 21:    # if sum of cards value exceed to 21
        if 11 in hand_card:       # if ace(11) present in hands
            sum_of_card_value -= 10      # treating ace as 1 because sum exceeds 21
            
    return sum_of_card_value


6)	As long as player’s hand value is less than 21, player can choose hit ot stand. Hit means he wants one card from pack of cards

We will write the function for hit

# function for hit : To receive another card from deck

def click_hit(pack_of_cards, hand_card):        # Parameter decks_card and list of hand cards
    #Remove one card from deck and add that card to player/delaers hand
    card = pack_of_cards.pop()
    hand_card.append(card)
    
    return pack_of_cards,hand_card


7)	Take the player’s option for hit/stand

        
        
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


8)	Check the player’s hand value and calculate bet amount and total amount to spend(player) will adjusted with winning/loosing amount

    if player_1_hand_value == 21 :
        
        print(f"Player_1 win as blackjack , his cards in hand is : {player_1_hand_card}")  
        
        total_amount_to_spend +=  ( game_bet * 1.5 )
        
        return "Player win" , total_amount_to_spend
        
    if player_1_hand_value > 21 :
        print(f"Player_1 loose as hand value exceed 21 , his cards in hand is : {player_1_hand_card}")
        
        total_amount_to_spend -=  game_bet 
        
        return "Player loose" , total_amount_to_spend


9)	After completion of player's hand,it's dealer's turn  now, dealer hits until their hand is worth at least 17

Based on dealer’s hand value, bet money calculated and total amount of player adjusted.

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








