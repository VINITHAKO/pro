c,d=map(int,input().split())
if c%10==0:
  c=str(c)
  e=0
  for i in range(len(c)-1,-1,-1):
    if c[i]=='0':
      e+=1
  if d<=e:
    print(c)
  else:
    c=c[:-e]
    c=c+'0'*d
    print(c)
elif 10%(c%10)==0:
  no=int('1'+'0'*d)
  while True:
    if no%c==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*d)
else:
  print(str(c)+d*'0')
