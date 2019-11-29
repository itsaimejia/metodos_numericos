import numpy as np
from math import *
from sympy import *
import sys, getopt, argparse

def funcion(x):
	return sin(3.1416*x)
	
def solucion(datos):
	a=float(eval(datos[0]))
	b=float(eval(datos[1]))
	n=int(datos[2])

	h = (b-a)/n
	x = a
	suma = funcion(x)
	for i in range(0,n-1,1):
		x+= h
		suma+=2*funcion(x)
    
	suma += funcion(b)
	area = h*(suma/2)

	print('Integral: ', area)


cadena=sys.argv[1:]
datos=[]

opts,args=getopt.getopt(cadena,"ha:b:f:n:",["help,a=,b=,f=,n="])

for opt,arg in opts:
	if opt in ("-h","--help"):
		parser=argparse.ArgumentParser(description='''
			El programa aplica el metodo de trapecio
			El metodo requiere el ingreso de datos en el formato
			-a <valor> -b <valor> -n <valor>
			''', epilog='''
			Al llegar al resultado este se despliega dandonos la solucion a la funcion
			al igual que se imprime la iteracion en donde fue encontrada la solucion entre
			otros datos 
			''')
		parser.add_argument('-a','--a_val', help='Limite inferior', required=True)
		parser.add_argument('-b','--b_val', help='Limite superior', required=True)
		parser.add_argument('-n','--num', help='Numero de trapecios', required=True)
		args=parser.parse_args()
	elif opt in ("-a", "--a_val"):
		datos.append(arg)
	elif opt in ("-b", "--b_val"):
		datos.append(arg)

	elif opt in ("-n", "--num"):
		datos.append(arg)

solucion(datos)








