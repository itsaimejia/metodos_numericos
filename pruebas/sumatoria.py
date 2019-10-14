from math import *

n=5000
suma1=0
suma2=0
for i in range(1,n+1):
	suma1+=(1/pow(i,2))

for i in range(n,1,-1):
	suma2+=(1/pow(i,2))

print("I->D: {}\nD->I: {}\nE: {}".format(suma1,suma2,(fabs(suma1-suma2))))

