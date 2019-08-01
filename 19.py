vin=int(input())
gowr=[]
din=[]
for i in range(vin):
    gowr.append(list(map(int,input().split())))
for kur in gowr:
    for num in kur:
        din.append(num)
din.sort()
for i in din:
    print(i,end=' ')
