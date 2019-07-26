v,i=input().split()
char=abs(len(i)-len(v))
for g in range(len(v)):
  if(len(g)==1 and i[g] in a):
    break
  if(v[g]!=i[g]):
    char=char+1
print(char)

