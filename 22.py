v=int(input())
lis=list(map(int,input().split()))
k1=lis[1:v:2]
k2=lis[0:v:2]
if(sum(k1)>=sum(k2)):
    print(sum(k1))
else:
    print(sum(k2))
