import numpy as np
n=int(input("Enter the number of rows:"))
m=int(input("Enter the number of columns:"))
a = [ [0] * m for i in range(n) ]
for i in range (n):
    for j in range(m):
        print("Enter Element",i+1,j+1,":")
        a[i][j] = int(input())
print("The matrix is:\n",np.matrix(a))
#Rank of the matrix
print("Rank of the matrix:",np.linalg.matrix_rank(a))
#Transpose of the matrix
print("Transpose of the matrix:\n",np.transpose(a))
#Determinant of the matrix
if(m==n):
	print("Determinant of the matrix:",np.linalg.det(a))
#Trace of the matrix
	print("Trace of the matrix:\n",np.trace(a))
#Inverse of the matrix
	print("Inverse of the matrix:\n",np.linalg.inv(a))
#Eigen values and eigen vectors of the matrix
	b,c=np.linalg.eig(a)
	print("Eigen values are:\n",b)
	print("Eigen vectors are:\n",c)
else:
	print("NOTE: ROWS MUST BE EQUAL TO COLUMNS TO OBTAIN DETERMINANT,TRACE,INVERSE,EIGEN VALUES AND EIGEN VECTORS")



