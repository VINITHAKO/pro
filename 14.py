#a
vinit,kura=map(int,input().split())
list1=list(map(int,input().split()))
vinit=[]
list1.insert(0,0)
for e in range(kura):
     din=[]
     k=0
     cc,dd=map(int,input().split())
     for i in range(cc,dd+1):         
         k^=list1[i]     
     vinit.append(k)
for e in vinit:
     print(e)
