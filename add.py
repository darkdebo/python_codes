row,colum=input("enter the row and colums:").split(",")

row=int(row)
colum=int(colum)
mat=[[0 for i in range(colum)] for j in range(row)]
mat2=[[0 for i in range(colum)] for j in range(row)]
result=[[0 for i in range(colum)] for j in range(row)]


for i in range(row):
    for j in range(colum):
        mat[i][j]=int(input("netr the elements:"))

print("first matrix:",mat)


for i in range(row):
    for j in range(colum):
        mat2[i][j]=int(input("netr the elements:"))

for i in range(row):
    for j in range(colum):
        for k in range(colum):
                result[i][j]=mat[i][j]*mat2[i][k]

print(result)        
