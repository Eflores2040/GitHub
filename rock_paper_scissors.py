#Edgar Flores

# September 27, 2017

# Rock, Paper, Scissors
import random
print("******************************")
print("Welcome to Rock Paper Scissors")
print("******************************")

com_wins = 0
player_wins = 0
while  com_wins <= 3 and  player_wins <= 3:
    player = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors :"))
    com = random.randint(0,2)
    if player == 0 and com == 0:
        print( "It's a draw! No points for anyone!")
        com_wins= com_wins + 0
        player_wins = player_wins + 0
    if player ==0 and com == 1:
        print( "Paper covers rock! The computer won this round!")
        com_wins = com_wins + 1
        player_wins = player_wins + 0

    if player == 0 and com == 2:
        print( "Rock crushes Scissors! You won that round!")
        com_wins = com_wins + 0
        player_wins = player_wins + 1
        
    if player == 1 and com == 0:
        print( "Paper covers rock! You won that round!")
        com_wins = com_wins + 0
        player_wins = player_wins + 1
        
    if player == 1 and com == 1:
        print( "It's a draw! No points for anyone!")
        com_wins= com_wins + 0
        player_wins = player_wins + 0
        
    if player == 1 and com == 2:
        print( "Scissors cuts Paper! The computer won that round!")
        com_wins = com_wins + 1
        player_wins = player_wins + 0
        
    if player == 2 and com == 0:
        print( "Rock crushes Scissors! The computer won that round!")
        com_wins = com_wins + 1
        player_wins = player_wins + 0
        
    if player == 2 and com == 1:
        print( "Scissors cuts Paper! You won that round!")
        com_wins = com_wins + 0
        player_wins = player_wins + 1

    if player == 2 and com == 2:
        print( "It's a draw! No points for anyone!")
        com_wins= com_wins + 0
        player_wins = player_wins + 0
    player_score = print("Player score is : %d " % player_wins)
    com_score = print("Computer score is : %d " % com_wins)
print("FINAL SCORE:")
print("\n\tPlayer score = %d" % player_wins)
print("\n\tComputer score = %d" % com_wins)
if player_wins == 4:
    print("************************************************")
    print("Congradulations, you won! Thank you for playing!")
    print("************************************************")
elif com_wins == 4:
    print("**********************************************")
    print("Sorry the computer won, better luck next time.")
    print("**********************************************")
