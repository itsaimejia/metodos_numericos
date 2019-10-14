decimal=int(input("Decimal: "))
lista=[]

while decimal >= 1:
	aux=decimal%2
	print("{} / 2: {}".format(decimal,aux))
	lista.insert(0,aux)
	decimal=decimal//2
print("Binario:")
print("".join(str(i) for i in lista))
print(lista)


	


"""
print("Binario: ")
binario="".join(str(i) for i in lista)
print("0.{}".format(binario))

"""
