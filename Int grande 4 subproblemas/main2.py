from math import ceil, floor

def validar (numero):
    if len(numero) != nDigitos:
        print("El número debe tener %s dígitos" % nDigitos)

#El algoritmo se mantiene igual que para base 10
def multiplicacion(x, y, n):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		m = int(ceil(float(n)/2))
		n = int(ceil(float(n)))

		x = int(x)
		y = int(y)

		IA = int(floor(x/n))
		DA = int(x%(n))

		IB = int(floor(y/n))
		DB = int(y%(n))

		a = multiplicacion(str(IA), str(IB), str(n/2))
		b = multiplicacion(str(DA), str(DB), str(n/2))
		c = multiplicacion(str(DA), str(IB), str(n/2))
		d = multiplicacion(str(DA), str(DB), str(n/2))

		prod =  pow(10, n * a) + pow(10, (n/2) * b) + pow(10, (n/2) * c) + d
		
		return prod


respuesta = 1

while respuesta != 0:
	# Main
	print("\nMultiplicación de dos números con dígitos de 2^n usando el método de divide y vencerás")

	print("\nIntroduzca el valor de n:")
	n = input()
	n = int(n)
	nDigitos = pow(2, n)

	A = ""
	B = ""

	while(len(A) != nDigitos):
		print("\nIngresa el primer número de %s dígitos:" % nDigitos)
		A = input()
		validar(A)

	while(len(B) != nDigitos):
		print("\nIngresa el segundo número de %s dígitos:" % nDigitos)
		B = input()
		validar(B)

	A = int(A)
	B = int(B)

	if A < 0 or B < 0:
		print("Error")
	elif A == 0 or B == 0:
		print("AxB: " + str(0))
	else:

		print("Numero A decimal: " + str(A))
		print("Numero B decimal: " + str(B))

		multi = multiplicacion(A, B, n)

		print("AxB en decimal: " + str(multi))
	
	respuesta = int(input("Calcular otro producto? (si = 1/no = 0): "))