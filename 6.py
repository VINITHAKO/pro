v1=int(input())
b=list(map(int,input().split()))
d=0
for i in range(0,v1-2):
	for j in range(1,v1-1):
		for k in range(2,v1):
			if(b[i]<b[j] and b[j]<b[k]):
				d+=1
print(d)
