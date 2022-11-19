k=(input("k:",))
li1=k.split(",")
li2=[]
for i in li1:
    li2.append(int(i))
m=max(li2)
n=2*m
sum1=0
a=0
b=1
li3=[]
while(sum1<n):
    li3.append(sum1)
    a=b
    b=sum1
    sum1=a+b
for i in li2:
    if i in li3:
        print(i,"is valid")
    else:
        print(i,"is not valid")
