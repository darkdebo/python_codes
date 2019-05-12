def binary_search(l,ele_to_search):
	i=0
	while i<len(l):
		if l[(len(l)-1)//2]==ele_to_search:
			return f"index is {(len(l)-1)//2} and element is {ele_to_search}"
		elif ele_to_search>l[(len(l)-1)//2]:
		    if ele_to_search==l[(len(l)-1)//2+i]:
		    		return f"index is {(len(l)-1)//2+i} and element is {ele_to_search}"	
		elif ele_to_search<l[(len(l)-1)//2]:
		    if ele_to_search==l[(len(l)-1)//2-i]:
		    		return f"index is {(len(l)-1)//2-i} and element is {ele_to_search}"	
		else:
		    return f"not found -1"  
		i+=1      		
		    		    		
n=int(input("enter a lenghth of array need:"))
l=[]
i=0
while i<=n:
	i=int(input("enter element:"))
	l.append(i)
	i+=1
n1=int(input("what element want to search:"))
l=sorted(l)	
print(binary_search(l,n1))            
