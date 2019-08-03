p,s=map(int,input().split())

v=list(map(int,input().split()))

t=list(map(int,input().split()))

c=[]

g=0

for i in range(p):

    e=t[i]/v[i]

    c.append(e)

while s>=0 and len(c)>0:

    mindex=c.index(max(c))

    if s>=v[mindex]:

        g=g+t[mindex]

        s=s-v[mindex]

    v.pop(mindex)

    t.pop(mindex)

    c.pop(mindex)

print(g)
