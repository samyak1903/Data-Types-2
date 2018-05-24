#Q.2-Sort the dictionary created in previous question according to marks. 

d={}
n=int(input("Enter the number pof elements to be added in the dictionary"))
for i in range(n):
    num=input("Enter name and marks as name:marks of " +str(i+1)+ " student")
    l=num.split(':')
    d[l[0]]=l[1]
print(sorted(d.values()))
      
    
    
                
