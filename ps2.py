######Problem Statement-2########
def represent(list1):
    k=1
    str1="".join(lst)
    str2=str1[1:4]
    str3=str1[4:7]
    str4=str1[7:]
    print(str2)
    print(str3)
    print(str4)



a='-'
print(a*30)                                             #Showing the Welcome Message and Rules
print("Welcome to the Game")
print(a*30)
print("Rules of the Game:")
print("Player 1 will use only odd numbers[1-9]")
print("Player 2 will use only even numbers[1-9]")
lsts=[0]*20

lst=['0']*10                                                # Defining an empty list
i=0
while i<10:
    lst.append("")
    i+=1                                                #Inserting 9 empty elements in the list
i=1
k=0
d=[0]*200
index1=0
f=0
while i<7:
    print("Current State Of Matrix")
    represent(lst)
    while True:                                         # Taking the input from Player 1 and checking the boundary conditions
        pn1=int(input("Player 1 Enter the Position in which number is to be Entered:"))
        if pn1>0 and pn1<10:
            break
        else:
            print("Incorrect Input")
    while True:
        pp1=int(input("Player 1 Enter the  number which is to be Entered:"))
        if pp1>0 and pp1<10 and pp1%2!=0:
            break
        else:
            print("Incorrect Input")
    lst[pn1] = str(pp1)
    print("Current State Of Matrix")
    represent(lst)
    while True:                                          # Taking the input from player 2 and checking the boundary conditions
        pn2=int(input("Player 2 Enter the Position in which number is to be Entered:"))
        if pn2>0 and pn2<10:
            break
        else:
            print("Incorrect Input")
    while True:
        pp2=int(input("Player 2 Enter the  number which is to be Entered:"))
        if pp2>0 and pp2<10 and pp2%2==0:
            break
        else:
            print("Incorrect Input")

    lst[pn2]=str(pp2)
    print("Current State Of Matrix")
    represent(lst)
    lsts[pn1]=pp1
    lsts[pn2]=pp2
    #print(lsts)
    #---------------------------------------------------------
    #Checking the sum
    for count in range(1,4):
        d[index1]+=lsts[count]
    index1+=1
    #print("index1",index1)
    for count in range(4,7):
        d[index1]+=lsts[count]
        #print("hi")
    index1+=1
    for count in range(7,10):
        d[index1]+= lsts[count]
        #print("hi")
    index1+=1
    for count in range(1, 8, 3):
        d[index1]+= lsts[count]
        #print("hi")
    index1+=1
    for count in range(2, 9, 3):
        #print(count)
        d[index1]+= lsts[count]
        #print("hi")
    index1+=1
    for count in range(3, 10, 3):
        d[index1]+= lsts[count]
    index1+=1
    for count in range(1, 10, 4):
        d[index1]+= lsts[count]
        #print("hi")
    index1+=1
    for count in range(3, 8, 2):
        d[index1]+= lsts[count]
        #print("hi")
    index1+=1
    for items in d:
        if items>14 and items%2==0:
            f=1
            break
        elif items>14 and items%2!=0:
            f=2
            break
    if f==1 or f==2:
        break
    i+=2
    #print("i is",i)
#k+=1
# Checking the winner
if f==1:
    print("Player 2 is the winner")
elif f==2:
    print("PLayer 1 is the winner")