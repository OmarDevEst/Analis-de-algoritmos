from math import ceil, floor

def validar (numero):
    if len(numero) != nDigitos:
        print("El número debe tener %s dígitos" % nDigitos)

#El algoritmo se mantiene igual que para base 10
def multiplicacion(x, y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		m = int(ceil(float(n)/2))

		IA = int(floor(x/2**m))
		DA = int(x%(2**m))

		IB = int(floor(y/2**m))
		DB = int(y%(2**m))

		a = multiplicacion(IA, IB)
		b = multiplicacion(DA, DB)
		c = multiplicacion(IA + DA, IB + DB) - a - b

		prod =  int(a*(2**(m*2)) + c*(2**m) + b)
		
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

		multi = multiplicacion(A, B)

		print("AxB en decimal: " + str(multi))
	
	respuesta = int(input("Calcular otro producto? (si = 1/no = 0): "))