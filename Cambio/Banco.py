def Cajero(Billetes,Cambio, i, Historial):
    if Cambio == 0: return 1
    if i == 9: return 0
    if Billetes[i].n > 0:
        if(Cambio/Billetes[i].denominacion >= 1):
            Cambio-=Billetes[i].denominacion
            Billetes[i].n = Billetes[i].n - 1
            Historial[i] += 1
            return Cajero(Billetes,Cambio,i, Historial)

    return Cajero(Billetes,Cambio,i+1, Historial)

class Billete:
    denominacion = 0
    n=0

    def print_denomicacion(self):
        print(self.denominacion)
    

print("Bienvenido a la práctica del cambio, método codicioso")
Billetes = []
Historial = [0,0,0,0,0,0,0,0,0]
Denominaciones =[500,200,100,50,20,10,5,2,1]
for i in range (0, 9):
    Billetei = Billete()
    Billetei.denominacion = Denominaciones[i]
    print("Dame el tamaño n de ", Denominaciones[i])
    Billetei.n = int(input(""))
    Billetes.append(Billetei)

Cambio=int(input("Cuánto cambio debo:"))

if Cajero(Billetes,Cambio, 0, Historial) == 0:
    print("No hay cambio")
else:
    print("Se entregó:")
    for i in range (0,8):
        if Historial[i] > 0:
            print(Historial[i], "de ", Denominaciones[i])