'''
3. Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function

'''

def Euclidean_distance():
    x=int(input("enter the x value:"))
    y=int(input("enter the y value:"))

    x1=0
    y1=0
    x_value_orgin_to_axis=(x-x1)**2
    y_value_origin_to_axis=(y-y1)**2

    distance=(x_value_orgin_to_axis + y_value_origin_to_axis)**0.5
    print(distance)



Euclidean_distance()

'''
output-
enter the x value:2
enter the y value:3
3.605551275463989    



'''