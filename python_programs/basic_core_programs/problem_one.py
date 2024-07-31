'''1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
b. Logic -> Replace <<UserName>> with the proper name
c. O/P -> Print the String with User Name.'''

username=input("enter the input:")
if(len(username)>=3):
    print(f"hello {username}, how are you")

else:
    print("please enter miinum three charecter")
