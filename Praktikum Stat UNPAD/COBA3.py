import numpy as np #BAGIAN 1
x = np.matrix([[1,2],[3,4]]) #membuat matrix cara 1
print('matrix 2x2:\n', x)
print('dimensi matrix:', x.shape)
y = np.matrix('[1,2;3,4;5,6]',dtype=np.int32) #membuat matrix cara 2
print('matrix 3x2:\n', y)
print('dimensi matrix:', y.shape)
z = np.matrix(np.random.rand(3,3), dtype=np.float32) #membuat matrix cara 3
print('matrix random 3x3:\n', z)
print('dimensi matrix:', z.shape)
za = np.matrix('[1;2;3]',dtype=np.int32)    #BAGIAN 2
print('matrix 3x1:]n',za)
print(x+x) #penjumlahan & pengurangan
print(y+y)
print(z+z)
print(y+za)
print(x+(2*x))
print(sum(y))
print(sum(z))
print(sum(x,za))
print(sum(za,y))
print(sum(za,za))
print(y-za)
print(za-z)
print((3*y)-za)
print(x*x) #perkalian
print(np.dot(x,x))
print(np.multiply(x,x))
print(z*z)
print(z*za)
print(np.multiply(y,za))
print(y/2)  #pembagian dan akar
print(z/za)
print(np.multiply(y,za)/3)
print(np.sqrt(y))
print(np.sqrt(np.multiply(y,za)))
print(x.T) #transpose
print(sum(x,za).T)
print(x.I) #inverse
print(sum(x,za).I)
print('y[0] =', y[0])   #elemen matrix
print('y[2] =', y[2])
print('z[-1] =', z[-1])
print('eigenvalues dan eigenvector\n', np.linalg.eig(x))    #eigen
print('eigenvalues dan eigenvector\n', np.linalg.eig(z))

