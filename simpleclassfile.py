class add:
	#init constructor and instance variable
	def __init__(self,a,b):
		self.a=a
		self.b=b
	#instance method	
    def addd(self):
       return self.a+self.b	

a=add(4,5) #object creation
print(a.addd()) #call the instance method
#output 9
