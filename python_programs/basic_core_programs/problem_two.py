'''2. Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails'''
import random 
flip_coin=int(input("enter how many time flip coin:"))
if(flip_coin>=1):
    head=0
    tail=0
    for i in range(flip_coin):
        if random.random() < 0.5:
            head +=1

        else:
            tail +=1


    head_percentage=(head/flip_coin)*100
    tail_percentage=(tail/flip_coin)*100

    print(f"the head percentage is {head_percentage}")
    print(f"the tail percent is {tail_percentage}")


    '''
    output-

    enter how many time flip coin:10
    the head percentage is 70.0
    tail percent is 30.0

    
    
    
    '''
    
