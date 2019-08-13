#a
vin,s=map(int,input().split())
k=[]
for i in range(s):
  k.append(list(map(int,input().split())))
cost=10000000
fin=0
for i in range(s):
  if k[i][0]==1:
    m=k[i][1]
    n=k[i][2]
    for j in range(i+1,s):
      if k[j][0]==m:
        m=k[j][1]
        n+=k[j][2]
    if n<cost and m==vin:
      cost=n
      fin+=1
if fin==0:
  print(-1)
else:
  print(cost)
