'''
1=s
-1=w
0=g
'''

import random

computer=random.choice([-1, 0, 1])
youstr=input("enter your choice: ")

youdict={"s":1,"w":-1,"g":0}
reverseddict={1:"Snake",-1:"Water",0:"Gun"}
you=youdict[youstr]

print(f"your choice {reverseddict[you]}\ncomputer choice{reverseddict[computer]}")

if(computer==you):
    print("Draw")
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("computer win")
    elif(computer==0 and you==1):
        print("computer win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==1 and you==-1):
        print("computer win")
    elif(computer==1 and you==0):
        print("you win")
    else:
        print("something went wrong")