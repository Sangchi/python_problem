'''
6. Factors
a. Desc -> Computes the prime factorization of N using brute force.
b. I/P -> Number to find the prime factors
c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
d. O/P -> Print the prime factors of number N.

'''

number = int(input("Enter the number to find its prime factors: "))
N = number
print("Prime factors:", end=" ")
while N % 2 == 0:
    print(2, end=" ")
    N //= 2

factor = 3
while factor * factor <= N:
    while N % factor == 0:
        print(factor, end=" ")
        N //= factor
    factor += 2

if N > 1:
    print(N)

