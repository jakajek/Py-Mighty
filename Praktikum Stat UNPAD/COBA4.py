# Contoh Struktur if...else
x = 5
y = 3
# Struktur if... (tanpa else)
if x > 3:
	x + y
# Struktur if...else
if x != 5:
	x + y
else:
	x - y

# Kondisi lebih dari satu (operator'and', 'or', dan 'in')
nilai = 70
# operator 'and' dan '&'
# 'and'
if nilai > 60 and nilai < 100:
	print ('lulus')
else:
	print('tidak lulus')
# '&'
if nilai > 60 & nilai < 100:
	print ('lulus')
else:
	print('tidak lulus')
# Operator 'or' dan '/'
# 'or'
if nilai < 60 or nilai > 100:
	print('lulus')
else:
	print('tidak lulus')
# '/'
if nilai < 60 / nilai > 100:
	print('lulus')
else:
	print('tidak lulus')
# Operator 'in'
x = 6
y = 3
a = (0,1,2,3,4)
b = (5,6,7,8,9)
if x in a:
	x + y
if x in b:
	x = x ** y
x

# Contoh Struktur if...elif...else
x = 5
if x < 5:
	x = x + 1
elif x > 5:
	x = x - 1
else:
	x **= 2
x

# Contoh If majemuk
x = 25
if x < 5:
	if x > 3:
		x = x + 1
	else:
		x=x-1
else:
	x=x+2
x

# Contoh struktur for
for i in range(10):
	print(i)
import numpy as np
daftar = np.linspace(1,10,10)
jumlah = 0
for i in daftar:
	jumlah = jumlah + 1
	print(jumlah)

# Contoh fungsi break
daftar = np.linspace(1,10,10);daftar
for i in daftar:
	print(i)
	if i > 4:
		break

# Contoh fungsi continue
daftar = (3,5,7,-2,-1,2,6,-1,-9,8)
for i in daftar:
	if i >= 0:
		continue
	print(i)

# Contoh Pengulangan while
jumlah = 0
i = 0
while jumlah < 10:
	jumlah = jumlah + i ** 2
	i += 1
	print('Iterasi ke-',i,'Jumlah = ',jumlah)

# Solusi 1. Menggunakan if majemuk
nilai = 70
if nilai>0 or nilai<100:
	if nilai>=80:
		print('Huruf Mutu = A')
	else:
		if nilai>=68:
			print('Huruf Mutu = B')
		else:
			if nilai>=55:
				print('Huruf Mutu = C')
			else:
				if nilai>=40:
					print('Huruf Mutu = D')
				else:
					print('Huruf Mutu = E')
else:
	print('Nilai < 0 atau > 100')
#Solusi 1. Menggunakan operator “in”
import numpy as np
nilai=65
if nilai in np.linspace(80,100,21):
	print('Huruf Mutu = A')
if nilai in np.linspace(68,78,23):
	print('Huruf Mutu = B')
if nilai in np.linspace(55,67,13):
	print('Huruf Mutu = C')
if nilai in np.linspace(40,54,15):
	print('Huruf Mutu = D')
if nilai in np.linspace(0,39,40):
	print('Huruf Mutu = E')

#Solusi 2. Menggunakan struktur 'for'
#dan operator 'in'
import numpy as np
x = 5
fac = 1
for i in np.arange(1, x + 1):
	fac = fac * i
	i = i + 1
print(fac)

#Solusi 3. Menggunakan struktur 'for'
#dan struktur 'if'
import numpy as np
x = [9,4,7,2,1,11,7,15,3,6] # Data array belum terurut
for i in range(len(x)-1):
	for z in np.arange(i, len(x)):
		a = x[i]
		b = x[z]
		if a > b:
			temp = x[i]
			x[i] = x[z]
			x[z] = temp
print(x)

