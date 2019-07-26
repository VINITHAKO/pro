from itertools import combinations
v,i=map(int,input().split())
b=len(str(v))
lst=list(combinations(str(v),b-i))
lst=sorted(lst)
print(*lst[0],sep='')
