import numpy as np

# print version
print(np.version.version)

# Array basics

# Array Creation
a = np.array([1,2,3])
b = np.array([(1,2,3),(4,5,6),(7,8,9)])
c = np.zeros((2,2))
d = np.ones((3,3))
print(d)

# Array Properties
# Rank or number of dimensions
print(b.ndim)

# Shape
print("Shape is ", b.shape) # Shape is the number of rows and columns

# Size
print("Size is", b.size) # Number of elements in the array

# Data type
print(b.dtype)

# Array Indexing
print("Print entire row ", b[0])
print("Print entire column", b[0,0], b[1,0])

# Print specific rows and columns
# Print 1st 2 rows and print 2nd and 3rd colums for these rows
print("Print specific rows and columns", b[:2,1:3]) 

# Arithmetic operations
m = np.array([(1,2),(3,4)])
n = np.array([(5,6),(7,8)])

# Element wise add
print("Element wise add",m+n)
print("ELement wise subtract",m-n)
print("Element wise mul", m*n)

# Dot products
#mxn
print("dot product is", m.dot(n))

print("Row wise sum for m is", np.sum(m,axis=1))
print("Column wise sum for m is", np.sum(m, axis=0))


