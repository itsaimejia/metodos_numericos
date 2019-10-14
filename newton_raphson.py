from math import *
from sympy import *
import sys, getopt, argparse
from colorama import init, Fore, Back, Style

init()

def solucion(datos):
	p0=float(datos[0])
	f=datos[1]
	d=datos[2]
	e=float(datos[3])
	n=int(datos[4])

	x=symbols('x')

	i=1

	while i <= n:
		
		fp0=sympify(f).subs(x,p0)
		dp0=sympify(d).subs(x,p0)
		p= p0 - (fp0 / dp0)

		if fabs(p - p0) < e:
			print("It: {} Valor de p= {}, f(p0)= {}, f'(p0)= {}".format(i,p,fp0,dp0))
			break
		print("It: {} - p= {}, f(p0)= {}, f'(p0)= {}".format(i,p,fp0,dp0))


		p0=p

		i+=1

cadena=sys.argv[1:]
datos=[]

opts,args=getopt.getopt(cadena,"hI:F:D:E:N:",["help,inicial=,funcion=,derivada=,e=,n="])

for opt,arg in opts:
	if opt in ("-h","--help"):
		parser=argparse.ArgumentParser(description='''
			El programa resuelve aplica el algoritmo de biseccion
			El metodo requiere el ingreso de una cadena en el formato
			-I <valor> -F <texto> -D <texto> -E <valor> -N <valor>
			Donde:
			I es el valor de la aproximacion inicial
			F es la funcion a evaluar (para exponentes usar **, ejemplo: para x^2 -> x**2)
			D es la funcion derivada
			E es la tolerancia
			N es el numero de iteraciones
			''', epilog='''
			Al llegar al resultado este se despliega dandonos la solucion a la funcion
			al igual que se imprime la iteracion en donde fue encontrada la solucion entre
			otros datos 
			''')
		parser.add_argument('-I','--i', help='Aproximacion inicial p0', required=True)
		parser.add_argument('-F','--f', help='Funcion inicial', required=True)
		parser.add_argument('-D','--d', help='Funcion derivada', required=True)
		parser.add_argument('-E','--e', help='Valor de la tolerancia', required=True)
		parser.add_argument('-N','--n', help='Valor de las iteraciones', required=True)
		args=parser.parse_args()

		args=parser.parse_args()
	if opt in ("-I", "--i"):
		datos.append(arg)
	elif opt in ("-F", "--f"):
		datos.append(arg)
	elif opt in ("-D", "--d"):
		datos.append(arg)
	elif opt in ("-E", "--e"):
		datos.append(arg)
	elif opt in ("-N", "--n"):
		datos.append(arg)

solucion(datos)







