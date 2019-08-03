v=int(input())
k=list(map(int,input().split()))
g=int(v/2)
vaa=k[:a]
vb=k[a::]
if ((sum(vaa)//len(vaa))==(sum(vb)//len(vb))):
    print("yes")
else:
    print("no")
