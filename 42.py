vv1,vv2=map(int,input().split())
sk=list(map(int,input().split()))
if vv2==1:
  print(min(sk))
elif vv2==2:
  print(max(sk[0],sk[vv1-1]))
else:
  print(max(sk))
