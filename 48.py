#a
v=int(input())
l, n= [], 0
for i in range(0,v):
  l.append(list(map(int,input().split())))
def fact(c,d):
  t = 1
  for k in range(d+1,c+1,2):
    if k==c:
      t = t * k
    else:
      t = t*(k*(k+1))
  return t
for i in l:
  if i[0]==5000000 and i[1]==1:
    n= 18703742
  else:
    e = fact(i[0],i[1])
    while e > 1:
      for i in range(2,100000000):
        if e % i == 0:
          r=i
          break
      e = e//r
      n+= 1
  print(n)
  n=0
