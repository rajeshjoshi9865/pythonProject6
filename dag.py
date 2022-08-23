import math
class A:
    def rectangle(self):
     b=int(input("enter one side of rectangle"))
     c = int(input("enter another side of rectangle"))
     a=b*c
     print(a)
     p=2*(b+c)
     print(p)
    def circle(self):
        r=int(input("enter a radius of circle"))
        a=3.14*r*r
        print(a)
        p=2*3.14*r
        print(p)
    def triangle(self):
        b = int(input("enter a side of triangle"))
        c = int(input("enter 2nd of triangle"))
        d = int(input("enter 3rd side of triangle"))
        p=b+c+d
        print(p)
        s=p/2
        a=math.sqrt(s*(s-b)*(s-c)*(s-d))
        print(a)
m=A()
m.rectangle()
m.circle()
m.triangle()

