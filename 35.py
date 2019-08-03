v1=input()
s1=list(set(v1))
y=1
b=0
check=False
while True:
    ch=v1[b]
    for j in range(0,len(v1)-y):
        if ch in v1[j:j+y]:
            check=True
        else:
            check=False
            b+=1
            if b>=len(v1):
              b=0
              y+=1
            break
    if check==True:
        break
print(y)
