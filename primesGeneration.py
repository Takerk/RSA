

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

limite=50000000
inicio=1000000

print('Generacion de p y q, ambos primos')
p=0
q=0
#print(esprimo(999769))
#encontrado=0
#n=inicio
#while(n<=limite):
 #   if esprimo(n):
  #      encontrado=n
   #     print(encontrado)
    #n=n+1

def listabinario(decimal):
    lista=[]
    binario=bin(decimal)
    for i in binario:
        lista.append(i)
    del lista[0]
    del lista[0]
    return lista


lbinario=listabinario(10949)
print(lbinario)
n=27641

def powermod(numero):
    base=numero
    del lbinario[0]
    for i in lbinario:
        if i=='1':
            print("entro a 1")
            numero=(numero*numero*base)%n
        else:
            print("entro a 0")
            numero=(numero*numero)%n
        print("el valor de i es: " ,i ," el numero es: ",numero)
    return numero

print(powermod(45))







