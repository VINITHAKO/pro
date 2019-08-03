vin = int(input())
vv1 = list(map(int,input().split()))
kk,l = 0,[]
c1 = [x for x in range(1,vin+1)]
for i in vv1:
  if i in c1:
    c1.remove(i)
sb = 0
for i in range(0,vin-1):
  s = vv1[i]
  for j in range(i+1,vin):
    if s == vv1[j]:
      if s < c1[sb]:
        vv1[j] = c1[sb]
        kk += 1
      else:
        vv1[i] = b1[kh]
        kk += 1
      sb += 1
print(kk)
print(*vv1)
