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
for items in i_data:
    o_data.append(items)
    #print(o_data)
    o_data1="".join(o_data)
    #print(o_data1)
    o_data3=o_data1[j:]
    print(o_data3)
    if '010' in o_data3:
        print("hi")
        #o_data2=o_data1+'0'
        #o_data1=o_data2
    j+=1
        #print(o_data2)
#print(o_data2)