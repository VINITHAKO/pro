gowri,kur=map(int,input().split())
vin=[]
sel=0
for i in range(gowri):
    vin.append(list(map(int,input().split())))   
for i in range(gowri):
    for j in range(kur-1):
        for k in range(j+1,kur+1):
            if vin[i][j:k]==[1]*len(vin[i][j:k]):
                 if all(vin[p+i][j:k]==[1]*len(vin[p+i][j:k]) for p in range(len(vin[i][j:k])-1)):
                     if len(vin[i][j:k])>sel:
                        sel=len(vin[i][j:k])
if len(vin)==1 and len(vin[0])==1 and vin[0][0]==1:
    print(1)
for i in range(sel):
    print(*[1]*sel)
