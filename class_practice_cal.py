class calculator:
       def __init__(self,*args):#constructor
              self.args=args#instance variables


       def ADD(self):#instance method
              s=0
              for i in self.args:
                     s=s+i
              return s
       @classmethod
       def myname(cls):#class method
              print("class method called")
              return 1


c=calculator(5,6,4)
print(c.ADD())
print(calculator.myname())
