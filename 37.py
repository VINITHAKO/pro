v1 = int(input())
N = [ int(x) for x in input().split()]
v1 = len(N)
if v1==1 :
    print(1)
   
cnt = 0
for i in range(1,v1-1) :
    if ((N[i] > N[i-1]) and (N[i] > N[i+1])) or ((N[i] < N[i-1]) and (N[i] < N[i+1])):
        cnt += 1
print(cnt)
