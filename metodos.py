archivo=open("holah.jpg")


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
