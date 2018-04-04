import numpy as np
import time

#Funcion que calcula la serie de Fibonacci dado un numero N

def fibonacci(N):

#Aca busco calcular los casos base para 0 y 1, de lo contrario retorna el numero de la serie que se pide

	if(N==0):
		return 0

	if(N==1):
		return 1
	
	else:
		num=fibonacci(N-1)+fibonacci(N-2)
		return num

def get_time(N):
	t0 = time.time()
	fibonacci(N)
	t1 = time.time()-t0
	return t1

for i in range (35):
	print fibonacci(i), ",", get_time(i)










