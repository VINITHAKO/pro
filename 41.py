c1,d1=input().split()
c1=int(c1)
d1=int(d1)
m2=''
n1=2
if(c1+d1<=3):
    for i in range(0,c1+d1):
        if(i%2!=0):
            m2=m2+'0'
        else:
            m2=m2+'1'
else:    
    for i in range(0,c1+d1):
        if(i==n1):
            m2=m2+'0'
            if(n1==d1):
                n1=n1+2
            else:
                n1=n1+3
        else:
            m2=m2+'1'
y1=len(m2)-1
if(int(m2[y1])==0):
    print('-1')
elif c1==1 and d1==2: print("011")
else:
    print(m2)
