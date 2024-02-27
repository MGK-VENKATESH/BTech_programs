import math
def collide(x1,y1,r1,x2,y2,r2):
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
    center=dist/2
    r=r1+r2
    if center<=r:
        print("the balls are colliding")
    else:
        print("they are not colliding")
x1=int(input("enter the value of x1:"))
y1=int(input("enter the value of y1:"))
r1=int(input("enter the value of r1:"))
x2=int(input("enter the value of x2:"))
y2=int(input("enter the value of y2:"))
r2=int(input("enter the value of r2:"))
collide(x1,y1,r1,x2,y2,r2)
