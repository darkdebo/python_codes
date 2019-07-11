a=[1,2,3,4,5,6,4,5,5]
#print(a.index(1))
#for i in a:
    #print(f"value {i} and index isn {a.index(i)}")
    #print(id(i))

#for i in range(len(a)):
    #print(i,'------>',a[i])    

#print(a[0::2])
#b=a.copy() 
#print(b)
#b1=a
#print(b1)

del a[-1]
print(a)

print(len(a))

b=[1,2]

print(b)

print(a+b)

print(a*2)

if 0 not in a:
    print(True)



#print(str.split.__doc__)
print(1 in a)

print(any([1,0,0,0,0,0,0,0,0,0]))
print(all([1,1,1,1,1,1,1,1,11,1,1]))

print(max(a),min(a),sorted(a))

for i in range(10):
    print(a.append(i))

print(a)

print(a.index(5,2,))



#print(dir(list))