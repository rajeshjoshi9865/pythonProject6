class A:
    #a = input("enter a destination you want to reach")
    def __init__(self,a):
        self.a=a
class b(A):
    def money(self):
        print("have u paid the money")
        b=int(input("if yes say 1 else 0"))
        if(b==1):
            print("your booking is sucessful")
        else:
            print("not sucessful")
c=b(input("enter a destination you want to reach"))
c.money()
