vi=int(input())
v1=2**vi
list1=[]
for i in range(0,v1):
    l=bin(i)[2:].zfill(vi)
    if(len(l)<len(bin(2**vi-1)[2:])):
        list1.append([l.count("1"),l])
    else:
        list1.append([l.count("1"),l])
list1.sort()
for i in range(len(list1)):
    print(list1[i][1])
