#a
vinit=input()
kay=map(int,input().split())
din=[]
for i in kay:
    cry=cin(i)
    din.append(cry)
sign=sorted(din)
sign.reverse()
for j in sign:
    print(int(j,2))
