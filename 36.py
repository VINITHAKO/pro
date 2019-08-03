v = int(input())
n = [ int(x) for x in input().split()]
v = len(n)
s = 0
for i in range(0,v-2):
    for j in range(i+1, v-1):
        for k in range(j+1, v):
            if n[i] > n[j] > n[k] :
                s =s+ 1
print(s)
