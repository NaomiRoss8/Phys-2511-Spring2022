# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 01:34:50 2022

@author: naomi
"""
def roll():
    import random
    num = [1, 2, 3, 4, 5, 6]
    dice = random.choice(num)
    return dice

def game():
    print("Let's begin the game!")
    print("Player 1's score: 0")
    print("Player 2's score: 0")
    
    player1 = 0
    player2 = 0
    
    while player1 < 100 or player2 < 100:
        number = roll()
        print("Player 1's total score:", player1)
        print("Player 1 has rolled:", number)
        player1 += number
        print("Player 1's new total score:", player1)
        if player1 > 100:
            print("Player 1 wins! Total Score is:", player1)
            break
        if player1 % 3 ==0:
            player1 += 5
            print("Player1 landed on a special square and may move an additional 4 spaces! Their new score is:", player1)
            if player1 > 100:
                print("Player 1 wins! Congratulations!! Their score is:", player1)
                break
        print("")
        number2 = roll()
        print("Player 2's total score:", player2)
        print("Player 2 has rolled:", number)
        player2 += number
        print("Player 2's new total score:", player2)
        if player2 > 100:
            print("Player 2 wins! Total Score is:", player2)
            break
        if player2 % 3 ==0:
            player2 += 5
            print("Player2 landed on a special square and may move an additional 4 spaces! Their new score is:", player2)
            if player2 > 100:
                print("Player 2 wins! Congratulations!! Their score is:", player2)
                break
            print("")
            print("")
game ()
