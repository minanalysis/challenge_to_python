# +
a=11
b=15 
c=1  

number=list(range(a,b+1))
number

count=0

for i in number: 
    if i%10 == c : 
        count = count+1
    if i//10 ==c : 
        count = count+1
        
print(count)



# +
a=111
b=211
c=2

number=list(range(a,b+1))
count=0 

for i in number:
    for j in range(len(str(i))):
        if str(i)[j]==str(c):
            count+=1
            
print(count)


# -
