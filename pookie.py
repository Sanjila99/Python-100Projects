pookie1=r"""

 /\_/\  
( -.- )
 > ^ <
"""
pookie2=r"""

 /\_/\  
( -.- )
 > 3 <
"""
pookie3=r"""

 /\_/\
( o.o )
 > ^ <
"""
pookie4=r"""

 /\_/\
( o.o )
 > ~ <
"""
def pookienation():
    choice=input("Enter your name  and i will print your pookie face:").lower()
    if choice=="dipshan":
        print(pookie4)
    elif choice=="sanjila":
        print(pookie1)
    elif choice=="spandana":
        print(pookie2)
    elif choice=="srijana":
        print(pookie3)
    else:
        print("You are not a pookie!!")

pookienation()