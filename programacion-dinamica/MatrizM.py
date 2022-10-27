def Verificar(arr):
    z=0

    for i in range(0,len(arr)-1):
        if not validadorDimenciones(arr[i], arr[i+1]):
            break
        else:
            z=z+1
                    
    
    if z == (len(arr)-1):
        print("La secuencia es correcta")
        return True
    else:
        print("La secuencia no es valida")
        return False

def validadorDimenciones(arr,arr2):
    flag = False
    
    if arr[2]==arr2[1]:
        flag=True
    else:
        flag=False
        
    return flag

def Calculador(arr):
    MatrizNoOp = [['0' for x in range(4)] for x in range(len(arr)-1)]
    
    arr2 = []
    
    for i in range(0,len(arr)-1):
        arr2 = NuevasDimensiones(arr[i],arr[i+1])
        for j in range(0,3):
            MatrizNoOp[i][j]=arr2[j]
        MatrizNoOp[i][3]=CalcularOperaciones(arr[i],arr[i+1])+""
    
    MatrizNoOp = Recursivo(MatrizNoOp,arr,0,len(MatrizNoOp))
    resultado = "La secuencia a seguir:\n" + str(MatrizNoOp[0][0])+"\nCon:"+str(MatrizNoOp[0][3]+" multiplaciones")
    salida = open("salida.txt", "w")
    salida.write(str(resultado))
       
def Recursivo(arr,arr2,a,b):
    i = a 
    if b == 1:
        print("Concluyo en caso base")
    else:
        for x in range(0,b-1):
            arr[x]= ComparaMatriz(arr[x],arr[x+1],arr2[2+i+x],arr2[x])
        b=b-1
        i=i+1
        Recursivo(arr,arr2,i,b)
    
    return arr
              
def ComparaMatriz(arr1,arr2,arrM1,arrM2):
    A= int(CalcularOperaciones(arr1,arrM1))+int(arr1[3])
    B= int(CalcularOperaciones(arrM2,arr2))+int(arr2[3])
    
    MatrizOp = ["1","2","3","4"]
    arrM=[]
    
    if(A>B):
        arrM= NuevasDimensiones(arrM2,arr2)
        for i in range (0,3):
            MatrizOp[i]=arrM[i]
        MatrizOp[3]=str(int(CalcularOperaciones(arrM2,arr2)) + int(arr2[3]))
    else:
        arrM= NuevasDimensiones(arr1,arrM1)
        for i in range (0,3):
            MatrizOp[i]=arrM[i]
            MatrizOp[3]=str(int(CalcularOperaciones(arr1,arrM1)) + int(arr1[3]))
    return MatrizOp    
    
def NuevasDimensiones(arr,arr2): 
    matriz_Provicional = ["","",""];
    matriz_Provicional[0]= "(" + arr[0]+arr2[0] + ")";
    matriz_Provicional[1]= arr[1];
    matriz_Provicional[2]= arr2[2];        
    return matriz_Provicional;

def CalcularOperaciones(arr,arr2):
    numero_Operaciones = int(arr[1])*int(arr[2])*int(arr2[2])
    return str(numero_Operaciones)
    
archivo = open("ejemploEntradaP4.txt", "r")

arr = []

for i in archivo.readlines():
    i = i.strip('\n')
    arr.append(i.split(' '))
    
if(Verificar(arr)):
    Calculador(arr)


