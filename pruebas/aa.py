import numpy as np 




texto = "1:-3:4;2:3:6;8:9:6"
renglones = texto.split(';')
numeros = []
for i in renglones:
    numeros.append(i.split(':'))

entrada=np.array(numeros)
m=len(entrada)
print(m)

matriz=[[float(entrada[i,j]) for j in range(0,m)]for i in range(0,m)]

print(matriz)

