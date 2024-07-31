'''
5. Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value.


'''
nth_harmonic=0
number=int(input("enter the number:"))
for i in range(number+1):
    if(i !=0):
        nth_harmonic +=1/i

print(f"the nth harmonic value is{nth_harmonic}")

