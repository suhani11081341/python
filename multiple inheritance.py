class Student:
    def __init__(self,rollno,name):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("student class detail",self.rollno,self.name)
class Test:
    def __init__(self,marks1,marks2):
       
        self.marks1=marks1
        self.marks2=marks2
    def display(self):
        
        print("Test class detail",self.marks1,self.marks2)
class Total(Test,Student):
    def __init__(self):
        Student.__init__(self,11081341,"suhani")
        Test.__init__(self,90,80)
        self.total_=self.marks1+self.marks2
    
    def display(self):
        Student.display(self)
        Test.display(self)
        print("totalling class ",self.total_)

s=Total()
(s.display())
        
