v1=int(input())
l=list(map(int,input().split()))
v2=[]
v3=1
for i in range(v1):
  n=l[i:]
  ans=len(n)
  for j in range(ans-1):
    if n[j]>0 and n[j+1]<0:
      v3=v3+1
    elif n[j]<0 and n[j+1]>0:
      v3=v3+1
    else:
      break
  v2.append(str(v3))
  v3=1
print(" ".join(v2))
