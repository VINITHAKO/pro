a=int(input())
b=list(map(int,input().split()))
c=[]
d=1
for i in b:
  if i not in c:
    c.append(i)
for i in range(len(c)-1):
  if (c[i]<c[i+1]):
    d+=1
print(d)
