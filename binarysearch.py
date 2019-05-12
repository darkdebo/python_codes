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
		    		    		
l=[1,23,225,455.]
print(binary_search(l,23))            
