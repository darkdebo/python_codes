#use of zip and dictionary
#
#name=["rohit","mohit"]
#roll_no=[24,21]
#age=[22,20]
#sample test

name=input("enter the names").split(",")
roll_no=input("enter the rooll no:").split(",")
age=input("enter the ages:").split(",")
z_object=list(zip(name,roll_no,age))
print(z_object)
key=["name","age","roll no"]
for i in z_object:
       print(dict(dict(zip(key,i))))

