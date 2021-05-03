from random import randint
from math import sqrt,degrees,atan2
a = []; b = []; c1 = []; c2 = []; c3 = []; c4 = []; c5 = []
maxr = 0; minr = 150; sr = 0; maxug = 0;
n = int(input())  
for i in range(2*n):  
    new_element = randint(-100,100)
    a.append(new_element) 
for i in range(1,len(a),2):
    x=a[i-1]
    y=a[i]
    ug=round(degrees(atan2(y,x)),2)
    b.append(x)
    b.append(y)
    b.append(ug)
for i in range(2,len(b)-3,3):
    for j in range(2,len(b)-i-1,3):
            if b[j] > b[j+3]:
                b[j], b[j+3] = b[j+3], b[j]
                b[j-1], b[j+2] = b[j+2], b[j-1]
                b[j-2], b[j+1] = b[j+1], b[j-2]
for i in range(2,len(b),3):            
    if b[i]>maxug and b[i]<=90:
        maxug=b[i]
for i in range(2,len(b),3):        
    x=b[i-2]
    y=b[i-1]
    if x>0 and y>0 and b[i] == maxug:
        c1.append(x)
        c1.append(y)
        c1.append(b[i])
    elif x<0 and y>0:
        c2.append(x)
        c2.append(y)
        c2.append(b[i])
    elif x<0 and y<0:
        c3.append(x)
        c3.append(y)
        c3.append(b[i])
    elif x>=0 and y<0:
        c4.append(x)
        c4.append(y)
        c4.append(b[i])       
    elif x>=0 and y>=0 and b[i]!=maxug:
        c5.append(x)
        c5.append(y)
        c5.append(b[i])            
c=c1+c2+c3+c4+c5
for i in range(2,len(c),3):        
    x=c[i-2]
    y=c[i-1]
    r=sqrt(x*x+y*y)
    sr=sr+r
    if r>maxr:
        maxr=r
    if r<minr:
        minr=r        
    print('точка-',int((i/3)+1),'X',x,'Y',y,r)
print('maximum distance', maxr,'minimum distance',minr,'average distance',sr/n)
