v1,v2=map(str,input().split())
vin=0
if len(v1)>len(v2):
  v1,v2=v2,v1
s=0
while s<len(v1):
  vin+=(ord(v2[s])-ord(v1[s]))
  s+=1
for s in range(s,len(v2)):
  vin+=ord(v2[s])-ord('a')+1
print(vin)
