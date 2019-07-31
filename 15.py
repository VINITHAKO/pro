#a
vinit=input()
kay=map(int,input().split())
din=[]
for k in kay:
    cry=cin(k)
    din.append(cry)
sign=sorted(din)
sign.reverse()
for l in sign:
    print(int(l,2))
