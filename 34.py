m1,n1=map(int,input().split())
cost=0
v=[]
for i in range(m1):
      v.append(input())
for i in range(m1):
      for j in range(n1-1):
            if(v[i][j]!='R' and v[i][j+1]!='R'):
                  cost+=3
            elif(v[i][j]!='G' and v[i][j+1]!='G'):
                  cost+=5
print(cost)
