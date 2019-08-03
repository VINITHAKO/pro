vin=int(input())
v1=list(map(int,input().split()))
v1.sort()
sin=0
s1=0
for i in range(len(v1)):
    if v1[i]>=sin:
        s1=s1+1
    sin=sin+v1[i]
print(s1)
