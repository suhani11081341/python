print("calling type 1")
class time:
    
    def __init__(self):
        self.hr=7
        self.min=40
    def getdata(self,r):
        self.r=r
        
    def add(self,p):
        min =self.min+p.min
        self.min=min%60
        self.hr+=p.hr+int(min/60)
        print(self.hr,self.min)
      
    def display(self):
        print(self.hr,"hr",self.min,"min")
        
t1=time()
t2=time()
t1.add(t2)
t1.display()

print("calling type 2")
class time:
    
    def __init__(self):
        self.hr=7
        self.min=40
    def getdata(self,r):
        self.r=r
        
    def add(self,p):
        temp=time()
        min =self.min+p.min
        temp.min=min%60
        temp.hr+=p.hr+int(min/60)
       
        return temp
      
    def display(self):
       return (self.hr,"hr",self.min,"min")
        
t1=time()
t2=time()
t3=t1.add(t2)
print(t1.display(),"+",t2.display())
t3.display()

print("calling type 2+")
class time:
    
    def __init__(self):
        self.hr=7
        self.min=40
    def getdata(self,r):
        self.r=r
        
    def add(self,p,q):
        
        min =q.min+p.min
        self.min=min%60
        self.hr=p.hr+int(min/60)+q.hr
        
    def display(self):
       return (self.hr,"hr",self.min,"min")
        
t1=time()
t2=time()
t3=time()
t3.add(t1,t2)
print(t1.display(),"+",t2.display())
print(t3.display())


print("calling type 3")
class time:
    
    def __init__(self):
        self.hr=7
        self.min=40
    def getdata(self,r):
        self.r=r
        
    def add(self,p,q):
        
        min =q.min+p.min
        self.min=min%60
        self.hr=p.hr+int(min/60)+q.hr
        return self
    def display(self):
       return (self.hr,"hr",self.min,"min")
        
t1=time()
t2=time()
t3=time()
t3=t3.add(t1,t2)
print(t1.display(),"+",t2.display())
print(t3.display())

print("calling type 4")
class time:
    
    def __init__(self):
        self.hr=7
        self.min=40
    def getdata(self,r):
        self.r=r
        
    def add(self,p,q):
        
        min =q.min+self.min
        self.min=min%60
        self.hr+=int(min/60)+q.hr
        return self
    def display(self):
       return (self.hr,"hr",self.min,"min")
        
t1=time()
t2=time()
t3=time()
t3=t1.add(t1,t2)
print(t1.display(),"+",t2.display())
print(t3.display())

print("calling type 5")
class time:
    
    def __init__(self):
        self.hr=7
        self.min=40
    def getdata(self,r):
        self.r=r
        
    def add(self,p,q):
        
        min =p.min+self.min
        self.min=min%60
        self.hr+=p.hr+int(min/60)
        return self
    def display(self):
       return (self.hr,"hr",self.min,"min")
        
t1=time()
t2=time()
t3=time()
t3=t2.add(t1,t2)
print(t1.display(),"+",t2.display())
print(t3.display())
