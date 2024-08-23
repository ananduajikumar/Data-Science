from numpy import random,linalg

a = random.randint(10,size=(2,2))

print("DETERMINANT OF THE MATRIX IS\n",linalg.det(a))
print("INVERSE OF THE MATRIX IS\n",linalg.inv(a))
print("RANK OF THE MATRIX IS\n",linalg.matrix_rank(a))
print("1D MATRIX IS\n",a.flatten())



output
DETERMINANT OF THE MATRIX IS
 5.000000000000001
INVERSE OF THE MATRIX IS
 [[ 0.2  0. ]
 [-1.8  1. ]]
RANK OF THE MATRIX IS
 2
1D MATRIX IS
 [5 0 9 1]
