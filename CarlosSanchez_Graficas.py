import numpy as np
import matplotlib.pyplot as plt

#Cargue de archivos en variables
pyt=np.genfromtxt('times_python.csv',delimiter=",")
cpp=np.genfromtxt('times_cpp.csv', delimiter=",")

#Obtengo las columnas de cada archivo para poder hacer la grafica
colp1=pyt[:,0]
colp2=pyt[:,1]
colc1=[:,0]
colc2=[:,1]

#Grafica de los archivos con respecto al tiempo
plt.figure()
plt.title('Grafica de tiempo vs N')
plt.plot(colp1,colp2, label='Datos para python')
plt.plot(colc1,colc2,label='Datos para c++')
plt.xlabel('Tiempo')
plt.ylabel('N')
plt.savefig('cpp_vs_python.png')
plt.legend()
