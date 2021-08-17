import numpy as np
np.fabs(3)
#1
y = 4
np.exp(y)
np.log(y)
np.log10(y)
np.sqrt(y)
#2
z = 3.21
np.modf(z)
np.ceil(z)
np.floor(z)
#3
x = 4.723965716
round(x)
round(x, 3)
pow(5, 2)
abs(x)
#4
a = [0, 0, 1, 4, 7, 16, 31, 64, 127]
b = np.array(a)
b
c = np.array([1, 4., -2, 7])
c
type(a)
type(b)
type(c)
#5
a2 = np.array([[0., 1, 2, 3, 4], [5, 6, 7, 8,9]])
a2
shape(a2)
a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
a3
shape(a3)
#5
b1 = np.linspace(0, 10, 5)
b1
b2 = np.logspace(1, 3, 5)
b2
b3 = np.arange(0, 10, 2)
b3
b4 = np.arange(0., 10., 2.)
b4
b5 = np.arange (0, 10, 1.5)
b5
b6 = np.zeros(5)
b6
b7 = np.ones(5)
b7
#6
c1 = np.linspace(-1., 5, 7)
c1
c1*6
c1/5
c1**3
c1+4
c1-10
(c1+3)*2
c2 = 5*np.ones(8)
c2
c2 += 4
c2
#7
y = np.array([0., 1.3, 5., 10.9, 18.9, 28.7, 40.])
t = np.array([0., .49, 1, 1.5, 2.08, 2.55, 3.2])
y[:-1]
y[1:]
y[1:]-y[:-1]
v = (y[1:]-y[:-1])/(t[1:]-t[:-1])
v
