from math import *
from sympy import *

import sys, getopt, argparse

def solucion(datos):
	f=datos[0]
	g=datos[1]
	p0=float(datos[2])
	e=float(datos[3])
	n=int(datos[4])

	x=symbols('x')

	i=1

	while i<=n:
		f0=sympify(f).subs(x,p0)
		p=sympify(g).subs(x,p0)
		if fabs(p-p0) < e:
			print("It: {} - p= {} - f(p0)= {}".format(i,p,f0))
			break
		print("It: {} - p= {} - f(p0)= {}".format(i,p,f0))
		i+=1

		p0=p

cadena=sys.argv[1:]
datos=[]

opts,args=getopt.getopt(cadena,"hF:G:P:E:N:",["help,f=,g=,p=,e=,n="])

for opt,arg in opts:
	if opt in ("-h","--help"):
		parser=argparse.ArgumentParser(description='''
			El programa resuelve aplica el algoritmo de punto fijo
			El metodo requiere el ingreso de datos en el formato
			-F <funcion> -G <funcion> -P <valor> -E <valor> -N <valor>
			Donde:
			F es la funcion inicial f(x),
			G es la funcion g(x),
			P el valor de aproximacion,
			E es la tolerancia
			N es el numero de iteraciones
			(para exponentes usar **, ejemplo: para x^2 -> x**2)
			''', epilog='''
			Al llegar al resultado este se despliega dandonos la solucion a la funcion
			al igual que se imprime la iteracion en donde fue encontrada la solucion entre
			otros datos 
			''')
		parser.add_argument('-F','--f', help='Funcion inicial f(x)', required=True)
		parser.add_argument('-G','--g', help='Funcion g(x)', required=True)
		parser.add_argument('-P','--p', help='Valor de aproximacion', required=True)
		parser.add_argument('-E','--e', help='Valor de la tolerancia', required=True)
		parser.add_argument('-N','--n', help='Valor de las iteraciones', required=True)
		args=parser.parse_args()

		args=parser.parse_args()
	if opt in ("-F", "--f"):
		datos.append(arg)
	elif opt in ("-G", "--g"):
		datos.append(arg)
	elif opt in ("-P", "--p"):
		datos.append(arg)
	elif opt in ("-E", "--e"):
		datos.append(arg)
	elif opt in ("-N", "--n"):
		datos.append(arg)

solucion(datos)

