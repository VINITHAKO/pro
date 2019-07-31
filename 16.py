#a
v1=int(input())
d=list(map(int,input().split()))
s=[1]*v1
for i in range(v1):
    if i==0:
        if d[i]>d[i+1]:
            s[i]=s[i]+s[i+1]
    elif i>0:
        if d[i]>d[i-1]:
            s[i]=s[i]+s[i-1]
print(sum(s))
