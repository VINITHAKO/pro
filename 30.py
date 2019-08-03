#a

v1=input()
dg=0
for i in range(0,len(v1)):
    kk=v1[0:i]+v1[i+1::]
    if int(kk)%8==0:
        dg=1
        break
if dg==1:
    print("yes")
else:
    print("no")
