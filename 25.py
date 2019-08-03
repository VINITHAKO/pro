v=int(input())
l=list(map(int,input().split()))
k=1
e=1
for i in range(1,v):
    if(l[i]>l[i-1]):
        k=k+1
    else:
        if(e<k):
            e=k
        k=1
if(e<k):
    e=k
print(e)
