from sympy import *
#print(list(primerange(1,100)))
def consecutive_prime(start,stop):
   p=list(primerange(0,start+stop))

   c=0
   for i in range(start,stop):
       for i in p:

            if isprime(i):
                c=c+i
                if isprime(c) and start<=c<=stop:
                    print(c)

consecutive_prime(3,20) 
consecutive_prime(20,45)                   
    