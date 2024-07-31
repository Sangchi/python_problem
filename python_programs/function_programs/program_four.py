'''
4. Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)

'''
import math
def Quadratic():
    a=int(input("enter value of a:"))
    b=int(input("enter the value of b:"))
    c=int(input("enter the value of c:"))

    delta=(b*b)-(4*(a*c))
    print(delta)
    if delta < 0:
        print("The equation has no real roots.")
    else:
        root_one=(-b +math.sqrt(delta))/(2*a)
        print(f"root_one {root_one}")
        root_two=(-b -math.sqrt(delta))/(2*a)
        print(f"root_two {root_two}")

Quadratic()