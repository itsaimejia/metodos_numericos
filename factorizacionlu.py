import numpy as np
from decimal import *
import sys, getopt, argparse


def solucion(datos):
    texto = datos[0]
    renglones = texto.split(';')
    numeros = []
    for i in renglones:
        numeros.append(i.split(':'))
    entrada=np.array(numeros)
    m=len(entrada)
    matrizA=np.zeros((m,m))
    u = np.zeros((m,m))
    l = np.zeros((m, m))

    for r in range(0,m):
        for c in range(0,m):
            matrizA[r,c]=float(entrada[r,c])
            u[r,c]=matrizA[r,c]

    for k in range(0,m):
        for r in range(0,m):
            if k==r:
                l[k,r]=1
            if k<r:
                factor=(float(matrizA[r,k])/float(matrizA[k,k]))
                l[r,k]=factor
                for c in range(0,m):
                    matrizA[r,c]=float(matrizA[r,c])-(factor*float(matrizA[k,c]))
                    u[r,c]=float(matrizA[r,c])
    print("Matriz L:")
    print(l)
    print("Matriz U:")
    print(u)



cadena = sys.argv[1:]
datos=[]

opts, args = getopt.getopt(cadena, "hA:", ["help,a="])

for opt, arg in opts:
    if opt in ("-h", "--help"):
        parser = argparse.ArgumentParser(description='''
        El programa solicita el valor de -A, que es la matriz A y tiene que ser ingresada de la siguiente forma
        -A A11:A12:A13;A21:A22:A23;A31:A32:A33
        siguiendo este orden obtenemos:
        [
         [A11 A12 A13],
         [A21 A22 A23],
         [A31 A32 A33]
        ]
			''', epilog='''
			
			''')
        parser.add_argument('-A', '--a', help='Matriz A', required=True)
        args = parser.parse_args()
    if opt in ("-A", "--a"):
        datos.append(arg)
solucion(datos)
