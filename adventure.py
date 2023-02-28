"""
Name:adventure.py
Author:Rex
Date:2/27/23
Purpose: A game :)
"""

#------------------------------------------------
#GENERAL OUTLINE
#There will be 4 main rooms. (Start,Gambling room, BlackJack table, and final room)
    #starting room(prompt to move to room 1 or 2)

    #Gambler's room(Roll dice)
    #   |      (Gain or lose 5 coins)                     
    #   V                           
    #Black-jack table           
    #    |    (Lose 5 coins if not played, gain 5 coins if user wins)                      
    #    V
    #  Final room  
    #The user will start with 10 coins. To win the game, the user must have 10 coins remaining in order to go into the final room
#------------------------------------------------


#Import sleep,sys, and randint
from time import sleep
from random import randint
import sys
#Set loop variable


#Main function
def main():
    start()
    
#Start game
def start():
    #Start each run with 10 coins
    coins = 10

    print("\nBefore you lie two doors.")
    sleep(2)
    print("\nThey are listed as Door 1 and Door 2.")
    sleep(2)
    print("\nWhich do you choose? (1 or 2)")
    answer = int(input("> "))

    if answer == 1:
        gamber_route(coins)
    elif answer == 2:
        game_over("You touch the doorknob of door 2 and are ran over by a Midwestern Orgeon Trail Wagon")
    else:
        print("Error")
#Set up loop

#----------------------------------------------------------------------------------------------------------------------------------
def gamber_route(coins):
    print("\nYou open the door to a bussiling gambling hall, where the air is thick of smoke and\n"
          "full of intoxicated patreons throwing away their life savings.")
    sleep(3)
    print("\nWhile trying to navigate your way through the maze of slot machines, you stumble into a man rolling dice.")
    sleep(3)
    print('\nHe looks up and says," You feelin lucky, punk?"')
    sleep(3)
    print("\nYou try explaining that you aren't interested, but the man sits you down of a game of Roll'em. ")
    sleep(3)
    print("\nYou are asked to roll one of two dice.")
    print("\nThe one on the left seems newer, while the one on the right seems a lot more ragged and used.")
    sleep(3)
    print("\nIf your dice rolls higher than a four, then you win 5 coins. Else, you lose 5 coins.")
    sleep(3)
    print("\nWhich die do you choose? (L / R)")
    answer = input("> ").lower()
    #If left die, user wins
    if "l" in answer:
        print("The die rolls a 5.")
        sleep(2)
        print("You won 5 coins!")
        coins = coins + 5
        black_jack(coins)
    #If right die, user losses
    elif "r" in answer:
        print("The die rolls a 2.")
        sleep(2)
        print("You lose 5 coins.")
        coins = coins - 5
        black_jack(coins)
    else:
        print("Error")
#-------------------------------------------------------------------------------------------------------------------------------
def black_jack(coins):
    print(f"\nAfter that encounter, you stumble your way through the rest of the gambling hall with {coins} coins on you.")
    sleep(3)
    print('\nThis time, you trip over a man crying about something along the lines of the loss of a "401K". Whatever the heck that is...')
    sleep(3)
    print("\nYou also ended up tripping into an active black-jack game. Cards and poker chips go everywhere!")
    sleep(3)
    print("\nThe men at the table (really muscular by the way) set up the table again and ask you (menacingly) if you wanted to play a game.")
    print("\nIf you don't, you'll lose 5 coins")
    sleep(3)
    print("\nDo you play blackjack? (Y / N)")
    answer = input("> ").lower()
    #Determine to go into blackjack minigame
    if answer == "y":
        black_jack_minigame(coins)
    elif answer == "n":
        coins = coins - 5
        final_room(coins)
    else:
        print("Error")
#-----------------------------------------------------------------------------------------------------------------------------------
def black_jack_minigame(coins):
    #It's not actually calculating cards and values, but randomly adding a number to the the dealer's cards and the user's. (if user decides to hit)
    dealer_cards = 11
    user_cards = 14
    dealer_hit = randint(1,10)
    user_hit = randint(1,10)

    print("\nEither you have some guts, or can't afford to lose more coins...or both?")
    sleep(3)
    print('\nThe goal is simple: Do not go over 21, but get close to it. Else, the men at the table will "make you pay".' 
          'I do not think they are reffering to a payment...')
    sleep(3)
    print("\nYou are handed a King of spades and a 4 of hearts (14).")
    sleep(2)
    print("\nThe dealer's cards are a 8 of spades and a 3 of clubs (11).")
    sleep(2)
    print("\nWould you like to hit? (Take another card?) (Y / N)")
    answer = input("> ").lower()

    #User hits
    if answer == "y":
        user_cards = user_cards + user_hit
        dealer_cards = dealer_cards + dealer_hit
        #If user has a higher number than dealer
        if (user_cards > dealer_cards):
            #If the number is less than or equal to 21, user wins
            if (user_cards <= 21):
                print("\nYou won!\n The men let you leave the gambling hall and into the final room.") 
                coins += 5
                final_room(coins)
            #If number is greater than 21, user losses
            elif (user_cards > 21):
                print("\nBust! You lost!")
                game_over("The man next to you laughs and slugs you in the stomach. You have the wind knocked out of you and can't continue the journey.")
                sleep(5)
                print("You are then also ran over by a Midwestern Orgeon Trail Wagon.")
        #If user has a lower or same number as dealer
        elif (user_cards <= dealer_cards):
            #If number is greater than 21, user losses
            if (user_cards > 21):
                print("\nBust! You lost!")
                game_over("The man next to you laughs and slugs you in the stomach. You have the wind knocked out of you and can't continue the journey.")
                sleep(5)
                print("You are then also ran over by a Midwestern Orgeon Trail Wagon.")
            #If user cards is lower than or equal to 21, AND dealer cards are greater than 21
            elif (user_cards <= 21) and (dealer_cards > 21):
                print("\nThe dealer busts! You win! The men let you walk into the final room.")
                coins += 5
                final_room(coins)
            #If the dealer has a higher number
            elif (dealer_cards >= user_cards):
                print("Dealer wins!")
                game_over("The man next to you laughs and slugs you in the stomach. You have the wind knocked out of you and can't continue the journey.")
                sleep(5)
                print("You are then also ran over by a Midwestern Orgeon Trail Wagon.")   
    
    #User doesn't hit
    elif answer == "n":
        dealer_cards = dealer_cards + dealer_hit 

        if (dealer_cards > 21):
           print("\nThe dealer busts! You win! The men let you walk into the final room.")
           coins += 5
           final_room(coins) 
        elif (dealer_cards <= 21) and (dealer_cards > user_cards):
            print("Dealer wins!")
            game_over("The man next to you laughs and slugs you in the stomach. You have the wind knocked out of you and can't continue the journey.")
            sleep(5)
            print("You are then also ran over by a Midwestern Orgeon Trail Wagon.")
        elif (dealer_cards < user_cards):
             print("\nYou won!\n The men let you leave the gambling hall and into the final room.") 
             coins += 5
             final_room(coins)
    #Invalid input
    else:
        print("Error")
#--------------------------------------------------------------------------------------------------------------------------------------
def final_room(coins):
    print(f"\nYou have {coins} coins. You need 10 coins to get into the treasure room")
    print(f"Do you have enough? (Y / N)")
    answer = input("> ").lower()
    #User says they have enough
    if answer == "y":
        #If they don't have enough coins
        if (coins < 10):
            print("\nYou walk up to the final door, about to become the richest person alive. But then....")
            sleep(3)
            game_over("A Midwestern Orgeon Trail Wagon runs you over!")
        #User has enough coins and ends game
        elif(coins >= 10):
            print("\nYou walk to the door and open it. Inside there's....")
            sleep(2)
            print("\nNothing?")
            sleep(1)
            print("\nMaybe it was never about the treasure, but the friends we made along the way :)")
            print("---------------THE END--------------")
    elif answer == "n":
        print("\nWell, at least you're honest.")
        print("\nTell you what, do you want another go around? See if you can get enough coins? (Y / N)")
        answer = input("> ").lower()
        if answer =="y":
            start()
        elif answer == "n":
            print("R..Really? Okay fine! Be that way...")
            sleep(2)
            game_over("A Midwestern Orgeon Trail wagon runs you over!")
#---------------------------------------------------------------------------------------------------
#Display game over and run play_again() function.(Also give reason to GAME OVER)
def game_over(reason):
    print("GAME OVER\n" + reason)
    play_again()




#---------------------------------------------------------------------------------------------------
#Ask if the user wants to go agian
def play_again():
    
        go_again = input("Wanna play again? (Y / N)").lower()

        #If yes
        if go_again == "y":
            main()
        else:
            print("Done")
            sys.exit()

#----------------------------------------------------------------------------------------------------
#If standalone, run function
#Else, run as module
if __name__ == "__main__":
    main()
    



