#MEMBUAT FUNGSI
#1 - pangkat
def pangkat(x):
	return x ** 2
# run pangkat
x = 2
y = pangkat(x)
print(x,y)

#2 - faktorial
def fakt(x):
	import numpy as np
	fakt = 1
	for i in np.arange(1, x + 1):
		fakt = fakt * i
		i = i + 1
	return fakt

#KATA KUNCI
def baku(x, mu, sigma):
	return(x-mu)/sigma
x = 5
#Fungsi Baku
z = baku(x,3.4,1.2)
print(z)

#NILAI DEFAULT
#fungsi baku dengan nilai sigma ditentukan dalam fungsi
def baku(x, mu, sigma = 1):
	return(x-mu)/sigma
x = 5
#Fungsi Baku
z = baku(x,3.4)
print(z)

#INPUT VARIABEL
def baku(x, mu):
	sigma = float(input('Nilai Sigma = '))
	return (x - mu)/sigma
x = 5
#Fungsi Baku
z = baku(x,3.4)
print(z)

#LATIHAN 1
# Fungsi faktorial
def fakt(x):
	import numpy as np
	fakt = 1
	for i in np.arange(1,x + 1):
		fakt = fakt * i
		i = i + 1
		return fakt

# Fungsi peluang binomial
def binom(n,k,p):
	return fakt(n)/(fakt(k)*fakt(n-k))*p**k*(1-p)**(n-k)
# Input data
n=input("banyak data = ")
x=input("banyak sukses = ")
p=input("peluang sukses = ")
# memanggil fungsi peluang binomial
hasil=binom(n,x,p)
print(hasil)

#LATIHAN 2
# Fungsi faktorial
def fakt(x):
	import numpy as np
	fakt = 1
	for i in np.arange(1, x + 1):
		fakt = fakt * i
		i = i + 1
		return fakt
# Fungsi peluang binomial
def binom(n,k,p):
	return fakt(n)/(fakt(k)*fakt(n-k))*p**k*(1-p)**(n-k)
# Input data
n=input("banyak data = ")
x=input("banyak sukses = ")
p=input("peluang sukses = ")
# memanggil fungsi peluang binomial
hasil=binom(n,x,p)
print(hasil)
# Menghitung peluang kumulatif binomial pada X=x
hasil=0
for k in range(x+1):
	hasil+=binom(n,k,p)
print(hasil)
# Menghitung peluang kumulatif binomial untuk semua X
hasil=0
for k in range(n+1):
	hasil+=binom(n,k,p)
	print('P( X=',k,') = ',binom(n,k,p), ' P(X <=',k,') = ',hasil)