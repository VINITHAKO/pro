v,i=input().split()
char=abs(len(i)-len(v))
for g in range(len(v)):
  if(len(i)==1 and i[g] in v):
    break
  if(v[g]!=i[g]):
    char=char+1
print(char)

