from playsound import playsound
from termcolor import colored, cprint
import random



player_score = 0
dealer_score = 0 
total_hands = 0


#Dealing Cards
def deal_card(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# Calculate the total of each hand
def total(turn):
    total = 0 
    face = ['j', 'q', 'k']
    for card in turn:
        if card in range (1,11):
            total += card
        elif card in face:
            total += 10 
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# Check for winner 
def show_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0],dealer_hand[1]

#game loop

while True:
    print(colored("\n----------Black Jack ------------", "cyan"))
    game_start = input(colored("Do you want to Play: \n Yes or No", "cyan"))
    if game_start == "yes":
        print("lets get started")
    else:
        break

    player_active = True
    dealer_active = True    

    #Deck of cards / player hands
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k', 'a',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k', 'a',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k', 'a',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k', 'a']
    player_hand = []
    dealer_hand = []
    for x in range(2):
        deal_card(dealer_hand)
        deal_card(player_hand)    
    while player_active or dealer_active:
        playsound('Dealing.wav')
        print(colored("-----------------------------", 'green'))
        print("   Dealer has:",    show_dealer_hand(),"       ")
        print(colored("-----------------------------", 'green'))
        print(colored("-----------------------------", 'red'))
        print(f"You have {player_hand}. total of {total(player_hand)}")
        print(colored("-----------------------------", 'red'))
        
        if player_active:
            stay_hit = input(colored("1:Stay\n2:Hit\n  ", "blue"))
        if total (dealer_hand) > 16:
            dealer_active = False
        else: 
            deal_card(dealer_hand)
        if stay_hit == "1":
            player_active = False
        else:
            deal_card(player_hand)
        if total(player_hand) >= 21:
            break
        elif total(dealer_hand) >= 21:
            break
    if total(player_hand) == 21:
        print(f"\nYou have {player_hand} for a total of {total(player_hand)}\n and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        playsound('BlackJack.wav')
        print("BlackJack!")  

    elif total(dealer_hand) == 21:
        print(f"\nYou have {player_hand} for a total of {total(player_hand)}\n and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        playsound('Busted.mp3')
        print("BlackJack!") 

    elif total(player_hand) > 21:
        print(colored("---------------------------", 'red'))
        print(f"You have {player_hand}. total of {total(player_hand)}")
        print(colored("---------------------------", 'red'))
        playsound('Busted.mp3')
        print("you busted :( Dealer wins")

    elif total(dealer_hand) > 21:
        print(colored("--------------------------", 'green'))
        print(f"Dealer has {dealer_hand}. total of {total(dealer_hand)}")
        print(colored("--------------------------", 'green'))
        print(colored("--------------------------", 'red'))
        print(f"You have {player_hand}. total of {total(player_hand)}")
        print(colored("--------------------------", 'red'))
        print("Dealer busted :( You win") 

    elif 21 - total(dealer_hand) < 21 - total(player_hand):
        print(colored("--------------------------", 'green'))
        print(f"Dealer has {dealer_hand}. total of {total(dealer_hand)}")
        print(colored("--------------------------", 'green'))
        print(colored("--------------------------", 'red'))
        print(f"You have {player_hand}. total of {total(player_hand)}")
        print(colored("-------------------------", 'red'))
        print("dealer wins!")
        
    elif  21 - total(dealer_hand) > 21 - total(player_hand):
        print(colored("------------------------", 'green'))
        print("|    Dealer has:",    show_dealer_hand(),"       ")
        print(colored("--------------------------", 'green'))
        print(colored("--------------------------", 'red'))
        print(f"You have {player_hand}. total of {total(player_hand)}")
        print(colored("-------------------------", 'red'))
        print("You win")  
