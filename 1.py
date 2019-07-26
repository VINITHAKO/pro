v=int(input())
ek=[]
for i in range(0,v):
 ij=input()
 ek.append(ij)
dd=[]
for i in zip(*ek):
 if(i.count(i[0])==len(i)):
  dd.append(i[0])
 else:
  break
print(''.join(dd))
