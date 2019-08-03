vi=int(input())
de=list(map(int,input().split()))
m=0
n=0
de.sort(reverse=True)
for i in de:
  de=m+i
  if n>de:
    m=de
  else:
    m=n
    n=de
print(m,n)
