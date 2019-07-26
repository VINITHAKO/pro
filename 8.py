import math
v3,k3=map(int,input().split())
de1=[]
bb1=list(map(int,input().split()))
for i in range(0,k3):
    l1,s1=map(int,input().split())
    sp1.append([l1,s1])
for i in sp1:
    ee1=i[0]-1
    mm1=i[1]-1
    print(math.gcd(bb1[ee1],bb1[mm1]))
