import random

archivo=open("primos.txt")
lineas=len(open("primos.txt").readlines())

print 'Número de lineas', lineas
plinea=random.randrange(268)
qlinea=random.randrange(268)
while(plinea==qlinea):
     qlinea=random.randrange(268)
print(plinea)
print(qlinea)
for i in range(lineas):
     if i==plinea:
          p=archivo.next()
     else:
          if i==qlinea:
               q=archivo.next()
          else:
               archivo.next()
archivo.close()
print('Numero p y q: ')
print(p)
print(q)


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

def powermod(mc,ed,n):
    base = mc
    lbinario = listabinario(ed);
    del lbinario[0]
    if ed < 0:
         del lbinario[0]
    for i in lbinario:
        if i=='1':
            print("entro a 1")
            mc = (mc*mc*base)% n
        else:
            print("entro a 0")
            mc=(mc*mc)%n
        print("el valor de i es: " ,i ," el numero es: ",mc)
    return mc

print(powermod(45))
