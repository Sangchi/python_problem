'''
4. Power of 2
a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
c. Logic -> repeat until i equals N.

'''
power=int(input("enter the number:"))
for i in range(power):
    if(i<2**power):
        powers=2**i
        print(f"the power of {i} is ={powers}")

    else:
        print("power limit is exceed")


        '''
        output-
        enter the number:10
        the power of 0 is =1
        the power of 1 is =2
        the power of 2 is =4
        the power of 3 is =8
        the power of 4 is =16
        the power of 5 is =32
        the power of 6 is =64
        the power of 7 is =128
        the power of 8 is =256
the power of 9 is =512

        
        
        '''





