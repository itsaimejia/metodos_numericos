from math import *
from sympy import *
import sys, getopt, argparse

def solucion(datos):
	p0=float(datos[0])
	p1=float(datos[1])
	f=datos[2]
	e=float(datos[3])
	n=int(datos[4])

	x=symbols('x')

	i=2
	
	q0=sympify(f).subs(x,p0)
	q1=sympify(f).subs(x,p1)

	while i <= n:

		p= p0 - (q0 * (p1 - p0) / (q1 - q0))

		if fabs(p-p1) < e:
			print("It: {} Valor de p= {}, q0= {}, q1= {}".format(i,p,q0,q1))
			break
		print("It: {} - p= {} ".format(i,p))

		p0 = p1
		p1 = p
		q0 = q1
		q1 = sympify(f).subs(x,p)

		i+=1


cadena=sys.argv[1:]
datos=[]

opts,args=getopt.getopt(cadena,"hA:B:F:E:N:",["help,a=,b=,f=,e=,n="])

for opt,arg in opts:
	if opt in ("-h","--help"):
		parser=argparse.ArgumentParser(description='''
			El programa resuelve aplica el metodo de la secante
			El metodo requiere el ingreso de datos en el formato
			-A <valor> -B <valor> -F <texto> -E <valor> -N <valor>
			Donde:
			A es la aproximacion cero
			B es la aproximacion uno
			F es la funcion a evluaar (para exponentes usar **, ejemplo: para x^2 -> x**2)
			E es la tolerancia
			N es el numero de iteraciones
			''', epilog='''
			Al llegar al resultado este se despliega dandonos la solucion a la funcion
			al igual que se imprime la iteracion en donde fue encontrada la solucion entre
			otros datos 
			''')
		parser.add_argument('-A','--a', help='Valor de la aproximacion 0', required=True)
		parser.add_argument('-B','--b', help='Valor de la aproximacion 1', required=True)
		parser.add_argument('-F','--f', help='Funcion a evluar', required=True)
		parser.add_argument('-E','--e', help='Valor de la tolerancia', required=True)
		parser.add_argument('-N','--n', help='Valor de las iteraciones', required=True)
		args=parser.parse_args()

		args=parser.parse_args()
	if opt in ("-A", "--a"):
		datos.append(arg)
	elif opt in ("-B", "--b"):
		datos.append(arg)
	elif opt in ("-F","--f"):
		datos.append(arg)
	elif opt in ("-E", "--e"):
		datos.append(arg)
	elif opt in ("-N", "--n"):
		datos.append(arg)

solucion(datos)







