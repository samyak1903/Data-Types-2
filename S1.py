#Q.1- Take 20 integer inputs from user and print the following:
#(Use the basic logic of loops) 

#1. number of positive numbers
#2. number of negetive numbers
#3. number of odd numbers
#4. number of even numbers
#5. number of 0s

l=[]
p,n,o,e,z=0,0,0,0,0

for num in range(20):
    num=int(input("Enter the value"))
    l.append(num)
for no in l:
    if no>0:
        p=p+1
    else:
        n=n+1
    if no%2==0:
        e=e+1
    else:
        o=o+1
    if no==0:
        z=z+1
print("Number of positive integers=%d\nNumber of negative integers=%d" %(p,n))
print("Number of even numbers=%d\nNumber of even numbers=%d" %(e,o))
print("Number of zeros=",z)
    
