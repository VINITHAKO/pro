v=input()
flag=0
for i in range(0,len(v)-1):
  for j in range(i+1,len(v)):
    if v[i]<v[j]:
      flag=1
      print(v[j:])
      break
  if flag==1:
    break
else:
  print(v)
