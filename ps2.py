######Problem Statement-2########

a='-'
print(a*30)                                             #Showing the Welcome Message and Rules
print("Welcome to the Game")
print(a*30)
print("Rules of the Game:")
print("Player 1 will use only odd numbers[1-9]")
print("Player 2 will use only even numbers[1-9]")

lst=[]                                                  # Defining an empty list
i=1
while i<10:
    lst.append("")
    i+=1                                                #Inserting 9 empty elements in the string
i=0
while i<9:
    while True:                                         # Taking the input from Player 1 and checking the boundary conditions
        pn1=int(input("Player 1 Enter the Position in which number is to be Entered:"))
        if pn1>0 and pn1<10:
            break
        else:
            print("Incorrect Input")
    while True:
        pp1=int(input("Player 1 Enter the  number which is to be Entered:"))
        if pp1>0 and pp1<10:
            break
        else:
            print("Incorrect Input")
    while True:                                          # Taking the input from player 2 and checking the boundary conditions
        pn2=int(input("Player 2 Enter the Position in which number is to be Entered:"))
        if pn2>0 and pn2<10:
            break
        else:
            print("Incorrect Input")
    while True:
        pp2=int(input("Player 2 Enter the  number which is to be Entered:"))
        if pp2>0 and pp2<10:
            break
        else:
            print("Incorrect Input")
    lst[pp1]=pn1
    lst[pp2]=pn2
    i+=1
