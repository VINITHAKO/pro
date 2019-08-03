c,d=map(int,input().split())
if c>d:
    c,d=d,c
vi=[]
for i in range(a):
    lis=list(map(int,input().split()))
    lis.sort()
    vi.append(lis)
for j in range(0,d):
    s=[]
    for i in range(0,c):
        s.append(vi[i][j])
    s.sort()
    p=0
    for i in range(0,c):
        vi[i][j]=s[p]
        r=r+1
for i in vi:
    print(*i)
