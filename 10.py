vini=int(input())
vino=[int(o) for o in input().split(" ")]
vine=0
for i in range(vini):
      for j in range(i):
           if(vino[j]<vino[i]):
                vine+=vino[j]
print(vine)
