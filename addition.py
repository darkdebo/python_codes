row,colum=input("enter the row and colums:").split(",")

row=int(row)
colum=int(colum)
mat=[[0 for i in range(colum)] for j in range(row)]
mat2=[[0 for i in range(colum)] for j in range(row)]


for i in range(row):
    for j in range(colum):
        mat[i][j]=int(input("netr the elements:"))

print("first matrix:",mat)


for i in range(row):
    for j in range(colum):
        mat2[i][j]=int(input("netr the elements:"))

print("second matrix:",mat2)        

for i in range(row):
    for j in range(colum):
        mat[i][j]+=mat2[i][j]  

print("sum of mat:",mat)        

for i in range(row):
    for j in range(colum):
        temp=mat[i][j]
        mat[j][i]=temp


print("transpose of mat1",mat)        