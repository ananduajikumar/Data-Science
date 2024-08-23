import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

#addition
def addition(A,B):
    return np.add(A,B)
print("sum of the number is",A+B)

#substraction
def substraction(A,B):
    return np.subtract(A,B)
print("suubstraction of the number is",substraction(A,B))

#multiplication
def multiplication(A,B):
    return np.multiply(A,B)
print("multiplication of the number is",multiplication(A,B))
      
      #multiplication
def multiplication(A,B):
    return np.dot(A,B)
print("multiplication of the number is",multiplication(A,B))
      
#division
def division(A,B):
    return np.division(A,B)
print("division of the number is",A/B)

import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

#transpose
def matrix_transpose (A):
    return np.transpose(A)
print("the transpose is",matrix_transpose(A))


#determinent
def determent(A):
    return np.linalg.det(A)
print("the detrtmintent is",determent(A))







output

sum of the number is [[ 6  8]
 [10 12]]
suubstraction of the number is [[-4 -4]
 [-4 -4]]
multiplication of the number is [[ 5 12]
 [21 32]]
multiplication of the number is [[19 22]
 [43 50]]
division of the number is [[0.2        0.33333333]
 [0.42857143 0.5
the transpose is [[1 3]
 [2 4]]
the detrtmintent is -2.0000000000000004








                           
