'''
1. Gambler
a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
b. I/P -> $Stake, $Goal and Number of times
c. Logic -> Play till the gambler is broke or has won
d. O/P -> Print Number of Wins and Percentage of Win and Loss.


'''
import random

def gambler(stake,goal):
    cash=stake
    wins=0
    bets=0

    while cash>0 and cash<goal:
        bets +=1
        if random.random() <0.5:

            cash +=1
            wins +=1

        else:
            cash -=1

    win_averge=(wins/bets)*100
    loss_average=100-win_averge
    return wins,win_averge,loss_average

stake=int(input("enter the stake: "))
goal=int(input("enter the goal:"))

print(gambler(stake,goal))
