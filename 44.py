m,n,o,p=map(int,input().split())
list1=list(map(int,input().split()))
list2=[]
for i in range(0,len(list1)):
    for j in range(i,len(list1)):
        for k in range(j,len(list1)):
            list2.append(n*list1[i]+o*list1[j]+p*list1[k])
print(max(list2))
