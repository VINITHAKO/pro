v=int(input())
k=list(map(int,input().split()))
g=int(v/2)
vaa=k[:g]
vb=k[g::]
if ((sum(vaa)//len(vaa))==(sum(vb)//len(vb))):
    print("yes")
else:
    print("no")
