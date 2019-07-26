chatr=int(input())
vi=[]
kow=0
for h in range (0,chatr+1):
    kow=abs((2**h)-chatr)
    vi.append(kow)
pode=min(vi)
print(pode)
