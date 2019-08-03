v1=input()
s1=list(set(p1))
y=1
b=0
check=False
while True:
    ke=p1[b]
    for j in range(0,len(p1)-y):
        if ke in p1[j:j+y]:
            check=True
        else:
            check=False
            b+=1
            if b>=len(p1):
              b=0
              y+=1
            break
    if check==True:
        break
print(y)
