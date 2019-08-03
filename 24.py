vi=int(input())
mn=2**vi
list1=[]
for i in range(0,mn):
    n=bin(i)[2:].zfill(vi)
    if(len(n)<len(bin(2**vi-1)[2:])):
        listn.append([1.count("1"),1])
    else:
        listn.append([l.count("1"),l])
list1.sort()
for i in range(len(list1)):
    print(list1[i][1])
