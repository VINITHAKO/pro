#a
v,n = map(int,input().split())
t = list(map(int,input().split()))
c,m = 0,[]
for i in range(0,len(t)):
  v = i
  for p in range(0,len(t)):
    for l in range(0,n):
      if l == n-1:
        try:
          c += t[p+i]
        except IndexError:
            v = v-1
            c +=t[v]
      else:
        c += t[i]
    m.append(c)
    c = 0
for i in range(0,len(t),n):
  c = sum(t[i:i+n])
  m.append(c)
print(*sorted(set(m)))
