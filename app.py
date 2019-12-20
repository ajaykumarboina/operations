#program to perform append operation on lists
a=[1,2,3,4,5,6,7,8]
b=[9,10,11,12,13,14,15]
print("A=",a)
print("B=",b)
for i in range(0,len(b)):
    a.append(b[i])
print("New list=",a)
#Program to append single element to an array
import numpy as np
c= []
d= int(input("\nEnter size of array to create array:"))
for i in range(d):
	print("Enter element",i,":")
	c.append(int(input()))
c= np.array(c)
print("The array is:",c)
y=int(input("Enter a number to append to the above array:"))
c=np.append(c,y)
print("The modified array is:",c)

	

 
