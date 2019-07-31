#a
    
from itertools import permutations
v, n = map(int, input().split())
y = list(map(int, input().split()))
for j in permutations(y, 2):
    if sum(j) == n:
        print('yes')
        break
else:
    print('no')
