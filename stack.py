print([2**i for i in range(10)])

a=[(x,y) for x in [10,20,30] for y in [1,2,3] if x!=y]

for i in a:
    print(type(i))

a=[1,2,3,'4',[1,2,5,512225,525,5]]

for i in a:
    print(i,'------->',a.index(i))