# Black Jack Game:

Welcome to 24/7 Blackjack! Blackjack, also known to some as twenty-one, is one of the most popular casino games around.

Blackjack is a card game that pits player versus dealer. It is played with one or more decks of cards.

1) Cards are counted as their respective numbers, face cards as ten, and ace as either eleven or one.
2) The goal of the game is to get a hand of cards that is as close to 21 as possible without going over.
3) Bet:In Blackjack, or 21, the player must decide what to bet before the hand. Click the chips to add them to your bet.Once you click "deal" your bet is set.
4) Game Play:
   a) Bet is set
   b) Once you click "deal" your bet is set, and two cards are dealt to the player face up and two cards are dealt to the dealer, one face up and one face down.
   c) Players can choose to "hit" (receive another card) or "stand" (keep their current hand).
   d) If a player's hand exceeds 21, they "bust" and lose the game.
   e) Once all players have finished their turn, the dealer reveals their face-down card and hits until their hand is worth at least 17
   f) If the dealer's hand exceeds 21, all remaining players win. Otherwise, players with a higher hand than the dealer win.

# Some points for Black Jack Game:

1) Set of cards : Game is played with one or more decks of cards. For Simplicity , we will design Game with one deck of card 2) Deck Of Cards: There are 4 suits ( Heart , spade , club and diamond).Each suits have 4 face cards( king,Jack,Queen,Ace) and 9 non Face cards ( 2,3 4,5,6,7,8,9,10)

Since , in black jack each Face Card has value 10 and ace has 11 or 1. So each suits will have value (2,3,4,5,6,7,8,9,10,10,10,10,11)

now Each suits are equal value

so value of card in one deck will be (2,3,4,5,6,7,8,9,10,10,10,10,11) * 4 times

We can present Deck Of Card with List value

3) We can shuffle the deck of cards using random.shuffle()

4) Betting : We are not going to deal with bet in this 1st version of game

5) deal:two cards are dealt to the player face up and two cards are dealt to the dealer, one face up and one face down.

we will write function for deal so that 2 cards are removed from deck of cards and given to players/dealer
6) We can use list to denotes dealers/players hand card


# when you play the above game via command

my_black_jack_game()

*******************************************************************
*******SKYLER CASINO WELCOMES ALL OF YOU FOR GAME OF LUCK *********
*                                                                 *
*******************************************************************


1. Play the Black Jack game
2. Exit the Game
Enter your choice: 1
Enter your Name :abhishek
How much money do you have (in rupees) ? : 2000
Welecome abhishek to Black jack Game
You have Total money in hand : Rs 2000.0
How Much You want to bet for this Game ? : 500
Before chooisng hit/stand : The player's card in  hand is : [3, 10]
Hey Player_1, Please choose your options : hit(1) or stand(2).....: 1
Player_1 loose as hand value exceed 21 , his cards in hand is : [3, 10, 10]
Your total money in hand at end of this game : 1500.0
1. Play the Black Jack game
2. Exit the Game
Enter your choice: 1
How Much You want to bet for this Game ? : 200
Before chooisng hit/stand : The player's card in  hand is : [10, 3]
Hey Player_1, Please choose your options : hit(1) or stand(2).....: 1
Player_1 loose as hand value exceed 21 , his cards in hand is : [10, 3, 10]
Your total money in hand at end of this game : 1300.0
1. Play the Black Jack game
2. Exit the Game
Enter your choice: 2
Thank You for your Game Time. Your Balance in HAND IS : 1300.0

Good BYE......See You Next Time
Going to exit the game
