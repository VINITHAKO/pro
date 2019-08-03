vx,vy=map(int,input().split())
ek=list(map(int,input().split()))
ek.sort()
ek.reverse()
vw=vy
j=0
for i in ek:
    if(vw>=i):
        no=int(vw/i)
        j=j+no
        vw=vw-no*i
    if vw==0:
        break
if(vw==0):
   print(j)
else:
   print("it is not posible to select coins ",S)  
