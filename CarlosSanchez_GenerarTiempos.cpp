#include <iostream>
#include <ctime>
using namespace std;



int fibonacci(int N){
//Aca busco calcular los casos base para 0 y 1, de lo contrario retorna el numero de la serie que se pide
int num;
	if(N==0)
	return 0;

	if(N==1)
	return 1;
	
	else
	num=fibonacci(N-1)+fibonacci(N-2);
	return num;
}

//Con esta funcion se calcula el tiempo que tarda la serie de Fibonacci en arrojar el resultado

float get_time(int N){

clock_t t;
t=clock();
fibonacci(N);
t=clock()-t;
float time =((float)t)/CLOCKS_PER_SEC;

return time;
}

//Codigo para funcion main en la que voy a calcular los primeros 35 numeros de la serie de Fibonacci y el tiempo que tarda en procesar esa respuesta

int main (){

int N=0;
	for(N=0;N<35;N++){
	cout << fibonacci(N) <<"," <<get_time(N) << endl; 
	
	}
return 0;

}


