#Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
s="MISSISSIPPI"
d={}
l=list(s)
p=[]
for i in l:
    p1=l.count(i)
    d[i]=p1
print(d)
