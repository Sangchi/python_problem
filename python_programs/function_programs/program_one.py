'''
1. 2D Array
a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
OutputStreamWriter to print the output to the screen.

'''

def twODarray():
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    twODarrays = []

    for i in range(m):
        row = []
        for j in range(n):
            result = i * j
            row.append(result)
        twODarrays.append(row)

    print("The 2D array is:")
    for element in twODarrays:
        print(element)

twODarray()


'''
output-

[0, 0, 0]
[0, 1, 2]
[0, 2, 4]


'''
