#CONTOH DIAGRAM GARIS -1-
import matplotlib.pyplot as plt
x =[3,6,8,11,13,14,17,19,21,24,33,37]
y = [7.5,12,13.2,15,17,22,24,37,34,38.5,42,47]
plt.plot(x,y)
plt.show()

#CONTOH DIAGRAM GARIS -2-
import matplotlib.pyplot as plt
x =[3,6,8,11,13,14,17,19,21,24,33,37]
y = [7.5,12,13.2,15,17,22,24,37,34,38.5,42,47]
x2 =[3,6,8,11,13,14,17,19,21,24,33]
y2 = [50,45,33,24,21.5,19,14,13,10,6,3]
plt.plot(x,y, label='ket garis 1')
plt.plot(x2, y2, label='ket garis 2')
plt.xlabel('label sumbu x')
plt.ylabel('label sumbu y')
plt.title('Judul grafik\ncontoh 1 ')
x_label=[0,5,10,15,20,25,30,35,40,45,50]
y_label=['0B','5B','10B','15B','20B','25B','30B','35B','40B','45B','50B']
plt.yticks(x_label,y_label)
plt.legend()
plt.show()

#CONTOH DIAGRAM PENCAR
import matplotlib.pyplot as plt
x =[3,6,8,11,13,14,17,19,21,24,33,37]
y = [7.5,12,13.2,15,17,22,24,37,34,38.5,42,47]
plt.scatter(x,y, label='keterangan', color='green', marker='.', s=100 )
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Judul\n Diagram Pencar')
plt.legend()
plt.show()

#CONTOH DIAGRAM BATANG
import matplotlib.pyplot as plt
kategori = ['kat1','kat2','kat3','kat4','kat5']
banyak = [4,5,3,2,1]
plt.bar(kategori,banyak, label="kategori")
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Judul\n Diagram Batang')
plt.legend()
plt.show()

#CONTOH DIAGRAM LINGKARAN-1-
import matplotlib.pyplot as plt
plt.pie(banyak, labels=kategori)
plt.show()

#CONTOH DIAGRAM LINGKARAN-2-
import matplotlib.pyplot as plt
cols = ['c','m','r', 'y','g']
plt.pie(banyak,labels=kategori, colors= cols, startangle=100, shadow=True, explode = (0.0,0.0,0.09,0,0), autopct = '%1.1f%%')
plt.title('Judul\n Diagram Lingkaran')
plt.show()

#CONTOH HISTOGRAM
import matplotlib.pyplot as plt
import numpy as np
dat=np.random.normal(50,10,100)
plt.hist(dat,rwidth=.9)
plt.show()

#CONTOH BOXPLOT
import matplotlib.pyplot as plt
from numpy.random import randn
import seaborn as sns
data1 = randn(100)
data2 = randn(100) + 2 # Off set the mean
sns.boxplot(data=[data1,data2])
plt.show()

#CONTOH HEATMAPS
import matplotlib.pyplot as plt
import seaborn as sns
flight_dframe = sns.load_dataset('flights')
flight_dframe = flight_dframe.pivot("month","year","passengers")
sns.heatmap(flight_dframe)
plt.show()