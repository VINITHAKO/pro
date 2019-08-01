gowri,kur=map(int,input().split())
vin=[]
sel=0
for k in range(gowri):
    vin.append(list(map(int,input().split())))   
for k in range(gowri):
    for l in range(kur-1):
        for m in range(l+1,kur+1):
            if vin[k][l:m]==[1]*len(vin[k][l:m]):
                 if all(vin[p+k][l:m]==[1]*len(vin[p+k][l:m]) for p in range(len(vin[k][l:m])-1)):
                     if len(vin[k][l:m])>sel:
                        sel=len(vin[k][l:m])
if len(vin)==1 and len(vin[0])==1 and vin[0][0]==1:
    print(1)
for k in range(sel):
    print(*[1]*sel)
