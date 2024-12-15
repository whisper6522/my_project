n=int(input())
a=[]
b=[]
c=n
if n%2==0:
    k=1
    m=1
else:
    k=0
    m=0
while n>0:
    a.append(n%2)
    n=n//2
a=a[::-1]
a.append(k)
a.append(m)
print(*a)
for i in range(-len(a)+1,1):
    b.append(a[i+len(a)-1]*2**(-i))
print(sum(b))
i=0
while True:
    if c-2**i<0:
        break
    i+=1
print(sum(b)-i)
