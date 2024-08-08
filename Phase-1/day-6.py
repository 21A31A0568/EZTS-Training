#prime using constructor
'''class classn:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        c=0
        for i in range(2,int(self.n/2)+1):
            if self.n%i==0:
                c=c+1
                break
        if c>0:
            return ("no")
        else:
            return("yes")
o1=classn(20)
o2=classn(13)
print(o1.isprime())
print(o2.isprime())'''
#palindrome
'''class classp:
    def __init__(self,n):
        self.n=n
    def pal(self):
        r=self.n[::-1]
        if r==self.n:
            return("palindrome")
        else:
            return("not palindrome")
ob1=classp("manu")
ob2=classp("mom")
print(ob1.pal())
print(ob2.pal())'''
#prime and palindrome
'''class total:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        c=0
        for i in range(2,int(self.n/2)+1):
            if self.n%i==0:
                c=c+1
                break
        if c>0:
            return ("no")
        else:
            return("yes")
    def pal(self):
        s=str(self.n)
        r=s[-1::-1]
        if r==s:
            return("palindrome")
        else:
            return("not palindrome")
o1=total(22)
print(o1.isprime())
print(o1.pal())
o2=total(13)
print(o2.isprime())
print(o2.pal())'''
#n,p
'''class total:
    def __init__(self,n,p):
        self.n=n
        self.p=p
    def isprime(self):
        c=0
        for i in range(2,int(self.n/2)+1):
            if self.n%i==0:
                c=c+1
                break
        if c>0:
            print ("no")
        else:
            print("yes")
    def pal(self):
        s=str(self.p)
        r=s[-1::-1]
        if r==s:
            print("palindrome")
        else:
            print("not palindrome")
o1=total(22,"sas")
o1.isprime()
o2=total(14,"hello")
o2.pal()
o3=total(13,"sas")
o3.isprime()
o3.pal()'''
#public access specifier
'''class car:
    ms=0
    name=""
    def __init__(self):
        self.ms=200
        self.name="car"
    def drive(self):
        print(self.ms)
    def type(self):
        print(self.name)
c=car()
c.drive()
c.ms=300
c.drive()
c.type()'''
#private access specifier
'''class car:
    __ms=0
    name=""
    def __init__(self):
        self.__ms=200
        self.name="car"
    def drive(self):
        print(self.__ms)
    def type(self):
        print(self.name)
c=car()
c.drive()
c.__ms=300
c.drive()
c.type()'''
#super
'''class parent:
    def __init__(self):
        print("this is parent class")
class child(parent):
    def __init__(self):
        super().__init__()
        print("this is child class")
o=child()'''
#
'''class dob:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
    def display1(self):
        d={1:"january",2:"february",3:"march",4:"april",5:"may",6:"june"}
        print(d[self.m])

class details(dob):
    def __init__(self,n,a,d,m,y):
        self.n=n
        self.a=a
        self.d=d
        self.m=m
        self.y=y
        super().__init__(d,m,y)
    def display(self):
        print(self.n)
        print(self.a)
        print(self.d)
        print(self.m)
        print(self.y)
        super().__init__(self.d,self.m,self.y)
p=details("abc",23,24,2,2001)
p.display()
p.display1()'''
#multilevel inheritance
'''class parent:
    def func1(self):
        print("this is class 1")
class child(parent):
    def func2(self):
        print("this is class 2")
class child2(child):
    def func3(self):
        print("this is class 3")
o=child2()
o.func3()
o.func2()
o.func1()'''
#
'''class vehicle:
    def __init__(self,f):
        self.f=f
    def display3(self):
        print(self.f)
class motor:
    def __init__(self,cc):
        self.cc=cc
    def display2(self):
        print(self.cc)
class car:
    def __init__(self,n,cc,f):


    def display():
v=car("BMW","300cc","petrol")
v.display()'''
#abstraction
from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,area):
        pass
class rect(shape):
    def __init__(self, l,b):
        self.l=l
        self.b=b
    def area1(self):
        print(self.l*self.b)
    @abstractmethod
    def area3(self):
        print(self.l*self.l)
class sqare(shape):
    def __init__(self,l):
        self.l=l
    def area2(self):
        print(self.l*self.l)
o1=rect(2,4)
o2=sqare(2)
o1.area1()
o2.area2()
#o1=area3()

#exception handling 1
'''try:
    a,b=map(int,input().split())
    c=a//b
except:
    print("error")
else:
    print(c)
finally:
    print("Hello")
'''










