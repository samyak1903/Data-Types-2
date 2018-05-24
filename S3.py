#Q.3- Write a program to find the product of all elements of a tuple. 
prod=1
l=[]
num=int(input("Enter the number of elements of tuple"))
for i in range(num):
    n=int(input("Enter the " +str(i+1)+ " value"))
    l.append(n)
t=tuple(l)
for i in t:
    prod=prod*i
print(prod)

    
    
