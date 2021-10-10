# Simulate soccer game
# 3 vs 3 players, each player has: defender, goalie, forward
# goal > defender > forward
# each player initialize w skill level (prob 40%-70%)
# if player fails ball passes to opposing player
# if the goalie fails to pass opposing forward get ball
# if the defender fails to pass opposing defender get ball
# if the forward fails to pass opposing goalie get ball
# when the forward scores a goal, the ball will start next round with opposing
# At the start of the game both goalies will be chosen
# first of 5 points
# output print sportcaster message
# email: eliot.kaplan@simspace.com
#Output: 
'''Goalie A attempts pass to defender A.
Defender A successfully receives pass!
Defender A attempts pass to forward A.
Defender B intercepts pass!
Defender B attempts pass to forward B.
Forward B successfully receives pass!
Forward B attempts shot on goal A!
GOAL! Team B score is 1.  Team A score is 0.
Play continues
Goalie A attempts pass to defender A.
…'''

import numpy as np

# Flip coin
start = np.random.randint(0,2)
if start = 0:
    start_A = 1
else:
    start_B = 1

skill = np.random.randint([0.4,0.8], size = 6)
teamA = {'goalie_a' : skill[0],
        'defender_a': skill[1],
        'forward_a': skill[2]
 }

teamB = {'goalie_b': skill[3],
         'defender_b': skill[4],
         'forward_b': skill[5]
         }

def pass_a(g_a, d_a, f_a, skill):
    skill = np.random.randint(0.4, 0.8)
    score_a = 0
    if start_A = 1:
        # 1 = has ball
        g_a = 1
        if skill[0] <= 0.6:
            d_a = 1*(0.4)
        else:
            d_a = 1*(0.6)
        
        if d_a = range(0.6,1.1):
            f_a = 1
            score_a += 1
            print(f"GOAL!  Team A score is {score_a}")







