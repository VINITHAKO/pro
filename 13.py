#a
v, d = [int(i) for i in input().split()]
l = []
vin = [int(i) for i in input().split()]
for _ in range(d):
    m, k = [int(i) for i in input().split()]
    l.append(min(vin[m-1:k]))
for i in l:
    print(i)
