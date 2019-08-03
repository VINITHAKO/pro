#a
inp=int(input())

vv=0

mn=0

c=[]

while vv<90 and vv<inp:

  k=0

  for j in str(inp-vv):

    k+=int(j)

  if k+(inp-vv)==inp:

    mn+=1

    c.append(inp-vv)

  vv+=1

print(mn)

for vv in c:

  print(vv)
