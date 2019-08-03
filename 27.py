v1,s1=map(int,input().split())
v=list(map(int,input().split()))
t=list(map(int,input().split()))
c=[]
g=0
for i in range(p1):
    e=t[i]/v[i]
    c.append(x)
while s1>=0 and len(c)>0:
    mindex=c.index(max(c))
    if s1>=v[mindex]:
        g=g+t[mindex]
        s1=s1-v[mindex]
    v.pop(mindex)
    t.pop(mindex)
    c.pop(mindex)
print(g)
