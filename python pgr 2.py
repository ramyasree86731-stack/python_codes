#funtions


def abc():
    print("hello world")
    print("123")

abc()


def add(a,b):
    print(a+b)

    
add(2,3)



#classes,object

class first:
    a = 78

    def method1(self):
        print("method1")
        

o1 = first()


print(o1.a)
o1.a = 80
print(o1.a)
o1.method1()

#inheritance concept

class Second(First):
    b = 45
    
    def Method2(self):
        print("Method2")
    
s1 = Second()
print(s1.b)
print(s1.a)


#print(o1.b)


#modules
#import cal

#cal.add(2,3)

#import cal as m

#m.sub(2,3)

#from cal import add

#add(4,5)

from cal import *

add(5,4)
sub(5,4)
mul(5,4)
div(5,4)



