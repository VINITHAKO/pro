vin,kow=map(int,input().split())
n=list(map(int,input().split()))
b=0
for i in n:
	if i<=(5-kow):
		b+=1
d=b//3
print(d)
