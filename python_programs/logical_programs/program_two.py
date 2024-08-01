'''
2. Coupon Numbers
a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
b. I/P -> N Distinct Coupon Number
c. Logic -> repeatedly choose a random number and check whether it's a new one.
d. O/P -> total random number needed to have all distinct numbers.
e. Functions => Write Class Static Functions to generate random number and to
process distinct coupons.



'''
import random

def coupon(N):

    for i in range(1,N+1):
        random_number=set()
        total_random_number=0

        while(len(random_number)<N):
            new_random_number=random.randint(1,N)
            total_random_number +=1
            random_number.add(new_random_number)

        return total_random_number,random_number
N=10
print(coupon(N))