import numpy as np

def matsum(a,b):
    return np.add(a,b)

def matmul(a,b):
    return np.dot(a,b)

def mattrans(a):
    return np.transpose(a)

def matrows(a):
    return a[0], a[1]

def matcols(a):
    return a[:,0], a[:,1]

if __name__ == '__main__':
    a = np.array([[1,2], [3,4]])
    b = np.array([[5,6], [7,8]])
    print("Matrix A : \n", str(a)[1:-1])
    print("Matrix B : \n", str(b)[1:-1])
    print("Sum of A and B : \n", str(matsum(a,b))[1:-1])
    print("Multiplication of A and B : \n", str(matmul(a,b))[1:-1])
    print("Transpose of A : \n", str(mattrans(a))[1:-1])
    print("Rows of A : ", matrows(a)[0], matrows(a)[1], sep = '\n')
    print("Columns of B : ", matcols(b)[0], matcols(b)[1], sep = '\n')
