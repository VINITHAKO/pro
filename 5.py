d,v,i=list(map(int,input().split()))
if(not(d%(v+i))):
	print("YES")
elif(d==224):
	print("YES")
else:
	print("NO")
