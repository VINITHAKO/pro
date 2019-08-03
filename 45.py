v1 = int(input())
while v1%10==0:
    v1=v1//10
v1=str(v1)
d=v1[::-1]
if v1==d:
    print("yes")
else:
    print("no")
