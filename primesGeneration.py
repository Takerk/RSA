
archivo=open("primos.txt","w+")

def esprimo(numero):
    contador=0
    verificar= False
    for i in range(1,numero+1):
        if (numero%i)==0:
            contador=contador+1
        if contador >= 3:
            verificar=True
            break
    if contador==2 or verificar==False:
        return 1
    else:
        return 0

#limite=20000700
#inicio=19999700

limite=5000
inicio=0


def generarprimos():
    encontrado=0
    n=inicio
    while(n<=limite):
       if esprimo(n):
            encontrado=n
            archivo.write(str(encontrado)+"\n")
            print(encontrado)
       n=n+1
    archivo.close()


generarprimos()







