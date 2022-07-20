
#Python Multi-Level inheritance
#Multi-level inheritance is archived when a derived class inherits another derived class
class student:  
    def name(self):  
        print("student name is raju")  
#The child class Dog inherits the base class Animal  
class raju(student):  
    def study(self):  
        print("studying python")  
#The child class Dogchild inherits another child class Dog  
class rajuclass(raju):  
    def clas(self):  
        print("study in B.Tech")  
d = rajuclass()  
d.name()  
d.study()  
d.clas() 
"""
output
student name is raju
studying python
study in B.Tech
PS C:\Users\Dell\Documents\3rd classwork> 
"""

#Python Multiple inheritance
#Python provides us the flexibility to inherit multiple base classes in the child class.
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20)) 
"""
Output:

30
200
0.5
"""
# use of super keyword
class A:
    a=10
    b=20
    def __init__(self):
        print("a")
class b(A):
    a=4
    b=5
    def m2 (self):
        super().m1()
        print(self.a,self.b)
        print(super().a,super().b)
ob=b()
ob.m1()
ob.m2()

 