#######Problem Statement-1###########
print("Welcome to Data Generator\n")
a='*'
print(a*20)
print("\nEnter The Binary Data to be Trasnmitted")
i_data=input("Enter Here:")     # Taking Input from the user
count=0
for items in i_data:             # Counting Number of one's
    if items=='1':
       count+=1

if count%2==0:                   # Checking If number of ones is even or odd
    i_data1=i_data+'1'

else:
    i_data1=i_data+'0'

print("Parity bit data:",i_data1)  # Printing The parity bit data
o_data=[]
j=0
k=0
o_data1=""
for items in i_data1:                      #bit Stuffing Logic Starts Here
    o_data1=o_data1+items




    o_data3=o_data1[j:]

    if '010' in o_data3:

        o_data1=o_data1+'0'

        j=k
        j+=2
        k+=1

    k+=1

o_datafinal=o_data1+'0101'                #Appending flag for end of the frame
print("Transmitting Data is:",o_datafinal)    #printing The final data