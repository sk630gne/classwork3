#simple example of inhertance
class student:  
    def name(self):  
        print("name of student=raju")  
#child class Dog inherits the base class Animal  
class raju(student):  
    def study(self):  
        print("studying python")  
d = raju()  
d.study()  
d.name()
"""
output:-
studying python
name of student=raju
PS C:\Users\Dell\Documents\3rd classwork> 
"""