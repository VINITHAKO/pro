#a
v,i=map(int,input().split())
iv=list(map(int,input().split()))
ss=[]
for i in range(0,i):
     c,d=map(int,input().split())
     ss.append([c,d])
for i in range(i):
     lower=[i][0]
     upper=ss[i][1]
     x=sum(iv[lower-1:upper])
     print(x)
