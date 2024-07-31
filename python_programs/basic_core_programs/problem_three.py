'''
3. Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.

'''

year=int(input("enter the year:"))
if year>=1000 and year<=9999:
    if(year%400==0 )or (year%100 !=0 and year%4==0 ):
        print(f"the{year}is leap year")

    else:
        print(f"{year} is not a leap year")

else:
    print(f"please enter valid creadiential")


