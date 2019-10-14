from math import *
from sympy import *
import sys, getopt, argparse

def solucion(datos):
	print(datos)
	a=float(datos[0])
	b=float(datos[1])
	f=datos[2]
	e=float(datos[3])
	n=int(datos[4])

	x=symbols('x')

	i=1
	fa=sympify(f).subs(x,a)

	while i <= n:

		c=(a + b) / 2
		fc=sympify(f).subs(x,c) #funcion f(c)
		if fc==0 or fabs(sympify(f).subs(x,c)) < e:
			print("\nIt: {} Solucion a la ecuación {} = {}, fc={}, fa={}".format(i,f,c,fc,fa))
			break
		print("\nIt:{} c = {}, fc={}, fa={}".format(i,c,fc,fa))
		i+=1
		if fa*fc>0:
			a=c
			fa=fc
		else:
			b=c


cadena=sys.argv[1:]
datos=[]

opts,args=getopt.getopt(cadena,"hA:B:F:E:N:",["help,a=,b=,f=,e=,n="])

for opt,arg in opts:
	if opt in ("-h","--help"):
		parser=argparse.ArgumentParser(description='''
			El programa resuelve aplica el algoritmo de biseccion
			El metodo requiere el ingreso de datos en el formato
			-A <valor> -B <valor> -F <texto> -E <valor> -N <valor>
			Donde:
			A es el valor de a\n
			B el valor de b\n
			F es la funcion a evaluar (para exponentes usar **, ejemplo: para x^2 -> x**2)\n
			E es la tolerancia\n
			N es el numero de iteraciones\n
			''', epilog='''
			Al llegar al resultado este se despliega dandonos la solucion a la funcion
			al igual que se imprime la iteracion en donde fue encontrada la solucion entre
			otros datos 
			''')
		parser.add_argument('-A','--a', help='Valor de a', required=True)
		parser.add_argument('-B','--b', help='Valor de b', required=True)
		parser.add_argument('-F','--f', help='Funcion a evaluar', required=True)
		parser.add_argument('-E','--e', help='Valor de la tolerancia', required=True)
		parser.add_argument('-N','--n', help='Valor de las iteraciones', required=True)
		args=parser.parse_args()

		args=parser.parse_args()
	if opt in ("-A", "--a"):
		datos.append(arg)
	elif opt in ("-B", "--b"):
		datos.append(arg)
	elif opt in ("-F", "--f"):
		datos.append(arg)
	elif opt in ("-E", "--e"):
		datos.append(arg)
	elif opt in ("-N", "--n"):
		datos.append(arg)

solucion(datos)







