v1=int(input())
d=[]
for m in range(0,v1):
    n=list(map(int,input().split()))
    for n in n:
        d.append(n)
print(*sorted(d),end="")
