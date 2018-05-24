#Q.1- Create two set using user defined values. 
#1. Calculate difference between two sets.
#2. Compare two sets.
#3. Print the result of intersection of two sets.

s1=set()
s2=set()
num1=int(input("Enter the number of elements in first set"))
for i in range(num1):
    n=int(input("Enter " +str(i+1)+ "value"))
    s1.add(n)
num2=int(input("Enter the number of elements in second set"))
for i in range(num2):
    n=int(input("Enter " +str(i+1)+ "value"))
    s2.add(n)
print("Difference of sets=",s1-s2)
print("Set comparison=", s1^s2)
print("Intersection=",s1&s2)
        
